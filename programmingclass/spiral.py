from turtle import *
for i in range(500): # this "for" loop will repeat these functions 500 times
    speed(0)
    color=['blue', 'purple', 'green', 'yellow','pink']

    pencolor(color[i % 5])
    forward(i)
    left(91)


done()
