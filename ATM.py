#------------------------------------ (((database part))) ------------------------------------
import sqlite3    
conn = sqlite3.connect("atm.db")
cur = conn.cursor()
        
cur.execute("""CREATE TABLE IF NOT EXISTS customer(id TEXT PRIMARY KEY, fname TEXT, lname TEXT, addr TEXT, prof TEXT, dd INTEGER, mm INTEGER, yy INTEGER)""")
cur.execute("""CREATE TABLE IF NOT EXISTS user(Id TEXT PRIMARY KEY, bal INTEGER, credit INTEGER)""")    
conn.commit()
conn.close()
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Insert(Ps,fname,lname,addr,prof,dd,mm,yy,bal,credit) :
    
    import sqlite3
    conn = sqlite3.connect("atm.db")
    cur = conn.cursor()
        
    cur.execute("INSERT INTO customer VALUES (?,?,?,?,?,?,?,?)",(Ps,fname,lname,addr,prof,dd,mm,yy))
    cur.execute("INSERT INTO user VALUES (?,?,?)",(Ps,bal,credit))
        
    conn.commit()
    conn.close() 
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def search(id) :
    import sqlite3
    conn = sqlite3.connect("atm.db")
    cur = conn.cursor()
        
    cur.execute("SELECT * FROM customer WHERE id = ?", (id,))
        
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def search2(Id) :
    import sqlite3
    conn = sqlite3.connect("atm.db")
    cur = conn.cursor()
        
    cur.execute("SELECT * FROM user WHERE Id = ?", (Id,))
        
    rowz = cur.fetchall()
    conn.commit()
    conn.close()
    return rowz
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def view() :
    import sqlite3
    conn = sqlite3.connect('atm.db')
    cur = conn.cursor()
        
    cur.execute("SELECT * FROM customer ")
        
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def update(Id, bal,credit) :
    import sqlite3
    conn = sqlite3.connect('atm.db')
    cur = conn.cursor()
        
    cur.execute("UPDATE user SET bal = ?, credit = ? WHERE Id = ?", ( bal,credit,Id))
        
    conn.commit()
    conn.close()
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------    
#------------------------------------ (((GUI part))) ------------------------------------

from tkinter import *
from tkinter import messagebox
import sqlite3

class Bank:

    def __init__(self,root):#login signin
        self.conn = sqlite3.connect("atm.db")
        self.login = False
        self.root = root
        self.header = Label(self.root,text="SASAKI TOMORU BANK",bg="DarkGoldenrod1",fg="gray14",font=("arial",30,"bold"))
        self.header.pack(fill= X)
        self.frame = Frame(self.root,bg="gray14",width=600,height=400)
        self.frame.pack()
        self.info = Label(self.frame,text="PLEASE ENTER YOUR PASSWORD",bg="gray14",fg="DarkGoldenrod1",font=("arial",13,"bold"))
        self.ID = StringVar()
        self.user = Entry(self.frame,bg="honeydew",highlightcolor="#50A8B0",highlightthickness=2,highlightbackground="white", textvariable = self.ID)
        self.login = Button(self.frame,text="LOG IN",bg="DarkGoldenrod1",fg="white",font=("arial",10,"bold"),command = self.Check_ID)
        self.signinn = Button(self.frame,text="SIGN IN",bg="DarkGoldenrod1",fg="white",font=("arial",10,"bold"),command = self.signin)
        self.info2 =Label(self.frame,text="For your own security,\nPlease do not anyone see your\nACCOUNT NUMBER\nwhile entering",bg="gray14",fg="DarkGoldenrod1",font=("arial",8,"bold"))
        self.cancel = Button(self.frame,text="CANCEL",bg="DarkGoldenrod1",fg="white",font=("arial",10,"bold"),command = self.root.destroy)
        self.info.place(x=100,y=70,width=400,height=30)
        self.user.place(x=200,y=120,width=200,height=30)
        self.login.place(x=250,y=180,width=100,height=30)
        self.signinn.place(x=250,y=220,width=100,height=30)
        self.info2.place(x=350,y=240,width=300,height=100)
        self.cancel.place(x=480,y=330,width=100,height=30)
