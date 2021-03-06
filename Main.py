# Masimthembe Ndabeni, Class 2
from tkinter import *

from PIL import Image, ImageTk
root = Tk()
from tkinter import messagebox
background_img = Image.open("LOTTO BG.jpeg")
bg_img = ImageTk.PhotoImage(background_img)
img = Label(root, image=bg_img)
img.place(x=0, y=0)



# Creating a Mother Class
class ID_Number:
    pass



class LotteryNumbers:
    def __init__(self, master):
        self.root = root
        self.root.title("Ithuba National Lottery of South Africa Login Form")
        self.root.geometry("1500x1000")


# Creating  Widgets
        self.username_lbl = Label(master, text="Please Enter Your Name :")
        self.username_lbl.place(x=10, y=40)
        self.username_entry = Entry(master, borderwidth=5)
        self.username_entry.place(x=200, y=40)

        self.password_lbl = Label(master, text="Please Enter Your Password :")
        self.password_lbl.place(x=10, y=65)
        self.password_entry = Entry(master, borderwidth=5, show="*")
        self.password_entry.place(x=200, y=65)

        self.email_lbl = Label(master, text="Please Enter Your Email :")
        self.email_lbl.place(x=10, y=90)
        self.email_entry = Entry(master, borderwidth=5)
        self.email_entry.place(x=200, y=90)

        self.user_address_lbl = Label(master, text="Please Enter Your Address :")
        self.user_address_lbl.place(x=10, y=150)
        self.user_address_entry = Text(master, width=37, height=10)
        self.user_address_entry.place(x=200, y=150)

        self.ID_number_lbl = Label(master, text="Please Enter Your ID Number :")
        self.ID_number_lbl.place(x=10, y=350)
        self.ID_number_entry = Entry(master, borderwidth=5, show="*")
        self.ID_number_entry.place(x=220, y=345)
        self.login_btn = Button(root, text='Login', borderwidth=5, command=self.login, bg="yellow")
        self.login_btn.place(x=10, y=400)
        self.clear_btn = Button(master, text='Clear', borderwidth=5, command=self.clear, bg="blue")
        self.clear_btn.place(x=300, y=400)
        self.logout_btn = Button(master, text='Logout', borderwidth=5, command=self.logout, bg="red")
        self.logout_btn.place(x=160, y=400)

    def login(self):

        Results = open("Results.txt", "r+")
        Results.writelines("Username: " + self.username_entry.get() + "\n")
        Results.writelines("Password: " + self.password_entry.get() + "\n")
        Results.writelines("Email Address: " + self.password_entry.get() + "\n")
        Results.writelines("Home Address: " + self.user_address_entry.get("1.0",'end-1c') + "\n")
        Results.writelines("Id No: " + self.ID_number_entry.get() + "\n")
        Results.close()


        Username = ["Karabo", "Masimthembe", "Mpendulo", "Jardien", "Likho"]
        Password = ["123", "456", "789", "101", "131"]
        Address =  ["10150 Lahlangubo Street", "21 ShowFlats Langa", "8001 Northern Suburb CapeTown", "8000 Mannemberg CapeTown", "345 Samora CapeTown"]
        email = ["karabo@gmail.com", "mndabeni6@gmail.com", "mpendulo@gmail.com", "jardien@gmail.com", "likho@gmail.com"]
        ID_Number = ["0001 01683 1233", "991030 5801 3084", "0002 11683 1433", "0003 05683 1233", "0006 08683 1243"]
        found = False
        for x in range(len(Username)):
            if self.username_entry.get() == Username[x] and self.password_entry.get() == Password[x] and self.user_address_entry.get("1.0",'end-1c') == Address[x] and self.email_entry.get() == email[x] and self.ID_number_entry.get() == ID_Number[x]:
                found = True

        if found == True:
            messagebox.showinfo("PERMISSION", "Access Granted")
            root.destroy()
            import Lotto_Station

        else:
            messagebox.showerror("ERROR INFO", "Access Denied")


    def clear(self):
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)
        self.user_address_entry.delete('1.0', END)
        self.email_entry.delete(0, END)
        self.ID_number_entry.delete(0, END)





    def logout(self):
        self.message_box = messagebox.askquestion('Exit Application', 'Are you sure you want to Logout?')
        if self.message_box == 'yes':
            self.root.destroy()
        else:
            pass



lottery = LotteryNumbers(root)
root.mainloop()
