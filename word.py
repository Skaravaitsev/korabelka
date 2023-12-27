from tkinter import *
from tkinter import filedialog
from tkinter import messagebox



def new():                                    # функция создания нового файла
   text_box.delete(1.0, END)



def savefile():                               # функция сохранения файла
    name = filedialog.asksaveasfilename()
    try:
        file = open(name, 'w')
        file.write(text_box.get("1.0", END))
        file.close()
    except:
        print('You lost this file((((')



def openfile():                               # функция открытия файла
    name = filedialog.asksaveasfilename()
    try:
        file = open(name, 'r')
        text_box.delete(1.0, END)
        text_box.insert('1.0', file.read())
    except:
        print('test_text2.txt')



def about():                                  # о программе
    messagebox.showinfo('About programm', 'Bloknot')

def helpwin():                                # окно 'помощь'
    helper = Toplevel(ws)
    helper.title('Helper file...')
    text_help = Text(helper)
    text_help.pack(fill = 'both', expand = True)
    file = open('test_text.txt', 'r')
    text_help.delete(1.0, END)
    text_help.insert('1.0', file.read())



###################################



ws = Tk()
ws.title('Bloknot')
ws.geometry('720x720')

mainmenu = Menu()                             # строка меню
filemenu = Menu(mainmenu, tearoff=1)
filemenu.add_command(label = 'Open...', command = openfile)     # каскад 'File'
filemenu.add_command(label = 'New', command = new)
filemenu.add_command(label = 'Save...', command = savefile)
filemenu.add_command(label = 'Exit', command = ws.destroy)

helpmenu = Menu(mainmenu, tearoff = 1)                          # каскад 'Synopsis'
helpmenu.add_command(label = 'Help', command = helpwin)
helpmenu.add_command(label = 'About programm', command = about)

mainmenu.add_cascade(label = 'File', menu = filemenu)
mainmenu.add_cascade(label = 'Synopsis', menu = helpmenu)

ws.config(menu = mainmenu)

text_box = Text(ws)
scrollbar = Scrollbar(text_box)                                 # прописываем скролбар
scrollbar['command'] = text_box.yview
text_box['yscrollcommand'] = scrollbar.set
text_box.pack(fill= 'both', expand = True)
scrollbar.pack(side = 'right', fill = 'y')


Button(text = 'Close', command = ws.destroy).pack(side = 'left')     # кнопка закрытия
ws.mainloop()



###################################
