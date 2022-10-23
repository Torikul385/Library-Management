from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import datetime
# from datetime import date
# from datetime import datetime
import tkinter


class Library:
    def __init__(self,root):
        self.root = root
        self.root.title("RUET LIBRARY")
        self.root.geometry("1550x800+0+0")
        #---------------------------- variables ----------------------------
        self.member = StringVar()
        self.member_id = IntVar()
        self.firstName = StringVar()
        self.lastName = StringVar()
        self.address = StringVar()
        self.postCode = IntVar()
        self.contact = IntVar()
        self.book1 = StringVar()
        self.book2 = StringVar()
        self.fine = IntVar()
        self.since = StringVar()

        self.book_id = IntVar()
        self.title = StringVar()
        self.author = StringVar()
        self.price = IntVar()
        self.type = StringVar()
        self.language = StringVar()
        self.amount = IntVar()
        self.dateLend1 = StringVar()
        self.remaining1 = IntVar()
        self.fine1 = IntVar()


        self.book_id2 = IntVar()
        self.title2 = StringVar()
        self.author2 = StringVar()
        self.price2 = IntVar()
        self.type2 = StringVar()
        self.language2 = StringVar()
        self.amount2 = IntVar()
        self.dateLend2 = StringVar()
        self.remaining2 = IntVar()
        self.fine2 = IntVar()
        #-------------------------------- variable for window-------------------------------
        # self.lend_1 = Tk()
        # self.lend_2 = Tk()

        #------------------- library title -----------------
        lbltitle = Label(root,text="RUET LIBRARY", bg="#126",bd=5,fg="#aaa",font=("Helvetica",25,"bold"),padx=2,pady=4)
        lbltitle.place(x=0,y=0,height=120,width=700)

        #-------------- search option ---------------
        searchFrame = Frame(self.root,bg="#124",padx=90,pady=38)
        searchFrame.place(x=700,y=0,height=120,width=850)

        s1text= Label(searchFrame,text="Search member (ID) ",font=("Helvetica",10,"bold"),bg="#124",fg="white",padx=10)
        s1text.grid(row=0,column=0)
        self.search_member_id = IntVar()
        s1Entry = Entry(searchFrame,width=30,bg="#412",fg="white",font=("Helvetica",10,"bold"),textvariable=self.search_member_id)
        s1Entry.grid(row=0,column=1)
        s1Button = Button(searchFrame,text="SEARCH",padx=10,pady=0,fg="#145",command=lambda:self.singleMemberInfo(self.search_member_id.get()))
        s1Button.grid(row=0,column=2)


        self.search_book_id = IntVar()
        s2text= Label(searchFrame,text="Search book (ID) ",font=("Helvetica",10,"bold"),bg="#124",fg="white",padx=10)
        s2text.grid(row=1,column=0)
        s2Entry = Entry(searchFrame,width=30,bg="#372",fg="white",font=("Helvetica",10,"bold"),textvariable=self.search_book_id)
        s2Entry.grid(row=1,column=1)
        s2Button = Button(searchFrame,text="SEARCH",padx=10,pady=0,fg="#145",command=lambda:self.singleBookInfo(self.search_book_id.get()))
        s2Button.grid(row=1,column=2)

        #--------------- frame ------------------------------
        frame = Frame(self.root,padx=10,pady=10,bg="#114")
        frame.place(x=0,y=120,height=350,width=1550)
        #----------------- data frame left -----------------------------
        dfLeft = LabelFrame(frame,bg="#114",text="Member Information",fg="#ccc",font=("Helvetica",10,"bold"),padx=5,pady=1)
        dfLeft.place(x=0,y=5,height=330,width=710)
        #----------------- data frame middle -------------------
        dfMiddle = LabelFrame(frame,bg="#114",text="Operations" , fg="#ccc",font=("Helvetica",10,"bold"),padx=20,pady=12)
        dfMiddle.place(x=715,y=5,height=330,width=520)
        #---------------- data frame right --------------------
        dfRight = LabelFrame(frame,bg="#114",text="Books List",fg="#ccc",font=("Helvetica",10,"bold"),padx=5,pady=1)
        dfRight.place(x=1235,y=5,height=330,width=280)
        # bfooter = Frame(dfRight,padx=5,pady=5,bg="#137")
        # bfooter.place(x=0,y=470,height=330,width=280)

        btfooter = Frame(dfRight,padx=5,pady=5,bg="#147")
        btfooter.place(x=0,y=0,width=280,height=320)

        bfxscroll = ttk.Scrollbar(btfooter,orient=HORIZONTAL)

        bfyscroll = ttk.Scrollbar(btfooter,orient=VERTICAL)


        self.bftable = ttk.Treeview(btfooter,column=("id","title","author"),xscrollcommand=bfxscroll.set,yscrollcommand=bfyscroll.set)
        bfxscroll.pack(side=BOTTOM,fill=X)
        bfyscroll.pack(side=RIGHT,fill=Y)

        bfxscroll.config(command=self.bftable.xview)
        bfyscroll.config(command=self.bftable.yview)

        self.bftable.heading("id",text="ID")
        self.bftable.heading("title",text="Title")
        self.bftable.heading("author",text="Author")

        self.bftable["show"] = "headings"
        self.bftable.pack(fill = BOTH,expand=1)

        self.bftable.column("id",width=80)
        self.bftable.column("title",width=80)
        self.bftable.column("author",width=80)
        self.fetch_book_data()
        #----------------------- member information box-------------------------------------------------------------------------------
        lblMember = Label(dfLeft,text="Member Type",bg="#114",fg="white",font=("Helvetica",10,"bold"),padx=5,pady=5)
        lblMember.grid(row=0,column=0,sticky=W)

        comMember = ttk.Combobox(dfLeft ,textvariable=self.member ,  font=("Helvetica" , 10 , "bold") , width=16, state="readonly")
        comMember["value"] = ("Admin Stuff" , "Student" , "Teacher" )
        comMember.current(0)
        comMember.grid(row=0,column=1)

        lblID = Label(dfLeft , text="ID No : " ,bg="#114",fg="white",font=("Helvetica",10,"bold"),padx=5,pady=5)
        lblID.grid(row=1,column=0,sticky=W)
        txtID = Entry(dfLeft  ,textvariable=self.member_id, font=("Helvetica" , 10 , "bold" ), bg="#114",fg="white" , width =18 )
        txtID.grid(row=1,column=1)

        lblFirstName = Label(dfLeft, text="First Name : " ,bg="#114",fg="white",font=("Helvetica",10,"bold"),padx=5,pady=5)
        lblFirstName.grid(row=2,column=0,sticky=W)
        txtFirstName = Entry(dfLeft  ,textvariable=self.firstName, font=("Helvetica" , 10 , "bold" ), bg="#114",fg="white" , width =18 )
        txtFirstName.grid(row=2,column=1)

        lblLastName = Label(dfLeft, text="Last Name : " ,bg="#114",fg="white",font=("Helvetica",10,"bold"),padx=5,pady=5)
        lblLastName.grid(row=3,column=0,sticky=W)
        txtLastName = Entry(dfLeft  ,textvariable=self.lastName, font=("Helvetica" , 10 , "bold" ), bg="#114",fg="white" , width =18 )
        txtLastName.grid(row=3,column=1)

        lbladdress = Label(dfLeft, text="Address : " ,bg="#114",fg="white",font=("Helvetica",10,"bold"),padx=5,pady=5)
        lbladdress.grid(row=4,column=0,sticky=W)
        txtaddress = Entry(dfLeft  ,textvariable=self.address, font=("Helvetica" , 10 , "bold" ), bg="#114",fg="white" , width =18 )
        txtaddress.grid(row=4,column=1)

        lblpost = Label(dfLeft, text="Post Code : " ,bg="#114",fg="white",font=("Helvetica",10,"bold"),padx=5,pady=5)
        lblpost.grid(row=5,column=0,sticky=W)
        txtpost = Entry(dfLeft  ,textvariable=self.postCode, font=("Helvetica" , 10 , "bold" ), bg="#114",fg="white" , width =18 )
        txtpost.grid(row=5,column=1)

        lblcontact = Label(dfLeft, text="Contact : " ,bg="#114",fg="white",font=("Helvetica",10,"bold"),padx=5,pady=5)
        lblcontact.grid(row=6,column=0,sticky=W)
        txtcontact = Entry(dfLeft  ,textvariable=self.contact, font=("Helvetica" , 10 , "bold" ), bg="#114",fg="white" , width =18 )
        txtcontact.grid(row=6,column=1)

        lblfine = Label(dfLeft, text="Total Fine : " ,bg="#114",fg="white",font=("Helvetica",10,"bold"),padx=5,pady=5)
        lblfine.grid(row=7,column=0,sticky=W)
        txtfine = Entry(dfLeft  ,textvariable=self.fine, font=("Helvetica" , 10 , "bold" ), bg="#114",fg="white" , width =18 )
        txtfine.grid(row=7,column=1)

        lblsince = Label(dfLeft, text="Member since : " ,bg="#114",fg="white",font=("Helvetica",10,"bold"),padx=5,pady=5)
        lblsince.grid(row=8,column=0,sticky=W)
        txtsince = Entry(dfLeft  ,textvariable=self.since, font=("Helvetica" , 10 , "bold" ), bg="#114",fg="white" , width =18 )
        txtsince.grid(row=8,column=1)
        #--------------------- Book 1 ---------------------------------------------------------
        lblbook1 = Label(dfLeft, text="Book 1 Information " ,bg="#114",fg="white",font=("Helvetica",10,"bold"),padx=15,pady=5)
        lblbook1.grid(row=0,column=2,sticky = E,columnspan=7)

        lbl1id = Label(dfLeft,text="ID : " , bg="#114",fg="white",font=("Helvetica",10,"bold"),padx=60,pady=5)
        lbl1id.grid(row=1,column=2,sticky=W,columnspan=4)
        txt1id = Entry(dfLeft,textvariable=self.book_id, bg="#114",fg="white",font=("Helvetica",10,"bold"),width=18)
        txt1id.grid(row=1,column=6,sticky=W)

        lbl1title = Label(dfLeft,text="Title : " , bg="#114",fg="white",font=("Helvetica",10,"bold"),padx=1,pady=5)
        lbl1title.grid(row=2,column=2,columnspan=4)
        txt1title = Entry(dfLeft,textvariable=self.title, bg="#114",fg="white",font=("Helvetica",10,"bold"),width=18)
        txt1title.grid(row=2,column=6,sticky=W)

        lbl1author = Label(dfLeft,text="Author :  " , bg="#114",fg="white",font=("Helvetica",10,"bold"),padx=1,pady=5)
        lbl1author.grid(row=3,column=2,columnspan=4)
        txt1author = Entry(dfLeft,textvariable=self.author, bg="#114",fg="white",font=("Helvetica",10,"bold"),width=18)
        txt1author.grid(row=3,column=6,sticky=W)

        lbl1type = Label(dfLeft,text="Type : " , bg="#114",fg="white",font=("Helvetica",10,"bold"),padx=1,pady=5)
        lbl1type.grid(row=4,column=2,columnspan=4)
        txt1type = Entry(dfLeft,textvariable=self.type, bg="#114",fg="white",font=("Helvetica",10,"bold"),width=18)
        txt1type.grid(row=4,column=6,sticky=W)

        lbl1language = Label(dfLeft,text="Language : " , bg="#114",fg="white",font=("Helvetica",10,"bold"),padx=1,pady=5)
        lbl1language.grid(row=5,column=2,columnspan=4)
        txt1language = Entry(dfLeft,textvariable=self.language, bg="#114",fg="white",font=("Helvetica",10,"bold"),width=18)
        txt1language.grid(row=5,column=6,sticky=W)

        lbl1lend = Label(dfLeft,text="Lend Date : " , bg="#114",fg="white",font=("Helvetica",10,"bold"),padx=1,pady=5)
        lbl1lend.grid(row=6,column=2,columnspan=4)
        txt1lend = Entry(dfLeft,textvariable=self.dateLend1, bg="#114",fg="white",font=("Helvetica",10,"bold"),width=18)
        txt1lend.grid(row=6,column=6,sticky=W)

        lbl1remaining = Label(dfLeft,text="Remaining : " , bg="#114",fg="white",font=("Helvetica",10,"bold"),padx=1,pady=5)
        lbl1remaining.grid(row=7,column=2,columnspan=4)
        txt1remaining = Entry(dfLeft,textvariable=self.remaining1, bg="#114",fg="white",font=("Helvetica",10,"bold"),width=18)
        txt1remaining.grid(row=7,column=6,sticky=W)

        lbl1fine = Label(dfLeft,text="Fine : " , bg="#114",fg="white",font=("Helvetica",10,"bold"),padx=1,pady=5)
        lbl1fine.grid(row=8,column=2,columnspan=4)
        txt1fine = Entry(dfLeft,textvariable=self.fine1, bg="#114",fg="white",font=("Helvetica",10,"bold"),width=18)
        txt1fine.grid(row=8,column=6,sticky=W)

        # ------------------- Book 2 information ------------------------
        lblbook2 = Label(dfLeft, text="Book 2 Information " ,bg="#114",fg="white",font=("Helvetica",10,"bold"),padx=15,pady=5)
        lblbook2.grid(row=0,column=10,sticky = E,columnspan=7)

        lbl2id = Label(dfLeft,text="" , bg="#114",fg="white",font=("Helvetica",10,"bold"),padx=1,pady=5)
        lbl2id.grid(row=1,column=12,sticky=W,columnspan=7)
        txt2id = Entry(dfLeft,textvariable=self.book_id2, bg="#114",fg="white",font=("Helvetica",10,"bold"),width=18)
        txt2id.grid(row=1,column=13,sticky=W)

        lbl2title = Label(dfLeft,text="" , bg="#114",fg="white",font=("Helvetica",10,"bold"),padx=1,pady=5)
        lbl2title.grid(row=2,column=12,sticky=W)
        txt2title = Entry(dfLeft,textvariable=self.title2, bg="#114",fg="white",font=("Helvetica",10,"bold"),width=18)
        txt2title.grid(row=2,column=13,sticky=W)

        lbl2author = Label(dfLeft,text="" , bg="#114",fg="white",font=("Helvetica",10,"bold"),padx=1,pady=5)
        lbl2author.grid(row=3,column=12,sticky=W)
        txt2author = Entry(dfLeft,textvariable=self.author2, bg="#114",fg="white",font=("Helvetica",10,"bold"),width=18)
        txt2author.grid(row=3,column=13,sticky=W)

        lbl2type = Label(dfLeft,text="" , bg="#114",fg="white",font=("Helvetica",10,"bold"),padx=1,pady=5)
        lbl2type.grid(row=4,column=12,sticky=W)
        txt2type = Entry(dfLeft,textvariable=self.type2, bg="#114",fg="white",font=("Helvetica",10,"bold"),width=18)
        txt2type.grid(row=4,column=13,sticky=W)

        lbl2language = Label(dfLeft,text="" , bg="#114",fg="white",font=("Helvetica",10,"bold"),padx=1,pady=5)
        lbl2language.grid(row=5,column=12,sticky=W)
        txt2language = Entry(dfLeft,textvariable=self.language2, bg="#114",fg="white",font=("Helvetica",10,"bold"),width=18)
        txt2language.grid(row=5,column=13,sticky=W)

        lbl2lend = Label(dfLeft,text="" , bg="#114",fg="white",font=("Helvetica",10,"bold"),padx=1,pady=5)
        lbl2lend.grid(row=6,column=12,sticky=W)
        txt2lend = Entry(dfLeft,textvariable=self.dateLend2, bg="#114",fg="white",font=("Helvetica",10,"bold"),width=18)
        txt2lend.grid(row=6,column=13,sticky=W)

        lbl2remaining = Label(dfLeft,text="" , bg="#114",fg="white",font=("Helvetica",10,"bold"),padx=1,pady=5)
        lbl2remaining.grid(row=7,column=12,sticky=W)
        txt2remaining = Entry(dfLeft,textvariable=self.remaining2, bg="#114",fg="white",font=("Helvetica",10,"bold"),width=18)
        txt2remaining.grid(row=7,column=13,sticky=W)

        lbl2fine = Label(dfLeft,text="" , bg="#114",fg="white",font=("Helvetica",10,"bold"),padx=1,pady=5)
        lbl2fine.grid(row=8,column=12,sticky=W)
        txt2fine = Entry(dfLeft,textvariable=self.fine2, bg="#114",fg="white",font=("Helvetica",10,"bold"),width=18)
        txt2fine.grid(row=8,column=13,sticky=W)
        #-------------------------------- all functional button --------------------------------------

        #------------------ data frame middle -----------------------------------
        addMember = Button(dfMiddle,text="Add Member",bg="#bbb",fg="#000",font=("Helvetica",10,"bold"),width=18,height=1,command=self.AddMember)
        addMember.place(x=50,y=0,width=150)

        # fau2 = Label(dfMiddle,text="")
        # fau2.grid(row=0,column=1,columnspan=3)

        addBook = Button(dfMiddle,text="Add Book",bg="#bbb",fg="#000",font=("Helvetica",10,"bold"),width=18,height=1,command=self.AddBook)
        addBook.place(x=250,y=0,width=150)

        receiveBook = Button(dfMiddle,text="Receive Book",bg="#bbb",fg="#000",font=("Helvetica",10,"bold"),width=18,height=1 , command=self.ReceiveBook)
        receiveBook.place(x=50,y=50,width=150)

        lendBook = Button(dfMiddle,text="Lend Book",bg="#bbb",fg="#000",font=("Helvetica",10,"bold"),width=18,height=1, command=self.lendBook)
        lendBook.place(x=250,y=50,width=150)

        memberInfo = Button(dfMiddle,text="Members Info",bg="#bbb",fg="#000",font=("Helvetica",10,"bold"),width=18,height=1 , command = self.memberInfo)
        memberInfo.place(x=50,y=100,width=150)

        bookInfo = Button(dfMiddle,text="Book Info",bg="#bbb",fg="#000",font=("Helvetica",10,"bold"),width=18,height=1 , command=self.BookInfo)
        bookInfo.place(x=250,y=100,width=150)

        delMember =  Button(dfMiddle,text="Delete Member",bg="#bbb",fg="#000",font=("Helvetica",10,"bold"),width=18,height=1 , command=self.delMember)
        delMember.place(x=50,y=150,width=150)

        delBook =  Button(dfMiddle,text="Delete Book",bg="#bbb",fg="#000",font=("Helvetica",10,"bold"),width=18,height=1 , command=self.deleteBook )
        delBook.place(x=250,y=150,width=150)

        Reset =  Button(dfMiddle,text="Reset Fields",bg="#bbb",fg="#000",font=("Helvetica",10,"bold"),width=18,height=1,command=self.resetAll)
        Reset.place(x=50,y=200,width=150)



        #------------------------------------- footer ----------------------------------------------------------
        footer = Frame(self.root,padx=5,pady=5,bg="#137")
        footer.place(x=0,y=470,height=320,width=1540)

        tfooter = Frame(footer,padx=5,pady=5,bg="#147")
        tfooter.place(x=0,y=0,width=1540,height=320)

        fxscroll = ttk.Scrollbar(tfooter,orient=HORIZONTAL)

        fyscroll = ttk.Scrollbar(tfooter,orient=VERTICAL)


        self.ftable = ttk.Treeview(tfooter,column=("member","id","first","last","address","post","contact","fine", "since", "book1","book2" , "fine1","fine2","lend1","lend2"),xscrollcommand=fxscroll.set,yscrollcommand=fyscroll.set)
        fxscroll.pack(side=BOTTOM,fill=X)
        fyscroll.pack(side=RIGHT,fill=Y)

        fxscroll.config(command=self.ftable.xview)
        fyscroll.config(command=self.ftable.yview)

        self.ftable.heading("member",text="Member Type")
        self.ftable.heading("id",text="Member ID")
        self.ftable.heading("first",text="First Name")
        self.ftable.heading("last",text="Last Name")
        self.ftable.heading("address",text="Address")
        self.ftable.heading("post",text="Post Code")
        self.ftable.heading("contact",text="Contact")
        self.ftable.heading("fine",text="Fine")
        self.ftable.heading("since",text="Since")
        self.ftable.heading("book1",text="Book 1")
        self.ftable.heading("book2",text="Book 2")
        self.ftable.heading("fine1",text="Fine 1")
        self.ftable.heading("fine2",text="Fine 2")
        self.ftable.heading("lend1",text="Lend 1")
        self.ftable.heading("lend2",text="Lend 2")


        self.ftable["show"] = "headings"
        self.ftable.pack(fill = BOTH,expand=1)

        self.ftable.column("member",width=100)
        self.ftable.column("id",width=100)
        self.ftable.column("first",width=100)
        self.ftable.column("last",width=100)
        self.ftable.column("address",width=100)
        self.ftable.column("post",width=100)
        self.ftable.column("contact" , width=100)
        self.ftable.column("fine",width=100)
        self.ftable.column("since",width=100)
        self.ftable.column("book1",width=100)
        self.ftable.column("book2",width=100)
        self.ftable.column("fine1",width=100)
        self.ftable.column("fine2",width=100)
        self.ftable.column("lend1",width=100)
        self.ftable.column("lend2",width=100)

        self.fetch_data()
