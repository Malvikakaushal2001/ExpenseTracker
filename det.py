#######################################
#####   CODE BY MALVIKA KAUSHAL   #####
#######################################

from tkinter import *
from tkinter import messagebox
import mysql.connector

def back():
    messagebox.showinfo("Go back","Redirected to HomePage")
    window.destroy()
    
    
    
    

def btnClick(numbers):
    global operator
    operator=operator + str(numbers)
    txt_Input.set(operator)

def btnClearDisplay():
     global operator
     operator=""
     txt_Input.set("")

def btnEqualsInput():
    global operator
    sumup=str(eval(operator))
    txt_Input.set(sumup)
    operator=""
    
        
#DEFINING LABELS AND TITLE   
window=Tk()
window.title("Personal Expense")
window .geometry("1800x1800")
window["bg"]="orange"
operator=""
head=Label(window,text="Personal Details",borderwidth=6, relief="raised",font=("Times New Roman",40),bg="yellow")
head.place(x=400,y=20)

amt=StringVar()
pay=StringVar()
meth=StringVar()
cre=StringVar()
Fi=StringVar()
UI=StringVar()

#Variables for Retrieving Data
LUI=StringVar()
AMR=StringVar()
DR=StringVar()
CR=StringVar()
FAR=StringVar()


radio = IntVar()
txt_Input=StringVar()
frame=Frame(window,bg="blue") #First Frame
frame.place(x=1,y=600)





#DEFINING FUNCTIONS
def saving():
    try:
        
        mydb=mysql.connector.connect(host="tcp://4.tcp.ngrok.io:14309",user="root",passwd="root",database="Personal_Details")

        mycursor=mydb.cursor()
        #mycursor.execute("Create table Inc( UserId int(5) primary key,Amt_Bank int(5),Debit int(5),Credit int(5),Final_Amt int(5))")

        Q="Insert into inc(UserId,Amt_Bank,Debit,Credit,Final_Amt) values (%s,%s,%s,%s,%s);"

        d=(UI.get(),amt.get(),pay.get(),cre.get(),Fi.get())
    
        mycursor.execute(Q,d)
    
        mydb.commit()
        messagebox.showinfo("Success","Saved Successfully !!")
    except:
        messagebox.showinfo("Error","User Id not unique !!")
        
    
def Retrieve():
    try:
        
        
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="Personal_Details")

        mycursor=mydb.cursor()
        
        Q="select * from inc where UserId='%s'"%LUI.get() 
        mycursor.execute(Q)
        result=mycursor.fetchone()
        AMR.set(result[1])
        DR.set(result[2])
        CR.set(result[3])
        FAR.set(result[4])
        t5.configure(state='disabled')
        mydb.close()
    except:
        messagebox.showinfo('No Data','No Such data available...')

        
#This is for clearing the previous text fields
def clearrr():
    amt.set('')
    pay.set('')
    cre.set('')
    Fi.set('')
    UI.set('')
    
#this is for clearing the data from new retrieving text fields
    
def clear():
    UI.set('')
    AMR.set('')
    DR.set('')
    CR.set('')
    FAR.set('')
    t5.configure(state='normal')
    
    
    



def amounty():
    g,g1,g2,g3=amt.get(),pay.get(),cre.get(),UI.get()
    a=""
    
    if(g.isdigit()==True and g1.isdigit()==True and g2.isdigit()==True and g3.isdigit()==True):
        a="Final Balance is "+str((int(amt.get())-int(pay.get()))+int(cre.get()))
    else:
        a="Please pass valid number"
    l8.config(text=a,font=("Times New Roman BOLD",16))

def chk():
    s,s1,s2=amt.get(),pay.get(),UI.get()
    r=""
    if(s.isdigit()==True and s1.isdigit()==True and s2.isdigit()==True):
        if((int(amt.get())-int(pay.get())) <0):
            r="Insufficient Balance. Write Again"
        else:
            r="Net Balance is "+str(int(amt.get())-int(pay.get()))         
    else:
            r="Please Pass Valid number"
    l4.config(text=r,font=("Times New Roman BOLD",16))
   
def selection():  
   selection = "You selected the option " + str(radio.get())
   
   l3.config(text=selection,font=("Times New Roman BOLD",16))


    
#GETTING ENTRY FOR LABELS
ti=Label(window,text="* fields COMPULSORY , ** UNIQUE",bg="SteelBlue",fg="black",relief="raised")
ti.place(x=3,y=10)
ti.config(font=("Times New Roman BOLD",10))

nm=Label(window,text="UserID(only Digits)**",bg="Chartreuse",fg="black")
nm.place(x=3,y=50)
nm.config(font=("Times New Roman BOLD",16))
nmt=Entry(window,bd=5,width=15,textvariable=UI,font=("Times New Roman BOLD",15),relief="raised")
nmt.place(x=210,y=50)


