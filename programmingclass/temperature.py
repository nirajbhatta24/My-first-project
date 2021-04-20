# If the temperature is greater than 30, its a hot day otherwise if its  less than 10;
# its a cold day; otherwise,
# it's neither hot nor cold

temp=float(input("Enter current temperature"))
if temp>30:
    print("It's a hot day")
elif temp<10:
    print("It's a cold day")
elif 10<temp<31:
    print("Neither hot nor cold")