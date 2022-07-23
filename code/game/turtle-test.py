from turtle import *

circle(50)
shape("turtle")
color("Red")

circle(100)
color("Blue")
circle(150)
color("Green")

circle(200)
color("Black")
shape("arrow")

for t in range(4):
    forward(100)
    left(90)
getscreen()._root.mainloop()


color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(70)
    if abs(pos()) < 1:
        break
end_fill()
done()
# https://michael0x2a.com/blog/turtle-examples
