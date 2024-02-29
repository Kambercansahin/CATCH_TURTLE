import turtle
import time
import random

# Screen
screen_board = turtle.Screen()
screen_board.bgcolor("#CD81D3")
screen_board.title("Turtle Catch")

FONT = ("Verdana", 15, "normal")
score = 0
times_up = False
timer=20
scoreTurtle = turtle.Turtle()
countdownTurtle = turtle.Turtle()


def created_score_turtle():
    scoreTurtle.hideturtle()
    scoreTurtle.color("Dark Blue")
    scoreTurtle.penup()
    max_height = screen_board.window_height() / 2
    y = max_height * 0.9
    scoreTurtle.setposition(0, y)
    scoreTurtle.write(arg="Score: 0", move=False, align="center", font=FONT)


def TurtleCatch():
    global times_up
    GameTurtle = turtle.Turtle()
    GameTurtle.shape("turtle")
    GameTurtle.color("#E1F147")
    GameTurtle.shapesize(3)
    GameTurtle.penup()
    GameTurtle.speed(2)
    starting_time = time.time()

    def handling_click(x, y):
        global score
        if not times_up:
            if -30 < x - GameTurtle.xcor() < 30 and -30 < y - GameTurtle.ycor() < 30:
                score += 1
                scoreTurtle.clear()
                scoreTurtle.write(arg="Score:{}".format(score), font=FONT)

    turtle.onscreenclick(handling_click)

    while True:
        current_time = time.time()
        GameTurtle.hideturtle()
        time.sleep(1)
        max_height = screen_board.window_height() / 3
        max_width = screen_board.window_width() / 3
        x = random.randint(-max_height, max_width)
        y = random.randint(-max_height, max_width)

        GameTurtle.setposition(x, y)
        GameTurtle.showturtle()
        time.sleep(0.8)
        elapsed_time = current_time - starting_time
        if (elapsed_time-2) >timer:
            break

    times_up = True


def countdown(time):
    countdownTurtle.hideturtle()
    countdownTurtle.clear()
    countdownTurtle.penup()


    max_height = screen_board.window_height() / 2
    y = max_height * 0.9
    countdownTurtle.setposition(0, y-30)


    if time > 0:
        countdownTurtle.clear()
        countdownTurtle.write(arg="Time:{}".format(time), move=False, align="center", font=FONT)
        screen_board.ontimer(lambda: countdown(time - 1), 1000)
    else:
        countdownTurtle.clear()
        countdownTurtle.write(arg="TIME'S UP!", move=False, align="center", font=FONT)


created_score_turtle()
countdown(timer)
TurtleCatch()

turtle.mainloop()