#----------------------------------------------------------------------------------------------------------------
    def signin(self):
        self.frame.destroy()
        self.frame = Frame(self.root,bg="gray14",width=600,height=400)
        root.geometry("600x420")
        self.firstName = Label(self.frame,text="Firstname",bg="gray14",fg="DarkGoldenrod1",font=("arial",10,"bold"))
        self.fn1 = StringVar()
        self.fn = Entry(self.frame,bg="honeydew",highlightcolor="#50A8B0",highlightthickness=2,highlightbackground="white",textvariable = self.fn1)
        self.lastName = Label(self.frame,text="Lastname",bg="gray14",fg="DarkGoldenrod1",font=("arial",10,"bold"))
        self.ln1 = StringVar()
        self.ln = Entry(self.frame,bg="honeydew",highlightcolor="#50A8B0",highlightthickness=2,highlightbackground="white",textvariable = self.ln1)
        self.address = Label(self.frame,text="Address",bg="gray14",fg="DarkGoldenrod1",font=("arial",10,"bold"))
        self.ad1 = StringVar()
        self.ad = Entry(self.frame,bg="honeydew",highlightcolor="#50A8B0",highlightthickness=2,highlightbackground="white",textvariable = self.ad1)
        self.profession = Label(self.frame,text="Profession",bg="gray14",fg="DarkGoldenrod1",font=("arial",10,"bold"),anchor = NW)
        self.pf1 = StringVar()
        self.pf = Entry(self.frame,bg="honeydew",highlightcolor="#50A8B0",highlightthickness=2,highlightbackground="white",textvariable = self.pf1)
        self.day = Label(self.frame,text="DD",bg="gray14",fg="DarkGoldenrod1",font=("arial",10,"bold"))
        self.d1 = StringVar()
        self.d = Entry(self.frame,bg="honeydew",highlightcolor="#50A8B0",highlightthickness=2,highlightbackground="white",textvariable = self.d1)
        self.month = Label(self.frame,text="MM",bg="gray14",fg="DarkGoldenrod1",font=("arial",10,"bold"))
        self.m1 = StringVar()
        self.m = Entry(self.frame,bg="honeydew",highlightcolor="#50A8B0",highlightthickness=2,highlightbackground="white",textvariable = self.m1)
        self.year = Label(self.frame,text="YY",bg="gray14",fg="DarkGoldenrod1",font=("arial",10,"bold"))
        self.y1 = StringVar()
        self.y = Entry(self.frame,bg="honeydew",highlightcolor="#50A8B0",highlightthickness=2,highlightbackground="white",textvariable = self.y1)
        self.pw1 = Label(self.frame,text="Password",bg="gray14",fg="DarkGoldenrod1",font=("arial",10,"bold"))
        self.pw2 = StringVar()
        self.pw3 = Entry(self.frame,bg="honeydew",highlightcolor="#50A8B0",highlightthickness=2,highlightbackground="white",textvariable = self.pw2)
        self.pw4 = Label(self.frame,text="Please enter\nONLY number!!!",bg="gray14",fg="DarkGoldenrod1",font=("arial",8,"bold"))
        self.btsubmit = Button(self.frame,text="Submit",bg="DarkGoldenrod1",fg="white",font=("arial",10,"bold"),command = self.Insert_command)
        self.cancel = Button(self.frame,text = "CANCEL",bg = "DarkGoldenrod1",fg = "white",font = ("arial",10,"bold"),command = self.root.destroy)
        self.firstName.place(x=50,y=50,width=100,height=30)
        self.fn.place(x=150,y=50,width=150,height=30)
        self.lastName.place(x=290,y=50,width=100,height=30)
        self.ln.place(x=380,y=50,width=150,height=30)
        self.address.place(x=50,y=100,width=100,height=30)
        self.ad.place(x=150,y=100,width=380,height=60)
        self.profession.place(x=50,y=180,width=100,height=30)
        self.pf.place(x=150,y=180,width=200,height=30)
        self.day.place(x=70,y=240,width=20,height=30)
        self.d.place(x=110,y=240,width=40,height=30)
        self.month.place(x=170,y=240,width=20,height=30)
        self.m.place(x=210,y=240,width=40,height=30)
        self.year.place(x=270,y=240,width=20,height=30)
        self.y.place(x=310,y=240,width=80,height=30)
        self.pw1.place(x=60,y=300,width=80,height=30)
        self.pw3.place(x=150,y=300,width=200,height=30)
        self.pw4.place(x=365,y=300,width=100,height=30)
        self.btsubmit.place(x=480,y=260,width=100,height=30)
        self.cancel.place(x=480,y=300,width=100,height=30)
        self.frame.pack()
