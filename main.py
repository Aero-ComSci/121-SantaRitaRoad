import turtle as tur
import random
import time

# Screen setup
win = tur.Screen()
win.title("Turtle Game")
win.bgcolor("white")
win.setup(width=600, height=600)

# Turtle setup
player = tur.Turtle()
player.shape("turtle")
player.shapesize(1)
player.penup()
player.speed(0)

# Scoreboard setup
points = 0
best = 0
sc = tur.Turtle()
sc.hideturtle()
sc.penup()
sc.goto(-200, 260)

def showscore():
    sc.clear()
    sc.write(f"Score: {points}")

# Timer setup
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

# Move the turtle to a random position
def move():
    x = random.randint(-280, 280)
    y = random.randint(-280, 280)
    player.goto(x, y)

# Handle turtle clicks
def on_click(x, y):
    global points, best, left, lastclick
    if left > 0:
        points += 1
        if points > best:
            best = points
        lastclick = time.time()
        left = 5
        showscore()
        move()

# End the game
def end_game():
    player.hideturtle()
    sc.goto(0, 0)
    sc.write(f"Game Over! High Score: {best}", align="center")
    win.update()

# Countdown timer
def countdown():
    global left
    left = max(0, 5 - int(time.time() - lastclick))
    update_timer()
    if left > 0:
        win.ontimer(countdown, 1000)

# Start the game
def start():
    global points, left
    points = 0
    left = 5
    lastclick = time.time()
    player.showturtle()
    sc.goto(-200, 260)
    showscore()
    countdown()
    move()

# Bind click event and start
player.onclick(on_click)
start()
win.mainloop()
