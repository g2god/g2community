"""
---------------------------------------------------------------------
         Language:Python
         Module:Tkinter
         File Type:Project
         Creted by:G2 Editz[MK]
         Status:Almost completed
         Database:MySQL
         Database Connection:Connected


---------------------------------------------------------------------
"""
#import section
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as mg
from PIL import ImageTk,Image,ImageFilter
from tkinter.messagebox import askyesno
import mysql.connector
import pygame as pg
import time
import random
#---------------------------------------------------------------------
#connecting to database
connection=mysql.connector.connect(host="localhost",port="3306",user="root",password="Mksql@123",database="mathan")
cursor=connection.cursor()
#---------------------------------------------------------------------
#mainwindow
root=Tk()
root.config(bg="#FFFFE0")
#bg image
img=Image.open("bg1.jpg")
img=img.resize((400,650))
blurimg=img.filter(ImageFilter.BLUR)
photo=ImageTk.PhotoImage(blurimg)
imlab=Label(root,image=photo)
imlab.pack()

root.geometry("400x650")
root.title("App")

#IMAGE

imgl=PhotoImage(file="login1.png")
img7=Image.open("595865.jpg")
img7=img7.resize((800,600))
photo7=ImageTk.PhotoImage(img7)

#---------------------------------------------------------------------
#mk=Frame(root,bg="black",width=400,height=50)
lb1=Label(root,text="G2 EDITZ",font=("LEMONMILK",25),fg="BLACK")
lb1.config(bg=root.cget("bg"),fg="BLACK")

lb2=Label(root,text="Subscribe To G2Editz",font=("LEMONMILK",20),fg="red")
lb2.config(bg=root.cget("bg"),fg="red")

#---------------------------------------------------------------------
#mk.place(x=0,y=0)
f2=Frame(root,width=380,height=450,bg="#FFFFE0")
f2.place(x=10,y=100)
#bgframe
"""img1=Image.open("bg2.jpg")
img1=img1.resize((380,450))
blurimg1=img1.filter(ImageFilter.BLUR)
photo1=ImageTk.PhotoImage(blurimg1)
imlab1=Label(f2,image=photo1)
imlab1.pack()"""
#image
"""img3=Image.open("earth.png")
imlab3=Label(f2,image=img3)
imlab3.place(x=150,y=150)"""

imgg=PhotoImage(file="g234.png")
Label(f2,image=imgg,bg="#FFFFE0").place(x=89,y=55)
#alighnment Button
lb1.place(x=125,y=12)
lb2.place(x=75,y=575)

