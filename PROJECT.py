import tkinter as tk 
from tkinter import *
from tkinter import messagebox

from tkinter import ttk

import mysql.connector as mys

#-------------------------------------------------------------------------------------------------------------------
def frmreturn(x):
    
    def returnbook(name):
        try:
            myconn=mys.connect(host='localhost',user="root",\
                                 passwd="adis",database="library")
            if myconn.is_connected():
                print("connection succssful")
            mycur=myconn.cursor()
            query="update book set avail='YES' , user= NULL where name='{}'".format(name)
            mycur.execute(query)
            myconn.commit()
            messagebox.showinfo("BOOK INFO","BOOK RETURNED")
            root.destroy()
            shop()
    
        except Exception as e:
            print(e)

    
    def buy(x):
        try:
            myconn=mys.connect(host='localhost',user="root",\
                                 passwd="adis",database="library")
            if myconn.is_connected():
                print("connection succssful")
            mycur=myconn.cursor()
            query="SELECT * FROM BOOK WHERE NAME='{}'".format(x)
            mycur.execute(query)
            rs=mycur.fetchone()
            rs=list(rs)
            regno=rs[0]
            name=rs[1]
            athr=rs[2]
            price=rs[3]
            lang=rs[4]
            txtregno.insert(END,regno)
            txtname.insert(END,name)
            txtathr.insert(END,athr)
            txtprice.insert(END,price)
            txtlang.insert(END,lang)
    
        except Exception as e:
            print(e)
    
    root = tk.Toplevel()
    root.geometry("1200x800")
    root.title("LIBRARY MENU")
    bg = PhotoImage(file="C:/Users/viswa/Documents/VISWA/DOC/12-B/PYTHON/LIBRARY/admin.png")
    # Create Canvas
    canvas1 = Canvas( root, width = 400,height = 400)
    canvas1.pack(fill = "both", expand = True)
    # Display image
    canvas1.create_image( 0, 0, image = bg, anchor = "nw")
    root['background'] = 'black'
    lblregno = tk.Label(root, text ="REGNO :",fg='white',bg='black',font = ("Times New Roman Bold", 15) ) 
    lblregno.place(x = 50, y = 100,width = 200)
    txtregno= tk.Entry(root, width = 35,fg='white',bg='black',font = ("Times New Roman Bold", 15)) 
    txtregno.place(x = 350, y = 100, width = 600) 
    lblname = tk.Label(root, text ="NAME :",fg='white',bg='black',font = ("Times New Roman Bold", 15)) 
    lblname.place(x = 50, y = 150,width = 200) 
    txtname = tk.Entry(root, width = 35,fg='white',bg='black',font = ("Times New Roman Bold", 15)) 
    txtname.place(x = 350, y = 150, width = 600) 
    lblathr = tk.Label(root, text ="AUTHOR :",fg='white',bg='black',font = ("Times New Roman Bold", 15) ) 
    lblathr.place(x = 50, y = 200,width = 200) 
    txtathr = tk.Entry(root, width = 35,fg='white',bg='black',font = ("Times New Roman Bold", 15)) 
    txtathr.place(x = 350, y =200, width = 600) 
    lblprice = tk.Label(root, text ="PRICE :",fg='white',bg='black',font = ("Times New Roman Bold", 15)) 
    lblprice.place(x = 50, y = 250,width = 200)
    txtprice = tk.Entry(root, width = 35,fg='white',bg='black',font = ("Times New Roman Bold", 15)) 
    txtprice.place(x = 350, y = 250, width = 600)
    lbllang = tk.Label(root, text ="LANG :",fg='white',bg='black',font = ("Times New Roman Bold", 15)) 
    lbllang.place(x = 50, y = 300,width = 200)
    txtlang = tk.Entry(root, width = 35,fg='white',bg='black',font = ("Times New Roman Bold", 15)) 
    txtlang.place(x = 350, y = 300, width = 600)
    btnreturn= tk.Button(root, text ="RETURN", 
                    fg='white',bg='black',font = ("Times New Roman Bold", 15),command=lambda: returnbook(x))
    btnreturn.place(x = 1000, y = 100, width = 150)
    buy(x)
    root.mainloop()
    
#-------------------------------------------------------------------------------------------------------------------

