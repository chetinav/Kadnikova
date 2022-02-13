from PIL import Image,ImageTk
import tkinter

root = tkinter.Tk()
root.title("Крыжовник")
root.minsize(width=900, height=350)
root.maxsize(width=1000, height=600)
frame1 = tkinter.Frame(root)
frame2 = tkinter.Frame(root)
frame3 = tkinter.Frame(root)
frame1.pack(side="left",)

frame3.pack(side="right")

label1 = tkinter.Label(frame1,text="Борщевик сибирский",font=("Segoe Print",10),bg="khaki2",fg="#2c2e0c").pack()
canvas1 = tkinter.Canvas(frame1, height=210, width=300)
image1 = Image.open('Pictures/борщевик.jpg')
photo1 = ImageTk.PhotoImage(image1)
image1 = canvas1.create_image(0, 0, anchor='nw',image=photo1)
canvas1.pack()
btn1 = tkinter.Button(frame1,text="Борщевик сибирский",font=("Segoe Print",10),bg="khaki2",fg="#2c2e0c",height=2,width=15)
btn1.pack(expand=1)


label3 = tkinter.Label(frame3,text="Мятлик луговой",font=("Segoe Print",10),bg="khaki2",fg="#2c2e0c").pack()
canvas3 = tkinter.Canvas(frame3, height=210, width=300)
image3 = Image.open('Pictures/мятлик.jpg')
photo3 = ImageTk.PhotoImage(image3)
image3 = canvas3.create_image(0, 0, anchor='nw',image=photo3)
canvas3.pack()
btn3 = tkinter.Button(frame3,text="Мятлик луговой",font=("Segoe Print",10),bg="khaki2",fg="#2c2e0c",height=2,width=15)
btn3.pack(side="top")

root.mainloop()