#---------------------------------------------------------------------
#screen after login
def vj():
    v=Toplevel()

    v.title("Options")
    v.geometry("400x650")
    def mark():
            def avg():
                n=Toplevel(top)
                n.title("Marksheet")
                n.configure(bg="PeachPuff")
                n.geometry("500x500")
                l=Label(n,text="MARKSHEET",font=("times",20,"bold"),fg="red",bg="PeachPuff").grid(row=0,column=2)
                name=Label(n,text="Name:",font=("times",10,"bold"),bg="PeachPuff").grid(row=1,column=0,padx=10,pady=5)
                nam=e.get()
                name=Label(n,text=nam,font=("times",10,"bold"),bg="PeachPuff").grid(row=1,column=2,padx=10,pady=5)
                sprno=Label(n,text="SPR No:",font=("times",10,"bold"),bg="PeachPuff").grid(row=2,column=0,padx=10,pady=5)
                year=Label(n,text="Year:",font=("times",10,"bold"),bg="PeachPuff").grid(row=3,column=0,padx=10,pady=5)
                dept=Label(n,text="Department:",font=("times",10,"bold"),bg="PeachPuff").grid(row=4,column=0,padx=10,pady=5)
                sec=Label(n,text="Scetion:",font=("times",10,"bold"),bg="PeachPuff").grid(row=5,column=0,padx=10,pady=5)
                eng=Label(n,text="English:",font=("times",10,"bold"),bg="PeachPuff").grid(row=6,column=0,padx=10,pady=5)
                pyt=Label(n,text="C Programing:",font=("times",10,"bold"),bg="PeachPuff").grid(row=7,column=0,padx=10,pady=5)
                phy=Label(n,text="Physics:",font=("times",10,"bold"),bg="PeachPuff").grid(row=8,column=0,padx=10,pady=5)
                che=Label(n,text="Engineering Graphics:",font=("times",10,"bold"),bg="PeachPuff").grid(row=9,column=0,padx=10,pady=5)
                mat=Label(n,text="Mathematics:",font=("times",10,"bold"),bg="PeachPuff").grid(row=10,column=0,padx=10,pady=5)
                sp=e1.get()
                sprno=Label(n,text=sp,font=("times",10,"bold"),bg="PeachPuff").grid(row=2,column=2,padx=10,pady=5)
                ye=e2.get()
                year=Label(n,text=ye,font=("times",10,"bold"),bg="PeachPuff").grid(row=3,column=2,padx=10,pady=5)
                de=e3.get()
                dept=Label(n,text=de,font=("times",10,"bold"),bg="PeachPuff").grid(row=4,column=2,padx=10,pady=5)
                se=e4.get()
                sec=Label(n,text=se,font=("times",10,"bold"),bg="PeachPuff").grid(row=5,column=2,padx=10,pady=5)
                en=e5.get()
                eng=Label(n,text=en,font=("times",10,"bold"),bg="PeachPuff").grid(row=6,column=2,padx=10,pady=5)
                py=e6.get()
                pyt=Label(n,text=py,font=("times",10,"bold"),bg="PeachPuff").grid(row=7,column=2,padx=10,pady=5)
                ph=e7.get()
                phy=Label(n,text=ph,font=("times",10,"bold"),bg="PeachPuff").grid(row=8,column=2,padx=10,pady=5)
                ch=e8.get()
                che=Label(n,text=ch,font=("times",10,"bold"),bg="PeachPuff").grid(row=9,column=2,padx=10,pady=5)
                ma=e9.get()
                mat=Label(n,text=ma,font=("times",10,"bold"),bg="PeachPuff").grid(row=10,column=2,padx=10,pady=5)
                a=int(e5.get())
                l=int(e6.get())
                w=int(e7.get())
                b=int(e8.get())
                j=int(e9.get())
                g=a+l+b+w+j
                avrg=g/5
                na=Label(n,text="Total:",font=("times",10,"bold"),bg="PeachPuff").grid(row=11,column=0,padx=10,pady=5)
                me=Label(n,text="Average:",font=("times",10,"bold"),bg="PeachPuff").grid(row=12,column=0,padx=10,pady=5)
                na=Label(n,text=g,font=("times",10,"bold"),bg="PeachPuff").grid(row=11,column=2,padx=10,pady=5)
                me=Label(n,text=avrg,font=("times",10,"bold"),bg="PeachPuff").grid(row=12,column=2,padx=10,pady=5)
                hy=Label(n,text="Remarks:",font=("times",25,"bold"),bg="PeachPuff").grid(row=14,column=0,padx=10,pady=25)
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
                n.protocol("WM_DELETE_WINDOW",contro)
                n.mainloop()

            def clear():
                e.delete(0,"end")
                e1.delete(0,"end")
                e2.delete(0,"end")
                e3.delete(0,"end")
                e4.delete(0,"end")
                e5.delete(0,"end")
                e6.delete(0,"end")
                e7.delete(0,"end")
                e8.delete(0,"end")
                e9.delete(0,"end")
            
            #---------------------------------------------------------------------
            top=Toplevel()
            top.title("MarkSheet")
            top.geometry("500x500")
            l=Label(top,text="INFORMATION",font=("times",20,"bold"),fg="red")
            but=Button(top,text="Get Marksheet",bg="green",fg="yellow",activeforeground="yellow",activebackground="blue",command=avg)
            but1=Button(top,text="Clear",bg="red",fg="yellow",activeforeground="yellow",activebackground="blue",command=clear)
            name=Label(top,text="Name:",font=("times",10,"bold"))
            sprno=Label(top,text="SPR No:",font=("times",10,"bold"))
            year=Label(top,text="Year:",font=("times",10,"bold"))
            dept=Label(top,text="Department:",font=("times",10,"bold"))
            sec=Label(top,text="Scetion:",font=("times",10,"bold"))
            eng=Label(top,text="English:",font=("times",10,"bold"))
            pyt=Label(top,text="C Programing:",font=("times",10,"bold"))
            phy=Label(top,text="Physics:",font=("times",10,"bold"))
            che=Label(top,text="Engineering Graphics:",font=("times",10,"bold"))
            mat=Label(top,text="Mathematics:",font=("times",10,"bold"))
            e=Entry(top,border=0)
            e1=Entry(top,border=0)
            s=["I","II","III","IV"]
            e2=ttk.Combobox(top,value=s,width=17)
            i=["CSE","MECH","EEE","ECE","CIVIL"]
            e3=ttk.Combobox(top,value=i,width=17)
            k=["A","B"]
            e4=ttk.Combobox(top,value=k,width=17)
            e5=Entry(top)
            e6=Entry(top)
            e7=Entry(top)
            e8=Entry(top)
            e9=Entry(top)
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
    #---------------------------------------------------------------------
    def game():


        gm=Toplevel()
        gm.title("Car Game")
        gm.geometry("800x600")
        #bgframe

        imlab7=Label(gm,image=photo7)
        imlab7.pack()
        def pygm():
            

            pg.init()

            screen=pg.display.set_mode((800,600))
            #title
            pg.display.set_caption("Car Game")

            #time
            clock=pg.time.Clock()

            #images bg
            grass=pg.image.load("grass.png")
            #bgimg function
            def background():
                screen.blit(grass,(-880,0))
                screen.blit(grass,(650,0))
                line1=pg.draw.line(screen,"white",(175,0),(0,1000000000),9)
                line2=pg.draw.line(screen,"white",(625,0),(0,1000000000),9)
                line3=pg.draw.line(screen,"yellow",(395,0),(395,50),9)
                line4=pg.draw.line(screen,"yellow",(395,100),(395,150),9)
                line5=pg.draw.line(screen,"yellow",(395,200),(395,250),9)
                line6=pg.draw.line(screen,"yellow",(395,300),(395,350),9)
                line7=pg.draw.line(screen,"yellow",(395,400),(395,450),9)
                line8=pg.draw.line(screen,"yellow",(395,500),(395,550),9)
                line9=pg.draw.line(screen,"yellow",(395,590),(395,650),9)
            #score
            def scorecard(carpass,score):
                font=pg.font.SysFont(None,35)
                passed = font.render("Passed:" + str(carpass),True,(255,255,255))
                score=font.render("Score:"+str(score),True,(0,0,0))
                screen.blit(passed,(0,50))
                screen.blit(score,(0,100)) 

            #image car

            car=pg.image.load("car.png")
            car_width=50

            def obstacle(obsx,obsy,obs):
                if obs == 0:
                    e=pg.image.load("e1.png")
                elif obs == 1:
                    e = pg.image.load("e2.png")
                elif obs == 2:
                    e = pg.image.load("e3.png")
                screen.blit(e,(obsx,obsy))
                

            #car movement
            def carm(x,y):
                screen.blit(car,(x,y))

            #Crash Message
            crash=pg.font.SysFont("None",100)
            crashrender=crash.render("YOU CRASHED",1,(220,119,220))

            #mainloop
            def gl():  
                #coordinates
                xchange=0
                x=400
                y=470
                obsspeed=10
                obs=0
                ychange=0
                obsx=random.randrange(200,600)
                obsy= -750
                e1_width=50
                e1_height=100
                carpass=0
                score=0
                level=0
                

                #close button

                b=False
                while not b:
                    for e in pg.event.get():
                        if e.type ==pg.QUIT:
                            
                            pg.quit()
                            b=True
                    #moving car
                        if e.type == pg.KEYDOWN:
                        
                            if e.key == pg.K_LEFT:
                                xchange= -5
                            if e.key == pg.K_RIGHT:
                                xchange= 5
                            if e.key == pg.K_s:
                                obsspeed += 2
                            if e.key == pg.K_b:
                                obsspeed -= 2
                        if e.type == pg.KEYUP:
                        
                            if e.key == pg.K_LEFT or e.key == pg.K_RIGHT:
                                xchange= 0

                    x += xchange 
                        
                    
                #bg  color

                    screen.fill((50,50,50))
                    #screen.fill("black")
                    background()
                    obsy -= (obsspeed/4)
                    obstacle(obsx,obsy,obs)
                    obsy += obsspeed
                    
                #car movement call
                    carm(x,y)


                    #calling score function
                    scorecard(carpass,score)
                    
                    if x > 650 - car_width or x < 150 :
                        screen.blit(crashrender,(150,250))
                        pg.display.update()
                        time.sleep(5)
                        gl()


                    if obsy > 600:
                        obsy = 0 - e1_height
                        obsx= random.randrange(170,630)
                        obs= random.randrange(0,3)
                        carpass += 1
                        score = carpass * 10
                        if int(carpass) % 10 == 0:
                                level += 1
                                obsspeed += 2
                                myfont=pg.font.SysFont(None,100)
                                level_text=myfont.render("Level"+ str(level),1,(0,0,0))
                                screen.blit(level_text,(100,200))
                                pg.display.update()
                                time.sleep(3)
                                
                                
                        
                    if y < obsy + e1_height:      
                        if x > obsx and x < obsx + e1_width or x + car_width > obsx and x+car_width < x :#+ e1_width:
                            screen.blit(crashrender,(150,250))
                            pg.display.update()
                            time.sleep(5) 
                            gl()
            
                #display update
                    pg.display.update()
                    clock.tick(120)
            gl()
            pg.quit()
            quit()



        Cargame=Label(gm,text="CAR GAME",font=("times",65,"bold"),bg="black",fg="red")
        Cargame.place(x=160,y=150)
        start=Button(gm,text="START",bg="green",fg="white",width=15,command=pygm)
        start.place(x=100,y=450)
        exit=Button(gm,text="EXIT",bg="red",fg="white",width=15,command=gm.destroy)
        exit.place(x=550,y=450)

    #menu
    menubar=Menu(v)
    fmenu=Menu(menubar,tearoff=0)
    fmenu.add_command(label="HOME",command=loggin)
    fmenu.add_separator()
    fmenu.add_command(label="Exit",command=v.quit)
    menubar.add_cascade(label="Menu",menu=fmenu)
    #labels
    name=Label(v,text="G2 EDITZ",font=("LEMONMILK",25),fg="red")
    opt1=Button(v,text="Marksheet",bg="PeachPuff",fg="black",width=30,command=mark)
    opt2=Button(v,text="Car Game",bg="yellow",fg="black",width=30,command=game)
    name.place(x=130,y=100)
    opt1.place(x=90,y=250)
    opt2.place(x=90,y=300)
    v.config(menu=menubar)
    v.resizable(False,False)

