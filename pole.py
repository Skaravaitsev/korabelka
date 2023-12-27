import turtle as t


class Board:
    def __init__(self, N, size, brd):
        t.pendown()
        self.N = N
        self.size = size
        t.tracer(0)
        for i in range(N):
            for j in range(N):
                x = (i - N / 2) * size
                y = (j - N / 2) * size
                self.square(x, y, size, size, (i + j))
                if brd[i][j] > 0:
                    self.queen(x, y, size, (i+j))
        t.update()

    def square(self, x, y, size_x, size_y, c):  # создание квадрата
        t.penup()
        t.goto(x, y)
        t.pendown()
        if c % 2 == 0:
            color = 'white'
        else:
            color = 'black'
        t.color('black', color)
        t.begin_fill()
        for i in range(2):
            t.forward(size_x)
            t.left(90)
            t.forward(size_y)
            t.left(90)
        t.end_fill()
        t.tracer(0)

    def ferz(self, x, y, line, size, c):  # создание ферзя
        t.penup()
        t.goto(x + line[0][0]*self.size, y + line[0][1]*self.size)
        t.pendown()
        if c % 2 ==0:
            color = 'red'
            t.color('orange', color)
        else:
            color = 'orange'
            t.color('red', color)
        t.begin_fill()
        for coords in line:
            t.goto(x + coords[0]*self.size, y + coords[1]*self.size)
        t.end_fill()

    def queen(self, x, y, size, c): #вырисовываем ферзя
        self.square(x + 0.1*self.size, y + 0.1*self.size, 0.8*self.size, self.size*0.1, (c+1))
        line = [[0.2, 0.2], [0.2, 0.9], [0.35, 0.2], [0.5, 0.9], [0.65, 0.2], [0.8, 0.9], [0.8, 0.2], [0.2, 0.2]]
        self.ferz(x, y, line, self.size, (c+1))