#----------------------------------------------------------------------------------------------------------------
    def verify(self):
        self.frame.destroy()
        self.MainMenu()
#---------------------------------------------------------------------------------------------------------------- 
    def showid(self):
        self.frame.destroy()
        self.frame=Frame(self.root,bg="gray14",width=600,height=400)
        root.geometry("600x420")
       
        self.firstName = Label(self.frame,text="Firstname",bg="gray14",fg="DarkGoldenrod1",font=("arial",10,"bold"))
        self.fn = Label(self.frame,text= self.FName,bg="gray14",fg="honeydew",font=("arial",10,"bold"),anchor = W)
        self.lastName = Label(self.frame,text="Lastname",bg="gray14",fg="DarkGoldenrod1",font=("arial",10,"bold"))        
        self.ln = Label(self.frame,text= self.LName,bg="gray14",fg="honeydew",font=("arial",10,"bold"),anchor = W)
        self.address = Label(self.frame,text="Address",bg="gray14",fg="DarkGoldenrod1",font=("arial",10,"bold"))      
        self.ad = Label(self.frame,text= self.ADD,bg="gray14",fg="honeydew",font=("arial",10,"bold"),anchor = NW)
        self.profession = Label(self.frame,text="Profession",bg="gray14",fg="DarkGoldenrod1",font=("arial",10,"bold"))
        self.pf = Label(self.frame,text= self.PRO,bg="gray14",fg="honeydew",font=("arial",10,"bold"),anchor = W)
        self.day = Label(self.frame,text="DD",bg="gray14",fg="DarkGoldenrod1",font=("arial",10,"bold"))
        self.d = Label(self.frame,text= self.D,bg="gray14",fg="honeydew",font=("arial",10,"bold"),anchor = W)
        self.month = Label(self.frame,text="MM",bg="gray14",fg="DarkGoldenrod1",font=("arial",10,"bold"))
        self.m = Label(self.frame,text= self.M,bg="gray14",fg="honeydew",font=("arial",10,"bold"),anchor = W)
        self.year = Label(self.frame,text="YY",bg="gray14",fg="DarkGoldenrod1",font=("arial",10,"bold"))
        self.y = Label(self.frame,text= self.Y,bg="gray14",fg="honeydew",font=("arial",10,"bold"),anchor = W)
        self.pw1 = Label(self.frame,text="Password",bg="gray14",fg="DarkGoldenrod1",font=("arial",10,"bold"))
        self.pw3 = Label(self.frame,text= self.Pass,bg="gray14",fg="honeydew",font=("arial",10,"bold"),anchor = W)
        self.btsubmit = Button(self.frame,text="Confirm",bg="DarkGoldenrod1",fg="white",font=("arial",10,"bold"),command = self.MakeID)
        self.cancel = Button(self.frame,text = "CANCEL",bg = "DarkGoldenrod1",fg = "white",font = ("arial",10,"bold"),command = self.root.destroy)
        self.firstName.place(x=50,y=50,width=100,height=30)
        self.fn.place(x=150,y=50,width=150,height=30)
        self.lastName.place(x=290,y=50,width=100,height=30)
        self.ln.place(x=380,y=50,width=150,height=30)
        self.address.place(x=50,y=100,width=100,height=30)
        self.ad.place(x=150,y=100,width=380,height=60)
        self.profession.place(x=50,y=180,width=100,height=30)
        self.pf.place(x=150,y=180,width=200,height=30)
        self.day.place(x=70,y=240,width=20,height=30)
        self.d.place(x=110,y=240,width=40,height=30)
        self.month.place(x=170,y=240,width=20,height=30)
        self.m.place(x=210,y=240,width=40,height=30)
        self.year.place(x=270,y=240,width=20,height=30)
        self.y.place(x=310,y=240,width=80,height=30)
        self.pw1.place(x=60,y=300,width=80,height=30)
        self.pw3.place(x=150,y=300,width=200,height=30)
        self.btsubmit.place(x=480,y=260,width=100,height=30)
        self.cancel.place(x=480,y=300,width=100,height=30)
        self.frame.pack()
