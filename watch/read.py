f=open("xyz.txt", 'r')
y=open('abc.txt', 'w')
contain=f.read()
copied=contain
y.write(copied)
f.close()
y.close()
