import random
number=random.randint(1,10)

while True:
    guess = int(input("please guess the number?"))
    if guess==number:
        print("congratulations")
