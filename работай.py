import csv
from tkinter import *

master = Tk()

label1 = Label(master, text = 'Moment', relief = 'groove', width = 20)
label2 = Label(master, text = 'Command_0', relief = 'groove', width = 20)
label3 = Label(master, text = 'Return_0', relief = 'groove', width = 20)
label4 = Label(master, text = 'Command_2', relief = 'groove', width = 20)
label5 = Label(master, text = 'Return_1', relief = 'groove', width = 20)

e1 = Entry(master, relief = 'groove', width = 20)
e2 = Entry(master, relief = 'groove', width = 20)
e3 = Entry(master, relief = 'groove', width = 20)
e4 = Entry(master, relief = 'groove', width = 20)
e5 = Entry(master, relief = 'groove', width = 20)

def память():
    csvfile = open('память.csv', 'a')
    writer = csv.writer(csvfile)
    patients = str(e1.get()),str(e2.get()),str(e3.get()),str(e4.get()),str(e5.get())
    writer.writerow(patients)

def чисто():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
                                 
button1 = Button(master, text = 'Label', relief = 'groove', width = 25, command=память)
button2 = Button(master, text = 'Clear', relief = 'groove', width = 25, command=чисто)


label1.grid( row = 1, column = 1, padx = 10 )
label2.grid( row = 1, column = 2, padx = 10 )
label3.grid( row = 1, column = 3, padx = 10 )
label4.grid( row = 1, column = 4, padx = 10 )
label5.grid( row = 1, column = 5, padx = 10 )

e1.grid( row = 2, column = 1, padx = 10 )
e2.grid( row = 2, column = 2, padx = 10 )
e3.grid( row = 2, column = 3, padx = 10 )
e4.grid( row = 2, column = 4, padx = 10 )
e5.grid( row = 2, column = 5, padx = 10 )

button1.grid( row = 6, column = 3, columnspan = 1)
button2.grid( row = 7, column = 3, columnspan = 1)

                
#Static Properties
master.title('Label') 