def frmaccount(x):
    def txt(i):
        for f in i:
            return(f)
        
    def delete(x):
        try:
            myconn=mys.connect(host='localhost',user="root",\
                             passwd="adis",database="library")
            if myconn.is_connected():
                print("connection succssful")
            mycur=myconn.cursor()
            query="select name from book where user ='{}'".format(x)
            mycur.execute(query)
            rs=mycur.fetchall()
            rs=list(rs)
            query="DELETE FROM user where NAME ='{}'".format(x)
            mycur.execute(query)
            myconn.commit()
            for i in rs:
                query="update book set user= NULL, avail= 'YES' where name ='{}'".format(txt(i))
                mycur.execute(query)
                myconn.commit()
                messagebox.showinfo("BOOK INFO","USER DELETED")
            root.destroy()
            shop()

        except Exception as e:
            print(e)        
    
    def button(x):
        try:
            myconn=mys.connect(host='localhost',user="root",\
                             passwd="adis",database="library")
            if myconn.is_connected():
                print("connection succssful")
            mycur=myconn.cursor()
            query="select name from book where user ='{}'".format(x)
            mycur.execute(query)
            rs=mycur.fetchall()
            rs=list(rs)
            button_dict={}
            for i in rs:
                def func(x=txt(i)):
                    root.destroy()
                    frmreturn(x)   
                button_dict[i]=tk.Button(canvas2, text=txt(i),fg='deepskyblue',bg='black',font = ("Times New Roman Bold", 10),command= func)
                button_dict[i].pack(side = TOP, expand = True, fill = BOTH)

        except Exception as e:
            print(e)

    
    root = tk.Toplevel()
    root.geometry("1400x800")
    root.title("LIBRARY MENU")
    bg = PhotoImage(file="C:/Users/viswa/Documents/VISWA/DOC/12-B/PYTHON/LIBRARY/admin.png")
    scroll_bar = Scrollbar(root)
    scroll_bar.pack( side = RIGHT,fill = Y )
    # Create Canvas
    canvas1 = Canvas( root, width = 900,height = 800)
    canvas1.pack(side = LEFT,fill = "both", expand = True)
    canvas2 = Canvas( root, width = 400,height =1500,bg='black',yscrollcommand = scroll_bar.set)
    canvas2.pack(side = RIGHT,fill = "both", expand = True)
    # Display image
    canvas1.create_image( 0, 0, image = bg, anchor = "nw")
    canvas2.configure(scrollregion = canvas2.bbox("all"))
    scroll_bar.config( command = canvas2.yview )
    lbluser = tk.Label(root, text ="USERNAME :",fg='deepskyblue',bg='black',font = ("Times New Roman Bold",15) ) 
    lbluser.place(x = 100, y = 350) 
    txtUser = tk.Label(root, text = x ,fg='deepskyblue',bg='black',font = ("Times New Roman Bold", 15)) 
    txtUser.place(x = 100, y = 400) 
    btndisplay= tk.Label(root, text ="RENTED BOOKS:",fg='deepskyblue',bg='black',font = ("Times New Roman Bold", 15))
    btndisplay.place(x = 650, y = 100)
    btndelete = tk.Button(root, text ="DELETE ACCOUNT", fg='white',bg='black',font = ("Times New Roman Bold", 15), command =lambda:delete(x))
    btndelete.place(x = 100, y = 600, width = 300)
    button(x)
    root.mainloop()

#-------------------------------------------------------------------------------------------------------------------
def frmacclogin():        
    def register():
        try:
            name = txtUser.get() 
            paswrd = txtpass.get()
            myconn=mys.connect(host='localhost',user="root",\
                                 passwd="adis",database="library")
            if myconn.is_connected():
                print("connection succssful")
            mycur=myconn.cursor()
            query="INSERT INTO USER VALUE ('{}','{}')".format(name,paswrd)
            mycur.execute(query)
            myconn.commit()
            messagebox.showinfo("BOOK INFO","USER REGISTERED")
            root.destroy()
            frmaccount(name)            
    
        except Exception as e:
            print(e)
        
    def login():
        try:
            name = txtUser.get() 
            paswrd = txtpass.get()
            myconn=mys.connect(host='localhost',user="root",\
                                 passwd="adis",database="library")
            if myconn.is_connected():
                print("connection succssful")
            mycur=myconn.cursor()
            query="select * from user where name='{}'".format(name)
            mycur.execute(query)
            rs=mycur.fetchone()
            if rs==None:
                messagebox.showinfo("USER","NO SUCH USER")
            else:
                rs=list(rs)
                username=rs[0]
                password=rs[1]
                if password != paswrd:
                    messagebox.showinfo("USER","INCORRECT PASSWORD")
                else:
                    root.destroy()
                    frmaccount(name)
    
        except Exception as e:
            print(e)
    
    root = tk.Toplevel() 
    root.geometry("1200x800")
    root.title("KINTER LOGIN PAGE")
    root['background'] = 'black'
    bg = PhotoImage(file="C:/Users/viswa/Documents/VISWA/DOC/12-B/PYTHON/LIBRARY/login.png")
    # Create Canvas
    canvas1 = Canvas( root, width = 400,height = 400)
    canvas1.pack(fill = "both", expand = True)
    # Display image
    canvas1.create_image( 0, 0, image = bg, anchor = "nw")
    lbluser = tk.Label(root, text ="USERNAME :",fg='white',bg='black',font = ("Times New Roman Bold", 15) ) 
    lbluser.place(x = 100, y = 200) 
    txtUser = tk.Entry(root, width = 35,fg='white',bg='black',font = ("Times New Roman Bold", 15)) 
    txtUser.place(x = 100, y = 250, width = 150) 
    lblpass = tk.Label(root, text ="PASSWORD :",fg='white',bg='black',font = ("Times New Roman Bold", 15)) 
    lblpass.place(x = 100, y = 400) 
    txtpass = tk.Entry(root,show="*", width = 35,fg='white',bg='black',font = ("Times New Roman Bold", 15)) 
    txtpass.place(x = 100, y = 450, width = 150) 
    btnlogin = tk.Button(root, text ="LOGIN", fg='white',bg='black',font = ("Times New Roman Bold", 15), command = login )
    btnlogin.place(x = 1000, y = 200, width = 150)
    btnclear = tk.Button(root, text ="REGISTER", fg='white',bg='black',font = ("Times New Roman Bold", 15), command = register )
    btnclear.place(x = 1000, y = 400, width = 150)
    heading = tk.Label(root, text ="LOGIN",fg='white',bg='black',font = ("Times New Roman Bold", 30) ) 
    heading.place(x = 500, y = 50)
    # Execute tkinter
    root.mainloop()