#----------------------------- all functions -------------------------------
    def fetch_book_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="root",database="world")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM books")
        datas = cursor.fetchall()
        if len(datas):
            self.bftable.delete(*self.bftable.get_children())
            for data in datas:
                val = []
                val.append(data[0])
                val.append(data[1])
                val.append(data[2])
                self.bftable.insert("",END,values=val)
            conn.commit()
        else:
            self.bftable.delete(*self.bftable.get_children())
            val = []
            self.bftable.insert("",END,values=val)
        conn.close()
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="root",database="world")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM member")
        rows = cursor.fetchall()
        fine1 = 0
        fine2 = 0
        if len(rows):
            self.ftable.delete(*self.ftable.get_children())
            for data in rows:
                data = list(data)
                fine1 = 0
                fine2 = 0
                fine = 0

                if data[13]:
                    fine1 = self.calculate_fine(data[13])
                if data[14]:
                    fine2 = self.calculate_fine(data[14])

                data[11] = fine1
                data[12] = fine2
                fine = fine1+fine2
                data[7] = fine
                self.ftable.insert("",END,values=data)
        conn.commit()
        conn.close()
    def calculate_fine(self,previous_date):
        current_date = datetime.datetime.now()
        days = current_date-previous_date
        days = days.days
        fine = 0
        if days in range(16,21):
            fine=10
        elif days in range(21,26):
            fine=20
        elif days in range(26,31):
            fine=30
        elif days>30:
            fine = 500
        return fine
    def search_member(self,id):
        conn = mysql.connector.connect(host="localhost",username="root",password="root",database="world")
        cursor = conn.cursor()
        command="SELECT * FROM member WHERE id=%s"
        cursor.execute(command,(id,))
        datas = cursor.fetchall()
        if len(datas)<1:
            messagebox.showerror("Error!", "This id is not registered!")
            return
        data = datas[0]
        self.member.set(data[0])
        self.member_id.set(data[1])
        self.firstName.set(data[2])
        self.lastName.set(data[3])
        self.address.set(data[4])
        self.postCode.set(data[5])
        self.contact.set(data[6])
        # print("Lend 1" , data[13].date)
        # print("Lend 2",datetime.datetime.now() - data[14])
        # print(type(data[13]))
        if data[10]:
            command="SELECT * FROM books WHERE id=%s"
            cursor.execute(command,(data[10],))
            book2_datas = cursor.fetchall()
            book2_data = book2_datas[0]
            self.book_id2.set(book2_data[0])
            self.title2.set(book2_data[1])
            self.author2.set(book2_data[2])
            self.type2.set(book2_data[3])
            self.language2.set(book2_data[4])
            self.dateLend2.set(data[14])
            # self.remaining2.set((datetime.datetime.now()-date(data[14])).days)
            # self.fine2 = IntVar()
        if data[9]:
            command="SELECT * FROM books WHERE id=%s"
            cursor.execute(command,(data[9],))
            book1_datas = cursor.fetchall()
            book1_data = book1_datas[0]
            self.book_id.set(book1_data[0])
            self.title.set(book1_data[1])
            self.author.set(book1_data[2])
            # self.price = IntVar()
            self.type.set(book1_data[3])
            self.language.set(book1_data[4])
            # self.amount = IntVar()
            self.dateLend1.set(data[13])
            # self.remaining1 = IntVar()
            # self.fine1 = IntVar()
        conn.close()
    def resetAll(self):
        self.member.set("")
        self.member_id.set(0)
        self.firstName.set("")
        self.lastName.set("")
        self.address.set("")
        self.postCode.set(0)
        self.contact.set(0)
        self.book1.set("")
        self.book2.set("")
        self.fine.set(0)
        self.since.set("")

        self.book_id.set(0)
        self.title.set("")
        self.author.set("")
        self.price.set(0)
        self.type.set("")
        self.language.set("")
        self.amount.set(0)
        self.dateLend1.set("")
        self.remaining1.set(0)
        self.fine1.set(0)


        self.book_id2.set(0)
        self.title2.set("")
        self.author2.set("")
        self.price2.set(0)
        self.type2.set("")
        self.language2.set("")
        self.amount2.set(0)
        self.dateLend2.set("")
        self.remaining2.set(0)
        self.fine2.set(0)
    def AddMember(self):
        if self.member_id.get() <1:
            messagebox.showerror("Error!","Please insert a valid id")
            return

        if not (isinstance(self.contact.get(),int) or isinstance(self.contact.get() , float)):
            messagebox.showerror("Error!","Contact number error")
            return

        conn = mysql.connector.connect(host="localhost",username="root",password="root",database="world")
        cursor = conn.cursor()
        command="INSERT INTO member (type,ID,firstName,lastName,address,post,contact,since) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        val = [self.member.get(), self.member_id.get(),self.firstName.get(),self.lastName.get(), self.address.get(),self.postCode.get(),self.contact.get(), datetime.datetime.now()]
        print(val)
        cursor.execute(command,val)
        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Done!","Successfully! Member Added")
