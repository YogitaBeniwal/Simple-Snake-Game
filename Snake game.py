import turtle
import time
import random

wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor('yellow')
wn.setup(width=600, height=600)
wn.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('red')
head.penup()
a = random.randint(-290, 290)
b = random.randint(-290, 250)
head.goto(a, b)
head.direction = 'stop'

food = turtle.Turtle()
food.speed(0)
food.shape('triangle')
food.color('dark green')
food.penup()
food.goto(100, 100)

def move_up():
    if head.direction != 'down':
        head.direction = 'up'

def move_down():
    if head.direction != 'up':
        head.direction = 'down'

def move_left():
    if head.direction != 'right':
        head.direction = 'left'

def move_right():
    if head.direction != 'left':
        head.direction = 'right'

def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == 'left':
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == 'right':
        x = head.xcor()
        head.setx(x + 20)

wn.listen()

wn.onkeypress(move_up, 'w')
wn.onkeypress(move_up, 'W')
wn.onkeypress(move_up, 'Up')
wn.onkeypress(move_down, 's')
wn.onkeypress(move_down, 'S')
wn.onkeypress(move_down, 'Down')
wn.onkeypress(move_left, 'a')
wn.onkeypress(move_left, 'A')
wn.onkeypress(move_left, 'Left')
wn.onkeypress(move_right, 'd')
wn.onkeypress(move_right, 'D')
wn.onkeypress(move_right, 'Right')

delay = 0.2
segments = []
score = 0
high_score = 0

board = turtle.Turtle()
board.speed(0)
board.shape('square')
board.color('black')
board.penup()
board.hideturtle()
board.goto(0, 250)
board.write('Score : 0  High Score : 0', align='center', font=('arial', 20, 'bold'))

while True:
    wn.update()
    
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        a = random.randint(-290, 290)
        b = random.randint(-290, 250)
        head.goto(a, b)
        head.direction = 'stop'
        for segment in segments:
            segment.goto(400, 400)
        segments.clear()
        score = 0
        board.clear()
        board.write('Score : {}  High Score : {}'.format(score, high_score), align='center', font=('arial', 20, 'bold'))

    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 250)
        food.goto(x, y)
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('white')
        new_segment.penup()
        segments.append(new_segment)
        score += 10
        if score > high_score:
            high_score = score
        board.clear()
        board.write('Score : {}  High Score : {}'.format(score, high_score), align='center', font=('arial', 20, 'bold'))

    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
                
    move()

    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = 'stop'
            for segment in segments:
                segment.goto(400, 400)
            segments.clear()
            score = 0
            board.clear()
            board.write('Score : {}  High Score : {}'.format(score, high_score), align='center', font=('arial', 20, 'bold'))

    time.sleep(delay)
