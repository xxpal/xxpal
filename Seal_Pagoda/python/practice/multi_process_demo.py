import turtle
# from threading import Thread

from multiprocessing import Process


def draw_circle():
    turtle.setup(width=500,height=500, startx=700, starty=100)
    turtle.circle(100)
    turtle.done()


def draw_rec():
    turtle.setup(width=500,height=500, startx=100, starty=100)
    turtle.penup()
    turtle.pendown()
    for i in range(4):
        turtle.forward(200)
        turtle.left(90) #90度
    turtle.end_fill()
    turtle.done()


if __name__ == '__main__':

    t1 = Process(target=draw_circle)
    t2 = Process(target=draw_rec)

    # t2 = Thread(target=draw_rec)
    # t1 = Thread(target=draw_circle)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
