import turtle

tina = turtle.Turtle()

screen = turtle.Screen()
screen.setup(500,500)
tina.shape("turtle")
tina_path = [1,2,3,4,5,]
tina_progress = 0


screen = turtle.Screen()
cam_colors = ["red","cyan","purple","blue","green"]

def show_anamtronics(cam_num):
    #tina show
    if(cam_num == tina_path[tina_progress]):
        tina.showturtle()
    else:
        tina.hideturtle()
def open_cam_1():
    print("cam 1 open")
    screen.bgcolor(cam_colors[0])
    show_anamtronics(1)
def open_cam_2():
    print("cam 2 open")
    screen.bgcolor(cam_colors[1])
    show_anamtronics(2)
def open_cam_3():
    print("cam 3 open")
    screen.bgcolor(cam_colors[2])
    show_anamtronics(3)
def open_cam_4():
    print("cam 4 open")
    screen.bgcolor(cam_colors[3])
    show_anamtronics(4)
def open_cam_5():
    print("cam 5 open")
    screen.bgcolor(cam_colors[4])
    show_anamtronics(5)
def exit_cam():
    print("office")
    screen.bgcolor("white")

exit_cam()

screen.listen()
screen.onkey(open_cam_1, "1")
screen.onkey(open_cam_2, "2")
screen.onkey(open_cam_3, "3")
screen.onkey(open_cam_4, "4")
screen.onkey(open_cam_5, "5")
screen.onkey(exit_cam, "0")

screen.ontimer

turtle.exitonclick()