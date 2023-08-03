def avg():
    n=Toplevel(screen)
    n.title("Marksheet")
    n.geometry("500x500")
    l=Label(n,text="MARKSHEET",font=("times",20,"bold"),fg="red").grid(row=0,column=2)
    name=Label(n,text="Name:",font=("times",10,"bold")).grid(row=1,column=0,padx=10,pady=5)
    nam=e.get()
    name=Label(n,text=nam,font=("times",10,"bold")).grid(row=1,column=2,padx=10,pady=5)
    sprno=Label(n,text="SPR No:",font=("times",10,"bold")).grid(row=2,column=0,padx=10,pady=5)
    year=Label(n,text="Year:",font=("times",10,"bold")).grid(row=3,column=0,padx=10,pady=5)
    dept=Label(n,text="Department:",font=("times",10,"bold")).grid(row=4,column=0,padx=10,pady=5)
    sec=Label(n,text="Scetion:",font=("times",10,"bold")).grid(row=5,column=0,padx=10,pady=5)
    eng=Label(n,text="English:",font=("times",10,"bold")).grid(row=6,column=0,padx=10,pady=5)
    pyt=Label(n,text="Python:",font=("times",10,"bold")).grid(row=7,column=0,padx=10,pady=5)
    phy=Label(n,text="Physics:",font=("times",10,"bold")).grid(row=8,column=0,padx=10,pady=5)
    che=Label(n,text="Chemistry:",font=("times",10,"bold")).grid(row=9,column=0,padx=10,pady=5)
    mat=Label(n,text="Mathematics:",font=("times",10,"bold")).grid(row=10,column=0,padx=10,pady=5)
    sp=e1.get()
    sprno=Label(n,text=sp,font=("times",10,"bold")).grid(row=2,column=2,padx=10,pady=5)
    ye=e2.get()
    year=Label(n,text=ye,font=("times",10,"bold")).grid(row=3,column=2,padx=10,pady=5)
    de=e3.get()
    dept=Label(n,text=de,font=("times",10,"bold")).grid(row=4,column=2,padx=10,pady=5)
    se=e4.get()
    sec=Label(n,text=se,font=("times",10,"bold")).grid(row=5,column=2,padx=10,pady=5)
    en=e5.get()
    eng=Label(n,text=en,font=("times",10,"bold")).grid(row=6,column=2,padx=10,pady=5)
    py=e6.get()
    pyt=Label(n,text=py,font=("times",10,"bold")).grid(row=7,column=2,padx=10,pady=5)
    ph=e7.get()
    phy=Label(n,text=ph,font=("times",10,"bold")).grid(row=8,column=2,padx=10,pady=5)
    ch=e8.get()
    che=Label(n,text=ch,font=("times",10,"bold")).grid(row=9,column=2,padx=10,pady=5)
    ma=e9.get()
    mat=Label(n,text=ma,font=("times",10,"bold")).grid(row=10,column=2,padx=10,pady=5)
    a=int(e5.get())
    l=int(e6.get())
    w=int(e7.get())
    b=int(e8.get())
    j=int(e9.get())
    g=a+l+b+w+j
    avrg=g/5
    na=Label(n,text="Total:",font=("times",10,"bold")).grid(row=11,column=0,padx=10,pady=5)
    me=Label(n,text="Average:",font=("times",10,"bold")).grid(row=12,column=0,padx=10,pady=5)
    na=Label(n,text=g,font=("times",10,"bold")).grid(row=11,column=2,padx=10,pady=5)
    me=Label(n,text=avrg,font=("times",10,"bold")).grid(row=12,column=2,padx=10,pady=5)
    hy=Label(n,text="Remarks:",font=("times",25,"bold")).grid(row=14,column=0,padx=10,pady=25)
    if avrg>=90:
        po=Label(n,text="Very Good",font=("times",25,"bold"),bg="green",fg="white").grid(row=14,column=2,padx=10,pady=25)
    elif avrg<90 and avrg>=50:
        kl=Label(n,text="Good",font=("times",25,"bold"),bg="blue",fg="white").grid(row=14,column=2,padx=10,pady=25)
    else:
        cl=Label(n,text="You Need To Concentrate More On Class",font=("times",25,"bold"),bg="red",fg="white").grid(row=14,column=2,padx=10,pady=25)
    def contro():
        fgh=askyesno(title="Thank You",message="Do You Want To Exit ?")
        if fgh:
            n.destroy()
    n.protocol("WM_DELETE_WINDOW",control)
    n.mainloop()
    

screen=Tk()
screen.title("MarkSheet")
screen.geometry("500x500")
l=Label(screen,text="INFORMATION",font=("times",20,"bold"),fg="red")
but=Button(screen,text="Get Marksheet",bg="green",fg="yellow",activeforeground="yellow",activebackground="blue",command=avg)
but1=Button(screen,text="Clear",bg="red",fg="yellow",activeforeground="yellow",activebackground="blue",command=clear)
name=Label(screen,text="Name:",font=("times",10,"bold"))
sprno=Label(screen,text="SPR No:",font=("times",10,"bold"))
year=Label(screen,text="Year:",font=("times",10,"bold"))
dept=Label(screen,text="Department:",font=("times",10,"bold"))
sec=Label(screen,text="Scetion:",font=("times",10,"bold"))
eng=Label(screen,text="English:",font=("times",10,"bold"))
pyt=Label(screen,text="Python:",font=("times",10,"bold"))
phy=Label(screen,text="Physics:",font=("times",10,"bold"))
che=Label(screen,text="Chemistry:",font=("times",10,"bold"))
mat=Label(screen,text="Mathematics:",font=("times",10,"bold"))
e=Entry()
e1=Entry()
s=["I","II","III","IV"]
e2=ttk.Combobox(screen,value=s,width=17)
i=["CSE","MECH","EEE","ECE","CIVIL"]
e3=ttk.Combobox(screen,value=i,width=17)
k=["A","B"]
e4=ttk.Combobox(screen,value=k,width=17)
e5=Entry()
e6=Entry()
e7=Entry()
e8=Entry()
e9=Entry()
e.grid(row=1,column=2,padx=10,pady=5)
e1.grid(row=2,column=2,padx=10,pady=5)
e2.grid(row=3,column=2,padx=10,pady=5)
e3.grid(row=4,column=2,padx=10,pady=5)
e4.grid(row=5,column=2,padx=10,pady=5)
e5.grid(row=6,column=2,padx=10,pady=5)
e6.grid(row=7,column=2,padx=10,pady=5)
e7.grid(row=8,column=2,padx=10,pady=5)
e8.grid(row=9,column=2,padx=10,pady=5)
e9.grid(row=10,column=2,padx=10,pady=5)
name.grid(row=1,column=0)
sprno.grid(row=2,column=0)
year.grid(row=3,column=0)
dept.grid(row=4,column=0)
sec.grid(row=5,column=0)
eng.grid(row=6,column=0)
pyt.grid(row=7,column=0)
che.grid(row=8,column=0)
mat.grid(row=9,column=0)
phy.grid(row=10,column=0)
but.grid(row=11,columnspan=2,padx=30,pady=10)
but1.grid(row=11,columnspan=3,padx=30,pady=10)
l.grid(row=0,column=2)