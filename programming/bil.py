def fun(num):
    if num<0:
        return 0
    else:
        return fun(num-1)
print(fun(5))