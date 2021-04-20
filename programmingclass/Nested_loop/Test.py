def add(a,b):
    print('function start')
    c=a+b
    return c

print("main start")
print('function is calling')
a=int(input("enter first number"))
b=int(input("enter another number"))
ans=add(a,b)
print("The sum is", ans)
print('program end')