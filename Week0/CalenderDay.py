import datetime
def calender(n):
  x = datetime.datetime(n,1,1)
  day = x.strftime("%A")
  print(day.lower())

