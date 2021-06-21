# Masimthembe Ndabeni
import random
from tkinter import *
from playsound import playsound
from PIL import Image, ImageTk

window = Tk()
background_img = Image.open("LOTTO BALLS.jpg")
bg_img = ImageTk.PhotoImage(background_img)
img = Label(window, image=bg_img)
img.place(x=0, y=0)
from tkinter import messagebox

window.title("Ithuba National Lottery of South Africa Lotto Station")
window.geometry("1000x400")
window.config(bg="yellow")


# Creating a Widgets
class LotteryNumbers:

    def __init__(self, master):

        self.master = None
        self.exit = None
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
        self.var.set("LET'S PLAY")
        self.frame1 = Frame(window)
        self.frame1.pack(side=TOP)
        self.label = Label(self.frame1, textvariable=self.var, font=("Arial", 48), width=24, bg="goldenrod")
        self.label.pack(side=TOP)
        self.label = Label(self.frame1, textvariable="", width=24)
        self.label.pack(side=TOP)
        self.label = Label(self.frame1, textvariable="", width=24)
        self.label.pack(side=TOP)

        self.frame2 = Frame(master)
        self.frame2.pack(side=TOP)
        self.txtDisplay1 = Entry(self.frame2, textvariable=self.num1, bd=20, insertwidth=1, font=("Arial", 30),
                                 justify="center", width=4, bg="goldenrod")
        self.txtDisplay1.pack(side=LEFT)
        self.txtDisplay2 = Entry(self.frame2, textvariable=self.num2, bd=20, insertwidth=1, font=("Arial", 30),
                                 justify="center", width=4, bg="goldenrod")
        self.txtDisplay2.pack(side=LEFT)
        self.txtDisplay3 = Entry(self.frame2, textvariable=self.num3, bd=20, insertwidth=1, font=("Arial", 30),
                                 justify="center", width=4, bg="goldenrod")
        self.txtDisplay3.pack(side=LEFT)
        self.txtDisplay4 = Entry(self.frame2, textvariable=self.num4, bd=20, insertwidth=1, font=("Arial", 30),
                                 justify="center", width=4, bg="goldenrod")
        self.txtDisplay4.pack(side=LEFT)
        self.txtDisplay5 = Entry(self.frame2, textvariable=self.num5, bd=20, insertwidth=1, font=("Arial", 30),
                                 justify="center", width=4, bg="goldenrod")
        self.txtDisplay5.pack(side=LEFT)
        self.txtDisplay6 = Entry(self.frame2, textvariable=self.num6, bd=20, insertwidth=1, font=("Arial", 30),
                                 justify="center", width=4, bg="goldenrod")
        self.txtDisplay6.pack(side=LEFT)

        self.frame3 = Frame(master)
        self.frame3.pack(side=TOP)
        self.button1 = Button(self.frame3, state=DISABLED, text="")
        self.button1.pack(side=TOP)
        self.button1 = Button(self.frame3, padx=8, width=18, pady=8, text='PLAY', command=self.Lotto_No, bg="goldenrod")
        self.button1.pack(side=TOP)

        self.frame4 = Frame(master)
        self.frame4.pack(side=RIGHT)
        self.exit_btn = Button(self.frame4, state=DISABLED, text="")
        self.exit_btn.pack(side=RIGHT)
        self.exit_btn = Button(self.frame4, padx=8, width=18, pady=8, text='EXIT', bg="goldenrod", command=self.close)
        self.exit_btn.pack(side=RIGHT)

        self.frame5 = Frame(master)
        self.frame5.pack(side=LEFT)
        self.exit_btn = Button(self.frame5, state=DISABLED, text="")
        self.exit_btn.pack(side=LEFT)
        self.exit_btn = Button(self.frame5, padx=8, width=18, pady=8, text='REPLAY', bg="goldenrod", command=self.relpay)
        self.exit_btn.pack(side=LEFT)



    def close(self):
        window.destroy()

    def relpay(self):
        self.txtDisplay1.delete(0, END)
        self.txtDisplay2.delete(0, END)
        self.txtDisplay3.delete(0, END)
        self.txtDisplay4.delete(0, END)
        self.txtDisplay5.delete(0, END)
        self.txtDisplay6.delete(0, END)

    def playmusic(self):
        self.p.start()

    def stopmusic(self):
        self.p.terminate()

