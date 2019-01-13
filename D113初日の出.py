import datetime

time = input()

date_dt = datetime.datetime.strptime(time, '%H:%M')

date_dt = date_dt - datetime.timedelta(hours=8)

print("{}:{}".format(date_dt.hour, date_dt.minute))
