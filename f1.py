from turtle import*
import colorsys
bgcolor("black")
tracer(100)

def draw():
    h=2
    for i in range(100):
        c=colorsys.hsv_to_rgb(h,1,1)
        h+=0.5
        up()
        goto(0,0)
        down()
        color("black")
        fillcolor (c)
        begin_fill()
        rt(98)
        circle(i,12)
        fd (290)
        fd(i)
        lt(29)
        for j in range(129):
            fd(i)
            circle(j,299,steps=4)
            end_fill()
draw()
time.sleep(100)
done()

    