#-------------------------------------------------------------------------------------------------------------------


def frmrent(x):        
    def register(x):
        try:
            name = txtUser.get() 
            paswrd = txtpass.get()
            myconn=mys.connect(host='localhost',user="root",\
                                 passwd="adis",database="library")
            if myconn.is_connected():
                print("connection succssful")
            mycur=myconn.cursor()
            query="INSERT INTO USER VALUES ('{}','{}')".format(name,paswrd)
            mycur.execute(query)
            myconn.commit()
            avail=NO
            query="UPDATE BOOK SET USER='{}' , AVAIL='{}' WHERE NAME='{}'".format(name,avail,x)
            mycur.execute(query)
            myconn.commit()
            messagebox.showinfo("BOOK INFO","USER REGISTERED")
            messagebox.showinfo("BOOK INFO","BOOK PURCHASED")
            root.destroy()
            shop()            
    
        except Exception as e:
            print(e)
        
    def login(x):
        try:
            name = txtUser.get() 
            paswrd = txtpass.get()
            myconn=mys.connect(host='localhost',user="root",\
                                 passwd="adis",database="library")
            if myconn.is_connected():
                print("connection succssful")
            mycur=myconn.cursor()
            query="select * from user where name='{}'".format(name)
            mycur.execute(query)
            rs=mycur.fetchone()
            rs=list(rs)
            username=rs[0]
            password=rs[1]
            if rs==None:
                messagebox.showinfo("USER","NO SUCH USER")
            if password != paswrd:
                messagebox.showinfo("USER","INCORRECT USER")
            else:
                query="update book set avail='NO' , user='{}' where name='{}'".format(name,x)
                mycur.execute(query)
                myconn.commit()
                messagebox.showinfo("BOOK INFO","LOGIN SUCCESSFULL")
                messagebox.showinfo("BOOK INFO","BOOK PURCHASED")
                root.destroy()
                shop()
    
        except Exception as e:
            print(e)
    
    root = tk.Toplevel() 
    root.geometry("1200x800")
    root.title("KINTER LOGIN PAGE")
    bg = PhotoImage(file="C:/Users/viswa/Documents/VISWA/DOC/12-B/PYTHON/LIBRARY/login.png")
    # Create Canvas
    canvas1 = Canvas( root, width = 400,height = 400)
    canvas1.pack(fill = "both", expand = True)
    # Display image
    canvas1.create_image( 0, 0, image = bg, anchor = "nw")
    lbluser = tk.Label(root, text ="USERNAME :",fg='white',bg='black',font = ("Times New Roman Bold", 15) ) 
    lbluser.place(x = 100, y = 200) 
    txtUser = tk.Entry(root, width = 35,fg='white',bg='black',font = ("Times New Roman Bold", 15)) 
    txtUser.place(x = 100, y = 250, width = 150) 
    lblpass = tk.Label(root, text ="PASSWORD :",fg='white',bg='black',font = ("Times New Roman Bold", 15)) 
    lblpass.place(x = 100, y = 400) 
    txtpass = tk.Entry(root,show="*", width = 35,fg='white',bg='black',font = ("Times New Roman Bold", 15)) 
    txtpass.place(x = 100, y = 450, width = 150) 
    btnlogin = tk.Button(root, text ="LOGIN", fg='white',bg='black',font = ("Times New Roman Bold", 15), command = lambda: login(x) )
    btnlogin.place(x = 1000, y = 200, width = 150)
    btnclear = tk.Button(root, text ="REGISTER", fg='white',bg='black',font = ("Times New Roman Bold", 15), command = lambda: register(x) )
    btnclear.place(x = 1000, y = 400, width = 150)
    heading = tk.Label(root, text ="LOGIN",fg='white',bg='black',font = ("Times New Roman Bold", 30) ) 
    heading.place(x = 500, y = 50)
    # Execute tkinter
    root.mainloop()

