#functions
def loggin():
    t1=Toplevel()
    t1.title("LOGIN")
    t1.geometry("400x650")
    #functions
    def light():
        #mg.showinfo("Message","You Logined")
        l=p.get()
        i=n.get()
        logvar=(i,l)
        cursor.execute(""" SELECT name,password from registeration """)
        r=cursor.fetchall()
        for j in r:
            print(j)
            if (j == logvar):
                    
                #mg.showinfo("Message","You Looged In")
                vj()
                break         
            else:
                mg.showinfo("Message","Check Your Details!!!")
                break