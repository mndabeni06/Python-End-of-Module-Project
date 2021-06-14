# Masimthembe Ndabeni
from doctest import master
from tkinter import *
import multiprocessing
from playsound import playsound
from validate_email import validate_email
root = Tk()
from tkinter import ttk
from tkinter import messagebox


# creating a mother class
class LotteryNumbers:
    def __init__(self, master):
        self.root = root
        self.root.title("Ithuba National Lottery of South Africa Lotto Station")
        self.root.geometry("600x500")
        self.root.config(bg="black")

# Age Check


lottery = LotteryNumbers(root)
root.mainloop()
