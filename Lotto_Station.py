# Masimthembe Ndabeni
from tkinter import *
from PIL import Image, ImageTk
import random

import multiprocessing
from playsound import playsound
window = Tk()
from tkinter import messagebox

# window = window
window.title("Ithuba National Lottery of South Africa Lotto Station")
window.geometry("1000x360")
window.config(bg="white")


# creating a mother class
class LotteryNumbers:


    def __init__(self, master):

        self.txtDisplay1 = None
        self.txtDisplay2 = None
        self.txtDisplay3 = None
        self.txtDisplay4 = None
        self.txtDisplay5 = None
        self.txtDisplay6 = None
        self.num1 = None
        self.num2 = None
        self.num3 = None
        self.num4 = None
        self.num5 = None
        self.num6 = None

        self.var = StringVar()
        self.var.set("Lets Play")
        self.frame1 = Frame(window)
        self.frame1.pack(side = TOP)
        self.label = Label(self.frame1, textvariable=self.var, font=("Arial", 48), width=24)
        self.label.pack(side =TOP)
        self.label = Label(self.frame1, textvariable="", width=24)
        self.label.pack(side =TOP)
        self.label = Label(self.frame1, textvariable="", width=24)
        self.label.pack(side =TOP)

        self.frame2 = Frame(master)
        self.frame2.pack(side = TOP)
        self.txtDisplay1=Entry(self.frame2, textvariable=self.num1, bd=20, insertwidth=1, font=("Arial", 30), justify="center", width=4)
        self.txtDisplay1.pack(side = LEFT)
        self.txtDisplay2=Entry(self.frame2, textvariable=self.num2, bd=20, insertwidth=1, font=("Arial", 30), justify="center", width=4)
        self.txtDisplay2.pack(side = LEFT)
        self.txtDisplay3=Entry(self.frame2, textvariable=self.num3, bd=20, insertwidth=1, font=("Arial", 30), justify="center", width=4)
        self.txtDisplay3.pack(side = LEFT)
        self.txtDisplay4=Entry(self.frame2, textvariable=self.num4, bd=20, insertwidth=1, font=("Arial", 30), justify="center", width=4)
        self.txtDisplay4.pack(side = LEFT)
        self.txtDisplay5=Entry(self.frame2, textvariable=self.num5, bd=20, insertwidth=1, font=("Arial", 30), justify="center", width=4)
        self.txtDisplay5.pack(side = LEFT)
        self.txtDisplay6=Entry(self.frame2, textvariable=self.num6, bd=20, insertwidth=1, font=("Arial", 30), justify="center", width=4)
        self.txtDisplay6.pack(side = LEFT)

        self.frame3 = Frame(master)
        self.frame3.pack(side = TOP)
        self.button1 = Button(self.frame3, state=DISABLED, text="")
        self.button1.pack(side = TOP)
        self.button1 = Button(self.frame3, padx=8, width=18, pady=8, text='PlAY', command=self.Lotto_No)
        self.button1.pack(side=TOP)

    def Lotto_No(self):
        self.lotto_list=[]
        self.lotto_list.append(int(self.txtDisplay1.get()))
        self.lotto_list.append(int(self.txtDisplay2.get()))
        self.lotto_list.append(int(self.txtDisplay3.get()))
        self.lotto_list.append(int(self.txtDisplay4.get()))
        self.lotto_list.append(int(self.txtDisplay5.get()))
        self.lotto_list.append(int(self.txtDisplay6.get()))

        self.lotto_list.sort()
        self.lotto_num = sorted(random.sample(range(1, 49),6))


        if any(self.lotto_list) <0 or any(self.lotto_list) <50:
            messagebox.showinfo("STATUS", "LET'S PLAY")
        self.similar = set(self.lotto_num).intersection(set(self.lotto_list))
        print("Original list", (self.lotto_num))
        print(len(self.similar))
        if len(self.lotto_num) == len(self.lotto_list):

                if len(self.similar) == 6:
                    messagebox.askquestion("STATUS", "jACKPOT!! YOU HAVE WON 6th Place!! , YOU HAVE WON R10 000 000 00, Do you want to claim your prize now?")
                elif len(self.similar) == 5:
                    messagebox.askquestion("STATUS", "CONGRATULATIONS YOU HAVE WON 5th Place!!, YOU HAVE WON R6 584 00 Do you want to claim your prize now?")
                elif len(self.similar) == 4:
                    messagebox.askquestion("STATUS", "CONGRATULATIONS YOU HAVE WON 4th Place!!, YOU HAVE WON R2 384 00, Do you want to claim your prize now?")
                elif len(self.similar) == 3:
                     messagebox.askquestion("CLAIM PRIZE", "CONGRATULATIONS YOU HAVE WON 3th Place, YOU HAVE R100, 50 Do you want to Claim Your Prize now?")
                elif len(self.similar) == 2:
                    messagebox.askquestion("CLAIM PRIZE", "CONGRATULATIONS YOU HAVE WON 2th Place, Do you want to Claim Your Prize now?")
                elif len(self.similar) == 1:
                    messagebox.askquestion("STATUS", "UNFORTUNATELY YOU WON NOTHING, DO YOU WANT TO PLAY ONE MORE TIME?")
        else:
            messagebox.showerror("ERROR INFO", "HARD LUCK")
            return



x = LotteryNumbers(window)
window.mainloop()
