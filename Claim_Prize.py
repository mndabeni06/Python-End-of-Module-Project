
from tkinter import *
from tkinter import ttk
winner = Tk()
from tkinter import messagebox
import smtplib
from email.mime.text import MIMEText
from PIL import Image, ImageTk
from email.mime.multipart import MIMEMultipart
background_img = Image.open("images.png")
bg_img = ImageTk.PhotoImage(background_img)
img = Label(winner, image=bg_img)
img.place(x=900, y=10)


winner.title("Ithuba National Lottery of South Africa ClaimPrize Station")
winner.geometry("1200x700")
winner.config(bg="#f48c06")


# Creating Widgets
class BankDetails:

    def __init__(self, master):
        self.accountHolder_lbl = Label(master, text="Please Enter Your AccountHolder Name :")
        self.accountHolder_lbl.place(x=10, y=35)
        self.accountHolder_entry = Entry(master, borderwidth=5)
        self.accountHolder_entry.place(x=300, y=38)

        self.bank_type = Label(master, text="Choose Your Bank: ")
        self.bank_type.place(x=10, y=80)
        self.var = StringVar
        self.choose_bank = ttk.Combobox(master,  textvariable=self.var, width=20, value=["ABSA", "FIRST NATIONAL BANK", "NEDBANK", "STANDARD BANK", "CAPITEC"])
        self.choose_bank.place(x=300, y=80)


        self.email_lbl = Label(master, text="Please Enter Your Email :")
        self.email_lbl.place(x=10, y=125)
        self.email_entry = Entry(master, borderwidth=5)
        self.email_entry.place(x=300, y=120)

        self.account_number_lbl = Label(master, text="Please Enter Your Account Number :")
        self.account_number_lbl.place(x=10, y=180)
        self.account_number_entry = Entry(master, borderwidth=5)
        self.account_number_entry.place(x=295, y=180)

        self.user_address_lbl = Label(master, text="Please Enter Your Address :")
        self.user_address_lbl.place(x=10, y=250)
        self.user_address_entry = Text(master, width=37, height=10)
        self.user_address_entry.place(x=280, y=250)

        self.ID_number_lbl = Label(master, text="Please Enter Your ID Number :")
        self.ID_number_lbl.place(x=10, y=450)
        self.ID_number_entry = Entry(master, borderwidth=5, show="*")
        self.ID_number_entry.place(x=280, y=450)
        self.login_btn = Button(master, text='Submit', borderwidth=5, command=self.submit, bg="green")
        self.login_btn.place(x=10, y=550)
        self.clear_btn = Button(master, text='Clear', borderwidth=5, command=self.clear, bg="gold")
        self.clear_btn.place(x=300, y=550)



# Defining a functions for the window
    def submit(self):

        Results = open("Results.txt", "r+")
        Results.writelines("Account Holder: " + self.accountHolder_entry.get() + "\n")
        Results.writelines("Bank: " + self.choose_bank.get() + "\n")
        Results.writelines("Account Holder Email: " + self.email_entry.get() + "\n")
        Results.writelines("Account Number: " + self.account_number_entry.get() + "\n")
        Results.close()


        Username = ["Karabo", "Masimthembe", "Mpendulo", "Jardien", "Likho"]
        Email = ["karabo@gmail.com", "mndabeni6@gmail.com", "mpendulo@gmail.com", "jardien@gmail.com", "likho@gmail.com"]
        AccountNumber = ["155510780187", "16902123457", "1804762123", "1678123457", "l153789012"]
        ID_Number = ["0001 01683 1233", "991030 580 084", "0002 11683 1433", "0003 05683 1233", "0006 08683 1243"]

        found = False
        for x in range(len(Username)):
            if self.accountHolder_entry.get() == Username[x] and self.email_entry.get() == Email[x] and self.account_number_entry.get() == AccountNumber[x] and self.ID_number_entry.get() == ID_Number[x]:
                found = True
            if found == True:
                    messagebox.askquestion("PERMISSION", "Access Granted, Do you wish to convert your currency?")


        sender_email_id = 'mndabeni6@gmail.com'
        receiver_email_id = 'mndabeni6@gmail.com'
        password = input("Enter your password: ")
        subject="Good Day"
        msg=MIMEMultipart()
        msg['From'] = sender_email_id
        msg['To'] = receiver_email_id
        msg['Subject']=subject
        body = "Ithuba National Lottery of South Africa wishes you all the best to your Future endeavours.\n"
        body = body + "CONGRATULATIONS YOU HAVE WON 2nd PRIZE!!, YOU HAVE R20.0 IN YOUR ACCOUNT  If you wish to convert your currency click here: https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=ZAR"
        msg.attach(MIMEText(body, 'plain'))
        text=msg.as_string()
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(sender_email_id, password)
        s.sendmail(sender_email_id, receiver_email_id, text)
        s.quit()






    def clear(self):
        self.account_number_entry.delete(0, END)
        self.choose_bank.delete(0,  END)
        self.user_address_entry.delete('1.0', END)
        self.email_entry.delete(0, END)
        self.ID_number_entry.delete(0, END)










y = BankDetails(winner)
winner.mainloop()
