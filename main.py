from turtle import Turtle, Screen
import random
screen = Screen()

race_on = False

screen.setup(500, 400)
bet = screen.textinput("BETS", "Place your bets, which turtle will win? (Enter a color)")
colors = ["red","orange","yellow","green","blue","purple"]
turtles = []
y = -100

for turtle in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y= y)
    y+=40
    new_turtle.color(colors[turtle])
    turtles.append(new_turtle)

if bet:
    race_on = True

while race_on:
    for turtle in turtles:
        distance = random.randint(0,10)
        turtle.forward(distance)
        if turtle.xcor() > 230:
            race_on = False
            winner = turtle.pencolor()
            if bet == winner:
                print(f'{bet} is the winner! Here is 2 million dollars')
            else:
                print(f'{winner} is the winner, not {bet}! You lose 2 million dollars')

screen.exitonclick()