#---------------------------------------------------------------------
#functions
def loggin():
    t1=Toplevel()
    t1.title("LOGIN")
    t1.geometry("400x650")
    #functions
    def light():
        l=p.get()
        i=n.get()
        logvar=(i,l)
        if (i=="Name") or (l=="Password") :
            mg.showerror("Invalid","Enter Valid Details")

        elif ( i or l) == "":
            mg.showerror("Invalid","Enter Valid Details")
        else:
            cursor.execute(""" SELECT name,password from registeration """)
            r=cursor.fetchall()
            for j in r:
                #print(j)
                if (j == logvar):
                        
                    mg.showinfo("Message","You successfully Logged In")
                    vj()
                    cursor.close()
                    connection.commit()
                    connection.close()                
                    break        
                else:
                    mg.showwarning("Message","Check Your Details!!!")
                    signnup()
                    cursor.close()
                    connection.commit()
                    connection.close()
                    break
    def c():
        n.delete(0,END)
        p.delete(0,END)
    
    #function entry
    def on_Enter(e):
        n.delete(0,"end")
    def on_leave(e):
        nam=n.get()
        if nam == "":
            n.insert(0,"Name")

    def on_Enter1(e):
        p.delete(0,"end")
    def on_leave1(e):
        nam=p.get()
        if nam == "":
            p.insert(0,"Password")
    
    
    #bg
    t1.configure(background="#FFFFFF")
    Label(t1,image=imgl,bg="#FFFFFF").place(x=120,y=30)
    name=Label(t1,text="Name",fg="RED",font=("Oswald"),bg="#FFFFFF")
    name.place(x=80,y=250)
    pwd=Label(t1,text="Password",fg="RED",font=("Oswald"),bg="#FFFFFF")
    pwd.place(x=80,y=300)
    n=Entry(t1,width=25,border=0)
    n.place(x=175,y=250)
    n.insert(0,"Name")
    n.bind('<FocusIn>',on_Enter)
    n.bind('<FocusOut>',on_leave)
    Frame(t1,width=190,height=2,bg="black").place(x=175,y=270)
    p=Entry(t1,width=25,border=0)
    p.insert(0,"Password")
    p.place(x=175,y=300)
    p.bind('<FocusIn>',on_Enter1)
    p.bind('<FocusOut>',on_leave1)
    Frame(t1,width=190,height=2,bg="black").place(x=175,y=320)

    enter=Button(t1,text="Enter",fg="black",width=25,bg="green",command=light)
    enter.place(x=100,y=500)
    exit=Button(t1,text="Exit",fg="black",width=25,bg="red",command=t1.destroy)
    exit.place(x=100,y=550)
    clr=Button(t1,text="Clear",fg="black",width=25,bg="white",command=c)
    clr.place(x=100,y=450)

    t1.resizable(False,False)
