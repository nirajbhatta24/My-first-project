# write a program to convert seconds to day,hour,and minute
sec=int(input("enter a second"))
min=(sec/60)
print(f"The minute is {min}")
hr=(sec/(60*60))
print(f"The hour is {hr}")
day=(sec/(24*60*60))
print(f"The day is {day}")