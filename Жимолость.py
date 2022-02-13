from PIL import Image,ImageTk
import tkinter

root = tkinter.Tk()
root.title("Жимолость")
root.minsize(width=900, height=350)
root.maxsize(width=1000, height=600)

frame1 = tkinter.Frame(root)
frame2 = tkinter.Frame(root)
frame3 = tkinter.Frame(root)

frame1.pack(side="left")
frame2.pack(side="left")
frame3.pack(side="left")


btn1 = tkinter.Button(frame1,text="Дельфиниум",font=("Segoe Print",10),bg="khaki2",fg="#2c2e0c",height=2,width=15)
btn1.pack(expand=1)
canvas1 = tkinter.Canvas(frame1, height=210, width=300)
image1 = Image.open('Pictures/дельфиниум.jpg')
photo1 = ImageTk.PhotoImage(image1)
image1 = canvas1.create_image(0, 0, anchor='nw',image=photo1)
canvas1.pack()

btn2 = tkinter.Button(frame2,text="Тимофеевка",font=("Segoe Print",10),bg="khaki2",fg="#2c2e0c",height=2,width=15)
btn2.pack(expand=1)
canvas2 = tkinter.Canvas(frame2, height=210, width=300)
image2 = Image.open('Pictures/тимофеевка.jpg')
photo2 = ImageTk.PhotoImage(image2)
image2 = canvas2.create_image(0, 0, anchor='nw',image=photo2)
canvas2.pack()

btn3 = tkinter.Button(frame3,text="Мятлик",font=("Segoe Print",10),bg="khaki2",fg="#2c2e0c",height=2,width=15)
btn3.pack(side="top")
canvas3 = tkinter.Canvas(frame3, height=210, width=300)
image3 = Image.open('Pictures/мятлик.jpg')
photo3 = ImageTk.PhotoImage(image3)
image3 = canvas3.create_image(0, 0, anchor='nw',image=photo3)
canvas3.pack()

root.mainloop()