def signnup():
    t2=Toplevel()
    t2.title("SIGN UP")
    t2.geometry("400x650")
    #functions
    
    def l():
        i=n1.get()
        j=us.get()
        k=em.get()
        l=p1.get()
        values=(i,j,k,l)
        if (i=="Name") or (j=="USERID") or (k=="Email") or (l=="Password") :
            mg.showerror("Invalid","Enter Valid Details")

        elif ( i or j or k or l) == "":
            mg.showerror("Invalid","Enter Valid Details")
        else:

            cursor.execute(""" SELECT * from registeration """)
            r=cursor.fetchall()
            for i in r:
                #print(i)
                if (i == values):
                    
                    mg.showinfo("Message","you Already Registered")
                    break
                else:
                    cursor.execute("INSERT INTO registeration (name,userid,email,password) VALUES (%s,%s,%s,%s)",values)
                    mg.showinfo("Message","You Registered")
                    #connection.commit()
                    cursor.close()
                    connection.commit()
                    connection.close()
                    vj()
                
                    break
                
            cursor.close()
            connection.commit()
            connection.close()
        
    def c():
        n1.delete(0,END)
        em.delete(0,END)
        us.delete(0,END)
        p1.delete(0,END)
    #bg
    t2.configure(background="#FFFFFF")
    Label(t2,image=imgl,bg="#FFFFFF").place(x=120,y=30)
    #label
    name=Label(t2,text="Name",fg="black",font=("Oswald"),bg="#FFFFFF")
    name.place(x=80,y=250)
    

    email=Label(t2,text="Email",fg="black",font=("Oswald"),bg="#FFFFFF")
    email.place(x=80,y=300)

    user=Label(t2,text="UserID",fg="black",font=("Oswald"),bg="#FFFFFF")
    user.place(x=80,y=350)
    
    pwd=Label(t2,text="Password",fg="black",font=("Oswald"),bg="#FFFFFF")
    pwd.place(x=80,y=400)
    #function entry
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

    def on_Enter2(e):
        em.delete(0,"end")
    def on_leave2(e):
        nam=em.get()
        if nam == "":
            em.insert(0,"Email")

    def on_Enter3(e):
        us.delete(0,"end")
    def on_leave3(e):
        nam=us.get()
        if nam == "":
            us.insert(0,"UserID")

    
    #entry
    n1=Entry(t2,border=0)
    n1.insert(0,"Name")
    n1.place(x=190,y=250)
    n1.bind('<FocusIn>',on_Enter)
    n1.bind('<FocusOut>',on_leave)
    Frame(t2,width=190,height=2,bg="black").place(x=175,y=270)
    
    em=Entry(t2,border=0)
    em.insert(0,"Email")
    em.place(x=190,y=300)
    em.bind('<FocusIn>',on_Enter2)
    em.bind('<FocusOut>',on_leave2)
    Frame(t2,width=190,height=2,bg="black").place(x=175,y=320)
    
    us=Entry(t2,border=0)
    us.insert(0,"USERID")
    us.place(x=190,y=350)
    us.bind('<FocusIn>',on_Enter3)
    us.bind('<FocusOut>',on_leave3)
    Frame(t2,width=190,height=2,bg="black").place(x=175,y=370)
    
    p1=Entry(t2,border=0)
    p1.insert(0,"Password")
    p1.place(x=190,y=400)
    p1.bind('<FocusIn>',on_Enter1)
    p1.bind('<FocusOut>',on_leave1)
    Frame(t2,width=190,height=2,bg="black").place(x=175,y=420)
    #Button
    enter=Button(t2,text="Enter",fg="black",width=25,bg="green",command=l)
    enter.place(x=100,y=500)
    exit=Button(t2,text="Exit",fg="black",width=25,bg="red",command=t2.destroy)
    exit.place(x=100,y=550)
    clr=Button(t2,text="Clear",fg="black",width=25,bg="#FFFFE0",command=c)
    clr.place(x=100,y=450)


#---------------------------------------------------------------------
#Button

login=Button(f2,text="LOGIN",fg="black",borderwidth=2,bg="blue",command=loggin,width=25)
login.place(x=100,y=300)

signup=Button(f2,text="SIGN UP",fg="black",borderwidth=2,bg="green",command=signnup,width=25)
signup.place(x=100,y=350)

exit=Button(root,text="Exit",fg="black",width=25,bg="red",command=root.destroy)
exit.place(x=110,y=500)

#ask yes or No
def contro():
    fgh=askyesno(title="Thank You",message="Do You Want To Exit ?")
    if fgh:
        root.destroy()
root.protocol("WM_DELETE_WINDOW",contro)

root.resizable(False,False)
root.mainloop()