import datetime

today = datetime.date.today()
print "Today is:", today

tomorrow = today + datetime.timedelta(days=1)

print "Tomorrow is:", tomorrow