#-------------------------------------------------------------------------------------------------------------------
def page(x):
    def close(x):
        root.destroy()
        frmrent(x)
    
    def buy(x):
        try:
            myconn=mys.connect(host='localhost',user="root",\
                                 passwd="adis",database="library")
            if myconn.is_connected():
                print("connection succssful")
            mycur=myconn.cursor()
            query="SELECT * FROM BOOK WHERE NAME='{}'".format(x)
            mycur.execute(query)
            rs=mycur.fetchone()
            rs=list(rs)
            regno=rs[0]
            name=rs[1]
            athr=rs[2]
            price=rs[3]
            lang=rs[4]
            txtregno.insert(END,regno)
            txtname.insert(END,name)
            txtathr.insert(END,athr)
            txtprice.insert(END,price)
            txtlang.insert(END,lang)
    
        except Exception as e:
            print(e)
    
    root = tk.Toplevel()
    root.geometry("1200x800")
    root.title("LIBRARY MENU")
    bg = PhotoImage(file="C:/Users/viswa/Documents/VISWA/DOC/12-B/PYTHON/LIBRARY/admin.png")
    # Create Canvas
    canvas1 = Canvas( root, width = 400,height = 400)
    canvas1.pack(fill = "both", expand = True)
    # Display image
    canvas1.create_image( 0, 0, image = bg, anchor = "nw")
    root['background'] = 'black'
    lblregno = tk.Label(root, text ="REGNO :",fg='white',bg='black',font = ("Times New Roman Bold", 15) ) 
    lblregno.place(x = 50, y = 100 , width = 200)
    txtregno= tk.Entry(root, width = 35,fg='white',bg='black',font = ("Times New Roman Bold", 15)) 
    txtregno.place(x = 350, y = 100, width = 600) 
    lblname = tk.Label(root, text ="NAME :",fg='white',bg='black',font = ("Times New Roman Bold", 15)) 
    lblname.place(x = 50, y = 150, width = 200) 
    txtname = tk.Entry(root, width = 35,fg='white',bg='black',font = ("Times New Roman Bold", 15)) 
    txtname.place(x = 350, y = 150, width =600) 
    lblathr = tk.Label(root, text ="AUTHOR :",fg='white',bg='black',font = ("Times New Roman Bold", 15) ) 
    lblathr.place(x = 50, y = 200, width = 200) 
    txtathr = tk.Entry(root, width = 35,fg='white',bg='black',font = ("Times New Roman Bold", 15)) 
    txtathr.place(x = 350, y =200, width = 600) 
    lblprice = tk.Label(root, text ="PRICE :",fg='white',bg='black',font = ("Times New Roman Bold", 15)) 
    lblprice.place(x = 50, y = 250, width = 200)
    txtprice = tk.Entry(root, width = 35,fg='white',bg='black',font = ("Times New Roman Bold", 15)) 
    txtprice.place(x = 350, y = 250, width = 600)
    lbllang = tk.Label(root, text ="LANG :",fg='white',bg='black',font = ("Times New Roman Bold", 15)) 
    lbllang.place(x = 50, y = 300, width = 200)
    txtlang = tk.Entry(root, width = 35,fg='white',bg='black',font = ("Times New Roman Bold", 15)) 
    txtlang.place(x = 350, y = 300, width = 600)
    btnrent= tk.Button(root, text ="RENT", 
                    fg='white',bg='black',font = ("Times New Roman Bold", 15),command=lambda:close(x))
    btnrent.place(x = 1000, y = 100, width = 100)
    buy(x)
    root.mainloop()
#-------------------------------------------------------------------------------------------------------------------

def shop():
    def close():
        root.destroy()
        frmacclogin()
        
    def txt(i):
        for f in i:
            return(f)
        
    def button():
        try:
            myconn=mys.connect(host='localhost',user="root",\
                             passwd="adis",database="library")
            if myconn.is_connected():
                print("connection succssful")
            mycur=myconn.cursor()
            query="select name from book where avail='YES'"
            mycur.execute(query)
            rs=mycur.fetchall()
            rs=list(rs)
            button_dict={}
            for i in rs:
                def func(x=txt(i)):
                    root.destroy()
                    page(x)   
                button_dict[i]=tk.Button(canvas2, text=txt(i),fg='white',bg='black',font = ("Times New Roman Bold", 10),command= func)
                button_dict[i].pack(side = TOP, expand = True, fill = BOTH)

        except Exception as e:
            print(e)
    
    root = tk.Toplevel()
    root.geometry("1400x800")
    root.title("LIBRARY MENU")
    bg = PhotoImage(file="C:/Users/viswa/Documents/VISWA/DOC/12-B/PYTHON/LIBRARY/login.png")
    scroll_bar = Scrollbar(root)
    scroll_bar.pack( side = RIGHT,fill = Y )
    # Create Canvas
    canvas1 = Canvas( root, width = 900,height = 800)
    canvas1.pack(side = LEFT,fill = "both", expand = True)
    canvas2 = Canvas( root, width = 400,height =1500,yscrollcommand = scroll_bar.set)
    canvas2.pack(side = RIGHT,fill = "both", expand = True)
    # Display image
    canvas1.create_image( 0, 0, image = bg, anchor = "nw")
    canvas2.configure(scrollregion = canvas2.bbox("all"))
    scroll_bar.config( command = canvas2.yview )
    btnacc = tk.Button(root, text ="ACCOUNT",
                    fg='white',bg='black',font = ("Times New Roman Bold", 10),command=close) 
    btnacc.place(x = 100, y = 700, width = 100)
    root['background'] = 'black'
    button()
    root.mainloop()

#-------------------------------------------------------------------------------------------------------------------
def frmUser():
    try:
        myconn = mys.connect(host='localhost', user="root",\
                         passwd="adis", database="library")
        if myconn.is_connected():
            print("connection succssful")
        mycur = myconn.cursor()
        query = "select * from user"
        mycur.execute(query)
        rs = mycur.fetchall()
        root = tk.Tk() 
        root.geometry("1200x800")
        root.title("USER DATABASE")
        root['background'] = 'thistle'
        ttk.Label(root, text ="USER DATABASE",font = ("Times New Roman Bold", 20)).pack()
        frame = Frame(root)
        frame.pack()
        tree = ttk.Treeview(frame, columns = (1,2), height = 300, show = "headings")
        tree.pack(side = 'right')
        tree.heading(1, text = "NAME")
        tree.column(1, width = 400)
        tree.heading(2, text = "NO OF BOOKS")
        tree.column(2, width = 300)
        scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
        scroll.pack(side = 'right', fill = 'y')
        count=0
        def count(x):
            query = "select regno from book where user='{}'".format(x)
            mycur.execute(query)
            rs = mycur.fetchall()
            rs=list(rs)
            for i in rs:
                count=+1
                return(count)                

        for val in rs:
            tree.insert('', 'end', values = (val[0],count(val[0])))
                                         
    except Exception as e:
            print(e)

