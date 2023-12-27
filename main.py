import turtle as t
import pole
import queen

N = 5
b = queen.Queen(N)
br = b.read_board()
a = pole.Board(N, 70, br)
t.mainloop()
