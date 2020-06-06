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
    in_3 = Label(tool_bar_2, textvariable = right_display).grid(row = 0, column = 0, padx = 5, pady = 5)
    in_6 = Label(tool_bar_2, textvariable = right_display2).grid(row = 1, column = 0, padx = 5, pady = 5)
    del_entry()
    btn_4 = Button(tool_bar_2, text = '#QuedateEnCasa', command = quedateEnCasa).grid(row= 3, column = 0, padx = 5, pady = 5)

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
    in_3 = Label(tool_bar_2, textvariable = right_display).grid(row = 0, column = 0, padx = 5, pady = 5)
    t = str_par.get()
    i = int(int_par.get())
    right_display2.set(f"The String that you want to parsing: \n {t} \n With {i} levels")
    in_6 = Label(tool_bar_2, textvariable = right_display2).grid(row = 1, column =0, padx = 5, pady =5)
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

    que = []
    que.append(start_symbol[0])
    p = ' '
    level = 1
    temp = {}
   
    while ((len(que) != 0) and (p != string) and (level <= integer)):
        done = False
        q = que.pop()
        level += 1
        while((done != True) and (p != string) and (level <= integer)):
            #for i in range(len(productions)):
                for i in range(len(q)):
                    if(q[i].isupper()):
                        non = q[i]
                    if(non == ''):
                        done = True
                    else:
                        q2 = ''
                        con = ''
                        for j in range(len(productions)):
                            q2 = q. 
        
    '''que = Queue(maxsize = 0)
    que.append(start_symbol[0])
    p = ''
    level = 1
    done = False
    print("Afuera del ciclo antes del ciclo \n")
    while ((que.empty() != True) and (p != string) and (level <= integer)):
        print("Adentro 1\n")
        done = False
        q = que.get()
        level+=1
        while((done != True) and (p != string) and (level <= integer)):
            print("Adentro 2\n")
            for i in range(len(q)):
                print(f"Adentro del primer if {i}\n")
                if(q[i].isupper()):
                    print(f"Adentro del primer for {q[i]}\n")
                    non = q[i]
                if(non == ''):
                    done = True
                else:
                    q3 = ''
                    con = ''
                    for j in range(len(productions)):
                        #BUscar un tipo index off
                        print(f"Adentro del segundo for {j}\n")
                        q2 = q.replace(non, productions[j][1])
                        print(f"Adentro del if que cambia al {non} con {productions[j][0]} en {productions[j][1]}\n")
                        print(f"{q2}\n")
                        if(q2[0].isupper()):
                            que.append(q2)
                            done = True
                            print(f"metida en la cola {q2}")
                        else:
                            for k in range(len(q2)):
                                if(q2[0].islower()):
                                    q3 = q3 + q2[k]
                                    print(f"{q3}\n")
                            if(q3 == string):
                                p = q3
                            else:
                                for l in range(len(q3)):
                                    con = con + q3[l]
                                    print(f"{con} comparacion")
                                if(con == q3):
                                    que.append(q3)
                                    print(f"{con} comparacion cola")
                                else:
                                    print(f"{con} comparacion Done")
                                    done = True
    print("Afuera del ciclo despues del ciclo\n")
    if(p == string):
        result.set("String accepted")
        in_7 = Label(tool_bar_2, textvariable = result).grid(row = 0, column = 1, padx = 5, pady =5)
    else:
        result.set("String is not accepted")
        in_7 = Label(tool_bar_2, textvariable = result).grid(row = 0, column = 1, padx = 5, pady =5)'''        

#Main
window = Tk()
window.title("Integrative practice 2")
window.maxsize(1010, 610)
window.config(bg = "skyblue")

#Global variables
entrada = StringVar()
right_display = StringVar()
right_display.set("Welcome! :)")
str_par = StringVar()
int_par = StringVar()
right_display2 = StringVar()
result = StringVar()

#Left_Frame_design and Right_Frame_design
left_frame = Frame(window, width = 300, height = 590, bg='grey')
left_frame.grid(row = 0, column = 0, padx = 10, pady = 10)
right_frame = Frame(window, width = 670, height = 590, bg='grey')
right_frame.grid(row = 0, column = 1, padx = 10, pady = 10)

#Left_Frame
in_1 = Label(left_frame, text = "INSTRUCTIONS").grid(row = 0, column = 0, padx = 5, pady = 5)
tool_bar = Frame(left_frame, width = 280, height = 550)
tool_bar.grid(row = 2, column = 0, padx = 5, pady = 5)
in_2 = Label(tool_bar, text = "Insert in the next text box the name of your txt \n Example: test1.txt").grid(row = 0, column = 0, padx = 5, pady = 5)
txt_1 = Entry(tool_bar, textvariable = entrada, width = 46).grid(row = 1, column = 0, padx = 5, pady = 5)
in_5 = Label(tool_bar, text = "Enter a string for parsing").grid(row = 2, column = 0, padx = 5, pady = 5)
txt_2 = Entry(tool_bar, textvariable = str_par, width = 46).grid(row = 3, column = 0, padx = 5, pady = 5)
in_7 = Label(tool_bar, text = "Enter the integer of levels for your tree").grid(row = 4, column = 0, padx = 5, pady = 5)
txt_3 = Entry(tool_bar, textvariable = int_par, width = 46).grid(row = 5, column = 0, padx = 5, pady = 5)
but_3 = Button(tool_bar, text = "Parsing", command = parsing_1).grid(row= 6, column = 0, padx = 5, pady = 5)
in_4 = Label(tool_bar, text = "If you want to refresh the .txt click the 'refresh' button").grid(row = 7, column = 0, padx = 5, pady = 5)
but_2 = Button(tool_bar, text='Refresh', command = del_right).grid(row=8, column = 0, padx = 5, pady = 5)

#Right_Frame
tool_bar_2 = Frame(right_frame, width = 650, height = 580)
tool_bar_2.grid(row = 2, column = 0, padx = 5, pady = 5)
in_3 = Label(tool_bar_2, textvariable = right_display).grid(row = 0, column = 0, padx = 5, pady = 5)
in_6 = Label(tool_bar_2, textvariable = right_display2).grid(row = 1, column = 0, padx = 5, pady = 5)

window.mainloop()