def frmDisplay():
    try:
        myconn = mys.connect(host='localhost', user="root",\
                         passwd="adis", database="library")
        if myconn.is_connected():
            print("connection succssful")
        mycur = myconn.cursor()
        query = "select * from book ORDER BY REGNO"
        mycur.execute(query)
        rs = mycur.fetchall()
        root = tk.Tk() 
        root.geometry("1200x800")
        root.title("LIBRARY DATABASE")
        root['background'] = 'thistle'
        ttk.Label(root, text ="LIBRARY DATABASE",font = ("Times New Roman Bold", 20)).pack()
        frame = Frame(root)
        frame.pack()
        tree = ttk.Treeview(frame, columns = (1,2,3,4,5,6), height = 300, show = "headings")
        tree.pack(side = 'right')
        tree.heading(1, text = "REGNO")
        tree.heading(2, text = "NAME")
        tree.heading(3, text = "AUTHOR")
        tree.heading(4, text = "PRICE")
        tree.heading(5, text = "LANG")
        tree.heading(6, text = "AVAIL")
        tree.column(1, width = 60)
        tree.column(2, width = 400)
        tree.column(3, width = 130)
        tree.column(4, width = 50)
        tree.column(5, width = 100)
        tree.column(6, width = 60)
        scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
        scroll.pack(side = 'right', fill = 'y')

        for val in rs:
            tree.insert('', 'end', values = (val[0], val[1], val[2],val[3],val[4],val[6]))
                                         
    except Exception as e:
            print(e)

def frmUpdate():
    def Clear():
        txtregno.delete(0,END)
        txtname.delete(0,END)
        txtathr.delete(0,END)
        txtprice.delete(0,END)
        txtlang.delete(0,END)
        
    def Update():
        regno = txtregno.get() 
        name = txtname.get()
        athr = txtathr.get()
        price = txtprice.get()
        lang = txtlang.get()
        avail= txtavail.get()
        myconn=mys.connect(host='localhost',user="root",\
                           passwd="adis",database="library")
        if myconn.is_connected():
            print("connection successful")
        mycur=myconn.cursor()
        query="update book set name='{}',athrname='{}',\
               price={},lang='{}',avail='{}' where regno={}".format(name,athr,price,lang,avail,regno)
        mycur.execute(query)
        myconn.commit()
        messagebox.showinfo("BOOK INFO","BOOK INFO UPDATED SUCCESSFULLY...")
        root.destroy()
        frmUpdate()
        
    def Search():
        try:
            myconn=mys.connect(host='localhost',user="root",\
                         passwd="adis",database="library")
            if myconn.is_connected():
                print("connection succssful")
            mycur=myconn.cursor()
            regno=txtregno.get()
            name = txtname.get()
            query="select * from book where regno={} or name='{}'".format(regno,name)
            mycur.execute(query)
            rs=mycur.fetchone()
            rs=list(rs)
            regno=rs[0]
            name=rs[1]
            athr=rs[2]
            price=rs[3]
            lang=rs[4]
            avail=rs[5]
            
            if rs==None:
                messagebox.showinfo("LIBRARY","NO BOOK FOUND")
            else:
                txtname.insert(END,name)
                txtathr.insert(END,athr)
                txtprice.insert(END,price)
                txtlang.insert(END,lang)
                txtavail.insert(END,avail)               
                
        except Exception as e:
            print(e)
         
    root = tk.Toplevel()
    root.geometry("500x500")
    root.title("LIBRARY MENU")
    bg = PhotoImage(file="C:/Users/viswa/Documents/VISWA/DOC/12-B/PYTHON/LIBRARY/window.png")
    # Create Canvas
    canvas1 = Canvas( root, width = 400,height = 400)
    canvas1.pack(fill = "both", expand = True)
    # Display image
    canvas1.create_image( 0, 0, image = bg, anchor = "nw")
    root['background'] = 'black'
    heading = tk.Label(root, text ="UPDATE",fg='white',bg='black',font = ("Times New Roman Bold", 15) ) 
    heading.place(x = 190, y = 40)
    lblregno = tk.Label(root, text ="REGNO",fg='white',bg='black',font = ("Times New Roman Bold", 10) ) 
    lblregno.place(x = 50, y = 100)
    txtregno= tk.Entry(root, width = 35,fg='white',bg='black',font = ("Times New Roman Bold", 10)) 
    txtregno.place(x = 350, y = 100, width = 100) 
    lblname = tk.Label(root, text ="NAME",fg='white',bg='black',font = ("Times New Roman Bold", 10)) 
    lblname.place(x = 50, y = 150) 
    txtname = tk.Entry(root, width = 35,fg='white',bg='black',font = ("Times New Roman Bold", 10)) 
    txtname.place(x = 350, y = 150, width = 100) 
    lblathr = tk.Label(root, text ="AUTHOR",fg='white',bg='black',font = ("Times New Roman Bold", 10) ) 
    lblathr.place(x = 50, y = 200) 
    txtathr = tk.Entry(root, width = 35,fg='white',bg='black',font = ("Times New Roman Bold", 10)) 
    txtathr.place(x = 350, y =200, width = 100) 
    lblprice = tk.Label(root, text ="PRICE",fg='white',bg='black',font = ("Times New Roman Bold", 10)) 
    lblprice.place(x = 50, y = 250)
    txtprice = tk.Entry(root, width = 35,fg='white',bg='black',font = ("Times New Roman Bold", 10)) 
    txtprice.place(x = 350, y = 250, width = 100)
    lbllang = tk.Label(root, text ="LANG",fg='white',bg='black',font = ("Times New Roman Bold", 10)) 
    lbllang.place(x = 50, y = 300)
    txtlang = tk.Entry(root, width = 35,fg='white',bg='black',font = ("Times New Roman Bold", 10)) 
    txtlang.place(x = 350, y = 300, width = 100)
    lblavail = tk.Label(root, text ="AVAIL",fg='white',bg='black',font = ("Times New Roman Bold", 10)) 
    lblavail.place(x = 50, y = 300)
    txtavail = tk.Entry(root, width = 35,fg='white',bg='black',font = ("Times New Roman Bold", 10)) 
    txtavail.place(x = 350, y = 300, width = 100)
    btnupdate = tk.Button(root, text ="UPDATE",
                    fg='white',bg='black',font = ("Times New Roman Bold", 10),command=Update) 
    btnupdate.place(x = 100, y = 400, width = 80)
    btnsearch = tk.Button(root, text ="SEARCH", 
                    fg='white',bg='black',font = ("Times New Roman Bold", 10),command=Search) 
    btnsearch.place(x = 200, y = 400, width = 80)
    btnclear = tk.Button(root, text ="CLEAR", 
                    fg='white',bg='black',font = ("Times New Roman Bold", 10),command=Clear) 
    btnclear.place(x = 300, y = 400, width = 80)
    root.mainloop()
    
