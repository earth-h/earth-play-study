import turtle

class Shape(object):
    def __init__(self, x, y, length, color):
        self.x = x
        self.y = y
        self.length = length
        self.color = color
    def setX(self, x):
        self.x = x
    def setY(self, y):
        self.y = y
    def setLength(self, length):
        self.length = length
    def setColor(self, color):
        self.color = color
    def getX(self):
        return self.x
    def getY(self):
        return self.y   
    def getLength(self):
        return self.length
    def getColor(self):
        return self.color

class Rectangle(Shape): #Shape 상속받아 생성자 구현
    def __init__(self, x, y, length, color):
        Shape.__init__(self, x, y, length, color)

class Triangle(Shape):
    def __init__(self, x, y, length, color):
        Shape.__init__(self, x, y, length, color)

class ClassDraw:
    def __init__(self, turtle):
        self.turtle = turtle

    def __del__(self):
        self.turtle.mainloop()

    def draw_rectangle(self, x, y, length, color):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.pencolor(color)
        for i in range(4):
            turtle.forward(length)
            turtle.left(90) # 사각형은 90도로 돌려야 함

    def draw_triangle(self, x, y, length, color):
        turtle.penup()
        turtle.goto(x, y) # (x,y) 좌표로 이동하여 그림
        turtle.pendown()
        turtle.pencolor(color)
        for i in range(3):
            self.turtle.forward(length)
            self.turtle.left(120) # 삼각형은 120도로 돌면 됨

turtle.shape('classic')
turtle.shapesize(2)

colorList = ['red', 'blue', 'navy', 'beige', 'black', 'pink', 'purple', 'green', 'orange', 'brown']

classDraw = ClassDraw(turtle)

for i in range(len(colorList)):
    if i % 2 == 0:
        triangle = Triangle(30 * (i + 1), 40 * (i + 1), 60, colorList[i])
        classDraw.draw_triangle(triangle.getX(), triangle.getY(), triangle.getLength(), triangle.getColor())
        rectangle = Rectangle(10 * (i + 1), 25 * (i + 1), 90, colorList[len(colorList) - 1 - i])
        classDraw.draw_rectangle(rectangle.getX(), rectangle.getY(), rectangle.getLength(), rectangle.getColor())
    else:
        triangle = Triangle(-10 * (i + 1), -15 * (i + 1), 60, colorList[i])
        classDraw.draw_triangle(triangle.getX(), triangle.getY(), triangle.getLength(), triangle.getColor())
        rectangle = Rectangle(-20 * (i + 1), -5 * (i + 1), 90, colorList[len(colorList) - 1 - i])
        classDraw.draw_rectangle(rectangle.getX(), rectangle.getY(), rectangle.getLength(), rectangle.getColor())
