import turtle
import random
import time
screen = turtle.Screen()
game_over=False
screen.bgcolor("light blue")
screen.title("Catch The Turtle")
FONT = ('Arial',30,"normal")
score=0
cd_turtle = turtle.Turtle()
#score turtle
score_turtle = turtle.Turtle()
t = turtle.Turtle()
t.hideturtle()
t.penup()
t.shapesize(3)
t.shape("turtle")
t.color("darkgreen")
def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.penup()
    score_turtle.color("dark blue")
    top_height = screen.window_height()/2
    y = top_height * 0.9
    score_turtle.goto(0,y)
    score_turtle.write("Score: 0",False,align="center",font=FONT)


def handle_click(x, y):
    global score
    score += 1
    score_turtle.clear()
    score_turtle.write(f"Score: {score}", False, align="center", font=FONT)
    print(f"Tıklanınca x: {x} ve y: {y}")
def randomly_turtle():
    if not game_over:
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        t.goto(x,y)
        t.showturtle()
        time.sleep(1.3)
        t.hideturtle()
        time.sleep(0.3)
        t.showturtle()
        t.onclick(handle_click)
        screen.ontimer(randomly_turtle, 1000)
        print(f"x: {x} , y: {y}")


def countdown(time=20):
    global game_over
    cd_turtle.hideturtle()
    cd_turtle.penup()
    cd_turtle.color("dark blue")
    top_height = screen.window_height()/2
    y = top_height * 0.8
    cd_turtle.goto(0,y)
    cd_turtle.clear()
    if time>0:
        cd_turtle.clear()
        cd_turtle.write(f"Time: {time}",False,align="center",font=FONT)
        screen.ontimer(lambda: countdown(time-1),1000)
    else:
        game_over = True
        hide_turtle()
        cd_turtle.clear()
        cd_turtle.write(f"Oyun Bitti Skorunuz: {score}",False,align="center",font=FONT)

def hide_turtle():
    t.hideturtle()




turtle.tracer(0)
setup_score_turtle()
countdown()
randomly_turtle()

turtle.tracer(1)

turtle.mainloop()