from tkinter import*
import tkinter.messagebox
import webbrowser
from tkinter import ttk
import random
import tempfile
import os
import time
import datetime
from tkinter import messagebox, Entry
from tkinter import filedialog


def main():
    app = Window1(root)
        
#=======================================================================================================================================
#===================================================================Window1=============================================================
#=======================================================================================================================================
root = Tk()

canvas = Canvas(width=650,height=315,bg='blue')

photo = PhotoImage(file='F:\\Project\\CMS\\logo1.png')

canvas.create_image(0,0,image=photo, anchor=NW)
        
class Window1:
    def __init__(self,master):
        self.master = master
        self.master.title("* Cafe Management System *  , Developed By :- Yashdeep Vaitage.")
        self.master.geometry("1350x725+0+0")
        self.master.config(bg='white')
        self.frame= Frame(self.master,bg="white")
        self.frame.pack()

        self.lblTitle = Label(self.frame, font=('times new roman', 20, 'bold'), text="Degree Collage of Physical Education, (H.V.P.M.) Amravati", bg='white',fg='orange')
        self.lblTitle.grid(row=2,column=0,pady=10)

        self.lblTitle = Label(self.frame, font=('Brush Script MT', 30, 'bold','underline'), text="Project Guide : Prof. A. D. Chavan", bg='white',fg='blue')
        self.lblTitle.grid(row=3,column=0,pady=3)
        
        self.lblTitle = Label(self.frame, font=('times new roman', 40, 'bold'), text="Welcome to Coffee House", bg='white',fg='black')
        self.lblTitle.grid(row=4,column=0,columnspan=3,pady=10)
#=================================================================Frame======================================================================

        self.Frame1 = LabelFrame(self.frame, width=1000,height=600, font=('times new roman', 20, 'bold'),relief='ridge',bg='black',bd=20)
        self.Frame1.grid(row=5,column=0)


#=================================================================Buttons======================================================================
        
        self.btnBill = Button(self.Frame1, font=('times new roman', 15, 'bold'),text="Bill",width=17,command =self.Login_System)
        self.btnBill.grid(row=3, column=1,pady=20,padx=8)

        self.btnDetail = Button(self.Frame1, font=('times new roman', 15, 'bold'),text="Employee Detail",width=17,command=self.Open_window)
        self.btnDetail.grid(row=3, column=2,pady=20,padx=8)

        self.btnFeed = Button(self.Frame1, font=('times new roman', 15, 'bold'),text="Feedback",width=17,command=self.Feed_window)
        self.btnFeed.grid(row=3, column=3,pady=20,padx=8)
       
        self.btnOther = Button(self.Frame1, font=('times new roman', 15, 'bold'),text="Other",width=17,command=self.Other_window)
        self.btnOther.grid(row=3, column=4,pady=20,padx=8)
         
        self.btnExit = Button(self.Frame1, font=('times new roman', 15, 'bold'),text="Exit", fg="red",width=17,command=self.iExit)
        self.btnExit.grid(row=3, column=5,pady=20,padx=8,columnspan=5)
