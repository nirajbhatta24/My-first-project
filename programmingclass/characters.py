'''

If name is less than 3 characters long- name must be at least 3 characters otherwise if it's more than 50 characters -
name must be maximum of 50 characters otherwise - name looks good!

'''

name=input("Enter a name: ")
len_name=len(name)
if len_name<3:
    print("Name must be at least 3 characters ")
elif len_name>10:
    print("Name must be maximum of 10 characters ")
else:
    print("Name looks good")