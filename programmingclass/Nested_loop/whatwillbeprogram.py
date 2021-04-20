#The python code below generates 50 random even integers, Rewrite the code so ut uses a ehilr loop instead if for loop.

m=int(input("Enter marks of math"))
sc=int(input("Enter marks of science"))
com=int(input("Enter marks of computer"))
nep=int(input("enter marks of nepali"))
tot=(m+sc+com+nep)
print("The total is", tot)
percentage= (tot/400)*100
print(f"You scored {percentage} %")
grade= percentage/25
print(f"You scored {grade} grade.")

if percentage>70:
    print("you scored distinction")
elif percentage>=60 and percentage<= 70:
    print("you scored first division")
elif percentage>=40 and percentage<=60:
    print("you're just passed.")
elif percentage<40:
    print("you're fail")