#----------------------------------------------------------------------------------------------------------------      
    def MainMenu(self):#เข้าหน้าหลังจาก login
        self.frame = Frame(self.root,bg="gray14",width=600,height=400)
        root.geometry("600x420")
        self.info = Label(self.frame,text="PLEASE SELECT TRANSACTION",bg="gray14",fg="DarkGoldenrod1",font=("arial",13,"bold"))
        self.depositt = Label(self.frame, text="Deposit Money",bg="gray14",fg="DarkGoldenrod1",font=("arial",10,"bold"))
        self.withdraww = Label(self.frame, text="Withdraw Money",bg="gray14",fg="DarkGoldenrod1",font=("arial",10,"bold"))
        self.balancee = Label(self.frame, text="Balance Inquiry",bg="gray14",fg="DarkGoldenrod1",font=("arial",10,"bold"))
        self.trans = Label(self.frame, text="Money Transfer",bg="gray14",fg="DarkGoldenrod1",font=("arial",10,"bold"))
        self.btdeposit = Button(self.frame,bg="DarkGoldenrod1",fg="white",font=("arial",10,"bold"),highlightthickness=2,highlightbackground="white",command = self.deposit)
        self.btwithdraw = Button(self.frame,bg="DarkGoldenrod1",fg="white",font=("arial",10,"bold"),highlightthickness=2,highlightbackground="white",command = self.withdraw)
        self.btbalance = Button(self.frame,bg="DarkGoldenrod1",fg="white",font=("arial",10,"bold"),highlightthickness=2,highlightbackground="white", command = self.balance)
        self.bttrans = Button(self.frame,bg="DarkGoldenrod1",fg="white",font=("arial",10,"bold"),highlightthickness=2,highlightbackground="white",command = self.transfer)
        self.info.place(x=100,y=50,width=400,height=30)
        self.depositt.place(x=410,y=100,width=150,height=30)
        self.withdraww.place(x=410, y=160, width=150, height=30)
        self.balancee.place(x=410, y=220, width=150, height=30)
        self.trans.place(x=410, y=280, width=150, height=30)
        self.btdeposit.place(x=560, y=100, width=30, height=30)
        self.btwithdraw.place(x=560, y=160, width=30, height=30)
        self.btbalance.place(x=560, y=220, width=30, height=30)
        self.bttrans.place(x=560, y=280, width=30, height=30)
        self.frame.pack()
#----------------------------------------------------------------------------------------------------------------
    def deposit(self):
        self.frame.destroy()
        self.frame = Frame(self.root,bg="gray14",width=600,height=400)
        root.geometry("600x420")
        
        self.info =Label(self.frame,text="PLEASE ENTER DEPOSIT AMOUNT",bg="gray14",fg="DarkGoldenrod1",font=("arial",13,"bold"))
        self.money = StringVar()
        self.amount = Entry(self.frame,bg="honeydew",highlightcolor="#50A8B0",highlightthickness=2,highlightbackground="white",textvariable = self.money )
        self.btsubmit = Button(self.frame,text="Submit",bg="DarkGoldenrod1",fg="white",font=("arial",10,"bold"),command = self.deposit_command)
        self.menu = Button(self.frame,text = "MENU",bg = "DarkGoldenrod1",fg = "white",font =("arial",10,"bold"),command = self.verify)
        self.cancel = Button(self.frame,text="CANCEL",bg="DarkGoldenrod1",fg="white",font=("arial",10,"bold"),command = self.root.destroy)
        self.info.place(x=100,y=70,width=400,height=30)
        self.amount.place(x=200,y=130,width=200,height=30)
        self.btsubmit.place(x=450,y=220,width=100,height=30)
        self.menu.place(x=450,y=260,width=100,height=30)
        self.cancel.place(x=450,y=300,width=100,height=30)
        self.frame.pack()
