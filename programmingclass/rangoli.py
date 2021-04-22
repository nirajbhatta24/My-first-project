import turtle
colors=['white','blue','yellow']
draw=turtle.Pen()
turtle.bgcolor('black')
draw.speed(50)

for a in range(360):
    draw.pencolor(colors[a%3])
    draw.width(a/100+1)
    draw.forward(a)
    draw.left(100)