def frmDelete():
    def Clear():
        txtregno.delete(0,END)
        txtname.delete(0,END)
        txtathr.delete(0,END)
        txtprice.delete(0,END)
        txtlang.delete(0,END)
    def Delete():
        regno = txtregno.get() 
        myconn=mys.connect(host='localhost',user="root",\
                           passwd="adis",database="library")
        if myconn.is_connected():
            print("connection successful")
        mycur=myconn.cursor()
        query="delete from book where regno={}".format(regno)
        mycur.execute(query)
        myconn.commit()
        messagebox.showinfo("LIBRARY INFO"," BOOK DELETED... ")
        root.destroy()
        frmDelete()
    def Search():
        try:
            myconn=mys.connect(host='localhost',user="root",\
                         passwd="adis",database="library")
            if myconn.is_connected():
                print("connection succssful")
            mycur=myconn.cursor()
            rno=txtregno.get()
            query="select * from book where regno={}".format(rno)
            mycur.execute(query)
            rs=mycur.fetchone()
            rs=list(rs)
            regno=rs[0]
            name=rs[1]
            athr=rs[2]
            price=rs[3]
            lang=rs[4]
            
            if rs==None:
                messagebox.showinfo("LIBRARY","NO BOOK FOUND")
            else:
                txtname.insert(END,name)
                txtathr.insert(END,athr)
                txtprice.insert(END,price)
                txtlang.insert(END,lang)
                
        except Exception as e:
            print(e)
        
    root = tk.Toplevel()
    root.geometry("500x500")
    root.title("LIBRARY MENU")
    bg = PhotoImage(file="C:/Users/viswa/Documents/VISWA/DOC/12-B/PYTHON/LIBRARY/window.png")
    # Create Canvas
    canvas1 = Canvas( root, width = 400,height = 400)
    canvas1.pack(fill = "both", expand = True)
    # Display image
    canvas1.create_image( 0, 0, image = bg, anchor = "nw")
    root['background'] = 'black'
    heading = tk.Label(root, text ="DELETE",fg='white',bg='black',font = ("Times New Roman Bold", 15) ) 
    heading.place(x = 190, y = 40)
    lblregno = tk.Label(root, text ="REGNO",fg='white',bg='black',font = ("Times New Roman Bold", 10) ) 
    lblregno.place(x = 50, y = 100)
    txtregno= tk.Entry(root, width = 35,fg='white',bg='black',font = ("Times New Roman Bold", 10)) 
    txtregno.place(x = 350, y = 100, width = 100) 
    lblname = tk.Label(root, text ="NAME",fg='white',bg='black',font = ("Times New Roman Bold", 10)) 
    lblname.place(x = 50, y = 150) 
    txtname = tk.Entry(root, width = 35,fg='white',bg='black',font = ("Times New Roman Bold", 10)) 
    txtname.place(x = 350, y = 150, width = 100) 
    lblathr = tk.Label(root, text ="AUTHOR",fg='white',bg='black',font = ("Times New Roman Bold", 10) ) 
    lblathr.place(x = 50, y = 200) 
    txtathr = tk.Entry(root, width = 35,fg='white',bg='black',font = ("Times New Roman Bold", 10)) 
    txtathr.place(x = 350, y =200, width = 100) 
    lblprice = tk.Label(root, text ="PRICE",fg='white',bg='black',font = ("Times New Roman Bold", 10)) 
    lblprice.place(x = 50, y = 250)
    txtprice = tk.Entry(root, width = 35,fg='white',bg='black',font = ("Times New Roman Bold", 10)) 
    txtprice.place(x = 350, y = 250, width = 100)
    lbllang = tk.Label(root, text ="LANG",fg='white',bg='black',font = ("Times New Roman Bold", 10)) 
    lbllang.place(x = 50, y = 300)
    txtlang = tk.Entry(root, width = 35,fg='white',bg='black',font = ("Times New Roman Bold", 10)) 
    txtlang.place(x = 350, y = 300, width = 100)
    btnupdate = tk.Button(root, text ="DELETE",
                    fg='white',bg='black',font = ("Times New Roman Bold", 10),command=Delete) 
    btnupdate.place(x = 100, y = 400, width = 80)
    btnsearch = tk.Button(root, text ="SEARCH", 
                    fg='white',bg='black',font = ("Times New Roman Bold", 10),command=Search) 
    btnsearch.place(x = 200, y = 400, width = 80)
    btnclear = tk.Button(root, text ="CLEAR", 
                    fg='white',bg='black',font = ("Times New Roman Bold", 10),command=Clear) 
    btnclear.place(x = 300, y = 400, width = 80)
    root.mainloop()
    
