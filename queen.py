class Queen:

    def __init__(self, N):
        self.N = N
        self.board = []
        for i in range(N):
            line = []
            for j in range(N):
                line.append(0)
            self.board.append(line)
        self.find(0)

    def check(self, i, j):  # проверка возможно ли разместить ферзя
        for x in range(i):
            if self.board[x][j] == 1:  # проверка по горизонтали есть ли ферзь
                return False
        for x, y in zip(range(i, -1, -1), range(j, -1, -1)):  # проверка по диагонали есть ли ферзь
            if self.board[x][y] == 1:
                return False
        for x, y in zip(range(i, -1, -1), range(j, self.N, -1)):  # проверка по диагонали(обратная) есть ли ферзь
            if self.board[x][y] == 1:
                return False
        return True

    def find(self, column):  # поиск решения
        if column >= self.N:  #если все ферзи раставлены успешно, то выводим доску
            for q in self.board:
                print(q)
            print()
            return True
        for i in range(self.N):  #пробуем разместить ферзя в каждую строку
            if self.check(column, i):
                self.board[column][i] = 1 #Поместить ферзя в позицию (столбец, i).
                if self.find(column + 1): #попробуем разместить ферзей в следующих столбцах
                    return True
                self.board[column][i] = 0
        return False

    def read_board(self):
        return self.board
