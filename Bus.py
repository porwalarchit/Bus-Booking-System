from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import sqlite3

def home_screen():
    conn = sqlite3.connect('BusDatabase.db')

    def add_bus():
        root.destroy()
        root1 = Tk()
        root1.geometry('400x580')
        Label(root1, text='Bus Booking Service', font='Arial 20 bold', fg='red').grid(row=0, column=1)

        name = StringVar()
        num = IntVar()
        addr = StringVar()
        operator = StringVar()
        bustype = StringVar()
        fr = StringVar()
        to = StringVar()
        date = StringVar()
        dept_time = StringVar()
        arr_time = StringVar()
        fare = IntVar()
        seats = IntVar()

        def database():
            Operator=operator.get()
            Bustype=bustype.get()
            Fr=fr.get()
            To=to.get()
            Date=date.get()
            Dept_time=dept_time.get()
            Arr_time=arr_time.get()
            Fare=fare.get()
            Seats=seats.get()

            with conn:
                cursor = conn.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS BUSDETAILS(Operator VARCHAR(40),Type CHAR(20), From_Bus VARCHAR(30), To_Bus VARCHAR(30), Date VARCHAR(12), Dep_Time VARCHAR(20), Arr_Time VARCHAR(20), Fare INT, Seats_Availabilty INT)")
            cursor.execute("INSERT INTO BUSDETAILS(Operator,Type, From_Bus, To_Bus, Date, Dep_Time, Arr_Time, Fare, Seats_Availabilty) VALUES(?,?,?,?,?,?,?,?,?)",(Operator, Bustype, Fr, To, Date, Dept_time, Arr_time,Fare, Seats) )
            conn.commit()
            messagebox.showinfo("Detail", "Detail Saved")

        img = Image.open('bus.png')
        img = img.resize((276,164))
        image1 = ImageTk.PhotoImage(img)
        Label(image=image1).grid(row=1, column=1)
        Label(root1, text='Bus Operator Details Filling', font='Arial 15 bold', fg='red').grid(row=2, column=1)

        Label(root1, text='Full Name : ').grid(row=3, column=0)
        name=Entry(root1)
        name.grid(row=3,column=1)

        Label(root1, text='Contact No ').grid(row=4, column=0)
        num = Entry(root1)
        num.grid(row=4, column=1)

        Label(root1, text='Address : ').grid(row=5, column=0)
        addr = Entry(root1)
        addr.grid(row=5, column=1)

        def add_details():
            Label(root1, text='Operator : ').grid(row=7, column=0)
            Entry(root1,textvar=operator).grid(row=7, column=1)

            Label(root1, text='Bus Type : ').grid(row=8, column=0)
            Entry(root1,textvar=bustype).grid(row=8, column=1)

            Label(root1, text='From : ').grid(row=9, column=0)
            Entry(root1,textvar=fr).grid(row=9, column=1)

            Label(root1, text='To : ').grid(row=10, column=0)
            Entry(root1,textvar=to).grid(row=10, column = 1)

            Label(root1, text='Date : ').grid(row=11, column=0)
            Entry(root1,textvar=date).grid(row=11, column = 1)

            Label(root1, text='Dep Time : ').grid(row=12, column=0)
            Entry(root1,textvar=dept_time).grid(row=12, column=1)

            Label(root1, text='Arr Time : ').grid(row=13, column=0)
            Entry(root1,textvar=arr_time).grid(row=13, column=1)

            Label(root1, text='Fare : ').grid(row=14, column=0)
            Entry(root1,textvar=fare).grid(row=14, column=1)

            Label(root1, text='Seats : ').grid(row=15, column=0)
            Entry(root1,textvar=seats).grid(row=15, column=1)

            def home_calling():
                database()
                root1.destroy()
                home_screen()

            Button(root1,text="Save",command=home_calling).grid(row=16,column=1)
        Button(root1, text='Add Details',command=add_details ).grid(row=6, column=1)

        root1.mainloop()

    def search_bus():
        root.destroy()
        root2 = Tk()
        root2.geometry('350x350')
        Label(root2, text='Bus Booking Service', font='Arial 20 bold', fg='red').grid(row=0, column=1)

        img1 = Image.open('bus.png')
        img1 = img1.resize((184, 110))
        image2 = ImageTk.PhotoImage(img1)
        Label(image=image2).grid(row=1, column=1)
        Label(root2, text='Listing Buses', font='Arial 15 bold', fg='red').grid(row=2, column=1)

        Label(root2, text="Bus Type").grid(row=3, column=0)
        clicked = StringVar()
        clicked.set("Bus Type")
        bustype = OptionMenu(root2, clicked, "AC", "Non AC", "AC-Sleeper", "Non AC-Sleeper").grid(row=3, column=1)

        Label(root2, text='From : ').grid(row=4, column=0)
        Entry(root2).grid(row=4, column=1)

        Label(root2, text='To : ').grid(row=5, column=0)
        Entry(root2).grid(row=5, column=1)

        Label(root2, text='Date : ').grid(row=6, column=0)
        Entry(root2).grid(row=6, column=1)

        def home_calling():
            root2.destroy()
            home_screen()

        Button(root2, text="Home", command=home_calling).grid(row=7, column=0)

        def find_bus():
            root2.destroy()
            root3=Tk()
            #root3.geometry('350x350')
            Label(root3, text='Bus Booking Service', font='Arial 15 bold', fg='red').grid(row=0, column=1)

            img1 = Image.open('bus.png')
            img1 = img1.resize((138, 82))
            image2 = ImageTk.PhotoImage(img1)
            Label(image=image2).grid(row=1, column=1)
            Label(root3, text='Bus Details...', font='Arial 10 bold', fg='red').grid(row=2, column=1)

            Label(root3, text='Operator : ').grid(row=3, column=0)

            Label(root3, text='Bus Type : ').grid(row=3, column=1)

            Label(root3, text='From : ').grid(row=3, column=2)

            Label(root3, text='To : ').grid(row=3, column=3)

            Label(root3, text='Date : ').grid(row=3, column=4)

            Label(root3, text='Dep Time : ').grid(row=3, column=5)

            Label(root3, text='Arr Time : ').grid(row=3, column=6)

            Label(root3, text='Fare : ').grid(row=3, column=7)

            Label(root3, text='Seats : ').grid(row=3, column=8)
            root3.mainloop()

        Button(root2, text="Search", command=find_bus).grid(row=7, column=1)
        root2.mainloop()

    root = Tk()
    root.geometry('780x500')
    Label(root,text='Bus Booking Service',font='Arial 25 bold',fg='red').grid(row=0,column=1)
    image1 = PhotoImage(file='bus.png')
    Label(root,image=image1).grid(row=1,column=1)
    Button(root,text='Add Bus',font=150,command=add_bus).grid(row=2,column=0)
    Button(root,text='Search Bus',font=150,command=search_bus).grid(row=2,column=2)
    Button(root,text='Exit',font=150,command=root.destroy).grid(row=3,column=1)

    root.mainloop()

root = Tk()
root.geometry('1000x600')
Label(root,text="Project Title : Bus Booking System",font='Arial 20 bold').grid(row=0,column=0)
Label(root,text="Developed as the part of course Advanced Programming Lab-1 & DBMS",font='Arial 20 bold').grid(row=1,column=0)
Label(root,text='Developed By : Archit Porwal, ER :191B059, Mobile :9956351040, E-mail :architporwal@gmail.com',font='Arial 15 bold',fg='blue').grid(row=2,column=0)
Label(root,text="--------------------------------",font='Arial 15',fg='blue').grid(row=3,column=0)
Label(root,text="Project Supervisors : Dr. Mahesh Kumar & Dr.Nilesh Patel",font='Arial 10 bold',fg='green').grid(row=4,column=0)
Label(root,text="Make mouse movement over this screen this close",font='Arial 10 bold',fg='red').grid(row=6,column=0)

def close(e=2):
    root.destroy()
    home_screen()
root.bind('<Motion>',close)

root.mainloop()