def frmInsert():
    def Clear():
        txtregno.delete(0,END)
        txtname.delete(0,END)
        txtathr.delete(0,END)
        txtprice.delete(0,END)
        txtlang.delete(0,END)
        
    def Insert():
        regno = txtregno.get() 
        name = txtname.get()
        athr = txtathr.get()
        price = txtprice.get()
        lang = txtlang.get()
        try:
            myconn=mys.connect(host='localhost',user="root",\
                           passwd="adis",database="library")
            if myconn.is_connected():
                print("connection successful")
            mycur=myconn.cursor()
            avail='YES'
            query="insert into book (regno,name,athrname,price,lang) values \
                   ({},'{}','{}',{},'{}')".format(regno,name,athr,price,lang)
            mycur.execute(query)
            myconn.commit()
            messagebox.showinfo("LIBRARY INFO"," BOOK INSERTED... ")
            root.destroy()
            frmInsert()
        except Exception as e:
            print(e)
            
        
    root = tk.Toplevel()
    root.geometry("500x500")
    root.title("LIBRARY MENU")
    bg = PhotoImage(file="C:/Users/viswa/Documents/VISWA/DOC/12-B/PYTHON/LIBRARY/window.png")
    # Create Canvas
    canvas1 = Canvas( root, width = 400,height = 400)
    canvas1.pack(fill = "both", expand = True)
    # Display image
    canvas1.create_image( 0, 0, image = bg, anchor = "nw")
    root['background'] = 'black'
    heading = tk.Label(root, text ="INSERT",fg='white',bg='black',font = ("Times New Roman Bold", 15) ) 
    heading.place(x = 190, y = 40)
    lblregno = tk.Label(root, text ="REGNO",fg='white',bg='black',font = ("Times New Roman Bold", 10) ) 
    lblregno.place(x = 50, y = 100)
    txtregno= tk.Entry(root, width = 35,fg='white',bg='black',font = ("Times New Roman Bold", 10)) 
    txtregno.place(x = 350, y = 100, width = 100) 
    lblname = tk.Label(root, text ="NAME",fg='white',bg='black',font = ("Times New Roman Bold", 10)) 
    lblname.place(x = 50, y = 150) 
    txtname = tk.Entry(root, width = 35,fg='white',bg='black',font = ("Times New Roman Bold", 10)) 
    txtname.place(x = 350, y = 150, width = 100) 
    lblathr = tk.Label(root, text ="AUTHOR",fg='white',bg='black',font = ("Times New Roman Bold", 10) ) 
    lblathr.place(x = 50, y = 200) 
    txtathr = tk.Entry(root, width = 35,fg='white',bg='black',font = ("Times New Roman Bold", 10)) 
    txtathr.place(x = 350, y =200, width = 100) 
    lblprice = tk.Label(root, text ="PRICE",fg='white',bg='black',font = ("Times New Roman Bold", 10)) 
    lblprice.place(x = 50, y = 250)
    txtprice = tk.Entry(root, width = 35,fg='white',bg='black',font = ("Times New Roman Bold", 10)) 
    txtprice.place(x = 350, y = 250, width = 100)
    lbllang = tk.Label(root, text ="LANG",fg='white',bg='black',font = ("Times New Roman Bold", 10)) 
    lbllang.place(x = 50, y = 300)
    txtlang = tk.Entry(root, width = 35,fg='white',bg='black',font = ("Times New Roman Bold", 10)) 
    txtlang.place(x = 350, y = 300, width = 100)
    btnupdate = tk.Button(root, text ="INSERT",
                    fg='white',bg='black',font = ("Times New Roman Bold", 10),command=Insert) 
    btnupdate.place(x = 100, y = 400, width = 80)
    btnclear = tk.Button(root, text ="CLEAR", 
                    fg='white',bg='black',font = ("Times New Roman Bold", 10),command=Clear) 
    btnclear.place(x = 300, y = 400, width = 80)
    root.mainloop()

#-------------------------------------------------------------------------------------------------------------------