#---------------------------------------delMember() -----------------------------------
    def delMember(self):
        if self.member_id.get() <1:
            messagebox.showerror("Error!","Please insert a valid id")
            return
        conn = mysql.connector.connect(host="localhost",username="root",password="root",database="world")
        cursor = conn.cursor()
        command="DELETE FROM member WHERE ID = (%s)"
        val = [self.member_id.get()]
        cursor.execute(command,val)
        conn.commit()
        conn.close()
        messagebox.showinfo("Done!","Successfully! Member Deleted")
        self.fetch_data()
#---------------- Delete Book--------------------------------------------
    def deleteBook(self):
        w = Toplevel(self.root)
        w.title("Delete Book")
        w.geometry("400x250+600+120")

        ltitle = Label(w,text="LEND BOOK", bg="#126",bd=5,fg="#aaa",font=("Helvetica",25,"bold"),padx=2,pady=4)
        ltitle.place(x=0,y=0,height=80,width=400)

        fr = Frame(w,padx=10,pady=10,bg="#114")
        fr.place(x=0,y=80,height=320,width=400)
        b_id = IntVar()
        lblID = Label(fr , text="Book ID No : " ,bg="#114",fg="white",font=("Helvetica",10,"bold"),padx=5,pady=5)
        lblID.grid(row=2,column=0,sticky=W)
        txtID = Entry(fr ,textvariable=b_id, font=("Helvetica" , 10 , "bold" ), bg="#114",fg="white" , width =18 )
        txtID.grid(row=2,column=1)

        but_Book = Button(fr,text="Book Info",bg="#117",fg="#bbb",font=("Helvetica",12,"bold"),padx=30,pady=5,bd=0,width=60 , command=lambda : self.singleBookInfo(b_id.get()))
        but_Book.place(x=15,y=100,height=30,width=120)

        but = Button(fr,text="Delete",bg="#117",fg="#bbb",font=("Helvetica",12,"bold"),padx=30,pady=5,bd=0,width=60 , command=lambda : self.delete_book(b_id.get(),w))
        but.place(x=300,y=100,height=30,width=80)

        w.mainloop()
    def delete_book(self,id,w):
        self.destroy_lend(w)
        if id <1:
            messagebox.showerror("Error!","Please insert a valid id")
            return
        conn = mysql.connector.connect(host="localhost",username="root",password="root",database="world")
        cursor = conn.cursor()
        command = "SELECT * FROM books WHERE ID = %s"
        cursor.execute(command,(id,))
        datas = cursor.fetchall()
        if len(datas)==0:
            messagebox.showerror("Error!","This book is not found!")
            return
        command = "SELECT * FROM member WHERE b1id=%s"
        cursor.execute(command,(id,))
        datas = cursor.fetchall()
        if len(datas):
            for data in datas:
                command = "UPDATE member SET b1id=null,fine1=null,lend1=null WHERE b1id=%s"
                cursor.execute(command,(data[9],))
                conn.commit()
        command = "SELECT * FROM member WHERE b2id=%s"
        cursor.execute(command,(id,))
        datas = cursor.fetchall()
        if len(datas):
            for data in datas:
                command = "UPDATE member SET b2id=null,fine2=null,lend2=null WHERE b2id=%s"
                cursor.execute(command,(data[10],))
                conn.commit()

        command="DELETE FROM books WHERE ID = %s"
        cursor.execute(command,(id,))
        conn.commit()
        conn.close()
        self.fetch_data()
        self.fetch_book_data()
        messagebox.showinfo("Done!","Successfully! Book Deleted")
    #-------------------------- delete book() -------------------------
    # def del_book(self,val):
    #     print(val)
    #     conn = mysql.connector.connect(host="localhost",username="root",password="root",database="world")
    #     cursor = conn.cursor()
    #     command="SELECT * FROM books WHERE id=%s"
    #     cursor.execute(command,(val[0],))
    #     datas = cursor.fetchall()
    #     print("Number of book found",len(datas))
    #     if(len(datas)):
    #         command="DELETE FROM books WHERE id=%s"
    #         val = [self.book_id.get()]
    #         cursor.execute(command,val)
    #         conn.close()
    #         messagebox.showinfo("Success!","The book is successfully deleted")
    #     else:
    #         conn.close()
    #         messagebox.showerror("Error!","This book is not registered")
    #---------------------------------------------- single book info -----------------------------------
    def singleBookInfo(self,id=-1):
        conn = mysql.connector.connect(host="localhost",username="root",password="root",database="world")
        cursor = conn.cursor()
        command = "SELECT * FROM books WHERE ID = %s"
        cursor.execute(command , (id , ))
        datas = cursor.fetchall()
        if len(datas) <1 :
            messagebox.showerror("Sorry!","Book not found!")
            return
        data = datas[0]

        w = Toplevel(self.root)
        w.title("Book Info")
        w.geometry("700x600+800+120")

        ltitle = Label(w,text="Book Info", bg="#126",bd=5,fg="#aaa",font=("Helvetica",25,"bold"),padx=2,pady=4)
        ltitle.place(x=0,y=0,height=100,width=700)

        fr = Frame(w,padx=10,pady=10,bg="#114")
        fr.place(x=0,y=100,height=500,width=700)

        dfLeft = LabelFrame(fr,bg="#114",text="Member information",fg="#ccc",font=("Helvetica",10,"bold"),padx=5,pady=1)
        dfLeft.place(x=0,y=0,height=480,width=680)


        lblID = Label(dfLeft , text="ID : " ,bg="#114",fg="white",font=("Helvetica",10,"bold"),padx=5,pady=5)
        lblID.grid(row=1,column=0,sticky=W)
        txtID = Label(dfLeft, text=data[0],bg="#114",fg="white",font=("Helvetica",10,"bold"),padx=5,pady=5)
        txtID.grid(row=1,column=1)


        lblTitle = Label(dfLeft , text="Title : " ,bg="#114",fg="white",font=("Helvetica",10,"bold"),padx=5,pady=5)
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle = Label(dfLeft  ,text=data[1], font=("Helvetica" , 10 , "bold" ), bg="#114",fg="white" , width =18 )
        txtTitle.grid(row=2,column=1)


        lblauthor = Label(dfLeft , text="Author : " ,bg="#114",fg="white",font=("Helvetica",10,"bold"),padx=5,pady=5)
        lblauthor.grid(row=3,column=0,sticky=W)
        txtauthor = Label(dfLeft  ,text=data[2], font=("Helvetica" , 10 , "bold" ), bg="#114",fg="white" , width =18 )
        txtauthor.grid(row=3,column=1)

        lbltype = Label(dfLeft , text="Type : " ,bg="#114",fg="white",font=("Helvetica",10,"bold"),padx=5,pady=5)
        lbltype.grid(row=4,column=0,sticky=W)
        txttype = Label(dfLeft  ,text=data[3], font=("Helvetica" , 10 , "bold" ), bg="#114",fg="white" , width =18 )
        txttype.grid(row=4,column=1)


        lblanguage = Label(dfLeft , text="Language: " ,bg="#114",fg="white",font=("Helvetica",10,"bold"),padx=5,pady=5)
        lblanguage.grid(row=5,column=0,sticky=W)
        txtlanguage = Label(dfLeft  ,text=data[4], font=("Helvetica" , 10 , "bold" ), bg="#114",fg="white" , width =18 )
        txtlanguage.grid(row=5,column=1)


        lblamount = Label(dfLeft , text="Price : " ,bg="#114",fg="white",font=("Helvetica",10,"bold"),padx=5,pady=5)
        lblamount.grid(row=6,column=0,sticky=W)
        txtamount = Label(dfLeft  ,text=data[5], font=("Helvetica" , 10 , "bold" ), bg="#114",fg="white" , width =18 )
        txtamount.grid(row=6,column=1)


        lblprice = Label(dfLeft , text="Amount : " ,bg="#114",fg="white",font=("Helvetica",10,"bold"),padx=5,pady=5)
        lblprice.grid(row=7,column=0,sticky=W)
        txtprice = Label(dfLeft  ,text=data[6], font=("Helvetica" , 10 , "bold" ), bg="#114",fg="white" , width =18 )
        txtprice.grid(row=7,column=1)


        # val = [self.iid.get(),self.title.get(),self.author.get(),self.type.get(),self.language.get(),self.amount.get(),self.price.get()]
        # print(val , "value from 1")
        but = Button(dfLeft,text="OK",bg="#117",fg="#bbb",font=("Helvetica",12,"bold"),padx=30,pady=5,bd=0,width=60,command=lambda : w.destroy())
        but.place(x=570,y=400,height=30,width=80)

        w.mainloop()
    #----------+---------------------------- single member info-----------------------------------------

    def singleMemberInfo(self,id):
        conn = mysql.connector.connect(host="localhost",username="root",password="root",database="world")
        cursor = conn.cursor()
        command = "SELECT * FROM member WHERE ID = %s"
        cursor.execute(command , (id , ))
        datas = cursor.fetchall()

        if len(datas) <1 :
            messagebox.showerror("Error!","Member not found!")
            return
        data = datas[0]


        w = Toplevel(self.root)
        w.title("Member Info")
        w.geometry("700x600+50+120")

        ltitle = Label(w,text="Member Info", bg="#126",bd=5,fg="#aaa",font=("Helvetica",25,"bold"),padx=2,pady=4)
        ltitle.place(x=0,y=0,height=100,width=700)

        fr = Frame(w,padx=10,pady=10,bg="#114")
        fr.place(x=0,y=100,height=500,width=700)
        fine1,fine2 = 0,0
        if data[13]:
            fine1 = self.calculate_fine(data[13])
        if data[14]:
            fine2 = self.calculate_fine(data[14])

        fine = fine1+fine2
        dfLeft = LabelFrame(fr,bg="#114",text="Member information",fg="#ccc",font=("Helvetica",10,"bold"),padx=5,pady=1)
        dfLeft.place(x=0,y=0,height=480,width=680)


        lblID = Label(dfLeft , text="Member Type : " ,bg="#114",fg="white",font=("Helvetica",10,"bold"),padx=5,pady=5)
        lblID.grid(row=1,column=0,sticky=W)
        txtID = Label(dfLeft, text=data[0],bg="#114",fg="white",font=("Helvetica",10,"bold"),padx=5,pady=5)
        txtID.grid(row=1,column=1)


        lblTitle = Label(dfLeft , text="ID : " ,bg="#114",fg="white",font=("Helvetica",10,"bold"),padx=5,pady=5)
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle = Label(dfLeft  ,text=data[1], font=("Helvetica" , 10 , "bold" ), bg="#114",fg="white" , width =18 )
        txtTitle.grid(row=2,column=1)


        lblauthor = Label(dfLeft , text="First Name : " ,bg="#114",fg="white",font=("Helvetica",10,"bold"),padx=5,pady=5)
        lblauthor.grid(row=3,column=0,sticky=W)
        txtauthor = Label(dfLeft  ,text=data[2], font=("Helvetica" , 10 , "bold" ), bg="#114",fg="white" , width =18 )
        txtauthor.grid(row=3,column=1)

        lbltype = Label(dfLeft , text="Last Name : " ,bg="#114",fg="white",font=("Helvetica",10,"bold"),padx=5,pady=5)
        lbltype.grid(row=4,column=0,sticky=W)
        txttype = Label(dfLeft  ,text=data[3], font=("Helvetica" , 10 , "bold" ), bg="#114",fg="white" , width =18 )
        txttype.grid(row=4,column=1)


        lblanguage = Label(dfLeft , text="Address : " ,bg="#114",fg="white",font=("Helvetica",10,"bold"),padx=5,pady=5)
        lblanguage.grid(row=5,column=0,sticky=W)
        txtlanguage = Label(dfLeft  ,text=data[4], font=("Helvetica" , 10 , "bold" ), bg="#114",fg="white" , width =18 )
        txtlanguage.grid(row=5,column=1)


        lblamount = Label(dfLeft , text="Post : " ,bg="#114",fg="white",font=("Helvetica",10,"bold"),padx=5,pady=5)
        lblamount.grid(row=6,column=0,sticky=W)
        txtamount = Label(dfLeft  ,text=data[5], font=("Helvetica" , 10 , "bold" ), bg="#114",fg="white" , width =18 )
        txtamount.grid(row=6,column=1)


        lblprice = Label(dfLeft , text="Contact : " ,bg="#114",fg="white",font=("Helvetica",10,"bold"),padx=5,pady=5)
        lblprice.grid(row=7,column=0,sticky=W)
        txtprice = Label(dfLeft  ,text=data[6], font=("Helvetica" , 10 , "bold" ), bg="#114",fg="white" , width =18 )
        txtprice.grid(row=7,column=1)

        lblprice1 = Label(dfLeft , text="Total Fine : " ,bg="#114",fg="white",font=("Helvetica",10,"bold"),padx=5,pady=5)
        lblprice1.grid(row=8,column=0,sticky=W)
        txtprice1 = Label(dfLeft  ,text=fine, font=("Helvetica" , 10 , "bold" ), bg="#114",fg="white" , width =18 )
        txtprice1.grid(row=8,column=1)

        lblprice2 = Label(dfLeft , text="Since : " ,bg="#114",fg="white",font=("Helvetica",10,"bold"),padx=5,pady=5)
        lblprice2.grid(row=9,column=0,sticky=W)
        txtprice2 = Label(dfLeft  ,text=data[8], font=("Helvetica" , 10 , "bold" ), bg="#114",fg="white" , width =18 )
        txtprice2.grid(row=9,column=1)

        lblprice3 = Label(dfLeft , text="Book 1 : " ,bg="#114",fg="white",font=("Helvetica",10,"bold"),padx=5,pady=5)
        lblprice3.grid(row=10,column=0,sticky=W)
        txtprice3= Label(dfLeft  ,text=data[9], font=("Helvetica" , 10 , "bold" ), bg="#114",fg="white" , width =18 )
        txtprice3.grid(row=10,column=1)

        lblprice4 = Label(dfLeft , text="Book 2 : " ,bg="#114",fg="white",font=("Helvetica",10,"bold"),padx=5,pady=5)
        lblprice4.grid(row=11,column=0,sticky=W)
        txtprice4 = Label(dfLeft  ,text=data[10], font=("Helvetica" , 10 , "bold" ), bg="#114",fg="white" , width =18 )
        txtprice4.grid(row=11,column=1)

        # val = [self.iid.get(),self.title.get(),self.author.get(),self.type.get(),self.language.get(),self.amount.get(),self.price.get()]
        # print(val , "value from 1")
        but = Button(dfLeft,text="OK",bg="#117",fg="#bbb",font=("Helvetica",12,"bold"),padx=30,pady=5,bd=0,width=60,command=lambda : w.destroy())
        but.place(x=570,y=390,height=30,width=80)

        w.mainloop()
    #-------------------------- lend Book() _____________________________
    def lendBook(self):
        w = Toplevel(self.root)
        w.title("Lend Book")
        w.geometry("400x250+600+120")

        ltitle = Label(w,text="LEND BOOK", bg="#126",bd=5,fg="#aaa",font=("Helvetica",25,"bold"),padx=2,pady=4)
        ltitle.place(x=0,y=0,height=80,width=400)

        fr = Frame(w,padx=10,pady=10,bg="#114")
        fr.place(x=0,y=80,height=320,width=400)

        m_id = IntVar()
        b_id = IntVar()

        lblID = Label(fr , text="Member ID No : " ,bg="#114",fg="white",font=("Helvetica",10,"bold"),padx=5,pady=5)
        lblID.grid(row=1,column=0,sticky=W)
        txtID = Entry(fr ,textvariable=m_id, font=("Helvetica" , 10 , "bold" ), bg="#114",fg="white" , width =18 )
        txtID.grid(row=1,column=1)

        lblID = Label(fr , text="Book ID No : " ,bg="#114",fg="white",font=("Helvetica",10,"bold"),padx=5,pady=5)
        lblID.grid(row=2,column=0,sticky=W)
        txtID = Entry(fr ,textvariable=b_id, font=("Helvetica" , 10 , "bold" ), bg="#114",fg="white" , width =18 )
        txtID.grid(row=2,column=1)

        but_Book = Button(fr,text="Book Info",bg="#117",fg="#bbb",font=("Helvetica",12,"bold"),padx=30,pady=5,bd=0,width=60 , command=lambda : self.singleBookInfo(b_id.get()))
        but_Book.place(x=15,y=100,height=30,width=120)

        but_member = Button(fr,text="Member Info",bg="#117",fg="#bbb",font=("Helvetica",12,"bold"),padx=30,pady=5,bd=0,width=60 , command=lambda : self.singleMemberInfo(m_id.get()))
        but_member.place(x=150,y=100,height=30,width=120)

        but = Button(fr,text="LEND",bg="#117",fg="#bbb",font=("Helvetica",12,"bold"),padx=30,pady=5,bd=0,width=60 , command=lambda : self.lend([m_id.get(),b_id.get()],w))
        but.place(x=300,y=100,height=30,width=80)

        self.fetch_data()
        w.mainloop()

    def destroy_lend(self,w):
        w.destroy()

    def lend(self,val,w):
        self.destroy_lend(w)
        if(val[0]<1 and val[1]<1):
            messagebox.showerror("Error", "Member id and Book id both are invalid!")
        elif(val[0]<1):
            messagebox.showerror("Error","Member id is invalid!")
        elif(val[1]<1):
            messagebox.showerror("Error", "Book id is invalid!")
