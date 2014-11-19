import re
from multiprocessing import Process

class open_ctxmgr(object):
    def __init__(self, file_name):
        self.file_name = file_name
        
    def __enter__(self):
        self.fobj = open(self.file_name, "r")
        return self.fobj
    
    def __exit__(self, exctype, exc, tb):
        self.fobj.close()
        return True

class Log(object):
    def __init__(self, host, auth, timestamp, request, code, size, referrer, userAgent):
        self.host = host
        self.auth = auth
        self.timestamp = timestamp
        self.request = request
        self.code = code
        self.size = size
        self.referrer = referrer
        self.userAgent = userAgent
        
    def __repr__(self):
        return self.host + " " \
            + self.auth + " "  \
            + self.timestamp + " " \
            + self.request + " " \
            + self.code + " " \
            + self.size + " " \
            + self.referrer + " " \
            + self.userAgent
    
class LogIterator(object):
    def __init__(self, file_name):
        self.fobj = open(file_name, "r")
        self.rgx = (r'(?P<host>[^ ]*) '
           r'(?P<ident>\S*) '
           r'(?P<auth>\S*) '
           r'\[(?P<ts>.*)\] '
           r'"(?P<request>[^"]*)" '
           r'(?P<code>\d{3}) '
           r'(?P<size>(\d+|-)) '
           r'"(?P<referrer>[^"]*)" '
           r'"(?P<ua>[^"]*)" '
           )

    def __iter__(self):
        return self
        
    def next(self):
        line = self.fobj.readline()
        if not line:
            self.fobj.close()
            raise StopIteration
        m = re.match(self.rgx, line)
        m = m.groupdict()
        return Log(m["host"], m["auth"], m["ts"], m["request"], m["code"], m["size"], m["referrer"], m["ua"])

rgx = (r'(?P<host>[^ ]*) '
           r'(?P<ident>\S*) '
           r'(?P<auth>\S*) '
           r'\[(?P<ts>.*)\] '
           r'"(?P<request>[^"]*)" '
           r'(?P<code>\d{3}) '
           r'(?P<size>(\d+|-)) '
           r'"(?P<referrer>[^"]*)" '
           r'"(?P<ua>[^"]*)" '
           )

def LogGenerator(file_name):
        fobj = open(file_name, "r")
        
        while True:
            line = fobj.readline()
            if not line:
                fobj.close()
                return
            
            m = re.match(rgx, line)
            m = m.groupdict()
            yield Log(m["host"], m["auth"], m["ts"], m["request"], m["code"], m["size"], m["referrer"], m["ua"])
            
def filter_404(logiter):
        while True:
            log = logiter.next()
            if not log:
                return
            
            if log.code == "404":
                yield log
    
class LogStore(object):
    def __init__(self, logiter):
        self.logs = list(logiter)
        
    def search_requests(self, regex):
        out = []
        for log in self.logs:
            if re.search(regex, log.request):
                out.append(log)
        
        return out
    
if __name__ == "__main__":
    store = LogStore(LogIterator("access.log"))
    print(len(store.search_requests("admin")))

        
#    for elt in filter_404(LogGenerator("access.log")):
#        print elt
    
#    it = LogIterator("access.log")
#    for elt in it:
#        print elt