#----------------------------------------------------------------------------------------------------------------
    def withdraw(self):
        self.frame.destroy()
        self.frame = Frame(self.root,bg="gray14",width=600,height=400)
        root.geometry("600x420")
        
        self.info =Label(self.frame,text="PLEASE ENTER WITHDRAW AMOUNT",bg="gray14",fg="DarkGoldenrod1",font=("arial",13,"bold"))
        self.with1 = StringVar()
        self.amount = Entry(self.frame,bg="honeydew",highlightcolor="#50A8B0",highlightthickness=2,highlightbackground="white",textvariable = self.with1)
        self.btsubmit = Button(self.frame,text="Submit",bg="DarkGoldenrod1",fg="white",font=("arial",10,"bold"),command = self.withdraw_command)
        self.menu = Button(self.frame,text = "MENU",bg = "DarkGoldenrod1",fg = "white",font =("arial",10,"bold"),command = self.verify)
        self.cancel = Button(self.frame,text="CANCEL",bg="DarkGoldenrod1",fg="white",font=("arial",10,"bold"),command = self.root.destroy)
        self.info.place(x=100,y=70,width=400,height=30)
        self.amount.place(x=200,y=130,width=200,height=30)
        self.btsubmit.place(x=450,y=220,width=100,height=30)
        self.menu.place(x=450,y=260,width=100,height=30)
        self.cancel.place(x=450,y=300,width=100,height=30)
        self.frame.pack() 
#----------------------------------------------------------------------------------------------------------------
    def balance(self):
        self.frame.destroy()
        self.user3 = search2(self.userID)
        self.Balance3 = self.user3[0]
        self.balance3 = self.Balance3[1]
        self.frame = Frame(self.root,bg="gray14",width=600,height=400)
        root.geometry("600x420")
        self.info =Label(self.frame,text="  Current Balance  ",bg="honeydew",fg="DarkGoldenrod1",font=("arial",15,"bold"))
        self.bl = Label(self.frame,text= str(self.balance3) ,bg="honeydew",fg="DarkGoldenrod1",font=("arial",15,"bold"))
        self.yesno =Label(self.frame,text="Would you like to do another transaction?",bg="gray14",fg="DarkGoldenrod1",font=("arial",12,"bold"))
        self.btsubmit = Button(self.frame,text="Yes",bg="DarkGoldenrod1",fg="white",font=("arial",10,"bold"),command = self.verify )
        self.cancel = Button(self.frame,text="No",bg="DarkGoldenrod1",fg="white",font=("arial",10,"bold"),command = self.root.destroy)
        self.info.place(x=50,y=30,width=300,height=100)
        self.bl.place(x=350,y=30,width=200,height=100)
        self.yesno.place(x=50,y=180,width=700,height=30)
        self.btsubmit.place(x=480,y=230,width=100,height=30)
        self.cancel.place(x=480,y=270,width=100,height=30)
        self.frame.pack()