#----------------------- db connection ----------------------------
        conn = mysql.connector.connect(host="localhost",username="root",password="root",database="world")
        cursor = conn.cursor()
        command = "SELECT * FROM member WHERE ID = %s"
        cursor.execute(command , (val[0] , ))
        datas = cursor.fetchall()

        if len(datas)<1:
            messagebox.showerror("Error!","Member not found!")
            return
        command="SELECT * FROM books WHERE ID = %s"
        cursor.execute(command,(val[1],))
        b_data = cursor.fetchall()
        if len(b_data)<1:
            messagebox.showerror("Error!","This book is not found!")
            return
        data = datas[0]
        e1 = 0
        e2 = 0
        if data[9] :
            e1=1
        if data[10]:
            e2=1

        # print(data[9])
        # print(data[10])

        # for data in cursor:
        #     if(data[9]):
        #         e1 = 1
        #         print("Book 1 is booked")
        #     else:
        #         e1 = 0
        #     if(data[10]):
        #         e2 = 1
        #         print("Book 2 is booked")
        #     else:
        #         e2 = 0
        if(e1==1 and e2==1):
            messagebox.showerror("Error","Already 2 books are lended")
            return

        command= "SELECT * FROM books WHERE id = %s"
        cursor.execute(command,(val[1],))
        amount_of_book = 0
        for data in cursor:
            amount_of_book = data[6]
            print(amount_of_book)
            if(amount_of_book<1):
                messagebox.showerror("Error","This book is not available in this moment!")
                return
            else:
                amount_of_book = amount_of_book -1
                command="UPDATE books SET amount = %s WHERE id = %s"
                cursor.execute(command,(amount_of_book , val[1] ))
                conn.commit()

        if(e1==0):

            command="UPDATE member SET b1id = %s, lend1 = %s WHERE ID = %s"
            cursor.execute(command,(val[1],datetime.datetime.now(),val[0]))
            conn.commit()
            conn.close()
            self.fetch_data()
            messagebox.showinfo("Successfull", "Book successfully lended!")
            return
        if(e2==0):

            command="UPDATE member SET b2id = %s, lend2 = %s WHERE ID = %s"
            cursor.execute(command,(val[1],datetime.datetime.now(),val[0]))

            conn.commit()
            conn.close()
            self.fetch_data()
            messagebox.showinfo("Successfull", "Book successfully lended!")
            return


    #--------------------- AddBook() -------------------------------------
    def AddBook(self):
        w = Toplevel(self.root)
        w.title("Add Book")
        w.geometry("700x400+300+120")

        ltitle = Label(w,text="ADD BOOK", bg="#126",bd=5,fg="#aaa",font=("Helvetica",25,"bold"),padx=2,pady=4)
        ltitle.place(x=0,y=0,height=100,width=700)

        fr = Frame(w,padx=10,pady=10,bg="#114")
        fr.place(x=0,y=100,height=300,width=700)

        dfLeft = LabelFrame(fr,bg="#114",text="Book information",fg="#ccc",font=("Helvetica",10,"bold"),padx=5,pady=1)
        dfLeft.place(x=0,y=0,height=270,width=680)

        self.iid = IntVar()
        lblID = Label(dfLeft , text="ID No : " ,bg="#114",fg="white",font=("Helvetica",10,"bold"),padx=5,pady=5)
        lblID.grid(row=1,column=0,sticky=W)
        txtID = Entry(dfLeft  ,textvariable=self.iid, font=("Helvetica" , 10 , "bold" ), bg="#114",fg="white" , width =18 )
        txtID.grid(row=1,column=1)

        self.title = StringVar()
        lblTitle = Label(dfLeft , text="Title : " ,bg="#114",fg="white",font=("Helvetica",10,"bold"),padx=5,pady=5)
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle = Entry(dfLeft  ,textvariable=self.title, font=("Helvetica" , 10 , "bold" ), bg="#114",fg="white" , width =18 )
        txtTitle.grid(row=2,column=1)

        self.author = StringVar()
        lblauthor = Label(dfLeft , text="Author : " ,bg="#114",fg="white",font=("Helvetica",10,"bold"),padx=5,pady=5)
        lblauthor.grid(row=3,column=0,sticky=W)
        txtauthor = Entry(dfLeft  ,textvariable=self.author, font=("Helvetica" , 10 , "bold" ), bg="#114",fg="white" , width =18 )
        txtauthor.grid(row=3,column=1)

        self.type = StringVar()
        lbltype = Label(dfLeft , text="Type :  " ,bg="#114",fg="white",font=("Helvetica",10,"bold"),padx=5,pady=5)
        lbltype.grid(row=4,column=0,sticky=W)
        comMember = ttk.Combobox(dfLeft ,textvariable=self.type,  font=("Helvetica" , 10 , "bold") , width=16, state="readonly")
        comMember["value"] = ("Science Fiction","Mathematics","Motivational","Business","Islamic","Grammar","War","Academic","History","Literature")
        comMember.current(0)
        comMember.grid(row=4,column=1)

        self.language = StringVar()
        lblanguage = Label(dfLeft , text="Language : " ,bg="#114",fg="white",font=("Helvetica",10,"bold"),padx=5,pady=5)
        lblanguage.grid(row=5,column=0,sticky=W)
        txtlanguage = Entry(dfLeft  ,textvariable=self.language, font=("Helvetica" , 10 , "bold" ), bg="#114",fg="white" , width =18 )
        txtlanguage.grid(row=5,column=1)

        self.amount = IntVar()
        lblamount = Label(dfLeft , text="Amount : " ,bg="#114",fg="white",font=("Helvetica",10,"bold"),padx=5,pady=5)
        lblamount.grid(row=6,column=0,sticky=W)
        txtamount = Entry(dfLeft  ,textvariable=self.amount, font=("Helvetica" , 10 , "bold" ), bg="#114",fg="white" , width =18 )
        txtamount.grid(row=6,column=1)

        self.price = IntVar()
        lblprice = Label(dfLeft , text="Price: " ,bg="#114",fg="white",font=("Helvetica",10,"bold"),padx=5,pady=5)
        lblprice.grid(row=7,column=0,sticky=W)
        txtprice = Entry(dfLeft  ,textvariable=self.price, font=("Helvetica" , 10 , "bold" ), bg="#114",fg="white" , width =18 )
        txtprice.grid(row=7,column=1)
        val = [self.iid.get(),self.title.get(),self.author.get(),self.type.get(),self.language.get(),self.amount.get(),self.price.get()]

        but = Button(dfLeft,text="ADD",bg="#117",fg="#bbb",font=("Helvetica",12,"bold"),padx=30,pady=5,bd=0,width=60,command=lambda : self.adBook([self.iid.get(),self.title.get(),self.author.get(),self.type.get(),self.language.get(),self.price.get(),self.amount.get()],w))
        but.place(x=570,y=200,height=30,width=80)

        w.mainloop()

    def destroy_addBoook(self,w):
        w.destroy()

    def adBook(self,val,w):
        self.destroy_addBoook(w)
        if val[0] <1:
            messagebox.showerror("Error!","Please insert a valid id")
            return
        conn = mysql.connector.connect(host="localhost",username="root",password="root",database="world")
        cursor = conn.cursor()
        command="SELECT * FROM books WHERE id=%s"
        cursor.execute(command,(val[0],))
        datas = cursor.fetchall()
        if(len(datas)>0):
            messagebox.showerror("Error!","This book is already registered.")
        else:
            command="INSERT INTO books (id,title,author,type,language,price,amount) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(command,val)
            conn.commit()
            self.fetch_book_data()
            messagebox.showinfo("Done!","Successfully! Book Added")
        conn.close()

