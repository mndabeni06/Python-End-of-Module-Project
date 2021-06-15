# Masimthembe Ndabeni
from _ast import Lambda
from tkinter import *
from PIL import Image, ImageTk
import multiprocessing
from playsound import playsound
from validate_email import validate_email
from random import randint
window = Tk()
from tkinter import messagebox
background_img = Image.open("pngwing.com.png")
bg_img = ImageTk.PhotoImage(background_img)
img = Label(window, image=bg_img)
img.place(x=0, y=0)



# creating a mother class
class LotteryNumbers:
    def __init__(self, master):
        self.window = window
        self.window.title("Ithuba National Lottery of South Africa Lotto Station")
        self.window.geometry("600x900")
        self.window.config(bg="black")

# Creating Label Widgets
        self.title_lbl = Label(window, text="Let's Play", width=60, height=2)
        self.title_lbl.place(x=50, y=10)
        self.title_lbl.config(bg="yellow")

        self.lotto_frame = LabelFrame(window, height=300, width=300)
        self.lotto_frame.config(bg="grey")
        self.lotto_frame.place(x=100, y=90)

        self.lotto_number = Button(self.lotto_frame, text="1", borderwidth=3, bg="yellow")
        self.lotto_number.place(x=0, y=0)
        self.lotto_number = Button(self.lotto_frame, text="2",  borderwidth=3, bg="yellow")
        self.lotto_number.place(x=50, y=0)
        self.lotto_number = Button(self.lotto_frame, text="3",  borderwidth=3, bg="yellow")
        self.lotto_number.place(x=100, y=0)
        self.lotto_number = Button(self.lotto_frame, text="4",  borderwidth=3, bg="yellow")
        self.lotto_number.place(x=150, y=0)
        self.lotto_number = Button(self.lotto_frame, text="5",  borderwidth=3, bg="yellow")
        self.lotto_number.place(x=200, y=0)
        self.lotto_number = Button(self.lotto_frame, text="6",  borderwidth=3, bg="yellow")
        self.lotto_number.place(x=250, y=0)

        self.lotto_number = Button(self.lotto_frame, text="7", borderwidth=3, bg="yellow" )
        self.lotto_number.place(x=0, y=50)
        self.lotto_number = Button(self.lotto_frame, text="8", borderwidth=3, bg="yellow")
        self.lotto_number.place(x=50, y=50)
        self.lotto_number = Button(self.lotto_frame, text="9", borderwidth=3, bg="yellow")
        self.lotto_number.place(x=100, y=50)
        self.lotto_number = Button(self.lotto_frame, text="10", borderwidth=3, bg="yellow")
        self.lotto_number.place(x=150, y=50)
        self.lotto_number = Button(self.lotto_frame, text="11", borderwidth=3, bg="yellow")
        self.lotto_number.place(x=200, y=50)
        self.lotto_number = Button(self.lotto_frame, text="12", borderwidth=3, bg="yellow")
        self.lotto_number.place(x=250, y=50)

        self.lotto_number = Button(self.lotto_frame, text="13", borderwidth=3, bg="yellow")
        self.lotto_number.place(x=0, y=100)
        self.lotto_number = Button(self.lotto_frame, text="14", borderwidth=3, bg="yellow")
        self.lotto_number.place(x=50, y=100)
        self.lotto_number = Button(self.lotto_frame, text="15", borderwidth=3, bg="yellow")
        self.lotto_number.place(x=100, y=100)
        self.lotto_number = Button(self.lotto_frame, text="16", borderwidth=3, bg="yellow")
        self.lotto_number.place(x=150, y=100)
        self.lotto_number = Button(self.lotto_frame, text="17", borderwidth=3, bg="yellow")
        self.lotto_number.place(x=200, y=100)
        self.lotto_number = Button(self.lotto_frame, text="18", borderwidth=3, bg="yellow")
        self.lotto_number.place(x=250, y=100)

        self.lotto_number = Button(self.lotto_frame, text="19", borderwidth=3, bg="yellow")
        self.lotto_number.place(x=0, y=150)
        self.lotto_number = Button(self.lotto_frame, text="20", borderwidth=3, bg="yellow")
        self.lotto_number.place(x=50, y=150)
        self.lotto_number = Button(self.lotto_frame, text="21", borderwidth=3, bg="yellow")
        self.lotto_number.place(x=100, y=150)
        self.lotto_number = Button(self.lotto_frame, text="22", borderwidth=3, bg="yellow")
        self.lotto_number.place(x=150, y=150)
        self.lotto_number = Button(self.lotto_frame, text="23",  borderwidth=3, bg="yellow")
        self.lotto_number.place(x=200, y=150)
        self.lotto_number = Button(self.lotto_frame, text="24",  borderwidth=3, bg="yellow")
        self.lotto_number.place(x=250, y=150)

        self.lotto_number = Button(self.lotto_frame, text="25",  borderwidth=3, bg="yellow")
        self.lotto_number.place(x=0, y=200)
        self.lotto_number = Button(self.lotto_frame, text="26",  borderwidth=3, bg="yellow")
        self.lotto_number.place(x=50, y=200)
        self.lotto_number = Button(self.lotto_frame, text="27",  borderwidth=3, bg="yellow")
        self.lotto_number.place(x=100, y=200)
        self.lotto_number = Button(self.lotto_frame, text="28",  borderwidth=3, bg="yellow")
        self.lotto_number.place(x=150, y=200)
        self.lotto_number = Button(self.lotto_frame, text="29",  borderwidth=3, bg="yellow")
        self.lotto_number.place(x=200, y=200)
        self.lotto_number = Button(self.lotto_frame, text="30",  borderwidth=3, bg="yellow")
        self.lotto_number.place(x=250, y=200)

        self.lotto_number = Button(self.lotto_frame, text="31",  borderwidth=3, bg="yellow")
        self.lotto_number.place(x=0, y=200)
        self.lotto_number = Button(self.lotto_frame, text="32",  borderwidth=3, bg="yellow")
        self.lotto_number.place(x=50, y=200)
        self.lotto_number = Button(self.lotto_frame, text="33",  borderwidth=3, bg="yellow")
        self.lotto_number.place(x=100, y=200)
        self.lotto_number = Button(self.lotto_frame, text="34",  borderwidth=3, bg="yellow")
        self.lotto_number.place(x=150, y=200)
        self.lotto_number = Button(self.lotto_frame, text="35",  borderwidth=3, bg="yellow")
        self.lotto_number.place(x=200, y=200)
        self.lotto_number = Button(self.lotto_frame, text="36",  borderwidth=3, bg="yellow")
        self.lotto_number.place(x=250, y=200)

        self.lotto_number = Button(self.lotto_frame, text="37",  borderwidth=3, bg="yellow")
        self.lotto_number.place(x=0, y=200)
        self.lotto_number = Button(self.lotto_frame, text="38",  borderwidth=3, bg="yellow")
        self.lotto_number.place(x=50, y=200)
        self.lotto_number = Button(self.lotto_frame, text="39",  borderwidth=3, bg="yellow")
        self.lotto_number.place(x=100, y=200)
        self.lotto_number = Button(self.lotto_frame, text="40",  borderwidth=3, bg="yellow")
        self.lotto_number.place(x=150, y=200)
        self.lotto_number = Button(self.lotto_frame, text="41",  borderwidth=3, bg="yellow")
        self.lotto_number.place(x=200, y=200)
        self.lotto_number = Button(self.lotto_frame, text="42",  borderwidth=3, bg="yellow")
        self.lotto_number.place(x=250, y=200)

        self.lotto_number = Button(self.lotto_frame, text="43",  borderwidth=3, bg="yellow")
        self.lotto_number.place(x=0, y=200)
        self.lotto_number = Button(self.lotto_frame, text="44",  borderwidth=3, bg="yellow")
        self.lotto_number.place(x=50, y=200)
        self.lotto_number = Button(self.lotto_frame, text="45",  borderwidth=3, bg="yellow")
        self.lotto_number.place(x=100, y=200)
        self.lotto_number = Button(self.lotto_frame, text="46",  borderwidth=3, bg="yellow")
        self.lotto_number.place(x=150, y=200)
        self.lotto_number = Button(self.lotto_frame, text="47",  borderwidth=3, bg="yellow")
        self.lotto_number.place(x=200, y=200)
        self.lotto_number = Button(self.lotto_frame, text="48",  borderwidth=3, bg="yellow")
        self.lotto_number.place(x=250, y=200)
        self.lotto_number = Button(self.lotto_frame, text="49",  borderwidth=3, bg="yellow")
        self.lotto_number.place(x=300, y=200)

