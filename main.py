#Computational Mathematics
#Integrative Practice 2
#Victor Antonio Godínez Rodríguez A01339529
#Raúl González Cardona A01654995
#Gilberto Huesca Juárez (Head of the Computer Department at Tec de Monterrey CCM)

#Imports
from tkinter import Label, StringVar, Button, Entry, Tk, Frame, messagebox
from queue import Queue
from treelib import Node, Tree

#Definitions
def open_txt(texto): #Opening of the file's
    archivo = open(texto, 'r')
    text = archivo.read()
    archivo.close()
    return (text)

def del_right(): #Create and delete the left side of the interface
    right_display.set("This is the end")
    right_display2.set("Thank you! :)")
    result.set("")
    result2.set("")
    Label(tool_bar_2, textvariable = right_display).grid(row = 0, column = 0, padx = 5, pady = 5)
    Label(tool_bar_2, textvariable = right_display2).grid(row = 1, column = 0, padx = 5, pady = 5)
    del_entry()
    Button(tool_bar_2, text = '#QuedateEnCasa', command = quedateEnCasa).grid(row= 3, column = 0, padx = 5, pady = 5)

def quedateEnCasa():#Create a healthy warning for the professor 
    messagebox.showinfo(message = "Please stay at home! :)", title = "DANGER!!!")

def del_entry():#Delete the entries of the textbox
    entrada.set("")
    str_par.set("")
    int_par.set("")

def parsing_1():#Show the general information that user give us 
    te = entrada.get()
    text = open_txt(te)
    right_display.set(f"La lectura del {te} \n {text}")
    Label(tool_bar_2, textvariable = right_display).grid(row = 0, column = 0, padx = 5, pady = 5)
    t = str_par.get()
    i = int(int_par.get())
    right_display2.set(f"The String that you want to parsing: \n {t} \n With {i} levels")
    Label(tool_bar_2, textvariable = right_display2).grid(row = 1, column =0, padx = 5, pady =5)
    parsing_2(te, t, i)

def parsing_2(te, string, integer):#Create top-down parsing algorithm
    #Information recolected from the txt files
    productions = []
    test = open(te, 'r')
    grammmar = test.readlines()
    test.close()
    non_terminal = grammmar[0].replace("\n", '').split(',')
    terminal = grammmar[1].replace("\n", '').split(',')
    start_symbol = grammmar[2].replace("\n", '').split(',')
    for i in range(3, len(grammmar)):
        productions.append(grammmar[i].replace("\n", '').split('->'))

    q = []#list that helps us to create the queue
    q.append(start_symbol[0])#here we add the initial symbol to the list(queue)
    p = ""#String created by the algorithm
    level = 1#Define the starting level of the tree
    tree = {}#Create the dictionary to generate the tree

    while((len(q) != 0) and (p != string) and (level <= integer)):#Define the conditions to start creating the parsing tree
        q1 = q.pop()#We take out the first aggregate element and we save it in q1
        done = False#This variable will help us to stop the loop's
        level += 1#We start to increment the level tree
        while((done != True) and (p != string)):#Define the conditions that help us to compare the user string and the string in the algorithm
            if(q1.islower() == True):#Identifies if there's terminal symbols in q1 
                done = True#Stop the follow iteration
                if(q1 == string):#Compare the user string with the string from queue
                    p = q1#We assign the string to p
            else:#This continous if there's non terminal symbols        
                for j in range(len(productions)):#This runs the rules of the grammar
                    for i in range(len(q1)):#This runs the lenght of the string
                        if(q1[i] == productions[j][0]):#Check if the letter of the string in the position [i] is equal to some rule of the grammar
                            q2 = q1.replace(q1[i], productions[j][1])#This replace the letter of q1 in [i] to the production in [j][1]
                            tree.setdefault(q1, set()).add(q2)#Add the changes to the tree
                            if(q2[0].isupper() == True):#Check if the first letter of q2 is upper
                                q.append(q2)#If is upper we add it to the queue
                            else:#Search if the first letter of the second string is upper
                                if(q2 == string):#Look if q2 is equal to the string, if it's we save q2 into p
                                    p = q2
                                else:#If q2 isn't equal to the string
                                    len2 = len(q2)#We take out the length of q2
                                    str2 = ""#This will save the prefix of the user string
                                    q3 = ""#This will save the prefix of the algorithm string
                                    for k in range(len2):#This runs the length of q2
                                        if(q2[k].isupper() == True):#Check if there's an upper letter in the length of q2
                                            q3 = q2.replace(q2[k:len2], "")#q3 will save the replace from k to len2 and replace it with ""
                                            break
                                    if(len(q3) > len(string)):#Help to stop the loop if the length of q3 is higher of the length of string
                                        done = True
                                    else:#If the length of q3 is smaller of the length of string
                                        for k in range(len(q3)):#Help us to create the prefix of the user string
                                            str2 = str2+string[k]
                                        if(str2 == q3):#If the prefix of the user string is equal to the prefix of the algorithm string we add it to the queue
                                            q.append(q2)
                        else:
                            done = True#Ends the while
    
    result2.set(f"Tree: \n{tree}")#Print the dictionary in the interface
    if(p == string):#If the algorithm string is equal to the user string, the string is accepted.
        result.set("String accepted :)")
        Label(tool_bar_2, textvariable = result).grid(row = 0, column = 1, padx = 5, pady = 5)
        Label(tool_bar_2, textvariable = result2).grid(row = 1, column = 1, padx = 5, pady = 5)
        messagebox.showinfo(message = "Please check the terminal :)", title = "Tree!!!")
    elif(len(string) > integer):#If the length of the string is higher of the integer, there's no solution because the level need to be higher
        result.set("There's no solution because lower tree level .-.")
        Label(tool_bar_2, textvariable = result).grid(row = 0, column = 1, padx = 5, pady = 5)
        Label(tool_bar_2, textvariable = result2).grid(row = 1, column = 1, padx = 5, pady = 5)
        messagebox.showinfo(message = "Please check the terminal :)", title = "Tree!!!")
    else:
        result.set("String not accepted :(")#If don't match some of the last conditions, the string can't be accepted. 
        Label(tool_bar_2, textvariable = result).grid(row = 0, column = 1, padx = 5, pady = 5)
        Label(tool_bar_2, textvariable = result2).grid(row = 1, column = 1, padx = 5, pady = 5)
        messagebox.showinfo(message = "Please check the terminal :)", title = "Tree!!!")

    '''vars = []
    for i in range(integer):
        var = StringVar()      #Failed tried to print the tree in the interface
        vars.append(var)'''
    print_tree(tree,start_symbol[0], 0, vars)

def print_tree(tree, star_symbol, level, vars):#Implementation of the definition to print the tree
    '''for i in range(level):
        vars[i].set(f"numero i: {i} \t"*level+star_symbol)        #Failed tried to print the tree in the interface
        Label(tool_bar_2, textvariable =  vars[i]).grid(row = i, column = 2, padx = 5, pady = 5)'''
    print("\t"*level+star_symbol)
    for parent in sorted(tree.get(star_symbol, [])):
        print_tree(tree, parent, level+1, vars)

#Main
window = Tk()#Specifications for the tkinter interface 
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

window.mainloop()#Loop to help that the interface doesn't close