
from tkinter import *
from tkinter import ttk
winner = Tk()
from tkinter import messagebox
import smtplib

winner.title("Ithuba National Lottery of South Africa ClaimPrize Station")
winner.geometry("700x600")
winner.config(bg="white")


class BankDetails:

    def __init__(self, master):
        self.accountHolder_lbl = Label(master, text="Please Enter Your AccountHolder Name :")
        self.accountHolder_lbl.place(x=10, y=40)
        self.accountHolder_entry = Entry(master, borderwidth=5)
        self.accountHolder_entry.place(x=300, y=40)

        self.bank_type = Label(master, text="Choose Your Bank: ")
        self.bank_type.place(x=10, y=80)
        self.var = StringVar
        self.choose_bank = ttk.Combobox(master, textvariable=self.var, width=18, value=["ABSA", "FIRST NATIONAL BANK", "NEDBANK", "STANDARD BANK", "CAPITEC"])
        self.choose_bank.place(x=300, y=80)


        self.email_lbl = Label(master, text="Please Enter Your Email :")
        self.email_lbl.place(x=10, y=120)
        self.email_entry = Entry(master, borderwidth=5)
        self.email_entry.place(x=300, y=120)

        self.account_number_lbl = Label(master, text="Please Enter Your Account Number :")
        self.account_number_lbl.place(x=10, y=180)
        self.account_number_entry = Entry(master, borderwidth=5, show="*")
        self.account_number_entry.place(x=290, y=180)

        self.user_address_lbl = Label(master, text="Please Enter Your Address :")
        self.user_address_lbl.place(x=10, y=250)
        self.user_address_entry = Text(master, width=37, height=10)
        self.user_address_entry.place(x=280, y=250)

        self.ID_number_lbl = Label(master, text="Please Enter Your ID Number :")
        self.ID_number_lbl.place(x=10, y=450)
        self.ID_number_entry = Entry(master, borderwidth=5, show="*")
        self.ID_number_entry.place(x=280, y=450)
        self.login_btn = Button(master, text='Submit', borderwidth=5, command=self.submit)
        self.login_btn.place(x=10, y=550)
        self.clear_btn = Button(master, text='Clear', borderwidth=5, command=self.clear)
        self.clear_btn.place(x=300, y=550)




    def submit(self):

        Username = ["Karabo", "Masimthembe", "Mpendulo", "Jardien", "Likho"]
        Email = ["karabo@gmail.com", "mndabeni6@gmail.com", "mpendulo@gmail.com", "jardien@gmail.com", "likho@gmail.com"]
        AccountNumber = ["155510780187", "16902123457", "1804762123", "1678123457", "l153789012"]
        ID_Number = ["0001 01683 1233", "991030 580 084", "0002 11683 1433", "0003 05683 1233", "0006 08683 1243"]

        found = False
        for x in range(len(Username)):
            if self.accountHolder_entry.get() == Username[x] and self.email_entry.get() == Email[x] and self.account_number_entry.get() == AccountNumber[x] and self.ID_number_entry.get() == ID_Number[x]:
                found = True
            if found == True:
                    messagebox.showinfo("PERMISSION", "Access Granted")




                    self.s = smtplib.SMTP('smtp.gmail.com', 587)
                    self.sender_mail_id = 'mndabeni6@gmail.com'
                    self.receiver_mail_id = 'mndabeni6@gmail.com'
                    self.password = input("Enter sender mail password: ")

                    self.s.starttls()
                    self.s.login(self.sender_mail_id, self.password)

                    self.message = ""
                    self.message = self.message + "CONGRATULATIONS YOU HAVE WON 2th PRIZE!!, YOU HAVE WON R20.0"
                    self.s.sendmail(self.sender_mail_id, self.receiver_mail_id, self.message)

                    self.s.quit()


        else:
            messagebox.showerror("ERROR INFO", "Access Denied")


    def clear(self):
        self.account_number_entry.delete(0, END)
        self.choose_bank.delete(0,  END)
        self.user_address_entry.delete('1.0', END)
        self.email_entry.delete(0, END)
        self.ID_number_entry.delete(0, END)










y = BankDetails(winner)
winner.mainloop()
