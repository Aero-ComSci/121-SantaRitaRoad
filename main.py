import turtle as tur
import random as rand
import time

win = tur.Screen()
win.title("Turtle Game")
win.bgcolor("lightblue")
win.setup(width=600, height=600)

player = tur.Turtle()
player.shape("turtle")
player.penup()
player.speed(0)
startcolor = "green"
player.color(startcolor)

points = 0
best = 0
sc = tur.Turtle()
sc.hideturtle()
sc.penup()
sc.goto(-200, 260)

def showscore():
    sc.clear()
    sc.write(f"Score: {points}", font=("Arial", 14, "normal"))

left = 5
lastclick = time.time()
timer = tur.Turtle()
timer.hideturtle()
timer.penup()
timer.goto(200, 260)

def update_timer():
    timer.clear()
    if left <= 0:
        end_game()
    else:
        timer.write(f"Time Left: {left}s")

colors = ["red", "blue", "yellow", "purple", "orange"]
sizes = [0.5, 1, 1.5, 2, 2.5]

def add_color():
    color = rand.choice(colors)
    player.color(color)
    player.stamp()
    player.color(startcolor)

def change_size():
    size = rand.choice(sizes)
    player.shapesize(size)

def move():
    x = rand.randint(-280, 280)
    y = rand.randint(-280, 280)
    player.goto(x, y)

def on_click(x, y):
    global points, best, left, lastclick
    if left > 0:
        points += 1
        if points > best:
            best = points
        lastclick = time.time()
        left = 5
        add_color()
        change_size()
        showscore()
        move()

def end_game():
    player.hideturtle()
    sc.goto(0, 0)
    sc.write(f"Game Over! High Score: {best}", align="center")
    win.update()

def countdown():
    global left
    left = max(0, 5 - int(time.time() - lastclick))
    update_timer()
    if left > 0:
        win.ontimer(countdown, 1000)

def start_game():
    global points, left
    points = 0
    left = 5
    lastclick = time.time()
    player.showturtle()
    sc.goto(-200, 260)
    showscore()
    countdown()
    move()

player.onclick(on_click)
start_game()
win.mainloop()
