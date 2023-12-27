import turtle
import time
import random

# Настройки окна
wn = turtle.Screen()
wn.title("Змейка")
wn.bgcolor("white")
wn.setup(width=600, height=600)
wn.tracer(0)

# Голова змеи
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("orange")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Еда для змеи
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Функции движения
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

# Управление змеей
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Функция для движения змеи
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Основной игровой цикл
while True:
    wn.update()

    # Проверка столкновения с границами
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Очистка сегментов
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()

    # Проверка столкновения с едой
    if head.distance(food) < 20:
        x = random.randint(-14, 14) * 20
        y = random.randint(-14, 14) * 20
        food.goto(x, y)

        # Добавление сегмента к змее
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

    # Движение сегментов тела змеи
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Проверка столкновения с телом змеи
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Очистка сегментов
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

    time.sleep(0.1)