def admin():
    
    root = tk.Toplevel()
    root.geometry("1200x800")
    root.title("LIBRARY MENU")
    bg = PhotoImage(file="C:/Users/viswa/Documents/VISWA/DOC/12-B/PYTHON/LIBRARY/admin.png")
    # Create Canvas
    canvas1 = Canvas( root, width = 400,height = 400)
    canvas1.pack(fill = "both", expand = True)
    # Display image
    canvas1.create_image( 0, 0, image = bg, anchor = "nw")
    root['background'] = 'brown'
    lblwelc = tk.Label(root, text = "ADMIN MENU",
                    fg ='black', bg='white',borderwidth=2, relief="ridge",font = ("Times New Roman Bold", 33))
    lblwelc.place(x = 370, y = 50)
    btninsert = tk.Button(root, text ="INSERT", 
                    fg='deepskyblue',bg='black',font = ("Times New Roman Bold", 15),command=frmInsert) 
    btninsert.place(x = 950, y = 200, width = 150)
    btnupdate = tk.Button(root, text ="UPDATE",
                    fg='deepskyblue',bg='black',font = ("Times New Roman Bold", 15),command=frmUpdate) 
    btnupdate.place(x = 950, y = 300, width = 150)
    btndelete = tk.Button(root, text ="DELETE",
                    fg='deepskyblue',bg='black',font = ("Times New Roman Bold", 15),command=frmDelete) 
    btndelete.place(x = 950, y = 400, width = 150)
    btndisplay = tk.Button(root, text ="DISPLAY", 
                    fg='deepskyblue',bg='black',font = ("Times New Roman Bold", 15),command=frmDisplay) 
    btndisplay.place(x = 950, y = 500, width = 150)
    btndisplay = tk.Button(root, text ="USERS", 
                    fg='deepskyblue',bg='black',font = ("Times New Roman Bold", 15),command=frmUser) 
    btndisplay.place(x = 950, y = 600, width = 150)
    root.mainloop()

#-------------------------------------------------------------------------------------------------------------------

def loginscr():
    def clear():
        txtUser.delete(0,END)
        txtpass.delete(0,END)
    
    def login():
        passw=txtpass.get()
        usern=txtUser.get()
        if passw=="adis" and usern=="ADIS": 
            myconn = mys.connect(host ="localhost",user = "root",passwd="adis",database ="library") 
            cursor = myconn.cursor() 
            messagebox.showinfo("Login Successful","LOGIN SUCCESSFUL")
            root.destroy()
            admin()
        else:
            messagebox.showinfo("LOGIN DENIED, TRY AGAIN" )
    
    root = tk.Toplevel() 
    root.geometry("1200x800")
    root.title("KINTER LOGIN PAGE")
    bg = PhotoImage(file="C:/Users/viswa/Documents/VISWA/DOC/12-B/PYTHON/LIBRARY/login.png")
    # Create Canvas
    canvas1 = Canvas( root, width = 400,height = 400)
    canvas1.pack(fill = "both", expand = True)
    # Display image
    canvas1.create_image( 0, 0, image = bg, anchor = "nw")
    lbluser = tk.Label(root, text ="USERNAME :",fg='white',bg='black',font = ("Times New Roman Bold",15) ) 
    lbluser.place(x = 100, y = 200) 
    txtUser = tk.Entry(root, width = 35,fg='white',bg='black',font = ("Times New Roman Bold", 15)) 
    txtUser.place(x = 100, y = 250, width = 150) 
    lblpass = tk.Label(root, text ="PASSWORD :",fg='white',bg='black',font = ("Times New Roman Bold", 15)) 
    lblpass.place(x = 100, y = 400) 
    txtpass = tk.Entry(root,show="*", width = 35,fg='white',bg='black',font = ("Times New Roman Bold", 15)) 
    txtpass.place(x = 100, y = 450, width = 150) 
    btnlogin = tk.Button(root, text ="LOGIN", fg='white',bg='black',font = ("Times New Roman Bold", 15), command = login )
    btnlogin.place(x = 1000, y = 200, width = 150)
    btnclear = tk.Button(root, text ="CLEAR", fg='white',bg='black',font = ("Times New Roman Bold", 15), command = clear )
    btnclear.place(x = 1000, y = 400, width = 150)
    heading = tk.Label(root, text ="LOGIN",fg='white',bg='black',font = ("Times New Roman Bold", 30) ) 
    heading.place(x = 500, y = 50)
    # Execute tkinter
    root.mainloop()

#-------------------------------------------------------------------------------------------------------------------

def WelcomeScr():
    def login():
        root.destroy()
        loginscr()
    def store():
        root.destroy()
        shop()

    root = tk.Tk() 
    root.geometry("1200x800")
    root.title("KINTER LOGIN PAGE")
    bg = PhotoImage(file="C:/Users/viswa/Documents/VISWA/DOC/12-B/PYTHON/LIBRARY/welcome.png")
    # Create Canvas
    canvas1 = Canvas( root, width = 400,height = 400)
    canvas1.pack(fill ="both", expand = True)
    # Display image
    canvas1.create_image( 0, 0, image = bg, anchor = "nw")
    # Create Buttons
    store = Button( root, text = "STORE", bg='white',font = ("Times New Roman Bold", 25), command = store)
    admin = Button( root, text = "ADMIN",bg='white',font = ("Times New Roman Bold", 25), command = login)
    # Display Buttons
    store_canvas = canvas1.create_window( 750, 600, anchor = "nw",window = store)
    admin_canvas = canvas1.create_window( 250, 600,anchor = "nw",window = admin)
    # Execute tkinter
    root.mainloop()

# main program
WelcomeScr()

# ------------------------------------------------------------------------------------------------------------------------