# Defining a Function to Run The Program
    def Lotto_No(self):
        self.lotto_list = []
        if int(self.txtDisplay1.get()) > 49:

            messagebox.showerror("STATUS", "NUMBER CANNOT BE HIGHER THAN 49")
        else:
            pass

        if int(self.txtDisplay2.get()) > 49:
            messagebox.showerror("STATUS", "NUMBER CANNOT BE HIGHER THAN 49")
        else:
            pass

        if int(self.txtDisplay3.get()) > 49:
            messagebox.showerror("STATUS", "NUMBER CANNOT BE HIGHER THAN 49")
        else:
            pass

        if int(self.txtDisplay4.get()) > 49:
            messagebox.showerror("STATUS", "NUMBER CANNOT BE HIGHER THAN 49")
        else:
            pass
        if int(self.txtDisplay5.get()) > 49:
            messagebox.showerror("STATUS", "NUMBER CANNOT BE HIGHER THAN 49")
        else:
            pass
        if int(self.txtDisplay6.get()) > 49:
            messagebox.showerror("STATUS", "NUMBER CANNOT BE HIGHER THAN 49")
        else:
            pass

        self.lotto_list.append(int(self.txtDisplay1.get()))
        self.lotto_list.append(int(self.txtDisplay2.get()))
        self.lotto_list.append(int(self.txtDisplay3.get()))
        self.lotto_list.append(int(self.txtDisplay4.get()))
        self.lotto_list.append(int(self.txtDisplay5.get()))
        self.lotto_list.append(int(self.txtDisplay6.get()))

        self.lotto_list.sort()
        self.lotto_num = sorted(random.sample(range(1, 49), 6))


        Results = open("Results.txt", "r+")
        Results.writelines("Player Numbers: " + self.txtDisplay1.get() + self.txtDisplay2.get()+ self.txtDisplay3.get() + self.txtDisplay4.get() + self.txtDisplay5.get()+ self.txtDisplay6.get() + "\n")
        Results.close()


        if any(self.lotto_list) < 0 or any(self.lotto_list) < 50:
            messagebox.showinfo("STATUS", "LET'S PLAY")
        self.similar = set(self.lotto_num).intersection(set(self.lotto_list))
        messagebox.showinfo("ORIGINAL LIST", (self.lotto_num))
        messagebox.showinfo('MATCHES', len(self.similar))
        if len(self.lotto_num) == len(self.lotto_list):

            if len(self.similar) == 6:
                messagebox.askquestion("STATUS",
                                       "JACKPOT!! YOU HAVE WON 6th PRIZE!! ,   Do you want to claim your R10 000 000 00 now?")
                import multiprocessing
                from playsound import playsound
                self.p = multiprocessing.Process(target=playsound, args=('Applause Crowd Cheering sound effect.mp3',))
                window.destroy()
                import Claim_Prize
            elif len(self.similar) == 5:
                messagebox.askquestion("STATUS",
                                       "CONGRATULATIONS YOU HAVE WON 5th PRIZE!!,   Do you want to claim your R6 584 00 now?")
                import multiprocessing
                from playsound import playsound
                self.p = multiprocessing.Process(target=playsound, args=('Applause Crowd Cheering sound effect.mp3',))
                window.destroy()
                import Claim_Prize
            elif len(self.similar) == 4:
                msg = messagebox.askquestion("STATUS",
                                       "CONGRATULATIONS YOU HAVE WON 4th PRIZE!!,  Do you want to claim your R2 384 00 now?")

                import multiprocessing
                from playsound import playsound
                self.p = multiprocessing.Process(target=playsound, args=('Applause Crowd Cheering sound effect.mp3',))
                window.destroy()
                import Claim_Prize
            elif len(self.similar) == 3:
                messagebox.askquestion("CLAIM PRIZE",
                                       "CONGRATULATIONS YOU HAVE WON 3rd PRIZE!!, Do you want to Claim Your R100.50 now?")
                import multiprocessing
                from playsound import playsound
                self.p = multiprocessing.Process(target=playsound, args=('Applause Crowd Cheering sound effect.mp3',))
                window.destroy()
                import Claim_Prize
            elif len(self.similar) == 2:
                messagebox.askquestion("CLAIM PRIZE",
                                       "CONGRATULATIONS YOU HAVE WON 2nd PRIZE!!, Do you want to Claim Your R20.00 now?")
                import multiprocessing
                from playsound import playsound
                self.p = multiprocessing.Process(target=playsound, args=('Applause Crowd Cheering sound effect.mp3',))
                window.destroy()
                import Claim_Prize
            elif len(self.similar) == 1:
                messagebox.showerror("STATUS", "UNFORTUNATELY YOU WON R0.00")

        else:

            messagebox.showerror("ERROR INFO", "HARD LUCK!! Try Next Time")
            return

x = LotteryNumbers(window)
window.mainloop()
