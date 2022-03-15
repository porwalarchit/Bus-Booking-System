from tkinter import *

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
root.bind('<Motion>',close)

root.mainloop()