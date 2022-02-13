from PIL import Image
from PIL import ImageTk
from tkinter import messagebox
from tkinter import *
import os
import sys
def show_info():
    s=''
    f=open("readme.txt",encoding="utf-8")
    for x in f:
        s=s+'\n'+x
    f.close()
    messagebox.showinfo("Как работать с программой", s)
def show_ms():
    s='О программе \n\n Справочник уральского садовода\n'
    s=s+ '© Кадникова Анна Дмитриевна МБОУ гимназия №18' 
    messagebox.showinfo("", s)
def yablonya():
    os.startfile(r'Яблоня.py')
def chernoplodka():
    os.startfile(r'Черноплодка.py')
def smorodina():
    os.startfile(r'Смородина.py')
def zhimolost():
    os.startfile(r'Жимолость.py')
def malina():
    os.startfile(r'Малина.py')
def sliva():
    os.startfile(r'Слива.py')
def kartofel():
    os.startfile(r'Картофель.py')
def svekla():
    os.startfile(r'Свекла.py')
def morkov():
    os.startfile(r'Морковь.py')
def luk():
    os.startfile(r'Лук.py')
def kryzhovnik():
    os.startfile(r'Крыжовник.py')
def klubnika():
    os.startfile(r'Клубника.py')
root=Tk()
root.iconbitmap('Pictures\icon.ico')
mainmenu = Menu(root) 
root.config(menu=mainmenu) 
 
sadmenu = Menu(mainmenu, tearoff=0)
sadmenu.add_command(label="Яблоня", command=yablonya)
sadmenu.add_command(label="Черноплодка", command=chernoplodka)
sadmenu.add_command(label="Смородина", command=smorodina)
sadmenu.add_command(label="Жимолость", command=zhimolost)
sadmenu.add_command(label="Малина", command=malina)
sadmenu.add_command(label="Слива", command=sliva)
sadmenu.add_command(label="Крыжовник", command=kryzhovnik)


omenu = Menu(mainmenu, tearoff=0)
omenu.add_command(label="Морковь", command=morkov)
omenu.add_command(label="Лук", command=luk)
omenu.add_command(label="Свекла", command=svekla)
omenu.add_command(label="Картофель", command=kartofel)
omenu.add_command(label="Клубника", command=klubnika)

exmenu = Menu(mainmenu, tearoff=0)
exmenu.add_command(label="Выход", command=root.destroy)

helpmenu = Menu(mainmenu, tearoff=0)
helpmenu.add_command(label="Помощь", command=show_info)
helpmenu.add_command(label="О программе",command=show_ms )

mainmenu.add_cascade(label="Сад",menu=sadmenu)
mainmenu.add_cascade(label="Огород",menu=omenu)
mainmenu.add_cascade(label="Справка",menu=helpmenu) #Я не понимаю, почему он выводит не по команде, с садом и огородом все было хорошо даже чернз меню все работает
mainmenu.add_cascade(label="Выход",menu=exmenu)

frame1=Frame(root)
frame2=Frame(root)
root.minsize(width=300, height=600)
root.maxsize(width=800, height=600)
root["bg"]="#c3e850"
root.title("Справочник уральского садовода")
label1=Label(root, text="Выберите садовую культуру, котоую вы хотите посадить: \nВы узнаете, вблизи каких растений стоит её расположить ",
             font=("Monotype Corsiva", 14),
             bg="#c3e850")
label1.pack()
frame1.pack(side=LEFT)
frame2.pack(side=RIGHT)

btn1 = Button(frame1,text="Яблоня",
              command=yablonya,
              font=("Segoe Print",10),
              bg="khaki2",
              fg="#2c2e0c",
              height=2,width=15)
btn1.pack(expand=1)

btn2 = Button(frame1,text="Черноплодка",
              command= chernoplodka,
              font=("Segoe Print", 10),
              bg="khaki2",
              fg="#2c2e0c",
              height=2,width=15)
btn2.pack(expand=1)
 
btn3 = Button(frame1,text="Смородина",
              command= smorodina,
              font=("Segoe Print", 10),
              bg="khaki2",
              fg="#2c2e0c",
              height=2,width=15)
btn3.pack(expand=1)

btn4 = Button(frame1,text="Жимолость",
              command= zhimolost,
              font=("Segoe Print", 10),
              bg="khaki2",
              fg="#2c2e0c",
              height=2,width=15)
btn4.pack(expand=1)

btn5 = Button(frame1,text="Малина",
              command= malina,
              font=("Segoe Print", 10),
              bg="khaki2",
              fg="#2c2e0c",
              height=2,width=15)
btn5.pack(expand=1)

btn6 = Button(frame1,text="Слива",
              command= sliva,
              font=("Segoe Print", 10),
              bg="khaki2",
              fg="#2c2e0c",
              height=2,width=15)
btn6.pack(expand=1)

btn7 = Button(frame2,text="Морковь",
              command=morkov,
              font=("Segoe Print",10),
              bg="khaki2",
              fg="#2c2e0c",
              height=2,width=15)
btn7.pack(expand=1)

btn8 = Button(frame2,text="Лук",
              command=luk,
              font=("Segoe Print",10),
              bg="khaki2",
              fg="#2c2e0c",
              height=2,width=15)
btn8.pack(expand=1)

btn9 = Button(frame2,text="Свекла",
              command=svekla,
              font=("Segoe Print",10),
              bg="khaki2",
              fg="#2c2e0c",
              height=2,width=15)
btn9.pack(expand=1)

btn10 = Button(frame2,text="Картофель",
              command=kartofel,
              font=("Segoe Print",10),
              bg="khaki2",
              fg="#2c2e0c",
              height=2,width=15)
btn10.pack(expand=1)

btn11 = Button(frame2,text="Клубника",
              command=klubnika,
              font=("Segoe Print",10),
              bg="khaki2",
              fg="#2c2e0c",
              height=2,width=15)
btn11.pack(expand=1)

btn12 = Button(frame2,text="Крыжовник",
              command=kryzhovnik,
              font=("Segoe Print",10),
              bg="khaki2",
              fg="#2c2e0c",
              height=2,width=15)
btn12.pack(expand=1)


root.mainloop()
