from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.y_mov = 10
        self.x_mov = 10
        self.move_speed = 0.1

    def move_ball(self):
        new_x = self.xcor() + self.x_mov
        new_y = self.ycor() + self.y_mov
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_mov *= -1

    def bounce_x(self):
        self.x_mov *= -1



