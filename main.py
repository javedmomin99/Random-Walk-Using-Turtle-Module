from turtle import Turtle, Screen
import random
tim = Turtle()
colours = [
    "CornFlowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
    "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"
]

directions = [0, 90, 180, 270]
pensize =[2,4,6,8,10]
speed = ["slow","slowest","normal","fast","fastest"]
for _ in range(0, 200):
    tim.color(random.choice(colours))
    tim.speed(random.choice(speed))
    tim.pensize(random.choice(pensize))
    tim.forward(30)
    tim.setheading(random.choice(directions))
