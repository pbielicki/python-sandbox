class open_ctxmgr(object):
    def __init__(self, file_name):
        self.file_name = file_name
        
    def __enter__(self):
        self.fobj = open(self.file_name, "r")
        return self.fobj
    
    def __exit__(self, exctype, exc, tb):
        self.fobj.close()
        return True
    
if __name__ == "__main__":
    with open_ctxmgr("access.log") as myfile:
        for line in myfile:
            print(line)
