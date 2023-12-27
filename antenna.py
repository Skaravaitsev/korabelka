import tkinter as tk
import Antenalib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def calculate_and_plot():
    frequency = float(entry_f.get())
    speed_of_sound = float(entry_c.get())
    distance_between_elements = float(entry_d.get())
    num_elements = int(entry_n.get())
    phi, XH = Antenalib.calculate_XH(frequency,speed_of_sound,distance_between_elements,num_elements)
    plt.plot(phi, XH)
    plt.grid(True)
    plt.title('Диаграмма направленности антенной решетки')
    plt.xlabel('Направление (градусы)')
    plt.ylabel('Чувствительность')
    plt.show()

window = tk.Tk()
window.title('Направленность')
window.geometry('900x700')

fnt = ('Times', 14, 'bold')

tk.Label(window, text='Частота сигнала, Гц', font=fnt).grid(column=0, row=0)
tk.Label(window, text='Скорость звука м/с', font=fnt).grid(column=0, row=1)
tk.Label(window, text='Расстояние между элементами, м', font=fnt).grid(column=0, row=2)
tk.Label(window, text='Количество элементов', font=fnt).grid(column=0, row=3)

entry_f = tk.Entry(window, font=fnt)
entry_f.grid(row=0, column=1)
entry_f.insert(0, '23000')

entry_c = tk.Entry(window, font=fnt)
entry_c.grid(row=1, column=1)
entry_c.insert(0, '1500')

entry_d = tk.Entry(window, font=fnt)
entry_d.grid(row=2, column=1)
entry_d.insert(0, '0.03')

entry_n = tk.Entry(window, font=fnt)
entry_n.grid(row=3, column=1)
entry_n.insert(0, '10')

result_label = tk.Label(window, text='', font=fnt)
result_label.grid(row=5, column=1)

calculate_button = tk.Button(window, text='Выполнить расчёт и построить график', font=fnt, command=calculate_and_plot)
calculate_button.grid(row=4, column=1)

tk.mainloop()
