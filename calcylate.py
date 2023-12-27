import tkinter as tk

string = '0'

def calc(s):
    global string
    if s == '=':   string = str(evalI(string))
    elif s =='c':  string = '0'


def update_input(value):                      # Функция для обновления текущего ввода
    current_input = input_label.get()
    input_label.delete(0, tk.END)
    input_label.insert(0, current_input + value)


def calculate():                              # Функция для вычисления результата
    try:
        result = eval(input_label.get())
        input_label.delete(0, tk.END)
        input_label.insert(0, str(result))
    except:
        input_label.delete(0, tk.END)
        input_label.insert(0, "Ошибка")

def clear_input():
    input_label.delete(0, tk.END)


window = tk.Tk()                              # Создаем главное окно
window.title("Калькулятор")


input_label = tk.Entry(window, width=50)      # Создаем поле для ввода
input_label.grid(row=0, column=0, columnspan=4)


buttons = [                                   # Создаем кнопки для цифр и операций
    ['1','2','3','C'],
        ['4','5','6','+'],
        ['7','8','9','-'],
        ['/','0','*','=']
]

row_val, col_val = 1, 0

for button in buttons:
    if button == 'c':
        tk.Button(window, text='c', padx=40, pady=40, command=clear_input).grid(row=row_val, column=col_val)
    elif button == '=':
        tk.Button(window, text=button, padx=210, pady=40, command=calculate).grid(row=row_val, column=col_val, columnspan=4)
    else:
        tk.Button(window, text=button, padx=40, pady=40, command=lambda b=button: update_input(b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Запускаем главный цикл программы
window.mainloop()
