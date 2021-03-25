import random

num=random.randint(1,10)

guess=int(input("please guess the number"))
while num!=guess:
    guess=int(input("oops !! try again"))
else:
    print("congratulation!!! U R right")