#---------------- member info ------------------------------
    def memberInfo(self):
        w = tkinter.Tk()
        w.title("Members information")
        w.geometry("1250x500+50+50")
        conn = mysql.connector.connect(host="localhost",username="root",password="root",database="world")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM member")
        e = Label(w,width=10,text="type",borderwidth=2,relief='ridge',anchor='w',bg='yellow')
        e.grid(row=0,column=0)
        e = Label(w,width=10,text="id",borderwidth=2,relief='ridge',anchor='w',bg='yellow')
        e.grid(row=0,column=1)
        e = Label(w,width=10,text="first name",borderwidth=2,relief='ridge',anchor='w',bg='yellow')
        e.grid(row=0,column=2)
        e = Label(w,width=10,text="last name",borderwidth=2,relief='ridge',anchor='w',bg='yellow')
        e.grid(row=0,column=3)
        e = Label(w,width=10,text="address",borderwidth=2,relief='ridge',anchor='w',bg='yellow')
        e.grid(row=0,column=4)
        e = Label(w,width=10,text="post",borderwidth=2,relief='ridge',anchor='w',bg='yellow')
        e.grid(row=0,column=5)
        e = Label(w,width=10,text="contact",borderwidth=2,relief='ridge',anchor='w',bg='yellow')
        e.grid(row=0,column=6)
        e = Label(w,width=10,text="fine",borderwidth=2,relief='ridge',anchor='w',bg='yellow')
        e.grid(row=0,column=7)
        e = Label(w,width=15,text="since",borderwidth=2,relief='ridge',anchor='w',bg='yellow')
        e.grid(row=0,column=8)
        e = Label(w,width=10,text="book 1",borderwidth=2,relief='ridge',anchor='w',bg='yellow')
        e.grid(row=0,column=9)
        e = Label(w,width=10,text="book 2",borderwidth=2,relief='ridge',anchor='w',bg='yellow')
        e.grid(row=0,column=10)
        e = Label(w,width=10,text="fine 1",borderwidth=2,relief='ridge',anchor='w',bg='yellow')
        e.grid(row=0,column=11)
        e = Label(w,width=10,text="fine 2",borderwidth=2,relief='ridge',anchor='w',bg='yellow')
        e.grid(row=0,column=12)
        e = Label(w,width=15,text="lend 1",borderwidth=2,relief='ridge',anchor='w',bg='yellow')
        e.grid(row=0,column=13)
        e = Label(w,width=15,text="lend 2",borderwidth=2,relief='ridge',anchor='w',bg='yellow')
        e.grid(row=0,column=14)
        i = 1
        for member in cursor:
            for j in range(len(member)):
                if(j==8 or j==13 or j==14):
                    e = Label(w,width=15,text=member[j], borderwidth=2,relief = 'ridge',anchor='w')
                else:
                    e = Label(w,width=10,text=member[j], borderwidth=2,relief = 'ridge',anchor='w')
                e.grid(row=i,column=j)
                # e.insert(END,member[j])
            i = i+1
        w.mainloop()

    def BookInfo(self):
        w = tkinter.Tk()
        w.title("Books information")
        w.geometry("800x500+300+50")
        conn = mysql.connector.connect(host="localhost",username="root",password="root",database="world")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
        e = Label(w,width=10,text="ID",borderwidth=2,relief='ridge',anchor='w',bg='yellow')
        e.grid(row=0,column=0)
        e = Label(w,width=10,text="Title",borderwidth=2,relief='ridge',anchor='w',bg='yellow')
        e.grid(row=0,column=1)
        e = Label(w,width=10,text="Author",borderwidth=2,relief='ridge',anchor='w',bg='yellow')
        e.grid(row=0,column=2)
        e = Label(w,width=10,text="Type",borderwidth=2,relief='ridge',anchor='w',bg='yellow')
        e.grid(row=0,column=3)
        e = Label(w,width=10,text="Language",borderwidth=2,relief='ridge',anchor='w',bg='yellow')
        e.grid(row=0,column=4)
        e = Label(w,width=10,text="Price",borderwidth=2,relief='ridge',anchor='w',bg='yellow')
        e.grid(row=0,column=5)
        e = Label(w,width=10,text="Amount",borderwidth=2,relief='ridge',anchor='w',bg='yellow')
        e.grid(row=0,column=6)


        i = 1
        for member in cursor:
            for j in range(len(member)):
                e = Label(w,width=10,text=member[j], borderwidth=2,relief = 'ridge',anchor='w')
                e.grid(row=i,column=j)
                # e.insert(END,member[j])
            i = i+1
        w.mainloop()

    def ReceiveBook(self):
        w = Toplevel(self.root)
        w.title("RECEIVE Book")
        w.geometry("400x250+600+120")

        ltitle = Label(w,text="Receive BOOK", bg="#126",bd=5,fg="#aaa",font=("Helvetica",25,"bold"),padx=2,pady=4)
        ltitle.place(x=0,y=0,height=80,width=400)

        fr = Frame(w,padx=10,pady=10,bg="#114")
        fr.place(x=0,y=80,height=320,width=400)

        m_id = IntVar()
        b_id = IntVar()

        lblID = Label(fr , text="Member ID No : " ,bg="#114",fg="white",font=("Helvetica",10,"bold"),padx=5,pady=5)
        lblID.grid(row=1,column=0,sticky=W)
        txtID = Entry(fr ,textvariable=m_id, font=("Helvetica" , 10 , "bold" ), bg="#114",fg="white" , width =18 )
        txtID.grid(row=1,column=1)

        lblID = Label(fr , text="Book ID No : " ,bg="#114",fg="white",font=("Helvetica",10,"bold"),padx=5,pady=5)
        lblID.grid(row=2,column=0,sticky=W)
        txtID = Entry(fr ,textvariable=b_id, font=("Helvetica" , 10 , "bold" ), bg="#114",fg="white" , width =18 )
        txtID.grid(row=2,column=1)

        but_Book = Button(fr,text="Book Info",bg="#117",fg="#bbb",font=("Helvetica",12,"bold"),padx=30,pady=5,bd=0,width=60 , command=lambda : self.singleBookInfo(b_id.get()))
        but_Book.place(x=15,y=100,height=30,width=120)

        but_member = Button(fr,text="Member Info",bg="#117",fg="#bbb",font=("Helvetica",12,"bold"),padx=30,pady=5,bd=0,width=60 , command=lambda : self.singleMemberInfo(m_id.get()))
        but_member.place(x=150,y=100,height=30,width=120)

        but = Button(fr,text="REceive",bg="#117",fg="#bbb",font=("Helvetica",12,"bold"),padx=30,pady=5,bd=0,width=60 , command=lambda : self.receive([m_id.get(),b_id.get()],w))
        but.place(x=300,y=100,height=30,width=80)


        w.mainloop()
    def destroy_receive(self,w):
        w.destroy()
    def receive(self,val,w):
        self.destroy_receive(w)
        conn = mysql.connector.connect(host="localhost",username="root",password="root",database="world")
        cursor = conn.cursor()
        command= "SELECT * FROM member WHERE ID= %s"
        cursor.execute(command,(val[0],))
        datas = cursor.fetchall()

        if(len(datas)):
            data = datas[0]
            if(val[1] != data[9] and val[1] != data[10]):
                messagebox.showerror("Error","Book Id is not found!")
                return
            else:
                if(val[1]==data[9]):
                     # command="UPDATE books SET amount = %s WHERE id = %s"
                    command = "UPDATE member SET b1id = NULL , lend1 = NULL  WHERE ID = %s"
                    cursor.execute(command,(val[0],))
                    conn.commit()

                    command= "SELECT * FROM member WHERE ID= %s"
                    cursor.execute(command,(val[0],))
                    datas = cursor.fetchall()
                    ids = datas[0]


                    command = "SELECT amount FROM books WHERE id = %s"
                    cursor.execute(command,(val[1],))
                    data_row = cursor.fetchall()
                    amount_of_book_row = data_row[0]
                    amount_of_book = amount_of_book_row[0]
                    amount_of_book = amount_of_book + 1

                    command = "UPDATE books SET amount= %s WHERE id = %s"
                    cursor.execute(command,(amount_of_book,val[1],))
                    conn.commit()
                    conn.close()
                    self.fetch_data()
                    messagebox.showinfo("Received","Book is received successfully!")
                else:
                    command = "UPDATE member SET b2id = NULL , lend2 = NULL  WHERE ID = %s"
                    cursor.execute(command,(val[0],))
                    conn.commit()

                    command = "SELECT amount FROM books WHERE id = %s"
                    cursor.execute(command,(val[1],))
                    data_row = cursor.fetchall()
                    amount_of_book_row = data_row[0]
                    amount_of_book = amount_of_book_row[0]
                    amount_of_book = amount_of_book + 1
                    command = "UPDATE books SET amount= %s WHERE id = %s"
                    cursor.execute(command,(amount_of_book,val[1],))

                    conn.commit()
                    conn.close()
                    self.fetch_data()
                    messagebox.showinfo("Received","Book is received successfully!")
        else:
            messagebox.showerror("Error","Member not found")


if __name__ == '__main__':
     root = Tk()
     obj = Library(root)
     root.mainloop()