l0=Label(window,text="Amount in Bank*",bg="Chartreuse",fg="black")
l0.place(x=3,y=100)
l0.config(font=("Times New Roman BOLD",16))
t1=Entry(window,bd=8,width=50,textvariable=amt,font=("Times New Roman BOLD",15))
t1.place(x=208,y=100)


l1=Label(window,text="Debit Money to Pay*",bg="Chartreuse",fg="black")
l1.place(x=3,y=170)
l1.config(font=("Times New Roman BOLD",16))
t2=Entry(window,bd=8,width=50,textvariable=pay,font=("Times New Roman BOLD",15))
t2.place(x=208,y=170)

l2=Label(window,text="Mode of Payment",bg="Chartreuse",fg="black")
l2.place(x=3,y=240)
l2.config(font=("Times New Roman BOLD",16))

#RADIO BUTTONS FOR MODE OF PAYMENT
R1 = Radiobutton(window, text="Net banking",font=("Times New Roman BOLD",15),borderwidth=5, relief="raised",bg="PaleGreen",fg="black", variable=radio, value=1,command=selection)
R1.place(x=200,y=240) 
R2 = Radiobutton(window, text="Cash",font=("Times New Roman BOLD",15),borderwidth=5, relief="raised",bg="PaleGreen",fg="black", variable=radio, value=2,command=selection)
R2.place(x=350,y=240)
R2 = Radiobutton(window, text="Cheque",font=("Times New Roman BOLD",15), borderwidth=5, relief="raised",bg="PaleGreen",fg="black",variable=radio, value=3,command=selection)
R2.place(x=440,y=240)
l3 = Label(window,font=("Times New Roman",13),fg="Red",bg="orange")
l3.place(x=200,y=300)



#BUTTON FOR SUBMITTING DATA
b1=Button(window,text="Calculate",command=chk,borderwidth=5, relief="raised",font=("Times New Roman",16),fg="white",bg="black")
b1.place(x=50,y=350)
l4=Label(window,font=("Times New Roman",16),fg="Red",bg="orange")
l4.place(x=200,y=360)

#Credit money
l5=Label(window,text="Any Money to Credit in Future??",bg="LightSeaGreen",fg="black")
l5.place(x=100,y=410)
l5.config(font=("Times New Roman BOLD",16))
l6=Label(window,text="Enter Credit Amount*",bg="Chartreuse",fg="black")
l6.place(x=3,y=450)
l6.config(font=("Times New Roman BOLD",16))
t3=Entry(window,bd=8,width=50,textvariable=cre,font=("Times New Roman BOLD",15))
t3.place(x=214,y=450)

#Final Amount
b2=Button(window,text="Final Amount",command=amounty,borderwidth=5, relief="raised",font=("Times New Roman",16),fg="white",bg="black")
b2.place(x=50,y=540)
l7=Label(window,text="(In case you don't have any credit money then pass 0)",font=("Times New Roman BOLD",16),fg="Red",bg="orange")
l7.place(x=200,y=500)

l8=Label(window,font=("Times New Roman BOLD",16),fg="Red",bg="Orange")
l8.place(x=200,y=550)

l9=Label(window,text="Enter Final Amt for Saving",font =("Times New Roman BOLD",10),fg="Black",bg="Orange")
l9.place(x=425,y=550)

t4=Entry(window,textvariable=Fi,font=("Times New Roman BOLD",10),fg="Red",bg="Orange")
t4.place(x=577,y=550)

b3=Button(window,text="Save",command=saving,borderwidth=5, relief="raised",font=("Times New Roman",14),fg="white",bg="Red")
b3.place(x=400,y=580)

b8=Button(window,text="Clear",command=clearrr,borderwidth=5, relief="raised",font=("Times New Roman",14),fg="white",bg="Red")
b8.place(x=500,y=580)

b9=Button(window,text="EXIT",command=window.destroy,borderwidth=5, relief="raised",font=("Times New Roman",14),fg="white",bg="Red")
b9.place(x=600,y=580)

#second frame

#For RIGHT side
l9=Label(window,text="Your CALCULATOR", borderwidth=5, relief="groove",bg="SteelBlue",fg="black")
l9.place(x=900,y=40)
l9.config(font=("Times New Roman BOLD",20))
txtDisplay=Entry(window,font=('Times New Roman BOLD',16),textvariable=txt_Input,bd=30,insertwidth=4,
                 bg="powder blue",justify="right").place(x=900,y=85)
b10=Button(window,text="Back",command=back,borderwidth=5, relief="raised",font=("Times New Roman",14),fg="white",bg="Red")
b10.place(x=1180,y=40)

