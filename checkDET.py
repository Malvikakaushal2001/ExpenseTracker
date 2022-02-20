from tkinter import *
def chk():
    s,s1=amt.get(),pay.get()
    r=""
    if(s.isdigit()==True and s1.isdigit()==True):
        if((int(amt.get())-int(pay.get())) <0):
            r="Insufficient Balance"
        else:
            r="Net Balance is "+str(int(amt.get())-int(pay.get()))         
    else:
            r="Please Pass Valid number"
    l4.config(text=r)
   
def selection():  
   selection = "You selected the option " + str(radio.get())
   
   l3.config(text=selection)
   
window=Tk()
window.title("Personal Expense")
window .geometry("1250x1200")
window["bg"]="orange"

head=Label(window,text="Personal Details",font=("Times New Roman",40))
head.place(x=400,y=20)

amt=StringVar()
pay=StringVar()
meth=StringVar()

radio = IntVar()
frame=Frame(window,bg="blue") #First Frame

l0=Label(window,text="Amount in Bank.")
l0.place(x=5,y=100)
l0.config(font=("Times New Roman",16))
t1=Entry(window,bd=8,width=50,textvariable=amt,font=("Times New Roman",12))
t1.place(x=150,y=100)


l1=Label(window,text="Amount to Pay")
l1.place(x=5,y=170)
l1.config(font=("Times New Roman",16))
t1=Entry(window,bd=8,width=50,textvariable=pay,font=("Times New Roman",12))
t1.place(x=150,y=170)

l2=Label(window,text="Mode of Payment")
l2.place(x=5,y=240)
l2.config(font=("Times New Roman",16))

R1 = Radiobutton(window, text="Net banking",font=("Times New Roman",12), variable=radio, value=1,command=selection)
R1.place(x=200,y=240) 
R2 = Radiobutton(window, text="Cash",font=("Times New Roman",12), variable=radio, value=2,command=selection)
R2.place(x=320,y=240)
R2 = Radiobutton(window, text="Cheque",font=("Times New Roman",12), variable=radio, value=3,command=selection)
R2.place(x=400,y=240)
l3 = Label(window,font=("Times New Roman",13),fg="Red",bg="orange")
l3.place(x=200,y=300)

b1=Button(window,text="Submit",command=chk,font=("Times New Roman",16),fg="white",bg="black")
b1.place(x=50,y=350)
l4=Label(window,font=("Times New Roman",13),fg="Red",bg="orange")
l4.place(x=200,y=360)

window.mainloop()
