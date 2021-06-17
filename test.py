from tkinter import*
import random
from tkinter import messagebox
lottery = Tk()
lottery.geometry("800x360")

def Lotto_No():
    lotto_list=[]
    lotto_list.append(int(txtDisplay1.get ()))
    lotto_list.append(int(txtDisplay2.get()))
    lotto_list.append(int( txtDisplay3.get()))
    lotto_list.append(int(txtDisplay4.get()))
    lotto_list.append( int(txtDisplay5.get()))
    lotto_list.append(int(txtDisplay6.get()))

    lotto_list.sort()
    lotto_num = sorted(random.sample(range(1, 49),6))

    if any(lotto_list) <0 or any(lotto_list) <50:
        messagebox.showinfo("STATUS", "LET'S PLAY")
        similar = set(lotto_num).intersection(set(lotto_list))
        print("Original list", (lotto_num))
        print(len(similar))
        if len(lotto_num) == len(lotto_list):

                if len(similar) == 6:
                    messagebox.showinfo("STATUS", "jACKPOT!! YOU HAVE WON")
                elif len(similar) == 5:
                    messagebox.showinfo("STATUS", "CONGRATULATIONS YOU HAVE WON 5th Place")
                elif len(similar) == 4:
                    messagebox.showinfo("STATUS", "CONGRATULATIONS YOU HAVE WON 4th Place")
                elif len(similar) == 3:
                     messagebox.askquestion("CLAIM PRIZE", "CONGRATULATIONS YOU HAVE WON 2th Place, Do you want to Claim Your Prize now?")
                    lottery.destroy()
                    import test2
                elif len(similar) == 2:
                    messagebox.askquestion("CLAIM PRIZE", "CONGRATULATIONS YOU HAVE WON 2th Place, Do you want to Claim Your Prize now?")
                    lottery.destroy()
                    import test2
        else:
            messagebox.showerror("ERROR INFO", "HARD LUCK")
            return





frame = Frame(lottery)
frame.pack()
num1 = StringVar()
num2 = StringVar()
num3 = StringVar()
num4 = StringVar()
num5 = StringVar()
num6 = StringVar()

var = StringVar()
var.set("Lets Play")
frame1 = Frame(lottery)
frame1.pack(side = TOP)
label = Label(frame1, textvariable=var, font=("Arial", 48), width=24)
label.pack(side =TOP)
label = Label(frame1, textvariable="", width=24)
label.pack(side =TOP)
label = Label(frame1, textvariable="", width=24)
label.pack(side =TOP)

frame2 = Frame(lottery)
frame2.pack(side = TOP)
txtDisplay1=Entry(frame2, textvariable=num1, bd=20, insertwidth=1, font=("Arial", 30), justify="center", width=4)
txtDisplay1.pack(side = LEFT)
txtDisplay2=Entry(frame2, textvariable=num2, bd=20, insertwidth=1, font=("Arial", 30), justify="center", width=4)
txtDisplay2.pack(side = LEFT)
txtDisplay3=Entry(frame2, textvariable=num3, bd=20, insertwidth=1, font=("Arial", 30), justify="center", width=4)
txtDisplay3.pack(side = LEFT)
txtDisplay4=Entry(frame2, textvariable=num4, bd=20, insertwidth=1, font=("Arial", 30), justify="center", width=4)
txtDisplay4.pack(side = LEFT)
txtDisplay5=Entry(frame2, textvariable=num5, bd=20, insertwidth=1, font=("Arial", 30), justify="center", width=4)
txtDisplay5.pack(side = LEFT)
txtDisplay6=Entry(frame2, textvariable=num6, bd=20, insertwidth=1, font=("Arial", 30), justify="center", width=4)
txtDisplay6.pack(side = LEFT)

frame3 = Frame(lottery)
frame3.pack(side = TOP)
button1 = Button(frame3, state=DISABLED, text="")
button1.pack(side = TOP)
button1 = Button(frame3, padx=8, width=18, pady=8, text='PlAY', command=Lotto_No)
button1.pack(side=TOP)
results_lbl = Label


lottery.mainloop()
