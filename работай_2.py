import csv
from tkinter import *

master = Tk()

label1 = Label(master, text = 'Moment', relief = 'groove', width = 20)
label2 = Label(master, text = 'Command_0', relief = 'groove', width = 20)
label3 = Label(master, text = 'Return_0', relief = 'groove', width = 20)
label4 = Label(master, text = 'Command_2', relief = 'groove', width = 20)
label5 = Label(master, text = 'Return_1', relief = 'groove', width = 20)

вход_1 = Entry(master, relief = 'groove', width = 20)
вход_2 = Entry(master, relief = 'groove', width = 20)
вход_3 = Entry(master, relief = 'groove', width = 20)
вход_4 = Entry(master, relief = 'groove', width = 20)
вход_5 = Entry(master, relief = 'groove', width = 20)

def память():
    csvfile = open('память.csv', 'a')
    художник = csv.writer(csvfile)
    картина = str(вход_1.get()),str(вход_2.get()),str(вход_3.get()),str(вход_4.get()),str(вход_5.get())
    художник.writerow(картина)

def чисто():
    вход_1.delete(0,END)
    вход_2.delete(0,END)
    вход_3.delete(0,END)
    вход_4.delete(0,END)
    вход_5.delete(0,END)
                                 
кнопка_1 = Button(master, text = 'Label', relief = 'groove', width = 25, command=память)
кнопка_2 = Button(master, text = 'Clear', relief = 'groove', width = 25, command=чисто)


label1.grid( row = 1, column = 1, padx = 10 )
label2.grid( row = 1, column = 2, padx = 10 )
label3.grid( row = 1, column = 3, padx = 10 )
label4.grid( row = 1, column = 4, padx = 10 )
label5.grid( row = 1, column = 5, padx = 10 )

вход_1.grid( row = 2, column = 1, padx = 10 )
вход_2.grid( row = 2, column = 2, padx = 10 )
вход_3.grid( row = 2, column = 3, padx = 10 )
вход_4.grid( row = 2, column = 4, padx = 10 )
вход_5.grid( row = 2, column = 5, padx = 10 )

кнопка_1.grid( row = 6, column = 3, columnspan = 1)
кнопка_2.grid( row = 7, column = 3, columnspan = 1)

                
#Static Properties
master.title('Label') 