#----------------------------------------------------------------------------------------------------------------  
    def transfer(self):
        self.frame.destroy()
        self.frame = Frame(self.root,bg="gray14",width=600,height=400)
        root.geometry("600x420")
        self.info =Label(self.frame,text="PLEASE ENTER ACCOUNT NUMBER",bg="gray14",fg="DarkGoldenrod1",font=("arial",11,"bold"))
        self.Another = StringVar()
        self.user = Entry(self.frame,bg="honeydew",highlightcolor="#50A8B0",highlightthickness=2,highlightbackground="white",textvariable = self.Another)
        self.info1 =Label(self.frame,text="PLEASE ENTER TRANSFER AMOUNT",bg="gray14",fg="DarkGoldenrod1",font=("arial",11,"bold"))
        self.trans = StringVar()
        self.user1 = Entry(self.frame,bg="honeydew",highlightcolor="#50A8B0",highlightthickness=2,highlightbackground="white",textvariable = self.trans)
        self.btsubmit = Button(self.frame,text="Correct",bg="DarkGoldenrod1",fg="white",font=("arial",10,"bold"),command = self.transfer_command)
        self.menu = Button(self.frame,text = "MENU",bg = "DarkGoldenrod1",fg = "white",font =("arial",10,"bold"),command = self.verify)
        self.cancel = Button(self.frame,text="CANCEL",bg="DarkGoldenrod1",fg="white",font=("arial",10,"bold"),command = self.root.destroy)
        self.info.place(x=100,y=50,width=400,height=30)
        self.user.place(x=150,y=90,width=300,height=30)
        self.info1.place(x=150,y=150,width=300,height=30)
        self.user1.place(x=200,y=190,width=200,height=30)
        self.btsubmit.place(x=480,y=220,width=100,height=30)
        self.menu.place(x=480,y=260,width=100,height=30)
        self.cancel.place(x=480,y=300,width=100,height=30)
        self.frame.pack()
#----------------------------------------------------------------------------------------------------------------     
    def Insert_command(self) :   
        self.FName = self.fn.get()
        self.LName = self.ln.get()
        self.ADD = self.ad.get()
        self.PRO = self.pf.get()
        self.D = self.d.get()
        self.M = self.m.get()
        self.Y = self.y.get()
        self.Pass = self.pw2.get()
        
        self.showid()
#----------------------------------------------------------------------------------------------------------------
    def MakeID(self) :
        self.userID = self.pw2.get()
        Insert(self.Pass,self.FName,self.LName,self.ADD,self.PRO,self.D,self.M,self.Y,0,1000)
        self.verify()
            
#----------------------------------------------------------------------------------------------------------------     
    def Check_ID(self) :
        self.userID = self.ID.get()
        try :
            if search(self.ID.get())[0] in view() :
                self.verify()
            else :
                self.root.destroy()
        except IndexError :
            pass
#----------------------------------------------------------------------------------------------------------------
    def deposit_command(self) :
        try :
            self.user = search2(self.userID)
            self.Balance1 = self.user[0]
            self.balance1 = self.Balance1[1]
            if int(self.money.get()) >= 0 :
                self.balance1 += int(self.money.get())
                update(self.userID,self.balance1,1000)
                self.verify()
            else :
                pass
        except ValueError :
            pass
#----------------------------------------------------------------------------------------------------------------
    def withdraw_command(self) :
        self.user2 = search2(self.userID)
        self.Balance2 = self.user2[0]
        self.balance2 = self.Balance2[1]
        try :
            if (self.balance2 - int(self.with1.get()) < -1000) :
                self.amount.delete(0,END)
            else :
               # if 
                self.balance2 -= int(self.with1.get())
                update(self.userID,self.balance2,1000)
                self.verify()
        except ValueError :
            pass
#----------------------------------------------------------------------------------------------------------------
    def transfer_command(self) :
        self.user4 = search2(self.userID)
        self.Balance4 = self.user4[0]
        self.balance4 = self.Balance4[1]
        try :   
            self.AnotherUser = search2(self.Another.get())
            self.AnotherBalance = self.AnotherUser[0]
            self.Anotherbalance = self.AnotherBalance[1]
        except IndexError :
            pass
        try :
            if (self.balance4 - int(self.trans.get()) < -1000) :
                self.user1.delete(0,END)
            else :
                self.balance4 -= int(self.trans.get())
                self.Anotherbalance += int(self.trans.get())
                update(self.userID,self.balance4,1000)
                update(self.Another.get(),self.Anotherbalance,1000)
                self.verify()
        except ValueError :
            pass
#----------------------------------------------------------------------------------------------------------------    

root = Tk()
root.title("ATM")
root.geometry("600x420")
obj = Bank(root)        
root.mainloop()

Bank(root)