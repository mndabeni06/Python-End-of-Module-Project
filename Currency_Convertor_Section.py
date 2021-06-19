from tkinter import *
from datetime import datetime
from tkinter import ttk
import requests
from tkinter import messagebox
root = Tk()
root.geometry("600x400")
root.title("Currency Converter")
canvas = Canvas(bg='skyblue', height=250, width=300)
canvas.pack(expand= YES, fill=BOTH)

# Adding Widgets to the Gui
l1 = Label(root,text="USD Currency Converter", font=('Sans Serif','12','bold'))
l1.place(x=150,y=15)
amt = Label(root,text="Amount",font=('Sans Serif',10,'bold'))
amt.place(x=20,y=80)
e1 = Entry(root,width=20,borderwidth=1,font=('roboto',10,'bold'))
e1.place(x=20,y=100)

# Adding String Variables
c1 = StringVar()
c2 = StringVar()
default_currency1 = ttk.Combobox(root, width = 20, textvariable = c1, state='readonly',font=('verdana',10,'bold'))
# Adding combobox drop down list
default_currency1['values'] = (
                          ' USD',
                          )

default_currency1.place(x=300,y=80)
default_currency1.current(0)


e2 = Entry(root,width=20,borderwidth=1,font=('roboto',10,'bold'))
e2.place(x=20,y=150)


default_currency2 = ttk.Combobox(root, width = 20, textvariable = c2, state='readonly',font=('verdana','10','bold'))

# Adding combobox drop down list
default_currency2['values'] =('ALL',
                          ' EUR',
                            'ZAR',
                          ' NZD',
                          ' AWG',
                          ' AUD',
                          ' AZN',
                          ' BSD',
                          ' BBD',
                          ' BYN',
                          ' BZD ',
                          ' BMD',
                          ' BOB',
                          'CHF',
                          ' BWP',
                          ' BGN',
                          ' BND',
                          ' KHR',
                          ' CAD',
                          ' KYD',
                          ' CLP',
                          ' CNY',
                          ' COP  ',
                          ' CRC',
                          ' HRK',
                          'CUP',
                          'CZK',
                          ' DKK',
                          ' DOP',
                          ' XCD',
                          ' EGP',
                          ' SVC',
                          ' AUD',
                          ' FJD',
                          ' GHS ',
                          ' GIP',
                          ' GTQ',
                          'GGP',
                          ' GYD',
                          ' HNL ',
                          ' HKD',
                          ' HUF',
                          ' ISK',
                          ' INR',
                          ' IDR',
                          ' IRR',
                          ' IMP ',
                          ' ILS',
                          ' JMD',
                          'JPY',
                          'KZT',
                          ' KPW',
                          ' KRW',
                          ' KGS',
                          ' LAK',
                          ' LBP',
                          ' LRD',
                          ' MKD',
                          ' MYR',
                          ' MUR ',
                          ' MXN',
                          ' MNT',
                          'MZN',
                          ' NAD',
                          ' NPR',
                          ' ANG',
                          ' NZD ',
                          ' NIO ',
                          ' NGN',
                          ' NOK',
                          ' OMR ',
                          ' PKR ',
                          ' PAB',
                          ' PYG',
                          'PEN',
                          'PHP',
                          ' PLN',
                          ' QAR',
                          ' RON',
                          ' RUB',
                          ' SHP',
                          ' SAR',
                          ' RSD',
                          ' SCR ',
                          ' SGD ',
                          ' SBD',
                          ' SOS',
                          'ZAR',
                          ' LKR',
                          ' SEK ',
                          ' CHF',
                          ' SRD',
                          ' SYP',
                          ' TWD',
                          ' THB',
                          ' TTD',
                          ' TRY ',
                          ' TVD',
                          ' UAH',
                          'GBP  ',
                          ' UYU',
                          ' UZS ',
                          ' VEF ',
                          ' VND',
                          ' YER',
                          'ZWD',)

default_currency2.place(x=300,y=150)
default_currency2.current()


text = Text(root,height=7,width=52,font=('verdana','10','bold'))
text.place(x=100,y=250)


# Defining functions
def show_data():
        amount = e1.get()
        from_currency  = c1.get()
        to_currency = c2.get()
        url =  ' http://api.currencylayer.com/live?access_key=4273d2c37f738367f08780b934ce7dda&format=1'

        if amount == '':
               messagebox.showerror("Currency Converter", "Oops! Please Fill the Amount")
        elif to_currency == '':
                messagebox.showerror("Currency Converter", "Please Choose the Currency")

        else:
                data = requests.get(url).json()
                currency = from_currency.strip()+to_currency.strip()
                amount = int(amount)
                cc = data['quotes'][currency]
                cur_conv = cc*amount
                e2.insert(0,cur_conv)

                text.insert('end',f'{amount} United State Dollar Equals {cur_conv} {to_currency} \n\n Last Time Update --- \t {datetime.now()}')

def clear():
        e1.delete(0,'end')
        e2.delete(0,'end')
        text.delete(1.0,'end')




# Search Button
B = Button(root,text="Search",command=show_data,font=('verdana','10','bold'),borderwidth=3,bg="Goldenrod",fg="white")
B.place(x=20,y=120)

# Clear Button
clear = Button(root,text="Clear",command=clear,font=('verdana','10','bold'),borderwidth=3,bg="blue",fg="white")
clear.place(x=20,y=170)

# Exit Button
btn_exit = Button(root, text="Exit", command=root.quit, borderwidth=5)
btn_exit.place(x=5, y=350)


root.mainloop()
