from turtle import Turtle, Screen
screen = Screen()
class Snake:

    def __init__(self):
        self.starting_position = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []
        self.structure()

    def structure(self):
        self.ibo = 1996
        for positions in self.starting_position:
            # print(i[0], i[1])

            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(positions)
            self.segments.append(new_segment)

    def move(self):
        # self.structure()
        print(len(self.segments))
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)

    def up(self):
        self.segments[0].setheading(90)

    def down(self):
        self.segments[0].setheading(270)

    def left(self):
        self.segments[0].setheading(180)

    def right(self):
        self.segments[0].setheading(0)







