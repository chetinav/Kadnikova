from PIL import Image,ImageTk
import tkinter

root = tkinter.Tk()
root.title("Морковь")
root.minsize(width=900, height=350)
root.maxsize(width=1000, height=600)
frame1 = tkinter.Frame(root)
frame2 = tkinter.Frame(root)

frame1.pack(side="left",)
frame2.pack(side="right")


label1 = tkinter.Label(frame1,text="Дельфиниум",font=("Segoe Print",10),bg="khaki2",fg="#2c2e0c").pack()
canvas1 = tkinter.Canvas(frame1, height=210, width=300)
image1 = Image.open('Pictures/дельфиниум.jpg')
photo1 = ImageTk.PhotoImage(image1)
image1 = canvas1.create_image(0, 0, anchor='nw',image=photo1)
canvas1.pack()
btn1 = tkinter.Button(frame1,text="Дельфиниум",font=("Segoe Print",10),bg="khaki2",fg="#2c2e0c",height=2,width=15)
btn1.pack(expand=1)

label2 = tkinter.Label(frame2, text="Тимофеевка",font=("Segoe Print",10),bg="khaki2",fg="#2c2e0c").pack()
canvas2 = tkinter.Canvas(frame2, height=210, width=300)
image2 = Image.open('Pictures/тимофеевка.jpg')
photo2 = ImageTk.PhotoImage(image2)
image2 = canvas2.create_image(0, 0, anchor='nw',image=photo2)
canvas2.pack()
btn2 = tkinter.Button(frame2,text="Тимофеевка",font=("Segoe Print",10),bg="khaki2",fg="#2c2e0c",height=2,width=15)
btn2.pack(expand=1)



root.mainloop()
