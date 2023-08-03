import tkinter
from tkinter import *
from PIL import ImageTk,Image

top=Tk()
top.geometry("800x600")
top.config(bg="#E0FFFF")


img7=Image.open("g234.png")
img7=img7.resize((300,300))
photo7=ImageTk.PhotoImage(img7)
Label(top,image=photo7,bg="#E0FFFF").pack()

img8=Image.open("search.png")
img8=img8.resize((22,22))
photo6=ImageTk.PhotoImage(img8)
Label(top,image=photo6,bg="#E0FFFF").place(x=685,y=295)

#f=Frame(top,width=450,height=50,background="white")
#f.place(x=150,y=250)
def on_Enter1(e):
    search.delete(0,"end")
def on_leave1(e):
    nam=search.get()
    if nam == "":
        search.insert(0,"Search Here")


search=Entry(top,width=60,font=55)
search.insert(0,"Search Here")
search.bind('<FocusIn>',on_Enter1)
search.bind('<FocusOut>',on_leave1)
search.place(x=140,y=300)



sbut=Button(top,text="SEARCH",bg="#57a1f8",fg="white",width=25,bd=0)
sbut.place(x=300,y=350)


sbut1=Button(top,text="EXIT",bg="red",fg="white",width=25,bd=0,command=top.destroy)
sbut1.place(x=300,y=400)


top.mainloop()