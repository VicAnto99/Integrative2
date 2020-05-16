#Imports
from tkinter import *

#Definitions
def read():
    t = entrada.get()
    text = open_txt(t)
    print(text)



#Apertura de archivo
def open_txt(texto):
    archivo = open(texto, 'r')
    text = archivo.read()
    archivo.close()

    return (text)


#Main

window = Tk()
window.title("Integrative practice 2")
window.maxsize(1010, 610)
window.config(bg = "skyblue")

entrada = StringVar()

#Left_Frame_design
left_frame = Frame(window, width = 300, height = 590, bg='grey')
left_frame.grid(row = 0, column = 0, padx = 10, pady = 10)
in_1 = Label(left_frame, text = "INSTRUCTIONS").grid(row = 0, column = 0, padx = 5, pady = 5)
tool_bar = Frame(left_frame, width = 280, height = 550)
tool_bar.grid(row = 2, column = 0, padx = 5, pady = 5)
in_2 = Label(tool_bar, text = "Insert in the next text box the name of your txt \n Example: test1.txt").grid(row = 0, column = 0, padx = 5, pady = 5)

txt = Entry(tool_bar, textvariable=entrada, width = 46).grid(row = 2, column = 0, padx = 5, pady = 5)
but_1 = Button(tool_bar, text='Read', command = read).grid(row=3)
in_3 = Label(tool_bar, textvariable = txt).grid(row = 3, column = 1)

#Right_Frame_design
right_frame = Frame(window, width = 670, height = 590, bg='grey')
right_frame.grid(row = 0, column = 1, padx = 10, pady = 10)

window.mainloop()