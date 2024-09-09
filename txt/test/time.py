from datetime import date

today = date.today() 

cur_date = (str(today.day)+"/"+str(today.month)+"/"+str(today.year))
print(cur_date)