#================================================================================================================================
    def Login_System(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window2(self.newWindow)


    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Home Page","Conform if you want to exit")
        if self.iExit > 0:
            self.master.destroy()
        else:
            command = self.newWindow
            return

    def Feed_window(self):
         self.feedWindow = Toplevel(self.master)
         self.fd = Window5(self.feedWindow)
        
    def Other_window(self):
        self.otherWindow = Toplevel(self.master)
        self.ot = Window4(self.otherWindow)


    def Open_window(self):
         self.openWindow = Toplevel(self.master)
         self.pic = Window3(self.openWindow)

        
    def new_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window2(self.newWindow)

canvas.pack()
#=======================================================================================================================================
#===================================================================Window5=============================================================
#=======================================================================================================================================

         
class Window5:
    def __init__(self,master):
        self.master = master
        self.master.title("Feedback Form")
        self.master.geometry("1350x725+0+0")
        self.master.config(bg='light blue')
        self.frame= Frame(self.master,bg='light blue')
        self.frame.pack()

#=======================================================================FRAME======================================================================
        self.TitleFrame = LabelFrame(self.frame, width=1350,height=725,relief='ridge',bg='cadet blue',bd=20)
        self.TitleFrame.pack(side=TOP)
        

        self.InfoFrame1 = Frame(self.frame, width=540, height=750, relief="raise",bg='maroon',bd=10)
        self.InfoFrame1.pack(side=LEFT)

        self.InfoFrame2 = Frame(self.InfoFrame1, width=440,height=650,relief='ridge',bg='cadet blue',bd=10)
        self.InfoFrame2.pack(side=TOP)

        self.SubFrame = Frame(self.frame, width=540, height=750, relief="ridge",bg='maroon',bd=10)
        self.SubFrame.pack(side=RIGHT)

        self.FillFrame = Frame(self.SubFrame, width=440, height=750, relief="raise",bg='cadet blue',bd=10)
        self.FillFrame.pack(side=TOP)

        self.IbtFrame2 = Frame(self.SubFrame, width=640, height=50, bd=10, relief="ridge",bg='sky blue')
        self.IbtFrame2.pack(side=BOTTOM)


#=======================================================================Title======================================================================
        self.lblTitle = Label(self.TitleFrame, font=('times new roman', 30, 'bold'), text="\t\t\tCustomers Feedback - Form\t\t",
                             bd=20, bg='teal',fg='cornsilk')
        self.lblTitle.grid(row=2,column=1,pady=10,columnspan=4)

#=======================================================================Content======================================================================
        def save_file():
            f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
            if f is None:
                 return

            q = txtFeedback.get("1.0","end-1c")

            f.write(q)
            f.close()

        def Reset():
            Name.set("")
            Email.set("")
            Comment.set("")
            txtFeedback.delete("1.0", END)
            var1.set(0)
            var2.set(0)
            var3.set(0)
            var4.set(0)
            var5.set(0)
            var6.set(0)
            var7.set(0)
            var8.set(0)
            var9.set(0)
            var10.set(0)
            var11.set(0)
            var12.set(0)
            var13.set(0)
            var14.set(0)
            var15.set(0)
            var16.set(0)
            var17.set(0)
            var18.set(0)
            var19.set(0)
            var20.set(0)

    

        Feedback_Ref = StringVar()
        DateofFeed = StringVar()
        Cname = StringVar()
        Email = StringVar()


        def Feedback():
            txtFeedback.delete("1.0", END)
            x = random.randint(10208, 500876)
            randomRef = str(x)
            Feedback_Ref.set("Feedback ID :\t\t" + randomRef)

            txtFeedback.insert(END, Feedback_Ref.get() + '\t\t' + DateofFeed.get() + "\n")
            txtFeedback.insert(END, 'Customer Name:\t\t' + lblCname.get()+"\n")
            txtFeedback.insert(END, 'Customer Email :\t\t'+ lblEmail.get()+"\n\n")
            txtFeedback.insert(END, 'Cleaness \t\t: '+ E_c1.get() + '\t\t'+E_c2.get()+ '\t'+E_c3.get()+ '\t'+E_c4.get()+"\n\n")
            txtFeedback.insert(END, 'Friendly Service \t\t: ' +E_c5.get()+ '\t\t'+E_c6.get()+ '\t'+E_c7.get()+ '\t'+E_c8.get()+"\n\n")
            txtFeedback.insert(END, 'Service Speed\t\t: '+E_c9.get()+ '\t\t'+E_c10.get()+ '\t'+E_c11.get()+ '\t'+E_c12.get() +"\n\n")
            txtFeedback.insert(END, 'Quality of Food\t\t: '+E_c13.get()+ '\t\t'+E_c14.get()+ '\t'+E_c15.get()+ '\t'+E_c16.get()+"\n\n")
            txtFeedback.insert(END, 'Visit us Again\t\t: ' +E_c17.get()+ '\t\t'+E_c18.get()+ '\t'+E_c19.get()+ '\t'+E_c20.get()+"\n\n")
            txtFeedback.insert(END, 'Suggetion\t\t: ' + lblComment.get()+"\n")

        DateofFeed.set(time.strftime("%d/%m/%y    %H:%M:%S"))
# =========================================================INFORMATION (ft2)============================================
        lblFeedback = Label(self.FillFrame, font=('times new roman', 14, 'bold'), text="Customers Feedback :", bd=2, anchor='w')
        lblFeedback.grid(row=0, column=0, sticky=W)  # 16
        txtFeedback = Text(self.FillFrame, font=('times new roman', 11, 'bold'), bd=5, width=65,height=25)
        txtFeedback.grid(row=1, column=0)  # 21/02/19
# ===========================================================================================================================

           
        def chkbutton_value():
            if (var1.get() == 1):
                E_c1.set("Excellent")
            elif var1.get() == 0:
                E_c1.set("     _ ")
            if (var2.get() == 1):
                E_c2.set("Good")
            elif var2.get() == 0:
                E_c2.set("   _ ")
            if (var3.get() == 1):
                E_c3.set("Fair")
            elif var3.get() == 0:
                E_c3.set("  _ ")
            if (var4.get() == 1):
                 E_c4.set("Poor")
            elif var4.get() == 0:
                E_c4.set("  _ ")
            if (var5.get() == 1):
                E_c5.set("Excellent")
            elif var5.get() == 0:
                E_c5.set("     _ ")
            if (var6.get() == 1):
                E_c6.set("Good")
            elif var6.get() == 0:
                E_c6.set("   _ ")
            if (var7.get() == 1):
                E_c7.set("Fair")
            elif var7.get() == 0:
                E_c7.set("  _ ")
            if (var8.get() == 1):
                E_c8.set("Poor")
            elif var8.get() == 0:
                E_c8.set("  _ ")
            if (var9.get() == 1):
                E_c9.set("Excellent")
            elif var9.get() == 0:
                E_c9.set("     _ ")
            if (var10.get() == 1):
                E_c10.set("Good")
            elif var10.get() == 0:
                E_c10.set("   _ ")
            if (var11.get() == 1):
                E_c11.set("Fair")
            elif var11.get() == 0:
                E_c11.set("  _ ")
            if (var12.get() == 1):
                E_c12.set("Poor")
            elif var12.get() == 0:
                E_c12.set("  _ ")
            if (var13.get() == 1):
                E_c13.set("Excellent")
            elif var13.get() == 0:
                E_c13.set("     _ ")
            if (var14.get() == 1):
                E_c14.set("Good")
            elif var14.get() == 0:
                E_c14.set("   _ ")
            if (var15.get() == 1):
                E_c15.set("Fair")
            elif var15.get() == 0:
                E_c15.set("  _ ")
            if (var16.get() == 1):
                E_c16.set("Poor")
            elif var16.get() == 0:
                E_c16.set("  _ ")
            if (var17.get() == 1):
                E_c17.set("Excellent")
            elif var17.get() == 0:
                E_c17.set("     _ ")
            if (var18.get() == 1):
                E_c18.set("Good")
            elif var18.get() == 0:
                E_c18.set("   _ ")
            if (var19.get() == 1):
                E_c19.set("Fair")
            elif var19.get() == 0:
                E_c19.set("  _ ")
            if (var20.get() == 1):
                E_c20.set("Poor")
            elif var20.get() == 0:
                E_c20.set("  _ ")


# ============================================================VARIABLE==================================================
        var1 = IntVar()
        var2 = IntVar()
        var3 = IntVar()
        var4 = IntVar()
        var5 = IntVar()
        var6 = IntVar()
        var7 = IntVar()
        var8 = IntVar()
        var9 = IntVar()
        var10 = IntVar()
        var11 = IntVar()
        var12 = IntVar()
        var13 = IntVar()
        var14 = IntVar()
        var15 = IntVar()
        var16 = IntVar()
        var17 = IntVar()
        var18 = IntVar()
        var19 = IntVar()
        var20 = IntVar()

        Name = StringVar()
        Email = StringVar()
        Comment = StringVar()

        E_c1 = StringVar()
        E_c2 = StringVar()
        E_c3 = StringVar()
        E_c4 = StringVar()
        E_c5 = StringVar()
        E_c6 = StringVar()
        E_c7 = StringVar()
        E_c8 = StringVar()
        E_c9 = StringVar()
        E_c10 = StringVar()
        E_c11 = StringVar()
        E_c12 = StringVar()
        E_c13 = StringVar()
        E_c14 = StringVar()
        E_c15 = StringVar()
        E_c16 = StringVar()
        E_c17 = StringVar()
        E_c18 = StringVar()
        E_c19 = StringVar()
        E_c20 = StringVar()
# ===========================================================================================================================
        lblCname = Label(self.InfoFrame2, font=('times new roman', 11, 'bold'), width=10, text="\tName : ", bd=8,fg='black', bg='cadet blue')
        lblCname.grid(row=1, column=0, sticky=W,columnspan=4)
        lblCname = Entry(self.InfoFrame2, font=('times new roman', 11, 'bold'), width=22, bd=9, justify='left', textvariable=Name)
        lblCname.grid(row=1, column=1)

        lblEmail = Label(self.InfoFrame2, font=('times new roman', 11, 'bold'), width=10, text="\tE-Mail :  ", bd=8,fg='black', bg='cadet blue')
        lblEmail.grid(row=1, column=2, sticky=W,columnspan=4)
        lblEmail = Entry(self.InfoFrame2, font=('times new roman', 11, 'bold'), width=26, bd=9, justify='left', textvariable=Email)
        lblEmail.grid(row=1, column=3)

        lblFd = Label(self.InfoFrame2, font=('times new roman', 11, 'bold'), width=11, text="Feed Appropriate", bd=6,fg='teal')
        lblFd.grid(row=2, column=0, sticky=W,pady=20,columnspan=3)

        lblExcellent = Label(self.InfoFrame2, font=('times new roman', 11, 'bold'), width=25, text="Excellent ", bd=6,fg='green')
        lblExcellent.grid(row=2, column=1, sticky=W,pady=20,columnspan=4)

        lblGood = Label(self.InfoFrame2, font=('times new roman', 11, 'bold'), width=11, text="Good", bd=6,fg='green')
        lblGood.grid(row=2, column=2, sticky=W,pady=20)

        lblFair = Label(self.InfoFrame2, font=('times new roman', 11, 'bold'), width=24, text="Fair", bd=6,fg='green')
        lblFair.grid(row=2, column=3, sticky=W,pady=20)

        lblPoor = Label(self.InfoFrame2, font=('times new roman', 11, 'bold'), width=11, text="Poor", bd=6,fg='green')
        lblPoor.grid(row=2, column=4, sticky=W,pady=20)

        lblClean = Label(self.InfoFrame2, font=('times new roman', 11, 'bold'), width=11, text="Cleaness :", bd=6,bg='light blue',fg='white')
        lblClean.grid(row=3, column=0, sticky=W,pady=10)

        e1 = Checkbutton(self.InfoFrame2, width=11,bd=6,fg='green',variable=var1, onvalue=1, offvalue=0, command=chkbutton_value)
        e1.grid(row=3, column=1,pady=20)

        e2 = Checkbutton(self.InfoFrame2, width=11,bd=6,fg='green',variable=var2, onvalue=1, offvalue=0, command=chkbutton_value)
        e2.grid(row=3, column=2,pady=20)

        e3 = Checkbutton(self.InfoFrame2, width=11,bd=6,fg='green',variable=var3, onvalue=1, offvalue=0, command=chkbutton_value)
        e3.grid(row=3, column=3,pady=20)

        e4 = Checkbutton(self.InfoFrame2, width=11,bd=6,fg='green',variable=var4, onvalue=1, offvalue=0, command=chkbutton_value)
        e4.grid(row=3, column=4,pady=20)

        lblFriendly = Label(self.InfoFrame2, font=('times new roman', 11, 'bold'), width=11, text="Friendly Service :", bd=6,bg='light blue',fg='white')
        lblFriendly.grid(row=4, column=0, sticky=W,pady=10)

        e5 = Checkbutton(self.InfoFrame2, width=11,bd=6,fg='green',variable=var5, onvalue=1, offvalue=0, command=chkbutton_value)
        e5.grid(row=4, column=1,pady=20)

        e6 = Checkbutton(self.InfoFrame2, width=11,bd=6,fg='green',variable=var6, onvalue=1, offvalue=0, command=chkbutton_value)
        e6.grid(row=4, column=2,pady=20)

        e7 = Checkbutton(self.InfoFrame2, width=11,bd=6,fg='green',variable=var7, onvalue=1, offvalue=0, command=chkbutton_value)
        e7.grid(row=4, column=3,pady=20)

        e8 = Checkbutton(self.InfoFrame2, width=11,bd=6,fg='green',variable=var8, onvalue=1, offvalue=0, command=chkbutton_value)
        e8.grid(row=4, column=4,pady=20)

        lblSpeed = Label(self.InfoFrame2, font=('times new roman', 11, 'bold'), width=11, text="Service Speed :", bd=6,bg='light blue',fg='white')
        lblSpeed.grid(row=5, column=0, sticky=W,pady=10)

        e9 = Checkbutton(self.InfoFrame2, width=11,bd=6,fg='green',variable=var9, onvalue=1, offvalue=0, command=chkbutton_value)
        e9.grid(row=5, column=1,pady=20)

        e10 = Checkbutton(self.InfoFrame2, width=11,bd=6,fg='green',variable=var10, onvalue=1, offvalue=0, command=chkbutton_value)
        e10.grid(row=5, column=2,pady=20)

        e11 = Checkbutton(self.InfoFrame2, width=11,bd=6,fg='green',variable=var11, onvalue=1, offvalue=0, command=chkbutton_value)
        e11.grid(row=5, column=3,pady=20)

        e12 = Checkbutton(self.InfoFrame2, width=11,bd=6,fg='green',variable=var12, onvalue=1, offvalue=0, command=chkbutton_value)
        e12.grid(row=5, column=4,pady=20)

        lblQuality = Label(self.InfoFrame2, font=('times new roman', 11, 'bold'), width=11, text="Quality of Food :", bd=6,bg='light blue',fg='white')
        lblQuality.grid(row=6, column=0, sticky=W,pady=10)

        e13 = Checkbutton(self.InfoFrame2, width=11,bd=6,fg='green',variable=var13, onvalue=1, offvalue=0, command=chkbutton_value)
        e13.grid(row=6, column=1,pady=20)

        e14 = Checkbutton(self.InfoFrame2, width=11,bd=6,fg='green',variable=var14, onvalue=1, offvalue=0, command=chkbutton_value)
        e14.grid(row=6, column=2,pady=20)

        e15 = Checkbutton(self.InfoFrame2, width=11,bd=6,fg='green',variable=var15, onvalue=1, offvalue=0, command=chkbutton_value)
        e15.grid(row=6, column=3,pady=20)

        e16 = Checkbutton(self.InfoFrame2, width=11,bd=6,fg='green',variable=var16, onvalue=1, offvalue=0, command=chkbutton_value)
        e16.grid(row=6, column=4,pady=20)

        lblVisit = Label(self.InfoFrame2, font=('times new roman', 11, 'bold'), width=11, text="Visit us again :", bd=6,bg='light blue',fg='white')
        lblVisit.grid(row=7, column=0, sticky=W,pady=10)

        e17 = Checkbutton(self.InfoFrame2, width=11,bd=6,fg='green',variable=var17, onvalue=1, offvalue=0, command=chkbutton_value)
        e17.grid(row=7, column=1,pady=20)

        e18 = Checkbutton(self.InfoFrame2, width=11,bd=6,fg='green',variable=var18, onvalue=1, offvalue=0, command=chkbutton_value)
        e18.grid(row=7, column=2,pady=20)

        e19 = Checkbutton(self.InfoFrame2, width=11,bd=6,fg='green',variable=var19, onvalue=1, offvalue=0, command=chkbutton_value)
        e19.grid(row=7, column=3,pady=20)

        e20 = Checkbutton(self.InfoFrame2, width=11,bd=6,fg='green',variable=var20, onvalue=1, offvalue=0, command=chkbutton_value)
        e20.grid(row=7, column=4,pady=20)

        lblComment = Label(self.InfoFrame2, font=('times new roman', 11, 'bold'), width=11, text="Suggetion :", bd=6,bg='light blue',fg='white')
        lblComment.grid(row=8, column=0, sticky=W,columnspan=4,pady=10)
        lblComment = Entry(self.InfoFrame2, font=('times new roman', 11, 'bold'), width=55, bd=5, justify='left', textvariable=Comment)
        lblComment.grid(row=8, column=1,columnspan=3,pady=10)


        self.btnSubmit = Button(self.IbtFrame2, font=('times new roman', 13, 'bold'),text="Save",fg='green',width=7,command=save_file)
        self.btnSubmit.grid(row=0, column=1,pady=2,padx=25,columnspan=1)

        self.btnRegister = Button(self.IbtFrame2, font=('times new roman', 13, 'bold'),text="Register",width=7,command=Feedback)
        self.btnRegister.grid(row=0, column=0,padx=25,pady=2 )

        self.btnReset = Button(self.IbtFrame2, font=('times new roman', 13, 'bold'),text="Reset",width=7,command=Reset)
        self.btnReset.grid(row=0, column=2,padx=25,pady=2 )

        self.btnClose = Button(self.IbtFrame2, font=('times new roman', 13, 'bold'),text="Drop",fg='red',width=7,command=self.master.destroy)
        self.btnClose.grid(row=0, column=3,pady=2,padx=25)



        
#=======================================================================================================================================
#===================================================================Window4=============================================================
#=======================================================================================================================================

         
class Window4:
    def __init__(self,master):
        self.master = master
        self.master.title("Other Details")
        self.master.geometry("1350x725+0+0")
        self.master.config(bg='ivory')
        self.frame= Frame(self.master,bg='ivory')
        self.frame.pack()

        Top = Frame(self.frame, width=600, height=850, bd=5, relief="raise")
        Top.pack(side=TOP)

        self.fr1 = Frame(self.frame, width=600, height=850, bd=5, relief="raise")
        self.fr1.pack(side=TOP)

        self.fr2 = Frame(self.fr1, width=600, height=850, bd=5, relief="raise" , bg='ivory')
        self.fr2.pack(side=LEFT)

        self.btnFrame = LabelFrame(self.fr2, width=1000,height=600, font=('times new roman', 20, 'bold'),relief='ridge',bg='black',bd=20)
        self.btnFrame.pack(side=BOTTOM)

        lblInfo = Label(Top, font=('times new roman', 25, 'bold'), text="\t\t\t\t       Other Details   \t\t\t\t                "
                , bd=20 , bg='grey',fg='black', anchor='w')
        lblInfo.grid(row=0, column=1,columnspan=3,pady=10)

        def Open_mail():
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

        self.btnMail = Button (self.btnFrame,font=('times new roman', 14, 'bold'),text="Go to Gmail",width=14,command=Open_mail)
        self.btnMail.grid(row=2, column=1,pady=20,padx=8)
        
        self.btnEnd = Button(self.btnFrame, font=('times new roman', 14, 'bold'),text="Back to Home",width=14,command=self.master.destroy)
        self.btnEnd.grid(row=2, column=2,pady=20,padx=8,columnspan=3)
        
#=======================================================================================================================================
#===================================================================Window3=============================================================
#=======================================================================================================================================

class Window3:
    def __init__(self,master):
        self.master = master
        self.master.title("Employee Information")
        self.master.geometry("1350x725+0+0")
        self.master.config(bg='ivory')
        self.frame= Frame(self.master,bg='brown')
        self.frame.pack()

        Tops = Frame(self.frame, width=600, height=850, bd=5, relief="raise")
        Tops.pack(side=TOP)

        fa1 = Frame(self.frame, width=600, height=850, bd=5, relief="raise", bg='White')
        fa1.pack(side=TOP)

        f1aa = Frame(fa1, width=600, height=850, bd=5, relief="raise" , bg='light blue')
        f1aa.pack(side=LEFT)

        fa2 = Frame(self.frame, width=600, height=850, bd=5, relief="raise", bg='White')
        fa2.pack(side=BOTTOM)

        f1ab = Frame(fa2, width=600, height=850, bd=5, relief="raise" , bg='light green')
        f1ab.pack(side=LEFT)


        
        Tops.configure(background='brown')


# ============================================================HEADING===================================================
        lblInfo = Label(Tops, font=('times new roman', 25, 'bold'), text="\t\t\t\t       Employee Information   \t\t \t                "
                , bd=20 , bg='black',fg='white', anchor='w')
        lblInfo.grid(row=0, column=0,columnspan=2,pady=10)



# ============================================================1st FRAME INFOMATION======================================
        lblSr = Label(f1aa, font=('times new roman', 12, 'bold'), width=30, text="Sr No. ", bd=2 , bg='ivory',fg='maroon')
        lblSr.grid(row=0, column=0, sticky=W,columnspan=1,pady=10)


        lblPost = Label(f1aa, font=('times new roman', 12, 'bold'), width=30, text="Post", bd=2 , bg='ivory',fg='maroon')
        lblPost.grid(row=0, column=1, sticky=W)


        lblSalary = Label(f1aa, font=('times new roman', 12, 'bold'), width=30, text="Salary", bd=2 , bg='ivory',fg='maroon')
        lblSalary.grid(row=0, column=2, sticky=W)


        lblTime = Label(f1aa, font=('times new roman', 12, 'bold'), width=30, text="Working Time", bd=2 , bg='ivory',fg='maroon')
        lblTime.grid(row=0, column=3, sticky=W)

        lblBonus = Label(f1aa, font=('times new roman', 12, 'bold'), width=30, text="Vacation Bonus", bd=2 , bg='ivory',fg='maroon')
        lblBonus.grid(row=0, column=4, sticky=W)
#===========================================================================================================================

        lblSr1 = Label(f1aa, font=('times new roman', 12, 'bold'), width=29, text="01", bd=5 , bg='ivory')
        lblSr1.grid(row=1, column=0, sticky=W,columnspan=1,pady=10)

        lblPost1 = Label(f1aa, font=('times new roman', 12, 'bold'), width=29, text="Cooke 1", bd=5 , bg='ivory')
        lblPost1.grid(row=1, column=1, sticky=W,columnspan=1,pady=10)

        lblSalary1 = Label(f1aa, font=('times new roman', 12, 'bold'), width=29, text="7000", bd=5 , bg='ivory')
        lblSalary1.grid(row=1, column=2, sticky=W,columnspan=1,pady=10)


        lblTime1 = Label(f1aa, font=('times new roman', 12, 'bold'), width=29, text="12:00 pm to 8:00 pm", bd=5 , bg='ivory')
        lblTime1.grid(row=1, column=3, sticky=W,columnspan=1,pady=10)


        lblVacation1 = Label(f1aa, font=('times new roman', 12, 'bold'), width=29, text="2000", bd=5 , bg='ivory')
        lblVacation1.grid(row=1, column=4, sticky=W,columnspan=1,pady=10)


#===========================================================================================================================

        lblSr2 = Label(f1aa, font=('times new roman', 12, 'bold'), width=29, text="02", bd=5 , bg='ivory')
        lblSr2.grid(row=2, column=0, sticky=W,columnspan=1,pady=10)

        lblPost2 = Label(f1aa, font=('times new roman', 12, 'bold'), width=29, text="Cooke 2", bd=5 , bg='ivory')
        lblPost2.grid(row=2, column=1, sticky=W)

        lblSalary2 = Label(f1aa, font=('times new roman', 12, 'bold'), width=29, text="7000 ", bd=5 , bg='ivory')
        lblSalary2.grid(row=2, column=2, sticky=W)

        lblTime2 = Label(f1aa, font=('times new roman', 12, 'bold'), width=29, text="12:00 pm to 8:00 pm ", bd=5 , bg='ivory')
        lblTime2.grid(row=2, column=3, sticky=W)

        
        lblVacation2 = Label(f1aa, font=('times new roman', 12, 'bold'), width=29, text="2000", bd=5 , bg='ivory')
        lblVacation2.grid(row=2, column=4, sticky=W)

#===========================================================================================================================

        lblSr3 = Label(f1aa, font=('times new roman', 12, 'bold'), width=29, text="03", bd=5 , bg='ivory')
        lblSr3.grid(row=3, column=0, sticky=W,columnspan=1,pady=10)

        lblPost3 = Label(f1aa, font=('times new roman', 12, 'bold'), width=29, text="Waiter 1", bd=5 , bg='ivory')
        lblPost3.grid(row=3, column=1, sticky=W)

        lblSalary3 = Label(f1aa, font=('times new roman', 12, 'bold'), width=29, text="5000", bd=5 , bg='ivory')
        lblSalary3.grid(row=3, column=2, sticky=W)

        lblTime3 = Label(f1aa, font=('times new roman', 12, 'bold'), width=29, text="12:30 pm  to  8:00 pm ", bd=5 , bg='ivory')
        lblTime3.grid(row=3, column=3, sticky=W)

        lblVaction3 = Label(f1aa, font=('times new roman', 12, 'bold'), width=29, text="1500", bd=5 , bg='ivory')
        lblVaction3.grid(row=3, column=4, sticky=W)


#===========================================================================================================================

        lblSr4 = Label(f1aa, font=('times new roman', 12, 'bold'), width=29, text="04", bd=5 , bg='ivory')
        lblSr4.grid(row=4, column=0, sticky=W,columnspan=1,pady=10)

        lblPost4 = Label(f1aa, font=('times new roman', 12, 'bold'), width=29, text="Waiter 2", bd=5 , bg='ivory')
        lblPost4.grid(row=4, column=1, sticky=W,columnspan=1,pady=10)

        lblSalary4 = Label(f1aa, font=('times new roman', 12, 'bold'), width=29, text="5000", bd=5 , bg='ivory')
        lblSalary4.grid(row=4, column=2, sticky=W,columnspan=1,pady=10)


        lblTime4 = Label(f1aa, font=('times new roman', 12, 'bold'), width=29, text="12:30 pm  to  8:00 pm ", bd=5 , bg='ivory')
        lblTime4.grid(row=4, column=3, sticky=W,columnspan=1,pady=10)

        lblVacation4 = Label(f1aa, font=('times new roman', 12, 'bold'), width=29, text="1500", bd=5 , bg='ivory')
        lblVacation4.grid(row=4, column=4, sticky=W,columnspan=1,pady=10)

        self.btn2 = Button(f1ab, font=('times new roman', 15, 'bold'),text="Back to Home",fg='red',width=17,command=self.master.destroy)
        self.btn2.grid(row=9, column=1,pady=10,padx=600,columnspan=5)

       







        
#=======================================================================================================================================
#===================================================================Window2=============================================================
#=======================================================================================================================================

class Window2:
    def __init__(self,master):
        self.master = master
        self.master.title("Billing Window")
        self.master.geometry("1350x725+0+0")
        self.master.config(bg='teal')
        self.frame= Frame(self.master,bg='teal')
        self.frame.pack()


        Tops = Frame(self.frame, bd=8, relief="raise")
        Tops.pack(side=TOP)

        fa1 = Frame(self.frame, bd=8, relief="raise")
        fa1.pack(side=TOP)

        f1 = Frame(self.frame, bd=8, relief="raise")
        f1.pack(side=LEFT)

        f2 = Frame(self.frame, bd=8, relief="raise")
        f2.pack(side=RIGHT)

        f1a = Frame(f1,  bd=8, relief="raise")
        f1a.pack(side=TOP)

        f2a = Frame(f1, bd=5, relief="raise")
        f2a.pack(side=BOTTOM)

        ft2 = Frame(f2, bd=10, relief="raise")
        ft2.pack(side=TOP)

        fb2 = Frame(f2,  bd=10, relief="raise")
        fb2.pack(side=BOTTOM)

        f1aa = Frame(f1a, bd=10, relief="raise")
        f1aa.pack(side=LEFT)

        f1ab = Frame(f1a,  bd=10, relief="raise")
        f1ab.pack(side=RIGHT)

        f2aa = Frame(f2a, bd=10, relief="raise")
        f2aa.pack(side=LEFT)

        f2ab = Frame(f2a, bd=10, relief="raise")
        f2ab.pack(side=RIGHT)

        Tops.configure(background='brown')
        f1.configure(background='black')
        f2.configure(background='black')
        fa1.configure(background="black")
# ============================================================HEADING===================================================
        lblInfo = Label(Tops, font=('times new roman', 40, 'bold'), text="\t \t       * Coffee House *   \t \t                "
                , bd=10, anchor='w')
        lblInfo.grid(row=0, column=1)


# =======================================================METHOD=========================================================
        def iPrint():
            q = txtReceipt.get("1.0","end-1c")
            filename = tempfile.mktemp(".txt")
            open (filename,"w").write(q)
            os.startfile(filename,"print")


        def CostofItem():
            Item1 = float(E_Capachino.get())
            Item2 = float(E_ValeCoffee.get())
            Item3 = float(E_AmericanCoffee.get())
            Item4 = float(E_AfricanCoffee.get())
            Item5 = float(E_ColdCoffee.get())
            Item6 = float(E_HotCoffee.get())
            Item7 = float(E_ChochlateCoffee.get())
            Item8 = float(E_MasalaMaggi.get())
            Item9 = float(E_CheeseMaggi.get())

            Item10 = float(E_MasalaRice.get())

            Item11 = float(E_FriedRice.get())
            Item12 = float(E_VegNoodles.get())
            Item13 = float(E_ManchurianNoodles.get())
            Item14 = float(E_VegManchurain.get())
            Item15 = float(E_ManchurianRice.get())
            Item16 = float(E_Pizza.get())
            Item17 = float(E_Sandwich.get())
            Item18 = float(E_French_Fries.get())

            PriceofCoffee = (Item1 * 40) + (Item2 * 50) + (Item3 * 60) + (Item4 * 50) + (Item5 * 45) + (Item6 * 45) + (
                Item7 * 60)
            PriceofFastFood = (Item8 * 30) + (Item9 * 40) + (Item16 * 110) + (Item17 * 45) + (Item18 * 50)
            PriceofChinise = (Item10 * 60) + (Item11 * 50) + (Item12 * 40) + (Item13 * 45) + (Item14 * 40) + (Item15 * 40)

            CoffeePrice = "Rs.", str('%.2f' % (PriceofCoffee))
            FastFoodPrice = "Rs.", str('%.2f' % (PriceofFastFood))
            ChinisePrice = "Rs.", str('%.2f' % (PriceofChinise))
            CostofCoffee.set(CoffeePrice)
            CostofFastFood.set(FastFoodPrice)
            CostofChinise.set(ChinisePrice)
            SC = "Rs.", str('%2f' % (4.59))
            ServiceCharge.set(SC)

            Tax = "Rs.", str('%.2f' % (PriceofCoffee + PriceofFastFood + PriceofChinise + 4.59))
            PaidTax.set(Tax)
            # TT = ((PriceofCoffee + PriceofFastFood + PriceofChinise + 1.59)*0.15)
            TC = "Rs.", str('%.2f' % (PriceofCoffee + PriceofFastFood + PriceofChinise + 4.59))
            TotalCost.set(TC)


        def Reset():
            PaidTax.set("")
            TotalCost.set("")
            CostofCoffee.set("")
            CostofFastFood.set("")
            CostofChinise.set("")
            ServiceCharge.set("")

            Name.set("")
            Emp.set("")
            tb.set("")

            txtReceipt.delete("1.0", END)

            E_Capachino.set("0")
            E_ValeCoffee.set("0")
            E_AmericanCoffee.set("0")
            E_AfricanCoffee.set("0")
            E_ColdCoffee.set("0")
            E_HotCoffee.set("0")
            E_ChochlateCoffee.set("0")
            E_MasalaMaggi.set("0")
            E_CheeseMaggi.set("0")

            E_MasalaRice.set("0")
            E_ManchurianRice.set("0")
            E_FriedRice.set("0")
            E_VegNoodles.set("0")
            E_ManchurianNoodles.set("0")
            E_VegManchurain.set("0")
            E_Pizza.set("0")
            E_Sandwich.set("0")
            E_French_Fries.set("0")

            var1.set(0)
            var2.set(0)
            var3.set(0)
            var4.set(0)
            var5.set(0)
            var6.set(0)
            var7.set(0)
            var8.set(0)
            var9.set(0)
            var10.set(0)
            var11.set(0)
            var12.set(0)
            var13.set(0)
            var14.set(0)
            var15.set(0)
            var16.set(0)
            var17.set(0)
            var18.set(0)
    
            txtCapchino.configure(state=DISABLED)
            txtValeCoffee.configure(state=DISABLED)
            txtAmericanCoffee.configure(state=DISABLED)
            txtAfricanCoffee.configure(state=DISABLED)
            txtColdCoffee.configure(state=DISABLED)
            txtHotCoffee.configure(state=DISABLED)
            txtChochlateCoffee.configure(state=DISABLED)
            txtMasalaMaggi.configure(state=DISABLED)
            txtCheeseMaggi.configure(state=DISABLED)
            txtVegNoodles.configure(state=DISABLED)
            txtManchurianNoodles.configure(state=DISABLED)
            txtMasalaRice.configure(state=DISABLED)
            txtFriedRice.configure(state=DISABLED)
            txtManchurianRice.configure(state=DISABLED)
            txtPizza.configure(state=DISABLED)
            txtSandwich.configure(state=DISABLED)
            txtFrench_Fries.configure(state=DISABLED)


        def Receipt():
            txtReceipt.delete("1.0", END)
            x = random.randint(10908, 500876)
            randomRef = str(x)
            Receipt_Ref.set("BILL" + randomRef)

            txtReceipt.insert(END, '\t********** THANKS FOR VISIT COFFEE HOUSE **********\t'  + "\n\n")
            txtReceipt.insert(END, 'Receipt Ref:\t\t\t' + Receipt_Ref.get() + '\t\t' + DateofOrder.get() + "\n")
            txtReceipt.insert(END, 'Customers Good Name \t:\t\t' + lblName.get() + "\nEmployee Name \t\t        :"'\t' + lblEmp.get() + "\n")
            txtReceipt.insert(END, 'Table No. \t\t        :\t' +lbltb.get()+"\n\n")
            txtReceipt.insert(END, 'Item\t\t\t\t\t' + "Cost of Items \n\n")
            txtReceipt.insert(END, 'Capachino\t\t\t\t\t' + E_Capachino.get() + "\n")
            txtReceipt.insert(END, 'Vale_Coffee\t\t\t\t\t' + E_ValeCoffee.get() + "\n")
            txtReceipt.insert(END, 'American_Coffee\t\t\t\t\t' + E_AmericanCoffee.get() + "\n")
            txtReceipt.insert(END, 'African_Coffee\t\t\t\t\t' + E_AfricanCoffee.get() + "\n")
            txtReceipt.insert(END, 'Cold_Coffee\t\t\t\t\t' + E_ColdCoffee.get() + "\n")
            txtReceipt.insert(END, 'Hot_Coffee\t\t\t\t\t' + E_HotCoffee.get() + "\n")
            txtReceipt.insert(END, 'Chochlate_Coffee\t\t\t\t\t' + E_ChochlateCoffee.get() + "\n")
            txtReceipt.insert(END, 'Masala_Maggi\t\t\t\t\t' + E_MasalaMaggi.get() + "\n")
            txtReceipt.insert(END, 'Cheese_Maggi\t\t\t\t\t' + E_CheeseMaggi.get() + "\n")
            txtReceipt.insert(END, 'Masala_Rice\t\t\t\t\t' + E_MasalaRice.get() + "\n")
            txtReceipt.insert(END, 'Fried_Rice\t\t\t\t\t' + E_FriedRice.get() + "\n")
            txtReceipt.insert(END, 'Veg_Noodles\t\t\t\t\t' + E_VegNoodles.get() + "\n")
            txtReceipt.insert(END, 'Manchurian_Noodles\t\t\t\t\t' + E_ManchurianNoodles.get() + "\n")
            txtReceipt.insert(END, 'Veg_Manchurian\t\t\t\t\t' + E_VegManchurain.get() + "\n")
            txtReceipt.insert(END, 'Manchurian_Rice\t\t\t\t\t' + E_ManchurianRice.get() + "\n")
            txtReceipt.insert(END, 'Pizza\t\t\t\t\t' + E_Pizza.get() + "\n")
            txtReceipt.insert(END, 'Sandwich\t\t\t\t\t' + E_Sandwich.get() + "\n")
            txtReceipt.insert(END, 'French_Fries\t\t\t\t\t' + E_French_Fries.get() + "\n")
            txtReceipt.insert(END,
                              'Cost of Coffee\t\t\t\t\t' + CostofCoffee.get() + "\n" + 'Tax Paid:\t\t\t\t\t' + PaidTax.get() + "\n")
            txtReceipt.insert(END, 'Cost of Fast_Food\t\t\t\t\t' + CostofFastFood.get() + "\n")
            txtReceipt.insert(END, 'Cost of Chinise\t\t\t\t\t' + CostofChinise.get() + "\n")
            txtReceipt.insert(END,
                              'Service Charge\t\t\t\t\t' + ServiceCharge.get() + "\n" + 'Total Cost:\t\t\t\t\t' + TotalCost.get() + "\n")
        

# ===========================================================CALCULATOR=================================================

        def chkbutton_value():
            if (var1.get() == 1):
                txtCapchino.configure(state=NORMAL)
            elif var1.get() == 0:
                txtCapchino.configure(state=DISABLED)
                E_Capachino.set("0")
            if (var2.get() == 1):
                txtValeCoffee.configure(state=NORMAL)
            elif var2.get() == 0:
                txtValeCoffee.configure(state=DISABLED)
                E_ValeCoffee.set("0")
            if (var3.get() == 1):
                txtAmericanCoffee.configure(state=NORMAL)
            elif var3.get() == 0:
                txtAmericanCoffee.configure(state=DISABLED)
                E_AmericanCoffee.set("0")
            if (var4.get() == 1):
                txtAfricanCoffee.configure(state=NORMAL)
            elif var4.get() == 0:
                txtAfricanCoffee.configure(state=DISABLED)
                E_AfricanCoffee.set("0")
            if (var5.get() == 1):
                txtColdCoffee.configure(state=NORMAL)
            elif var5.get() == 0:
                txtColdCoffee.configure(state=DISABLED)
                E_ColdCoffee.set("0")
            if (var6.get() == 1):
                txtHotCoffee.configure(state=NORMAL)
            elif var6.get() == 0:
                txtHotCoffee.configure(state=DISABLED)
                E_HotCoffee.set("0")
            if (var7.get() == 1):
                txtChochlateCoffee.configure(state=NORMAL)
            elif var7.get() == 0:
                txtChochlateCoffee.configure(state=DISABLED)
                E_ChochlateCoffee.set("0")
            if (var8.get() == 1):
                txtMasalaMaggi.configure(state=NORMAL)
            elif var8.get() == 0:
                txtMasalaMaggi.configure(state=DISABLED)
                E_MasalaMaggi.set("0")
            if (var9.get() == 1):
                txtCheeseMaggi.configure(state=NORMAL)
            elif var9.get() == 0:
                txtCheeseMaggi.configure(state=DISABLED)
                E_CheeseMaggi.set("0")
            if (var10.get() == 1):
                txtMasalaRice.configure(state=NORMAL)
            elif var10.get() == 0:
                txtMasalaRice.configure(state=DISABLED)
                E_MasalaRice.set("0")
            if (var11.get() == 1):
                txtFriedRice.configure(state=NORMAL)
            elif var11.get() == 0:
                txtFriedRice.configure(state=DISABLED)
                E_FriedRice.set("0")
            if (var12.get() == 1):
                txtVegNoodles.configure(state=NORMAL)
            elif var12.get() == 0:
                txtVegNoodles.configure(state=DISABLED)
                E_VegNoodles.set("0")
            if (var13.get() == 1):
                txtManchurianNoodles.configure(state=NORMAL)
            elif var13.get() == 0:
                txtManchurianNoodles.configure(state=DISABLED)
                E_ManchurianNoodles.set("0")
            if (var14.get() == 1):
                txtVegManchurian.configure(state=NORMAL)
            elif var14.get() == 0:
                txtVegManchurian.configure(state=DISABLED)
                E_VegManchurain.set("0")
            if (var15.get() == 1):
                txtManchurianRice.configure(state=NORMAL)
            elif var15.get() == 0:
                txtManchurianRice.configure(state=DISABLED)
                E_ManchurianRice.set("0")
            if (var16.get() == 1):
                txtPizza.configure(state=NORMAL)
            elif var16.get() == 0:
                txtPizza.configure(state=DISABLED)
                E_Pizza.set("0")
            if (var17.get() == 1):
                txtSandwich.configure(state=NORMAL)
            elif var17.get() == 0:
                txtSandwich.configure(state=DISABLED)
                E_Sandwich.set("0")
            if (var18.get() == 1):
                txtFrench_Fries.configure(state=NORMAL)
            elif var18.get() == 0:
                txtFrench_Fries.configure(state=DISABLED)
                E_French_Fries.set("0")


# ============================================================VARIABLE==================================================
        var1 = IntVar()
        var2 = IntVar()
        var3 = IntVar()
        var4 = IntVar()
        var5 = IntVar()
        var6 = IntVar()
        var7 = IntVar()
        var8 = IntVar()
        var9 = IntVar()
        var10 = IntVar()
        var11 = IntVar()
        var12 = IntVar()
        var13 = IntVar()
        var14 = IntVar()
        var15 = IntVar()
        var16 = IntVar()
        var17 = IntVar()
        var18 = IntVar()

        DateofOrder = StringVar()

        Receipt_Ref = StringVar()
        PaidTax = StringVar()
        TotalCost = StringVar()
        CostofCoffee = StringVar()
        CostofFastFood = StringVar()
        CostofChinise = StringVar()
        ServiceCharge = StringVar()
        Name = StringVar()
        Emp = StringVar()
        tb = IntVar()

        E_Capachino = StringVar()
        E_ValeCoffee = StringVar()
        E_AmericanCoffee = StringVar()
        E_AfricanCoffee = StringVar()
        E_ColdCoffee = StringVar()
        E_HotCoffee = StringVar()
        E_ChochlateCoffee = StringVar()
        E_MasalaMaggi = StringVar()
        E_CheeseMaggi = StringVar()

        E_MasalaRice = StringVar()
        E_ManchurianRice = StringVar()
        E_FriedRice = StringVar()
        E_VegNoodles = StringVar()
        E_ManchurianNoodles = StringVar()
        E_VegManchurain = StringVar()
        E_Pizza = StringVar()
        E_Sandwich = StringVar()
        E_French_Fries = StringVar()

        E_Capachino.set("0")
        E_ValeCoffee.set("0")
        E_AmericanCoffee.set("0")
        E_AfricanCoffee.set("0")
        E_ColdCoffee.set("0")
        E_HotCoffee.set("0")
        E_ChochlateCoffee.set("0")
        E_MasalaMaggi.set("0")
        E_CheeseMaggi.set("0")

        E_MasalaRice.set("0")
        E_ManchurianRice.set("0")
        E_FriedRice.set("0")
        E_VegNoodles.set("0")
        E_ManchurianNoodles.set("0")
        E_VegManchurain.set("0")
        E_Pizza.set("0")
        E_Sandwich.set("0")
        E_French_Fries.set("0")

        DateofOrder.set(time.strftime("%d/%m/%y    %H:%M:%S"))

# =====================================================COFFEE===========================================================
        lblCoffee = Label(f1aa, font=('times new roman', 11, 'bold'), width=31, text="COFFEE : \t\t Quantity : ", bd=6)
        lblCoffee.grid(row=0, column=0, sticky=W)

        Capachino = Checkbutton(f1aa, text="Capachino \t", variable=var1, onvalue=1, offvalue=0,
                                font=('times new roman', 11, 'bold', 'italic'), command=chkbutton_value, width=22).grid(row=1,
                                                                                                                sticky=W)
        ValeCoffee = Checkbutton(f1aa, text="Vale Coffee \t", variable=var2, onvalue=1, offvalue=0,
                                 font=('times new roman', 11, 'bold', 'italic'), command=chkbutton_value, width=22).grid(row=2,
                                                                                                                 sticky=W)
        AmericanCoffee = Checkbutton(f1aa, text="American Coffee \t", variable=var3, onvalue=1, offvalue=0,
                                     font=('times new roman', 11, 'bold', 'italic'), command=chkbutton_value, width=22).grid(
            row=3, sticky=W)
        AfricanCoffee = Checkbutton(f1aa, text="African Coffee \t", variable=var4, onvalue=1, offvalue=0,
                                    font=('times new roman', 11, 'bold', 'italic'), command=chkbutton_value, width=22).grid(
            row=4, sticky=W)
        ColdCoffee = Checkbutton(f1aa, text="Cold Coffee \t", variable=var5, onvalue=1, offvalue=0,
                                 font=('times new roman', 11, 'bold', 'italic'), command=chkbutton_value, width=22).grid(row=5,
                                                                                                                 sticky=W)
        HotCoffee = Checkbutton(f1aa, text="Hot Coffee \t", variable=var6, onvalue=1, offvalue=0,
                                font=('times new roman', 11, 'bold', 'italic'), command=chkbutton_value, width=22).grid(row=6,
                                                                                                                sticky=W)
        ChochlateCoffee = Checkbutton(f1aa, text="Chochlate Coffee  \t", variable=var7, onvalue=1, offvalue=0,
                                      font=('times new roman', 11, 'bold', 'italic'), command=chkbutton_value, width=22).grid(
            row=7, sticky=W)

# =======================================================MAGGI==========================================================
        lblMaggi = Label(f1aa, font=('times new roman', 11, 'bold'), width=31, text="MAGGI : \t\t\t ", bd=6)
        lblMaggi.grid(row=8, column=0, sticky=W)

        MasalaMaggi = Checkbutton(f1aa, text="Masala Maggi \t", variable=var8, onvalue=1, offvalue=0,
                                  font=('times new roman', 11, 'bold', 'italic'), command=chkbutton_value, width=22).grid(row=9,
                                                                                                                  sticky=W)
        CheeseMaggi = Checkbutton(f1aa, text="Cheese Maggi \t", variable=var9, onvalue=1, offvalue=0,
                                  font=('times new roman', 11, 'bold', 'italic'), command=chkbutton_value, width=22).grid(
            row=10, sticky=W)

# ==================================================CHINESE_FOOD========================================================
        lblChinise = Label(f1ab, font=('times new roman', 11, 'bold'), width=31, text="CHINESE_FOOD : \t    Quantity :", bd=6)
        lblChinise.grid(row=0, column=0, sticky=W)

        Rice = Checkbutton(f1ab, text="Masala Rice \t", variable=var10, onvalue=1, offvalue=0,
                           font=('times new roman', 11, 'bold', 'italic'), command=chkbutton_value, width=22).grid(row=1,
                                                                                                           sticky=W)
        FriedRice = Checkbutton(f1ab, text="Fried Rice \t", variable=var11, onvalue=1, offvalue=0,
                                font=('times new roman', 11, 'bold', 'italic'), command=chkbutton_value, width=22).grid(row=2,
                                                                                                                sticky=W)
        Noodles = Checkbutton(f1ab, text="Veg Noodles \t", variable=var12, onvalue=1, offvalue=0,
                              font=('times new roman', 11, 'bold', 'italic'), command=chkbutton_value, width=22).grid(row=3,
                                                                                                              sticky=W)
        ManchurianNoodles = Checkbutton(f1ab, text="Manchurian Noodles \t", variable=var13, onvalue=1, offvalue=0,
                                        font=('times new roman', 11, 'bold', 'italic'), command=chkbutton_value, width=29).grid(
            row=4, sticky=W)
        VegManchurian = Checkbutton(f1ab, text="Veg Manchurian \t", variable=var14, onvalue=1, offvalue=0,
                                    font=('times new roman', 11, 'bold', 'italic'), command=chkbutton_value, width=22).grid(
            row=5, sticky=W)
        ManchurianRice = Checkbutton(f1ab, text="Manchurian_Rice \t", variable=var15, onvalue=1, offvalue=0,
                             font=('times new roman', 11, 'bold', 'italic'), command=chkbutton_value, width=22).grid(
            row=6, sticky=W)

# ==========================================================FAST_FOOD===================================================
        lblFastFood = Label(f1ab, font=('times new roman', 11, 'bold'), width=31, text="SPECIAL_ITEMS : \t\t", bd=6)
        lblFastFood.grid(row=7, column=0, sticky=W)

        Pizza = Checkbutton(f1ab, text="Pizza \t", variable=var16, onvalue=1, offvalue=0,
                            font=('times new roman', 11, 'bold', 'italic'), command=chkbutton_value, width=15).grid(row=8,
                                                                                                                    sticky=W)
        Sandwich = Checkbutton(f1ab, text="Sandwich \t", variable=var17, onvalue=1, offvalue=0,
                               font=('times new roman', 11, 'bold', 'italic'), command=chkbutton_value, width=22).grid(row=9,
                                                                                                                       sticky=W)
        French_Fries = Checkbutton(f1ab, text="French Fries \t", variable=var18, onvalue=1, offvalue=0,
                              font=('times new roman', 11, 'bold', 'italic'), command=chkbutton_value, width=22).grid(row=10,
                                                                                                                      sticky=W)

# ===========================================ENTER WIDGET FOR COFFEE & MAGGI============================================
        txtCapchino = Entry(f1aa, font=('times new roman', 11, 'bold'), bd=8, width=6, justify='left',
                            textvariable=E_Capachino, state=DISABLED)
        txtCapchino.grid(row=1, column=1)

        txtValeCoffee = Entry(f1aa, font=('times new roman', 11, 'bold'), bd=8, width=6, justify='left',
                              textvariable=E_ValeCoffee, state=DISABLED)
        txtValeCoffee.grid(row=2, column=1)
        
        txtAmericanCoffee = Entry(f1aa, font=('times new roman', 11, 'bold'), bd=8, width=6, justify='left',
                                  textvariable=E_AmericanCoffee, state=DISABLED)
        txtAmericanCoffee.grid(row=3, column=1)

        txtAfricanCoffee = Entry(f1aa, font=('times new roman', 11, 'bold'), bd=8, width=6, justify='left',
                                 textvariable=E_AfricanCoffee, state=DISABLED)
        txtAfricanCoffee.grid(row=4, column=1)

        txtColdCoffee = Entry(f1aa, font=('times new roman', 11, 'bold'), bd=8, width=6, justify='left',
                              textvariable=E_ColdCoffee, state=DISABLED)
        txtColdCoffee.grid(row=5, column=1)

        txtHotCoffee = Entry(f1aa, font=('times new roman', 11, 'bold'), bd=8, width=6, justify='left',
                             textvariable=E_HotCoffee, state=DISABLED)
        txtHotCoffee.grid(row=6, column=1)

        txtChochlateCoffee = Entry(f1aa, font=('times new roman', 11, 'bold'), bd=8, width=6, justify='left',
                                   textvariable=E_ChochlateCoffee, state=DISABLED)
        txtChochlateCoffee.grid(row=7, column=1)

        txtMasalaMaggi = Entry(f1aa, font=('times new roman', 11, 'bold'), bd=8, width=6, justify='left',
                               textvariable=E_MasalaMaggi, state=DISABLED)
        txtMasalaMaggi.grid(row=9, column=1)

        txtCheeseMaggi = Entry(f1aa, font=('times new roman', 11, 'bold'), bd=8, width=6, justify='left',
                               textvariable=E_CheeseMaggi, state=DISABLED)
        txtCheeseMaggi.grid(row=10, column=1)

# =============================ENTER WIDGET FOR CHINESE_FOOD & FAST_FOOD==========================================

        txtMasalaRice = Entry(f1ab, font=('times new roman', 11, 'bold'), bd=8, width=6, justify='left',
                              textvariable=E_MasalaRice, state=DISABLED)
        txtMasalaRice.grid(row=1, column=1)

        txtFriedRice = Entry(f1ab, font=('times new roman', 11, 'bold'), bd=8, width=6, justify='left',
                             textvariable=E_FriedRice, state=DISABLED)
        txtFriedRice.grid(row=2, column=1)

        txtVegNoodles = Entry(f1ab, font=('times new roman', 11, 'bold'), bd=8, width=6, justify='left',
                              textvariable=E_VegNoodles, state=DISABLED)
        txtVegNoodles.grid(row=3, column=1)

        txtManchurianNoodles = Entry(f1ab, font=('times new roman', 11, 'bold'), bd=8, width=6, justify='left',
                                     textvariable=E_ManchurianNoodles, state=DISABLED)
        txtManchurianNoodles.grid(row=4, column=1)

        txtVegManchurian = Entry(f1ab, font=('times new roman', 11, 'bold'), bd=8, width=6, justify='left',
                                 textvariable=E_VegManchurain, state=DISABLED)
        txtVegManchurian.grid(row=5, column=1)

        txtManchurianRice = Entry(f1ab, font=('times new roman', 11, 'bold'), bd=8, width=6, justify='left',
                                  textvariable=E_ManchurianRice, state=DISABLED)
        txtManchurianRice.grid(row=6, column=1)

        txtPizza = Entry(f1ab, font=('times new roman', 11, 'bold'), bd=8, width=6, justify='left',
                         textvariable=E_Pizza, state=DISABLED)
        txtPizza.grid(row=8, column=1)

        txtSandwich = Entry(f1ab, font=('times new roman', 11, 'bold'), bd=8, width=6, justify='left',
                            textvariable=E_Sandwich, state=DISABLED)
        txtSandwich.grid(row=9, column=1)

        txtFrench_Fries = Entry(f1ab, font=('times new roman', 11, 'bold'), bd=8, width=6, justify='left',
                           textvariable=E_French_Fries, state=DISABLED)
        txtFrench_Fries.grid(row=10, column=1)

# ==================================================COST_OF_ITEM (f2aa)=================================================
        lblCostofCoffee = Label(f2aa, font=('times new roman', 10, 'bold'), width=22, text="Cost of Coffee", bd=8)
        lblCostofCoffee.grid(row=0, column=0)
        lblCostofCoffee = Entry(f2aa, font=('times new roman', 11, 'bold'), width=22, bd=8, justify='left',
                                textvariable=CostofCoffee)
        lblCostofCoffee.grid(row=0, column=1)

        lblCostofFastFood = Label(f2aa, font=('times new roman', 10, 'bold'), width=22, text="Cost of Fast_Food", bd=8)
        lblCostofFastFood.grid(row=1, column=0, sticky=W)
        lblCostofFastFood = Entry(f2aa, font=('times new roman', 11, 'bold'), width=22, bd=8, justify='left',
                          textvariable=CostofFastFood)
        lblCostofFastFood.grid(row=1, column=1, sticky=W)

        lblCostofChinise = Label(f2aa, font=('times new roman', 10, 'bold'), width=22, text="Cost of Chinise", bd=8)
        lblCostofChinise.grid(row=2, column=0, sticky=W)
        lblCostofChinise = Entry(f2aa, font=('times new roman', 11, 'bold'), width=22, bd=8, justify='left',
                         textvariable=CostofChinise)
        lblCostofChinise.grid(row=2, column=1, sticky=W)

        lblServiceCharge = Label(f2ab, font=('times new roman', 10, 'bold'), width=22, text="Service Charge", bd=8)
        lblServiceCharge.grid(row=0, column=0, sticky=W)
        lblServiceCharge = Entry(f2ab, font=('times new roman', 11, 'bold'), width=22, bd=8, justify='left',
                         textvariable=ServiceCharge)
        lblServiceCharge.grid(row=0, column=1, sticky=W)

# ================================================PAYMENT_INFORMATION (f2ab)============================================
        lblPaidTax = Label(f2ab, font=('times new roman', 10, 'bold'), width=22, text="Paid Tax", bd=8)
        lblPaidTax.grid(row=1, column=0, sticky=W)
        lblPaidTax = Entry(f2ab, font=('times new roman', 11, 'bold'), width=22, bd=8, justify='left', textvariable=PaidTax)
        lblPaidTax.grid(row=1, column=1, sticky=W)

        lblTotalCost = Label(f2ab, font=('times new roman', 10, 'bold'), width=22, text="Total Cost", bd=8)
        lblTotalCost.grid(row=2, column=0, sticky=W)
        lblTotalCost = Entry(f2ab, font=('times new roman', 11, 'bold'), width=22, bd=8, justify='left', textvariable=TotalCost)
        lblTotalCost.grid(row=2, column=1, sticky=W)

# =========================================================INFORMATION (ft2)============================================
        lblReceipt = Label(ft2, font=('times new roman', 14, 'bold'), text="Receipt :", bd=2, anchor='w')
        lblReceipt.grid(row=0, column=0, sticky=W)  # 16
        txtReceipt = Text(ft2, font=('times new roman', 11, 'bold'), bd=5, width=75,height=25)
        txtReceipt.grid(row=1, column=0)  # 21/02/19


# ========================================================BUTTON(fb2)===================================================
        btnTotal = Button(fb2, padx=10, pady=4, bd=4, fg="black", font=('times new roman', 12, 'bold',), width=8,
                          text="Total", command=CostofItem).grid(row=0, column=0)

        btnReceipt = Button(fb2, padx=10, pady=4, bd=4, fg="black", font=('times new roman', 12, 'bold'), width=9,
                            text="Receipt", command=Receipt).grid(row=0, column=1)
        
        btnPrint = Button(fb2, padx=10, pady=4, bd=4, fg="black", font=('times new roman', 12, 'bold'), width=8,
                          text="Print",command=iPrint).grid(row=0, column=2)
        
        btnReset = Button(fb2, padx=10, pady=4, bd=4, fg="black", font=('times new roman', 12, 'bold'), width=8,
                          text="Reset", command=Reset).grid(row=0, column=3)

        btnExit = Button(fb2, padx=9, pady=4, bd=4, fg="red", font=('times new roman', 12, 'bold'), width=8,
                         text="Exit", command=self.master.destroy).grid(row=0, column=4)



# =====================================================CUSTOMER_INFORMATION (fa1)=======================================


        lblName = Label(fa1, font=('times new roman', 14, 'bold'), width=22, text="Customers Good Name : ", bd=6)
        lblName.grid(row=0, column=0, sticky=W,columnspan=1)
        lblName = Entry(fa1, font=('times new roman', 14, 'bold'), width=25, bd=5, justify='left', textvariable=Name)
        lblName.grid(row=0, column=1,columnspan=1)

        lblEmp = Label(fa1, font=('times new roman', 14, 'bold'), width=22, text="Waiter Name : ", bd=6)
        lblEmp.grid(row=0, column=2, sticky=W,columnspan=1)
        lblEmp = Entry(fa1, font=('times new roman', 14, 'bold'), width=25, bd=5, justify='left', textvariable=Emp)
        lblEmp.grid(row=0, column=3, sticky=W,columnspan=1)

        lbltb = Label(fa1, font=('times new roman', 14, 'bold'), width=22, text="Table No. : ", bd=6)
        lbltb.grid(row=0, column=4, sticky=W,columnspan=1)
        lbltb = Entry(fa1, font=('times new roman', 14, 'bold'), width=5, bd=5, justify='left', textvariable=tb)
        lbltb.grid(row=0, column=5, sticky=W,columnspan=1)


        

        


# =========================================================win=========================================================

if __name__ == '__main__':
        main()



