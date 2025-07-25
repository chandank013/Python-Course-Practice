from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import tkinter
import datetime

class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")


        #=================================Variable=====================================#
        self.member_type = StringVar()
        self.prn_no = StringVar()
        self.id_no = StringVar()
        self.first_name = StringVar()
        self.last_name = StringVar()
        self.address1 = StringVar()
        self.address2 = StringVar()
        self.postcode = StringVar()
        self.mobile_var = StringVar()
        self.book_id = StringVar()
        self.book_title = StringVar()
        self.author_name = StringVar()
        self.date_borrowed = StringVar()
        self.date_due = StringVar()
        self.days_on_book = StringVar()
        self.late_return_fine = StringVar()
        self.date_over_due = StringVar()
        self.finalprice = StringVar()



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

        comMember=ttk.Combobox(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.member_type,width=27,state="readonly")
        comMember["value"]=("Admin Staff","Student","Lecturers")
        comMember.current(0)
        comMember.grid(row=0,column=1,sticky="w")

        lblPRN_No = Label(DataFrameLeft, bg="powder blue", text="PRN No:", 
                        font=("arial",12,"bold"), padx=2)
        lblPRN_No.grid(row=1, column=0, sticky="w")
        txtPRN_No = Entry(DataFrameLeft, textvariable=self.prn_no, font=("arial",13,"bold"), width=29)
        txtPRN_No.grid(row=1, column=1)


        lblTitle=Label(DataFrameLeft,bg="powder blue",text="ID No:",
                       font=("arial",12,"bold"),padx=2,pady=4)
        lblTitle.grid(row=2,column=0,sticky="w")
        txtTitle=Entry(DataFrameLeft,textvariable=self.id_no,font=("arial",13,"bold"),width=29)
        txtTitle.grid(row=2,column=1)

        lblFirstName=Label(DataFrameLeft,bg="powder blue",text="First Name", 
                        font=("arial",12,"bold"),   padx=2,pady=6)
        lblFirstName.grid(row=3,column=0,sticky="w")
        txtFirstName=Entry(DataFrameLeft,textvariable=self.first_name,font=("arial",13,"bold"),width=29)
        txtFirstName.grid(row=3,column=1)

        lblLastName=Label(DataFrameLeft,bg="powder blue",text="Last Name", 
                        font=("arial",12,"bold"), padx=2,pady=6)
        lblLastName.grid(row=4,column=0,sticky="w")
        txtLastName=Entry(DataFrameLeft,textvariable=self.last_name,font=("arial",13,"bold"),width=29)
        txtLastName.grid(row=4,column=1)

        lblAddress1=Label(DataFrameLeft,bg="powder blue",text="Address1", 
                        font=("arial",12,"bold"),padx=2,pady=6)
        lblAddress1.grid(row=5,column=0,sticky="w")
        txtAddress1=Entry(DataFrameLeft,textvariable=self.address1,font=("arial",13,"bold"),width=29)
        txtAddress1.grid(row=5,column=1)

        lblAddress2=Label(DataFrameLeft,bg="powder blue",text="Address2", 
                        font=("arial",12,"bold"),padx=2,pady=6)
        lblAddress2.grid(row=6,column=0,sticky="w")
        txtAddress2=Entry(DataFrameLeft,textvariable=self.address2,font=("arial",13,"bold"),width=29)
        txtAddress2.grid(row=6,column=1)

        lblPostCode=Label(DataFrameLeft,bg="powder blue",text="PostCode", 
                        font=("arial",12,"bold"),padx=2,pady=4)
        lblPostCode.grid(row=7,column=0,sticky="w")
        txtPostCode=Entry(DataFrameLeft,textvariable=self.postcode,font=("arial",13,"bold"),width=29)
        txtPostCode.grid(row=7,column=1)

        lblMobile=Label(DataFrameLeft,bg="powder blue",text="Mobile", 
                        font=("arial",12,"bold"),padx=2,pady=6)
        lblMobile.grid(row=8,column=0,sticky="w")
        txtMobile=Entry(DataFrameLeft,textvariable=self.mobile_var,font=("arial",13,"bold"),width=29)
        txtMobile.grid(row=8,column=1)

        lblBookId=Label(DataFrameLeft,bg="powder blue",text="BookId:", 
                        font=("arial",12,"bold"),padx=2,pady=6)
        lblBookId.grid(row=0,column=2,sticky="w")
        txtBookId=Entry(DataFrameLeft,textvariable=self.book_id,font=("arial",13,"bold"),width=29)
        txtBookId.grid(row=0,column=3)

        lblBookTitle=Label(DataFrameLeft,bg="powder blue",text="BookTitle:", 
                        font=("arial",12,"bold"),padx=2,pady=6)
        lblBookTitle.grid(row=1,column=2,sticky="w")
        txtBookTitle=Entry(DataFrameLeft,textvariable=self.book_title,font=("arial",13,"bold"),width=29)
        txtBookTitle.grid(row=1,column=3)

        lblAuthor=Label(DataFrameLeft,bg="powder blue",text="Author Name:", 
                        font=("arial",12,"bold"),padx=2,pady=6)
        lblAuthor.grid(row=2,column=2,sticky="w")
        txtAuthor=Entry(DataFrameLeft,textvariable=self.author_name,font=("arial",13,"bold"),width=29)
        txtAuthor.grid(row=2,column=3)

        lblDateBorrowed=Label(DataFrameLeft,bg="powder blue",text="DateBorrowed:", 
                        font=("arial",12,"bold"),padx=2,pady=6)
        lblDateBorrowed.grid(row=3,column=2,sticky="w")
        txtDateBorrowed=Entry(DataFrameLeft,textvariable=self.date_borrowed,font=("arial",13,"bold"),width=29)
        txtDateBorrowed.grid(row=3,column=3)

        lblDateDue=Label(DataFrameLeft,bg="powder blue",text="DateDue:", 
                        font=("arial",12,"bold"),padx=2,pady=6)
        lblDateDue.grid(row=4,column=2,sticky="w")
        txtDateDue=Entry(DataFrameLeft,textvariable=self.date_due,font=("arial",13,"bold"),width=29)
        txtDateDue.grid(row=4,column=3)

        lblDaysOnBook=Label(DataFrameLeft,bg="powder blue",text="DaysOnBook:", 
                        font=("arial",12,"bold"),padx=2,pady=6)
        lblDaysOnBook.grid(row=5,column=2,sticky="w")
        txtDaysOnBook=Entry(DataFrameLeft,textvariable=self.days_on_book,font=("arial",13,"bold"),width=29)
        txtDaysOnBook.grid(row=5,column=3)

        lblLateReturnFine=Label(DataFrameLeft,bg="powder blue",text="Late Return Fine:", 
                        font=("arial",12,"bold"),padx=2,pady=6)
        lblLateReturnFine.grid(row=6,column=2,sticky="w")
        txtLateReturnFine=Entry(DataFrameLeft,textvariable=self.late_return_fine,font=("arial",13,"bold"),width=29)
        txtLateReturnFine.grid(row=6,column=3)

        lblDateOverDate=Label(DataFrameLeft,bg="powder blue",text="Date Over Due:", 
                        font=("arial",12,"bold"),padx=2,pady=6)
        lblDateOverDate.grid(row=7,column=2,sticky="w")
        txtDateOverDate=Entry(DataFrameLeft,textvariable=self.date_over_due,font=("arial",13,"bold"),width=29)
        txtDateOverDate.grid(row=7,column=3)

        lblActualPrice=Label(DataFrameLeft,bg="powder blue",text="Actual Price:", 
                        font=("arial",12,"bold"),padx=2,pady=6)
        lblActualPrice.grid(row=8,column=2,sticky="w")
        txtActualPrice=Entry(DataFrameLeft,textvariable=self.finalprice,font=("arial",13,"bold"),width=29)
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
                    "Introduction to Machine Learning",
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
                    "The Art of Computer Programming",
                    ]
        # sort the list of books
        listBooks.sort()

        def SelectBook(event=""):
            # Get the selected book from the listbox
            value=str(listBox.get(listBox.curselection()))
            x=value
            if(x=="Mockingbird"):
                self.book_id.set("B001")
                self.book_title.set("To Kill a Mockingbird")
                self.author_name.set("Harper Lee")

                d1= datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.date_borrowed.set(d1.strftime("%d/%m/%Y"))
                self.date_due.set(d3.strftime("%d/%m/%Y"))
                self.days_on_book.set("15")
                self.late_return_fine.set("Rs.50")
                self.date_over_due.set("No")
                self.finalprice.set("Rs.788")
            elif (x == "Introduction to Machine Learning"):
                self.book_id.set("B002")
                self.book_title.set("Introduction to Machine Learning")
                self.author_name.set("Ethem Alpaydin")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.date_borrowed.set(d1.strftime("%d/%m/%Y"))
                self.date_due.set(d3.strftime("%d/%m/%Y"))
                self.days_on_book.set("15")
                self.late_return_fine.set("Rs.50")
                self.date_over_due.set("No")
                self.finalprice.set("Rs.600")

            elif(x=="Pride & Prejudice"):
                self.book_id.set("B003")
                self.book_title.set("Pride & Prejudice")
                self.author_name.set("Jane Austen")
                d1= datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.date_borrowed.set(d1.strftime("%d/%m/%Y"))
                self.date_due.set(d3.strftime("%d/%m/%Y"))
                self.days_on_book.set("15")
                self.late_return_fine.set("Rs.50")
                self.date_over_due.set("No")
                self.finalprice.set("Rs.500")
            elif(x=="Gatsby"):
                self.book_id.set("B004")
                self.book_title.set("The Great Gatsby")
                self.author_name.set("F. Scott Fitzgerald")
                d1= datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.date_borrowed.set(d1.strftime("%d/%m/%Y"))
                self.date_due.set(d3.strftime("%d/%m/%Y"))
                self.days_on_book.set("15")
                self.late_return_fine.set("Rs.50")
                self.date_over_due.set("No")
                self.finalprice.set("Rs.700")
            elif(x=="Catcher in the Rye"):
                self.book_id.set("B005")
                self.book_title.set("The Catcher in the Rye")
                self.author_name.set("J.D. Salinger")
                d1= datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.date_borrowed.set(d1.strftime("%d/%m/%Y"))
                self.date_due.set(d3.strftime("%d/%m/%Y"))
                self.days_on_book.set("15")
                self.late_return_fine.set("Rs.50")
                self.date_over_due.set("No")
                self.finalprice.set("Rs.550")
            elif(x=="The Hobbit"):
                self.book_id.set("B006")
                self.book_title.set("The Hobbit")
                self.author_name.set("J.R.R. Tolkien")
                d1= datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.date_borrowed.set(d1.strftime("%d/%m/%Y"))
                self.date_due.set(d3.strftime("%d/%m/%Y"))
                self.days_on_book.set("15")
                self.late_return_fine.set("Rs.50")
                self.date_over_due.set("No")
                self.finalprice.set("Rs.800")
            elif(x=="Animal Farm"):
                self.book_id.set("B007")
                self.book_title.set("Animal Farm")
                self.author_name.set("George Orwell")
                d1= datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.date_borrowed.set(d1.strftime("%d/%m/%Y"))
                self.date_due.set(d3.strftime("%d/%m/%Y"))
                self.days_on_book.set("15")
                self.late_return_fine.set("Rs.50")
                self.date_over_due.set("No")
                self.finalprice.set("Rs.400")
            elif(x=="Lord of the Flies"):
                self.book_id.set("B008")
                self.book_title.set("Lord of the Flies")
                self.author_name.set("William Golding")
                d1= datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.date_borrowed.set(d1.strftime("%d/%m/%Y"))
                self.date_due.set(d3.strftime("%d/%m/%Y"))
                self.days_on_book.set("15")
                self.late_return_fine.set("Rs.50")
                self.date_over_due.set("No")
                self.finalprice.set("Rs.450")
            elif(x=="Jane Eyre"):
                self.book_id.set("B009")
                self.book_title.set("Jane Eyre")
                self.author_name.set("Charlotte Brontë")
                d1= datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.date_borrowed.set(d1.strftime("%d/%m/%Y"))
                self.date_due.set(d3.strftime("%d/%m/%Y"))
                self.days_on_book.set("15")
                self.late_return_fine.set("Rs.50")
                self.date_over_due.set("No")
                self.finalprice.set("Rs.600")
            elif(x=="Wuthering Heights"):
                self.book_id.set("B010")
                self.book_title.set("Wuthering Heights")
                self.author_name.set("Emily Brontë")
                d1= datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.date_borrowed.set(d1.strftime("%d/%m/%Y"))
                self.date_due.set(d3.strftime("%d/%m/%Y"))
                self.days_on_book.set("15")
                self.late_return_fine.set("Rs.50")
                self.date_over_due.set("No")
                self.finalprice.set("Rs.650")
            elif(x=="Algo Basics"):
                self.book_id.set("B011")
                self.book_title.set("Algorithm Basics")
                self.author_name.set("John Doe")
                d1= datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.date_borrowed.set(d1.strftime("%d/%m/%Y"))
                self.date_due.set(d3.strftime("%d/%m/%Y"))
                self.days_on_book.set("15")
                self.late_return_fine.set("Rs.50")
                self.date_over_due.set("No")
                self.finalprice.set("Rs.500")
            elif(x=="Physics Essentials"):
                self.book_id.set("B012")
                self.book_title.set("Physics Essentials")
                self.author_name.set("Jane Smith")
                d1= datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.date_borrowed.set(d1.strftime("%d/%m/%Y"))
                self.date_due.set(d3.strftime("%d/%m/%Y"))
                self.days_on_book.set("15")
                self.late_return_fine.set("Rs.50")
                self.date_over_due.set("No")
                self.finalprice.set("Rs.600")
            elif(x=="Calculus"):
                self.book_id.set("B013")
                self.book_title.set("Calculus")
                self.author_name.set("Albert Einstein")
                d1= datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.date_borrowed.set(d1.strftime("%d/%m/%Y"))
                self.date_due.set(d3.strftime("%d/%m/%Y"))
                self.days_on_book.set("15")
                self.late_return_fine.set("Rs.50")
                self.date_over_due.set("No")
                self.finalprice.set("Rs.700")
            elif(x=="Conceptual Chemistry"):
                self.book_id.set("B014")
                self.book_title.set("Conceptual Chemistry")
                self.author_name.set("Marie Curie")
                d1= datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.date_borrowed.set(d1.strftime("%d/%m/%Y"))
                self.date_due.set(d3.strftime("%d/%m/%Y"))
                self.days_on_book.set("15")
                self.late_return_fine.set("Rs.50")
                self.date_over_due.set("No")
                self.finalprice.set("Rs.550")
            elif(x=="Microeconomics"):
                self.book_id.set("B015")
                self.book_title.set("Microeconomics")
                self.author_name.set("Adam Smith")
                d1= datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.date_borrowed.set(d1.strftime("%d/%m/%Y"))
                self.date_due.set(d3.strftime("%d/%m/%Y"))
                self.days_on_book.set("15")
                self.late_return_fine.set("Rs.50")
                self.date_over_due.set("No")
                self.finalprice.set("Rs.500")
            elif(x=="OS Concepts"):
                self.book_id.set("B016")
                self.book_title.set("Operating System Concepts")
                self.author_name.set("Andrew S. Tanenbaum")
                d1= datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.date_borrowed.set(d1.strftime("%d/%m/%Y"))
                self.date_due.set(d3.strftime("%d/%m/%Y"))
                self.days_on_book.set("15")
                self.late_return_fine.set("Rs.50")
                self.date_over_due.set("No")
                self.finalprice.set("Rs.800")
            elif(x=="Engg Mathematics"):
                self.book_id.set("B017")
                self.book_title.set("Engineering Mathematics")
                self.author_name.set("B.S. Grewal")
                d1= datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.date_borrowed.set(d1.strftime("%d/%m/%Y"))
                self.date_due.set(d3.strftime("%d/%m/%Y"))
                self.days_on_book.set("15")
                self.late_return_fine.set("Rs.50")
                self.date_over_due.set("No")
                self.finalprice.set("Rs.600")
            elif(x=="DSA in C"):
                self.book_id.set("B018")
                self.book_title.set("Data Structures and Algorithms in C")
                self.author_name.set("Mark Allen Weiss")
                d1= datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.date_borrowed.set(d1.strftime("%d/%m/%Y"))
                self.date_due.set(d3.strftime("%d/%m/%Y"))
                self.days_on_book.set("15")
                self.late_return_fine.set("Rs.50")
                self.date_over_due.set("No")
                self.finalprice.set("Rs.700")
            elif(x=="AI Handbook"):
                self.book_id.set("B019")
                self.book_title.set("Artificial Intelligence Handbook")
                self.author_name.set("Stuart Russell")
                d1= datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.date_borrowed.set(d1.strftime("%d/%m/%Y"))
                self.date_due.set(d3.strftime("%d/%m/%Y"))
                self.days_on_book.set("15")
                self.late_return_fine.set("Rs.50")
                self.date_over_due.set("No")
                self.finalprice.set("Rs.900")
            elif(x=="Digital Logic"):
                self.book_id.set("B020")
                self.book_title.set("Digital Logic Design")
                self.author_name.set("M. Morris Mano")
                d1= datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.date_borrowed.set(d1.strftime("%d/%m/%Y"))
                self.date_due.set(d3.strftime("%d/%m/%Y"))
                self.days_on_book.set("15")
                self.late_return_fine.set("Rs.50")
                self.date_over_due.set("No")
                self.finalprice.set("Rs.650")
            elif(x=="Brief History of Time"):
                self.book_id.set("B021")
                self.book_title.set("A Brief History of Time")
                self.author_name.set("Stephen Hawking")
                d1= datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.date_borrowed.set(d1.strftime("%d/%m/%Y"))
                self.date_due.set(d3.strftime("%d/%m/%Y"))
                self.days_on_book.set("15")
                self.late_return_fine.set("Rs.50")
                self.date_over_due.set("No")
                self.finalprice.set("Rs.750")
            elif(x=="Cosmos"):
                self.book_id.set("B022")
                self.book_title.set("Cosmos")
                self.author_name.set("Carl Sagan")
                d1= datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.date_borrowed.set(d1.strftime("%d/%m/%Y"))
                self.date_due.set(d3.strftime("%d/%m/%Y"))
                self.days_on_book.set("15")
                self.late_return_fine.set("Rs.50")
                self.date_over_due.set("No")
                self.finalprice.set("Rs.800")
            elif(x=="Selfish Gene"):
                self.book_id.set("B023")
                self.book_title.set("The Selfish Gene")
                self.author_name.set("Richard Dawkins")
                d1= datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.date_borrowed.set(d1.strftime("%d/%m/%Y"))
                self.date_due.set(d3.strftime("%d/%m/%Y"))
                self.days_on_book.set("15")
                self.late_return_fine.set("Rs.50")
                self.date_over_due.set("No")
                self.finalprice.set("Rs.600")
            elif(x=="The Gene"):
                self.book_id.set("B024")
                self.book_title.set("The Gene: An Intimate History")
                self.author_name.set("Siddhartha Mukherjee")
                d1= datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.date_borrowed.set(d1.strftime("%d/%m/%Y"))
                self.date_due.set(d3.strftime("%d/%m/%Y"))
                self.days_on_book.set("15")
                self.late_return_fine.set("Rs.50")
                self.date_over_due.set("No")
                self.finalprice.set("Rs.700")
            elif(x=="The Innovators"):
                self.book_id.set("B025")
                self.book_title.set("The Innovators: How a Group of Hackers, Geniuses, and Geeks Created the Digital Revolution")
                self.author_name.set("Walter Isaacson")
                d1= datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.date_borrowed.set(d1.strftime("%d/%m/%Y"))
                self.date_due.set(d3.strftime("%d/%m/%Y"))
                self.days_on_book.set("15")
                self.late_return_fine.set("Rs.50")
                self.date_over_due.set("No")
                self.finalprice.set("Rs.800")
            elif(x=="Code Book"):
                self.book_id.set("B026")
                self.book_title.set("The Code Book: The Science of Secrecy from Ancient Egypt to Quantum Cryptography")
                self.author_name.set("Simon Singh")
                d1= datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.date_borrowed.set(d1.strftime("%d/%m/%Y"))
                self.date_due.set(d3.strftime("%d/%m/%Y"))
                self.days_on_book.set("15")
                self.late_return_fine.set("Rs.50")
                self.date_over_due.set("No")
                self.finalprice.set("Rs.650")
            elif(x=="The Art of Computer Programming"):
                self.book_id.set("B027")
                self.book_title.set("The Art of Computer Programming")
                self.author_name.set("Donald E. Knuth")
                d1= datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.date_borrowed.set(d1.strftime("%d/%m/%Y"))
                self.date_due.set(d3.strftime("%d/%m/%Y"))
                self.days_on_book.set("15")
                self.late_return_fine.set("Rs.50")
                self.date_over_due.set("No")
                self.finalprice.set("Rs.900")



        listBox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=20,height=16)
        listBox.bind("<<ListboxSelect>>", SelectBook)
        listBox.grid(row=0,column=0,padx=4)
        # Scrollbar for Listbox
        listScrollBar=Scrollbar(DataFrameRight)
        listScrollBar.grid(row=0,column=1,sticky="ns")
        listScrollBar.config(command=listBox.yview)

        for book in listBooks:
            listBox.insert(END, book)

        #==================================ButtonFrame==============================#
        FrameButton = Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        FrameButton.place(x=0,y=530,width=1530,height=70)

        btnAddData = Button(FrameButton, text="Add Data", font=("arial", 12, "bold"), width=23, bg="Blue", fg="white", padx=2, pady=6, command=self.add_data)
        btnAddData.grid(row=0, column=0)

        btnShowData = Button(FrameButton, text="Show Data", font=("arial", 12, "bold"), width=23, bg="Blue", fg="white", padx=2, pady=6, command=self.show_data)
        btnShowData.grid(row=0, column=1)

        btnUpdateData = Button(FrameButton, text="Update Data", font=("arial", 12, "bold"), width=23, bg="Blue", fg="white", padx=2, pady=6, command=self.update_data)
        btnUpdateData.grid(row=0, column=2)

        btnDeleteData = Button(FrameButton, text="Delete Data", font=("arial", 12, "bold"), width=23, bg="Blue", fg="white", padx=2, pady=6, command=self.delete_data)
        btnDeleteData.grid(row=0, column=3)

        btnResetData = Button(FrameButton, text="Reset Data", font=("arial", 12, "bold"), width=23, bg="Blue", fg="white", padx=2, pady=6, command=self.reset_data)
        btnResetData.grid(row=0, column=4)

        btnExit = Button(FrameButton, text="Exit", font=("arial", 12, "bold"), width=23, bg="Blue", fg="white", padx=2, pady=6, command=self.exit_program)
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
        self.library_table.heading("postcode", text="PostId")
        self.library_table.heading("mobile", text="Mobile")
        self.library_table.heading("book_id", text="Book ID")
        self.library_table.heading("book_title", text="Book Title")
        self.library_table.heading("author_name", text="Author Name")
        self.library_table.heading("date_borrowed", text="Date Of Borrowed")
        self.library_table.heading("date_due", text="Date Of Due")
        self.library_table.heading("days_on_book", text="Days On Book")
        self.library_table.heading("late_return_fine", text="Late Return Fine")
        self.library_table.heading("date_over_due", text="Date Over Due")
        self.library_table.heading("actual_price", text="Final Price")

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

        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>", self.get_curser)

    def add_data(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="MySql@013",
                database="college"
            )
            my_cursor = conn.cursor()
            my_cursor.execute("INSERT INTO library VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                        (self.member_type.get(),
                         self.prn_no.get(),
                         self.id_no.get(),
                         self.first_name.get(),
                         self.last_name.get(),
                         self.address1.get(),
                         self.address2.get(),
                         self.postcode.get(),
                         self.mobile_var.get(),
                         self.book_id.get(),
                         self.book_title.get(),
                         self.author_name.get(),
                         self.date_borrowed.get(),
                         self.date_due.get(),
                         self.days_on_book.get(),
                         self.late_return_fine.get(),
                         self.date_over_due.get(),
                         self.finalprice.get()))
            conn.commit()
            self.fetch_data()
            messagebox.showinfo("Success", "Data has been added successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong:\n{str(e)}")
        finally:
            conn.close()
    
    def fetch_data(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",

                user="root",
                password="MySql@013",
                database="college"
            )
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM library")
            rows = my_cursor.fetchall()
            if len(rows) != 0:
                self.library_table.delete(*self.library_table.get_children())
                for row in rows:
                    self.library_table.insert("", END, values=row)
                conn.commit()
            conn.close()
        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong:\n{str(e)}")

    def get_curser(self, event=""):
        curser_row = self.library_table.focus()
        content = self.library_table.item(curser_row)
        row = content['values']
        
        self.member_type.set(row[0])
        self.prn_no.set(row[1])
        self.id_no.set(row[2])
        self.first_name.set(row[3])
        self.last_name.set(row[4])
        self.address1.set(row[5])
        self.address2.set(row[6])
        self.postcode.set(row[7])
        self.mobile_var.set(row[8])
        self.book_id.set(row[9])
        self.book_title.set(row[10])
        self.author_name.set(row[11])
        self.date_borrowed.set(row[12])
        self.date_due.set(row[13])
        self.days_on_book.set(row[14])
        self.late_return_fine.set(row[15])
        self.date_over_due.set(row[16])
        self.finalprice.set(row[17])

    def show_data(self):
        self.txtBox.insert(END, "Member Type\t\t " + self.member_type.get() + "\n")
        self.txtBox.insert(END, "PRN No:\t\t " + self.prn_no.get() + "\n")
        self.txtBox.insert(END, "ID No:\t\t " + self.id_no.get() + "\n")
        self.txtBox.insert(END, "First Name:\t\t " + self.first_name.get() + "\n")
        self.txtBox.insert(END, "Last Name:\t\t " + self.last_name.get() + "\n")
        self.txtBox.insert(END, "Address 1:\t\t " + self.address1.get() + "\n")
        self.txtBox.insert(END, "Address 2:\t\t " + self.address2.get() + "\n")
        self.txtBox.insert(END, "Postcode:\t\t " + self.postcode.get() + "\n")
        self.txtBox.insert(END, "Mobile:\t\t " + self.mobile_var.get() + "\n")
        self.txtBox.insert(END, "Book ID:\t\t " + self.book_id.get() + "\n")
        self.txtBox.insert(END, "Book Title:\t\t " + self.book_title.get() + "\n")
        self.txtBox.insert(END, "Author Name:\t\t " + self.author_name.get() + "\n")
        self.txtBox.insert(END, "Date Borrowed:\t\t " + self.date_borrowed.get() + "\n")
        self.txtBox.insert(END, "Date Due:\t\t " + self.date_due.get() + "\n")
        self.txtBox.insert(END, "Days on Book:\t\t " + self.days_on_book.get() + "\n")
        self.txtBox.insert(END, "Late Return Fine:\t " + self.late_return_fine.get() + "\n")
        self.txtBox.insert(END, "Date Over Due:\t\t " + self.date_over_due.get() + "\n")
        self.txtBox.insert(END, "Actual Price:\t\t " + self.finalprice.get() + "\n")

    def exit_program(self):
        exit_program=tkinter.messagebox.askyesno("Library Management System", "Are you sure you want to exit?")
        if exit_program>0:
            self.root.destroy()
            return

    def update_data(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="MySql@013",
                database="college"
            )
            my_cursor = conn.cursor()
            sql = """
                UPDATE library SET
                Member=%s, `ID`=%s, FirstName=%s, LastName=%s, Address1=%s,             Address2=%s,
                PostId=%s, Mobile=%s, BookId=%s, BookTitle=%s, Author=%s,
                dateborrowed=%s, datedue=%s, daysofbook=%s,             latereturnfine=%s,
                dateoverdue=%s, finalprice=%s
                WHERE PRN_No=%s
            """
            values = (
                self.member_type.get(),
                self.id_no.get(),
                self.first_name.get(),
                self.last_name.get(),
                self.address1.get(),
                self.address2.get(), 
                self.postcode.get(), 
                self.mobile_var.get(),
                self.book_id.get(), 
                self.book_title.get(), 
                self.author_name.get(),
                self.date_borrowed.get(), 
                self.date_due.get(), 
                self.days_on_book.get(),
                self.late_return_fine.get(), 
                self.date_over_due.get(), 
                self.finalprice.get(),
                self.prn_no.get()  # condition value for WHERE clause
            )
            my_cursor.execute(sql, values)
            conn.commit()
            self.fetch_data()
            self.reset_data()
            messagebox.showinfo("Success", "Data has been updated successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong:\n{str(e)}")
        finally:
            conn.close()
        
    def reset_data(self):
        self.member_type.set("Select Member Type")
        self.prn_no.set("")
        self.id_no.set("")
        self.first_name.set("")
        self.last_name.set("")
        self.address1.set("")
        self.address2.set("")
        self.postcode.set("")
        self.mobile_var.set("")
        self.book_id.set("")
        self.book_title.set("")
        self.author_name.set("")
        self.date_borrowed.set("")
        self.date_due.set("")
        self.days_on_book.set("")
        self.late_return_fine.set("")
        self.date_over_due.set("")
        self.finalprice.set("")
        self.txtBox.delete(1.0, END)
        
    def delete_data(self):
        try:
            if self.prn_no.get() == "" or self.id_no.get() == "":
                messagebox.showerror("Error", "First select the Member")
            else:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="MySql@013",
                    database="college"
                )
                my_cursor = conn.cursor()
                sql = "DELETE FROM library WHERE PRN_No=%s"
                values = (self.prn_no.get(),)  # Tuple with one element
                my_cursor.execute(sql, values)
                conn.commit()
                self.fetch_data()
                self.reset_data()
                messagebox.showinfo("Success", "Data has been deleted successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Error due to: {str(e)}")
        finally:
            if 'conn' in locals() and conn.is_connected():
                conn.close()



if __name__ == "__main__":
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()
