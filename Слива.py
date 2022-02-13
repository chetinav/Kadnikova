from PIL import Image,ImageTk
import tkinter

root = tkinter.Tk()
root.title("Слива")
root.minsize(width=900, height=350)
root.maxsize(width=1000, height=600)

frame2 = tkinter.Frame(root)
frame3 = tkinter.Frame(root)

frame2.pack(side="left")
frame3.pack(side="right")


label2 = tkinter.Label(frame2, text="Мать-и-мачеха",font=("Segoe Print",10),bg="khaki2",fg="#2c2e0c").pack()
canvas2 = tkinter.Canvas(frame2, height=210, width=300)
image2 = Image.open('Pictures/мать-и-мачеха.jpg')
photo2 = ImageTk.PhotoImage(image2)
image2 = canvas2.create_image(0, 0, anchor='nw',image=photo2)
canvas2.pack()
btn2 = tkinter.Button(frame2,text="Мать-и-мачеха",font=("Segoe Print",10),bg="khaki2",fg="#2c2e0c",height=2,width=15)
btn2.pack(expand=1)

label3 = tkinter.Label(frame3,text="Мятлик луговой",font=("Segoe Print",10),bg="khaki2",fg="#2c2e0c").pack()
canvas3 = tkinter.Canvas(frame3, height=210, width=300)
image3 = Image.open('Pictures/мятлик.jpg')
photo3 = ImageTk.PhotoImage(image3)
image3 = canvas3.create_image(0, 0, anchor='nw',image=photo3)
canvas3.pack()
btn3 = tkinter.Button(frame3,text="Мятлик луговой",font=("Segoe Print",10),bg="khaki2",fg="#2c2e0c",height=2,width=15)
btn3.pack(side="top")

root.mainloop()
