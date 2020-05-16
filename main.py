#Imports
from tkinter import *

#Definitions
def read(): #Lectura de la entrada
    t = entrada.get()
    text = open_txt(t)
    in_3 = Label(right_frame, text = f"La lectura del {entrada.get()} \n {text}").grid(row = 0, column = 0, padx = 5, pady = 5)

def open_txt(texto): #Apertura de archivo
    archivo = open(texto, 'r')
    text = archivo.read()
    archivo.close()
    return (text)

def del_right():
    in_3.after(1000 , in_3.master.destroy)
    del_entry()

def del_entry():
    txt.set("")

#Main
window = Tk()
window.title("Integrative practice 2")
window.maxsize(1010, 610)
window.config(bg = "skyblue")

#Global variables
entrada = StringVar()

#Left_Frame_design
left_frame = Frame(window, width = 300, height = 590, bg='grey')
left_frame.grid(row = 0, column = 0, padx = 10, pady = 10)
in_1 = Label(left_frame, text = "INSTRUCTIONS").grid(row = 0, column = 0, padx = 5, pady = 5)
tool_bar = Frame(left_frame, width = 280, height = 550)
tool_bar.grid(row = 2, column = 0, padx = 5, pady = 5)
in_2 = Label(tool_bar, text = "Insert in the next text box the name of your txt \n Example: test1.txt").grid(row = 0, column = 0, padx = 5, pady = 5)
txt = Entry(tool_bar, textvariable = entrada, width = 46).grid(row = 2, column = 0, padx = 5, pady = 5)
but_1 = Button(tool_bar, text='Read', command = read).grid(row=3)
in_4 = Label(tool_bar, text = "If you want to refresh the .txt click the 'refresh' button").grid(row = 4, column = 0, padx = 5, pady = 5)
but_2 = Button(tool_bar, text='Refresh', command = del_right).grid(row=5)

#Right_Frame_design
right_frame = Frame(window, width = 670, height = 590, bg='grey')
right_frame.grid(row = 0, column = 1, padx = 10, pady = 10)
in_3 = Label(right_frame, text = "")

window.mainloop()