from tkinter import *
from tkinter import ttk
# import mysql.connector

class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")

        lbltitle = Label(self.root, text="LIBRARY MANAGEMENT SYSTEM", 
                         bg="powder blue", fg="green", bd=20, relief=RIDGE,
                         font=("times new roman", 50, "bold"), padx=2, pady=6)
        lbltitle.pack(side=TOP, fill=X)

        frame = Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=130,width=1530,height=400)

        #==================================DataFrameLeft=============================#
        DataFrameLeft=LabelFrame(frame,text="Library Membership Information", 
                         bg="powder blue", fg="green", bd=12, relief=RIDGE,
                         font=("times new roman", 12, "bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)

        lblMember=Label(DataFrameLeft,bg="powder blue",text="Member Type",font=("arial",12,"bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky="w")

        comMember=ttk.Combobox(DataFrameLeft,font=("arial",12,"bold"),width=27,state="readonly")
        comMember["value"]=("Admin Staf","Student","Lecturers")
        comMember.current(0)
        comMember.grid(row=0,column=1,sticky="w")

        lblPRN_No = Label(DataFrameLeft, bg="powder blue", text="PRN No:", 
                        font=("arial",12,"bold"), padx=2)
        lblPRN_No.grid(row=1, column=0, sticky="w")
        txtPRN_No = Entry(DataFrameLeft, font=("arial",13,"bold"), width=29)
        txtPRN_No.grid(row=1, column=1)


        lblTitle=Label(DataFrameLeft,bg="powder blue",text="ID No:",
                       font=("arial",12,"bold"),padx=2,pady=4)
        lblTitle.grid(row=2,column=0,sticky="w")
        txtTitle=Entry(DataFrameLeft,font=("arial",13,"bold"),width=29)
        txtTitle.grid(row=2,column=1)

        lblFirstName=Label(DataFrameLeft,bg="powder blue",text="First Name", 
                        font=("arial",12,"bold"),   padx=2,pady=6)
        lblFirstName.grid(row=3,column=0,sticky="w")
        txtFirstName=Entry(DataFrameLeft,font=("arial",13,"bold"),width=29)
        txtFirstName.grid(row=3,column=1)

        lblLastName=Label(DataFrameLeft,bg="powder blue",text="Last Name", 
                        font=("arial",12,"bold"), padx=2,pady=6)
        lblLastName.grid(row=4,column=0,sticky="w")
        txtLastName=Entry(DataFrameLeft,font=("arial",13,"bold"),width=29)
        txtLastName.grid(row=4,column=1)

        lblAddress1=Label(DataFrameLeft,bg="powder blue",text="Address1", 
                        font=("arial",12,"bold"),padx=2,pady=6)
        lblAddress1.grid(row=5,column=0,sticky="w")
        txtAddress1=Entry(DataFrameLeft,font=("arial",13,"bold"),width=29)
        txtAddress1.grid(row=5,column=1)

        lblAddress2=Label(DataFrameLeft,bg="powder blue",text="Address2", 
                        font=("arial",12,"bold"),padx=2,pady=6)
        lblAddress2.grid(row=6,column=0,sticky="w")
        txtAddress2=Entry(DataFrameLeft,font=("arial",13,"bold"),width=29)
        txtAddress2.grid(row=6,column=1)

        lblPostCode=Label(DataFrameLeft,bg="powder blue",text="PostCode", 
                        font=("arial",12,"bold"),padx=2,pady=4)
        lblPostCode.grid(row=7,column=0,sticky="w")
        txtPostCode=Entry(DataFrameLeft,font=("arial",13,"bold"),width=29)
        txtPostCode.grid(row=7,column=1)

        lblMobile=Label(DataFrameLeft,bg="powder blue",text="Mobile", 
                        font=("arial",12,"bold"),padx=2,pady=6)
        lblMobile.grid(row=8,column=0,sticky="w")
        txtMobile=Entry(DataFrameLeft,font=("arial",13,"bold"),width=29)
        txtMobile.grid(row=8,column=1)

        lblBookId=Label(DataFrameLeft,bg="powder blue",text="BookId:", 
                        font=("arial",12,"bold"),padx=2,pady=6)
        lblBookId.grid(row=0,column=2,sticky="w")
        txtBookId=Entry(DataFrameLeft,font=("arial",13,"bold"),width=29)
        txtBookId.grid(row=0,column=3)

        lblBookTitle=Label(DataFrameLeft,bg="powder blue",text="BookTitle:", 
                        font=("arial",12,"bold"),padx=2,pady=6)
        lblBookTitle.grid(row=1,column=2,sticky="w")
        txtBookTitle=Entry(DataFrameLeft,font=("arial",13,"bold"),width=29)
        txtBookTitle.grid(row=1,column=3)

        lblAuthor=Label(DataFrameLeft,bg="powder blue",text="Author Name:", 
                        font=("arial",12,"bold"),padx=2,pady=6)
        lblAuthor.grid(row=2,column=2,sticky="w")
        txtAuthor=Entry(DataFrameLeft,font=("arial",13,"bold"),width=29)
        txtAuthor.grid(row=2,column=3)

        lblDateBorrowed=Label(DataFrameLeft,bg="powder blue",text="DateBorrowed:", 
                        font=("arial",12,"bold"),padx=2,pady=6)
        lblDateBorrowed.grid(row=3,column=2,sticky="w")
        txtDateBorrowed=Entry(DataFrameLeft,font=("arial",13,"bold"),width=29)
        txtDateBorrowed.grid(row=3,column=3)

        lblDateDue=Label(DataFrameLeft,bg="powder blue",text="DateDue:", 
                        font=("arial",12,"bold"),padx=2,pady=6)
        lblDateDue.grid(row=4,column=2,sticky="w")
        txtDateDue=Entry(DataFrameLeft,font=("arial",13,"bold"),width=29)
        txtDateDue.grid(row=4,column=3)

        lblDaysOnBook=Label(DataFrameLeft,bg="powder blue",text="DaysOnBook:", 
                        font=("arial",12,"bold"),padx=2,pady=6)
        lblDaysOnBook.grid(row=5,column=2,sticky="w")
        txtDaysOnBook=Entry(DataFrameLeft,font=("arial",13,"bold"),width=29)
        txtDaysOnBook.grid(row=5,column=3)

        lblLateReturnFine=Label(DataFrameLeft,bg="powder blue",text="Late Return Fine:", 
                        font=("arial",12,"bold"),padx=2,pady=6)
        lblLateReturnFine.grid(row=6,column=2,sticky="w")
        txtLateReturnFine=Entry(DataFrameLeft,font=("arial",13,"bold"),width=29)
        txtLateReturnFine.grid(row=6,column=3)

        lblDateOverDate=Label(DataFrameLeft,bg="powder blue",text="Date Over Due:", 
                        font=("arial",12,"bold"),padx=2,pady=6)
        lblDateOverDate.grid(row=7,column=2,sticky="w")
        txtDateOverDate=Entry(DataFrameLeft,font=("arial",13,"bold"),width=29)
        txtDateOverDate.grid(row=7,column=3)

        lblActualPrice=Label(DataFrameLeft,bg="powder blue",text="Actual Price:", 
                        font=("arial",12,"bold"),padx=2,pady=6)
        lblActualPrice.grid(row=8,column=2,sticky="w")
        txtActualPrice=Entry(DataFrameLeft,font=("arial",13,"bold"),width=29)
        txtActualPrice.grid(row=8,column=3)

        #==================================DataFrameRight==============================#

        DataFrameRight=LabelFrame(frame,text="Book Details", 
                         bg="powder blue", fg="green", bd=12, relief=RIDGE,
                         font=("times new roman", 12, "bold"))
        DataFrameRight.place(x=910,y=5,width=540,height=350)

        self.txtBox=Text(DataFrameRight,font=("arial",12,"bold"),width=32,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)

        # List of books 50 books name
        listBooks = ["Mockingbird",
                    "1984",
                    "Pride & Prejudice",
                    "Gatsby",
                    "Catcher in the Rye",
                    "The Hobbit",
                    "Animal Farm",
                    "Lord of the Flies",
                    "Jane Eyre",
                    "Wuthering Heights",
                    "Algo Basics",
                    "Physics Essentials",
                    "Calculus",
                    "Conceptual Chemistry",
                    "Microeconomics",
                    "OS Concepts",
                    "Engg Mathematics",
                    "DSA in C",
                    "AI Handbook",
                    "Digital Logic",
                    "Brief History of Time",
                    "Cosmos",
                    "Selfish Gene",
                    "The Gene",
                    "The Innovators",
                    "Code Book",
                    "Elegant Universe",
                    "Astrophysics Basics",
                    "Human Body Guide",
                    "Sapiens",
                    "Atomic Habits",
                    "7 Habits",
                    "Think & Grow Rich",
                    "Deep Work",
                    "Power of Now",
                    "Mindset",
                    "Grit",
                    "Influence People",
                    "Rich Dad Poor Dad",
                    "Subtle Art",
                    "Guns Germs Steel",
                    "People's History",
                    "India After Gandhi",
                    "Anne Frank Diary",
                    "Freedom Walk",
                    "Art of War",
                    "The Prince",
                    "Why Nations Fail",
                    "Communist Manifesto",
                    "Freedom at Midnight"]
        # sort the list of books
        listBooks.sort()
        
        listBox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=20,height=16)
        listBox.grid(row=0,column=0,padx=4)
        # Scrollbar for Listbox
        listScrollBar=Scrollbar(DataFrameRight)
        listScrollBar.grid(row=0,column=1,sticky="ns")
        listScrollBar.config(command=listBox.yview)

        for book in listBooks:
            listBox.insert(END, book)

        #==================================Button Frame==============================#
        FrameButton = Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        FrameButton.place(x=0,y=530,width=1530,height=70)

        btnAddData = Button(FrameButton, text="Add Data", font=("arial", 12, "bold"), width=23, bg="Blue", fg="white", padx=2, pady=6)
        btnAddData.grid(row=0, column=0)
        btnShowData = Button(FrameButton, text="Show Data", font=("arial", 12, "bold"), width=23, bg="Blue", fg="white", padx=2, pady=6)
        btnShowData.grid(row=0, column=1)
        btnUpdateData = Button(FrameButton, text="Update Data", font=("arial", 12, "bold"), width=23, bg="Blue", fg="white", padx=2, pady=6)
        btnUpdateData.grid(row=0, column=2)
        btnDeleteData = Button(FrameButton, text="Delete Data", font=("arial", 12, "bold"), width=23, bg="Blue", fg="white", padx=2, pady=6)
        btnDeleteData.grid(row=0, column=3)
        btnResetData = Button(FrameButton, text="Reset Data", font=("arial", 12, "bold"), width=23, bg="Blue", fg="white", padx=2, pady=6)
        btnResetData.grid(row=0, column=4)
        btnExit = Button(FrameButton, text="Exit", font=("arial", 12, "bold"), width=23, bg="Blue", fg="white", padx=2, pady=6)
        btnExit.grid(row=0, column=5)


        #==================================Information Frame==========================#
        FrameDetails = Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        FrameDetails.place(x=0,y=600,width=1530,height=195)


        Table_Frame = Frame(FrameDetails, bd=6, relief=RIDGE, bg="powder blue")
        Table_Frame.place(x=0, y=2, width=1460, height= 190)

        xscroll=ttk.Scrollbar(Table_Frame, orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_Frame, orient=VERTICAL)
        self.library_table = ttk.Treeview(Table_Frame, columns=("member_type", "prn_no", "id_no", "first_name", "last_name", 
                                                        "address1", "address2", "postcode", "mobile", "book_id", 
                                                        "book_title", "author_name", "date_borrowed", "date_due", 
                                                        "days_on_book", "late_return_fine", "date_over_due", 
                                                        "actual_price"),xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("member_type", text="Member Type")
        self.library_table.heading("prn_no", text="PRN No")
        self.library_table.heading("id_no", text="ID No")
        self.library_table.heading("first_name", text="First Name")
        self.library_table.heading("last_name", text="Last Name")
        self.library_table.heading("address1", text="Address 1")
        self.library_table.heading("address2", text="Address 2")
        self.library_table.heading("postcode", text="Postcode")
        self.library_table.heading("mobile", text="Mobile")
        self.library_table.heading("book_id", text="Book ID")
        self.library_table.heading("book_title", text="Book Title")
        self.library_table.heading("author_name", text="Author Name")
        self.library_table.heading("date_borrowed", text="Date Borrowed")
        self.library_table.heading("date_due", text="Date Due")
        self.library_table.heading("days_on_book", text="Days on Book")
        self.library_table.heading("late_return_fine", text="Late Return Fine")
        self.library_table.heading("date_over_due", text="Date Over Due")
        self.library_table.heading("actual_price", text="Actual Price") 

        self.library_table["show"] = "headings"
        self.library_table.pack(fill=BOTH, expand=1)

        self.library_table.column("member_type", width=100)
        self.library_table.column("prn_no", width=100)
        self.library_table.column("id_no", width=100)
        self.library_table.column("first_name", width=100)
        self.library_table.column("last_name", width=100)
        self.library_table.column("address1", width=100)
        self.library_table.column("address2", width=100)
        self.library_table.column("postcode", width=100)
        self.library_table.column("mobile", width=100)
        self.library_table.column("book_id", width=100)
        self.library_table.column("book_title", width=100)
        self.library_table.column("author_name", width=100)
        self.library_table.column("date_borrowed", width=100)
        self.library_table.column("date_due", width=100)
        self.library_table.column("days_on_book", width=100)
        self.library_table.column("late_return_fine", width=100)
        self.library_table.column("date_over_due", width=100)
        self.library_table.column("actual_price", width=100)



if __name__ == "__main__":
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()
