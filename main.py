from turtle import Turtle, Screen
import random

colors = ['red', 'green', 'blue', 'orange', 'yellow', 'pink']
screen = Screen()
user_bet = screen.textinput(title='Make your bet!', prompt="Which colour of turtle will win? : ('red',"
                                                           " 'green', 'blue', 'orange', 'yellow', 'pink')")
screen.setup(800, 800)
clo = -1
position = -50
turtles = []

for _ in range(0, 6):
    clo += 1
    position += 50
    tur = Turtle(shape='turtle')
    tur.color(colors[clo])
    tur.penup()
    tur.goto(x=-350, y=-125 + position)
    turtles.append(tur)

is_on = True
while is_on:
    for tur in turtles:
        distance = random.randint(0, 10)
        tur.forward(distance)
        if tur.xcor() > 350:
            winner = tur.pencolor()
            is_on = False
            if user_bet != winner:
                Turtle().write(f"The winner is {winner} turtle.\nYour choice is {user_bet} turtle.You lose!",
                               align="center", font=("Arial", 20, "normal"))
            else:
                Turtle().write(f"The winner is {winner} turtle.\nYou win!",
                               align="center", font=("Arial", 20, "normal"))
Turtle().hideturtle()

screen.exitonclick()
