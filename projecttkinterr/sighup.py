import tkinter
from tkinter import *

def new():
    

    top=Toplevel()
    top.geometry("800x600")
    top.config(bg="#FFFFFF")
    #top.iconbitmap("search.ico")
    imlab=Label(top,image=photo)
    imlab.place(x=0,y=0)
   
    #Label(top,image=photo7,bg="#FFFFFF").pack()


    Label(top,image=photo6,bg="#FFFFFF").place(x=685,y=295)

    #f=Frame(top,width=450,height=50,background="white")
    #f.place(x=150,y=250)
    def on_Enter1(e):
        search.delete(0,"end")
    def on_leave1(e):
        nam=search.get()
        if nam == "":
            mg.showwarning("WARNING","Enter Somethig")
            search.insert(0,"Search Here")

    def srch():
        a=search.get()
        #b="https://"+a+".com"
        b="https://www.google.com/search?q="+a+"&rlz=1C1ONGR_enIN1044IN1044&oq=hello&gs_lcrp=EgZjaHJvbWUqCQgAECMYJxiKBTIJCAAQIxgnGIoFMgoIARAuGLEDGIAEMg0IAhAAGIMBGLEDGIAEMg0IAxAuGIMBGLEDGIAEMg0IBBAuGIMBGLEDGIAEMg0IBRAuGIMBGLEDGIAEMg0IBhAuGIMBGLEDGIoFMgcIBxAAGIAEMgcICBAAGIAEMgoICRAuGLEDGIAE0gEMMjc4ODUzNWoxajE1qAIAsAIA&sourceid=chrome&ie=UTF-8"
        webview.create_window(a,b )
        webview.start()


    search=Entry(top,width=60,font=55)
    search.insert(0,"Search Here")
    search.bind('<FocusIn>',on_Enter1)
    search.bind('<FocusOut>',on_leave1)
    search.place(x=140,y=300)

    Label(top,image=photo6,bg="#FFFFFF").place(x=685,y=295)

    sbut=Button(top,text="SEARCH",bg="#57a1f8",fg="white",width=25,bd=0,command=srch)
    sbut.place(x=300,y=350)


    sbut1=Button(top,text="EXIT",bg="red",fg="white",width=25,bd=0,command=top.destroy)
    sbut1.place(x=300,y=400)
