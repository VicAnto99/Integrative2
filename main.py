#Computational Mathematics
#Integrative Practice 2
#Victor Antonio Godínez Rodríguez A01339529
#Raúl González Cardona A01654995
#Gilberto Huesca Juárez (Head of the Computer Department at Tec de Monterrey CCM)

#Imports
from tkinter import Label, StringVar, Button, Entry, Tk, Frame, messagebox
from queue import Queue

#Definitions
def open_txt(texto): #Apertura de archivo
    archivo = open(texto, 'r')
    text = archivo.read()
    archivo.close()
    return (text)

def del_right():
    right_display.set("This is the end")
    right_display2.set("Thank you! :)")
    result.set("")
    result2.set("")
    Label(tool_bar_2, textvariable = right_display).grid(row = 0, column = 0, padx = 5, pady = 5)
    Label(tool_bar_2, textvariable = right_display2).grid(row = 1, column = 0, padx = 5, pady = 5)
    del_entry()
    Button(tool_bar_2, text = '#QuedateEnCasa', command = quedateEnCasa).grid(row= 3, column = 0, padx = 5, pady = 5)

def quedateEnCasa():
    messagebox.showinfo(message = "Please stay at home! :)", title = "DANGER!!!")

def del_entry():
    entrada.set("")
    str_par.set("")
    int_par.set("")

def parsing_1():
    te = entrada.get()
    text = open_txt(te)
    right_display.set(f"La lectura del {te} \n {text}")
    Label(tool_bar_2, textvariable = right_display).grid(row = 0, column = 0, padx = 5, pady = 5)
    t = str_par.get()
    i = int(int_par.get())
    right_display2.set(f"The String that you want to parsing: \n {t} \n With {i} levels")
    Label(tool_bar_2, textvariable = right_display2).grid(row = 1, column =0, padx = 5, pady =5)
    parsing_2(te, t, i)

def parsing_2(te, string, integer):
    productions = []
    test = open(te, 'r')
    grammmar = test.readlines()
    test.close()
    non_terminal = grammmar[0].replace("\n", '').split(',')
    terminal = grammmar[1].replace("\n", '').split(',')
    start_symbol = grammmar[2].replace("\n", '').split(',')
    for i in range(3, len(grammmar)):
        productions.append(grammmar[i].replace("\n", '').split('->'))

    q = []
    q.append(start_symbol[0])
    p = ""
    level = 1
    tree = {}

    while((len(q) != 0) and (p != string) and (level <= integer)):
        q1 = q.pop()
        done = False
        level += 1
        while((done != True) and (p != string)):
            if(q1.islower() == True):
                done = True
                if(q1 == string):
                    p = q1
            else:        
                for j in range(len(productions)):
                    for i in range(len(q1)):
                        if(q1[i] == productions[j][0]):
                            q2 = q1.replace(q1[i], productions[j][1])
                            tree.setdefault(q1, set()).add(q2)
                            if(q2[0].isupper() == True):
                                q.append(q2)
                            else:
                                if(q2 == string):
                                    p = q2
                                else:
                                    len2 = len(q2)
                                    str2 = ""
                                    q3 = ""
                                    for k in range(len2):
                                        if(q2[k].isupper() == True):
                                            q3 = q2.replace(q2[k:len2], "")
                                            break
                                    if(len(q3) > len(string)):
                                        done = True
                                    else:
                                        for k in range(len(q3)):
                                            str2 = str2+string[k]
                                        if(str2 == q3):
                                            q.append(q2)
                        else:
                            done = True
    
    result2.set(f"Tree: \n{tree}")
    if(p == string):
        result.set("String accepted :)")
        Label(tool_bar_2, textvariable = result).grid(row = 0, column = 1, padx = 5, pady = 5)
        Label(tool_bar_2, textvariable = result2).grid(row = 1, column = 1, padx = 5, pady = 5)
    elif(len(string) > integer):
        result.set("There's no solution because lower tree level .-.")
        Label(tool_bar_2, textvariable = result).grid(row = 0, column = 1, padx = 5, pady = 5)
        Label(tool_bar_2, textvariable = result2).grid(row = 1, column = 1, padx = 5, pady = 5)
    else:
        result.set("String not accepted :(")
        Label(tool_bar_2, textvariable = result).grid(row = 0, column = 1, padx = 5, pady = 5)
        Label(tool_bar_2, textvariable = result2).grid(row = 1, column = 1, padx = 5, pady = 5)

#Main
window = Tk()
window.title("Integrative practice 2")
window.maxsize(2000, 610)
window.config(bg = "skyblue")

#Global variables
entrada = StringVar()
right_display = StringVar()
right_display.set("Welcome! :)")
str_par = StringVar()
int_par = StringVar()
right_display2 = StringVar()
result = StringVar()
result2 = StringVar()

#Left_Frame_design and Right_Frame_design
left_frame = Frame(window, width = 300, height = 590, bg='grey')
left_frame.grid(row = 0, column = 0, padx = 10, pady = 10)
right_frame = Frame(window, width = 670, height = 590, bg='grey')
right_frame.grid(row = 0, column = 1, padx = 10, pady = 10)

#Left_Frame
Label(left_frame, text = "INSTRUCTIONS").grid(row = 0, column = 0, padx = 5, pady = 5)
tool_bar = Frame(left_frame, width = 280, height = 550)
tool_bar.grid(row = 2, column = 0, padx = 5, pady = 5)
Label(tool_bar, text = "Insert in the next text box the name of your txt \n Example: test1.txt").grid(row = 0, column = 0, padx = 5, pady = 5)
Entry(tool_bar, textvariable = entrada, width = 46).grid(row = 1, column = 0, padx = 5, pady = 5)
Label(tool_bar, text = "Enter a string for parsing").grid(row = 2, column = 0, padx = 5, pady = 5)
Entry(tool_bar, textvariable = str_par, width = 46).grid(row = 3, column = 0, padx = 5, pady = 5)
Label(tool_bar, text = "Enter the integer of levels for your tree").grid(row = 4, column = 0, padx = 5, pady = 5)
Entry(tool_bar, textvariable = int_par, width = 46).grid(row = 5, column = 0, padx = 5, pady = 5)
Button(tool_bar, text = "Parsing", command = parsing_1).grid(row= 6, column = 0, padx = 5, pady = 5)
Label(tool_bar, text = "If you want to refresh the .txt click the 'refresh' button").grid(row = 7, column = 0, padx = 5, pady = 5)
Button(tool_bar, text='Refresh', command = del_right).grid(row=8, column = 0, padx = 5, pady = 5)

#Right_Frame
tool_bar_2 = Frame(right_frame, width = 650, height = 580)
tool_bar_2.grid(row = 2, column = 0, padx = 5, pady = 5)
Label(tool_bar_2, textvariable = right_display).grid(row = 0, column = 0, padx = 5, pady = 5)
Label(tool_bar_2, textvariable = right_display2).grid(row = 1, column = 0, padx = 5, pady = 5)

window.mainloop()