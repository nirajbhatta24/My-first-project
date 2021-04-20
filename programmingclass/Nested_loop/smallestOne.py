"""
Given threeintegers, print the smallestone.(Threeintegers should be user input)


"""
a=int(input("enter a first number "))
b=int(input("enter a second number"))
c=int(input("enter a third number"))
if a<b and a<c:
    print("a is smallest number")
elif b<a and b<c:
    print(f"b is smallest number")
elif c<a and c<b:
    print(f"{c}is smallest number")