
from tkinter.messagebox import askyesno
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox as mg
import webbrowser
import webview

root=Tk()
root.geometry("800x600")
root.config(bg="#FFFFFF")
#root.iconbitmap("g234.ico")
root.title("G2 PEDIA")
#root.overrideredirect(True)
#root.attributes('-alpha',0.9)################
#image
img5=Image.open("login.png")
img5=img5.resize((300,300))
photo5=ImageTk.PhotoImage(img5)
Label(root,image=photo5,bg="#FFFFFF").pack()

img=Image.open("sm3.jpg")
img=img.resize((800,600))
photo=ImageTk.PhotoImage(img)


img8=Image.open("search.png")
img8=img8.resize((22,22))
photo6=ImageTk.PhotoImage(img8)

img7=Image.open("g234.png")
img7=img7.resize((300,300))
photo7=ImageTk.PhotoImage(img7)


def on_Enter(e):
    n1.delete(0,"end")
def on_leave(e):
    nam=n1.get()
    if nam == "":
        n1.insert(0,"Name")

def on_Enter1(e):
    p1.delete(0,"end")
def on_leave1(e):
    nam=p1.get()
    if nam == "":
        p1.insert(0,"Password")

def v():
    n=input()
    a="www."+n+".com"
    webbrowser.open(a)



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



def newsign():
    top1=Toplevel()
    top1.geometry("800x600")
    top1.config(bg="#FFFFFF")
    #root.iconbitmap("g234.ico")
    top1.title("G2 PEDIA")
    #root.overrideredirect(True)
    #root.attributes('-alpha',0.9)################
    #image
    img5=Image.open("login.png")
    img5=img5.resize((300,300))
    photo5=ImageTk.PhotoImage(img5)
    Label(top1,image=photo5,bg="#FFFFFF").pack()



    def on_Enter(e):
        n1.delete(0,"end")
    def on_leave(e):
        nam=n1.get()
        if nam == "":
            n1.insert(0,"Name")

    def on_Enter1(e):
        p1.delete(0,"end")
    def on_leave1(e):
        nam=p1.get()
        if nam == "":
            p1.insert(0,"Password")

    f=Frame(top1,width=450,height=350,bg="#FFFFFF")
    f.place(x=75,y=350)
    #entry
    n1=Entry(top1,border=0,bg="#FFFFFF",width=25,font=(20))
    n1.insert(0,"Name")
    n1.place(x=295,y=320)
    n1.bind('<FocusIn>',on_Enter)
    n1.bind('<FocusOut>',on_leave)
    Frame(top1,width=190,height=2,bg="black").place(x=295,y=350)
        
    p1=Entry(top1,border=0,bg="#FFFFFF",width=25,font=(20))

    p1.insert(0,"Password")
    p1.place(x=295,y=375)
    p1.bind('<FocusIn>',on_Enter1)
    p1.bind('<FocusOut>',on_leave1)
    Frame(top1,width=190,height=2,bg="black").place(x=295,y=405)

    but=Button(top1,text="Sign Up",fg="white",bg="#57a1f8",font=("Microsoft yaHei UI Light",15,"bold"),bd=0,width=35,pady=7,command="")
    but.place(x=200,y=450)

    Label(top1,text="Already Have An Account?",fg="black",bg="#FFFFFF",bd=0,font=(10)).place(x=200,y=520)
    sign=Button(top1,text="Sign in",fg="blue",bg="#FFFFFF",bd=0,font=("Microsoft yaHei UI Light",10),activebackground="#FFFFFF",activeforeground="yellow",command=new).place(x=395,y=515)




def signin():
    if (n1.get() == "mk") and (p1.get() == "mk123"):
        mg.showinfo("Message","You Logined Succesfully")
        new()

    else:
        mg.showwarning("Warning","Check Your Details")

f=Frame(root,width=450,height=350,bg="#FFFFFF")
f.place(x=75,y=350)
#entry
n1=Entry(root,border=0,bg="#FFFFFF",width=25,font=(20))
n1.insert(0,"Name")
n1.place(x=295,y=320)
n1.bind('<FocusIn>',on_Enter)
n1.bind('<FocusOut>',on_leave)
Frame(root,width=190,height=2,bg="black").place(x=295,y=350)
    
p1=Entry(root,border=0,bg="#FFFFFF",width=25,font=(20))

p1.insert(0,"Password")
p1.place(x=295,y=375)
p1.bind('<FocusIn>',on_Enter1)
p1.bind('<FocusOut>',on_leave1)
Frame(root,width=190,height=2,bg="black").place(x=295,y=405)

but=Button(root,text="Sign In",fg="white",bg="#57a1f8",font=("Microsoft yaHei UI Light",15,"bold"),bd=0,width=35,pady=7,command=signin)
but.place(x=200,y=450)

Label(root,text="Don't Have An Account?",fg="black",bg="#FFFFFF",bd=0,font=(10)).place(x=200,y=520)
signup=Button(root,text="Sign up",fg="blue",bg="#FFFFFF",bd=0,font=("Microsoft yaHei UI Light",10),activebackground="#FFFFFF",activeforeground="yellow",command=newsign).place(x=380,y=515)


#ask yes or No
def control():
    ip=askyesno(title="Thank You",message="Do You Want To Exit ?")
    if ip:
        root.destroy()
root.protocol("WM_DELETE_WINDOW",control)

root.resizable(False,False)
root.mainloop()