import tkinter
from tkinter import *
from PIL import ImageTk,Image,ImageFilter
import pygame as pg
import time
import random

gm=Tk()
gm.title("Car Game")
gm.geometry("800x600")
#bgframe
img1=Image.open("595865.jpg")
img1=img1.resize((800,600))
#blurimg1=img1.filter(ImageFilter.BLUR)
photo1=ImageTk.PhotoImage(img1)
imlab1=Label(gm,image=photo1)
imlab1.pack()
def pygm():
    

    pg.init()

    screen=pg.display.set_mode((800,600))
    #title
    pg.display.set_caption("Car Game")

    #time
    clock=pg.time.Clock()

    #images bg
    grass=pg.image.load("grass.png")
    #line=pg.image.load()
    #centerline=pg.image.load()
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
gm.mainloop()