#Calculator Row 1
btn7=Button(window,padx=16,bd=5,fg="black",bg="powder blue",font=("Times New Roman Bold",20),text="7",command=lambda:btnClick(7)).place(x=900,y=170)
btn8=Button(window,padx=16,bd=5,fg="black",bg="powder blue",font=("Times New Roman Bold",20),text="8",command=lambda:btnClick(8)).place(x=970,y=170)
btn9=Button(window,padx=16,bd=5,fg="black",bg="powder blue",font=("Times New Roman Bold",20),text="9",command=lambda:btnClick(9)).place(x=1040,y=170)
Addition=Button(window,padx=16,bd=5,fg="black",bg="powder blue",font=("Times New Roman Bold",20),text="+",command=lambda:btnClick("+")).place(x=1105,y=170)
#Calculator Row 2
btn4=Button(window,padx=16,bd=5,fg="black",bg="powder blue",font=("Times New Roman Bold",20),text="4",command=lambda:btnClick(4)).place(x=900,y=220)
btn5=Button(window,padx=16,bd=5,fg="black",bg="powder blue",font=("Times New Roman Bold",20),text="5",command=lambda:btnClick(5)).place(x=970,y=220)
btn6=Button(window,padx=16,bd=5,fg="black",bg="powder blue",font=("Times New Roman Bold",20),text="6",command=lambda:btnClick(6)).place(x=1040,y=220)
Subtraction=Button(window,padx=16,bd=5,fg="black",bg="powder blue",font=("Times New Roman Bold",20),text="-",command=lambda:btnClick("-")).place(x=1110,y=220)
#Calculator Row 3
btn1=Button(window,padx=16,bd=5,fg="black",bg="powder blue",font=("Times New Roman Bold",20),text="1",command=lambda:btnClick(1)).place(x=900,y=270)
btn2=Button(window,padx=16,bd=5,fg="black",bg="powder blue",font=("Times New Roman Bold",20),text="2",command=lambda:btnClick(2)).place(x=970,y=270)
btn3=Button(window,padx=16,bd=5,fg="black",bg="powder blue",font=("Times New Roman Bold",20),text="3",command=lambda:btnClick(3)).place(x=1040,y=270)
Multiply=Button(window,padx=16,bd=5,fg="black",bg="powder blue",font=("Times New Roman Bold",20),text="*",command=lambda:btnClick("*")).place(x=1105,y=270)

#Calculator Row 4
btn0=Button(window,padx=16,bd=5,fg="black",bg="powder blue",font=("Times New Roman Bold",20),text="0",command=lambda:btnClick(0)).place(x=900,y=320)
btnClear=Button(window,padx=16,bd=5,fg="black",bg="powder blue",font=("Times New Roman Bold",20),text="C",command=btnClearDisplay).place(x=970,y=320)
btnEquals=Button(window,padx=16,bd=5,fg="black",bg="powder blue",font=("Times New Roman Bold",20),text="=",command=btnEqualsInput).place(x=1040,y=320)
Division=Button(window,padx=16,bd=5,fg="black",bg="powder blue",font=("Times New Roman Bold",20),text="/",command=lambda:btnClick("/")).place(x=1110,y=320)

#View Data
l10=Label(window,text="View Entered data", borderwidth=5, relief="groove",bg="SteelBlue",fg="black")
l10.place(x=900,y=390)
l10.config(font=("Times New Roman BOLD",20))

l11=Label(window,text="Enter last UserID", borderwidth=5, bg="Chartreuse",fg="black")
l11.place(x=800,y=450)
l11.config(font=("Times New Roman BOLD",10))
t5=Entry(window,bd=8,width=20,textvariable=LUI,font=("Times New Roman BOLD",10))
t5.place(x=908,y=450)

b4=Button(window,text="View Data",command=Retrieve,borderwidth=5, relief="raised",font=("Times New Roman BOLD",13),fg="white",bg="Red")
b4.place(x=1080,y=450)

l12=Label(window,text="Bank Amt(last)", borderwidth=5, bg="Chartreuse",fg="black")
l12.place(x=800,y=490)
l12.config(font=("Times New Roman BOLD",10))
t6=Entry(window,bd=8,width=20,textvariable=AMR,font=("Times New Roman BOLD",10))
t6.place(x=908,y=490)

l12=Label(window,text="Debit(last)", borderwidth=5, bg="Chartreuse",fg="black")
l12.place(x=800,y=520)
l12.config(font=("Times New Roman BOLD",10))
t7=Entry(window,bd=8,width=20,textvariable=DR,font=("Times New Roman BOLD",10))
t7.place(x=908,y=520)

l12=Label(window,text="Credit(last)", borderwidth=5, bg="Chartreuse",fg="black")
l12.place(x=800,y=550)
l12.config(font=("Times New Roman BOLD",10))
t8=Entry(window,bd=8,width=20,textvariable=CR,font=("Times New Roman BOLD",10))
t8.place(x=908,y=550)

l12=Label(window,text="Final Bal(last)", borderwidth=5, bg="Chartreuse",fg="black")
l12.place(x=800,y=580)
l12.config(font=("Times New Roman BOLD",10))
t9=Entry(window,bd=8,width=20,textvariable=FAR,font=("Times New Roman BOLD",10))
t9.place(x=908,y=580)


b4=Button(window,text="Clear",command=clear,borderwidth=5, relief="raised",font=("Times New Roman BOLD",13),fg="white",bg="Red")
b4.place(x=1080,y=580)


window.mainloop()

