# Creating Label for sets
        self.powerball_set = Label(window, text="POWER BALL", width=15, bg="green")
        self.powerball_set.place(x=180, y=450)
        self.powerball_results = Entry(window, borderwidth=5)
        self.powerball_results.place(x=150, y=500)
        self.powerball_set = Label(window, text="LOTTO PLUS", width=15, bg="gold")
        self.powerball_set.place(x=180, y=550)
        self.powerball_results = Entry(window, borderwidth=5)
        self.powerball_results.place(x=150, y=600)
        self.powerball_set = Label(window, text="LOTTO", width=15, bg="goldenrod")
        self.powerball_set.place(x=180, y=650)
        self.powerball_results = Entry(window, borderwidth=5)
        self.powerball_results.place(x=150, y=700)

        self.powerball_btn = Button(window, text="PLAY POWERBALL", bg='green', borderwidth=5)
        self.powerball_btn.place(x=5, y=780)
        self.lotto_plus_btn = Button(window, text="PLAY LOTTO PLUS", bg='gold', borderwidth=5)
        self.lotto_plus_btn.place(x=200, y=780)
        self.lotto_btn = Button(window, text="PLAY LOTTO", bg='goldenrod', borderwidth=5)
        self.lotto_btn.place(x=400, y=780)

        self.replay_btn = Button(window, text="REPLAY", bg='blue', borderwidth=5)
        self.replay_btn.place(x=50, y=850)
        self.prize_btn = Button(window, text="CLAIM PRIZE!!!", bg='red', borderwidth=5)
        self.prize_btn.place(x=200, y=850)
        self.exit_btn = Button(window, text="EXIT", bg='gold', borderwidth=5)
        self.exit_btn.place(x=400, y=850)





# Defining Functions














lottery = LotteryNumbers(window)
window.mainloop()
