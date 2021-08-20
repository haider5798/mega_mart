from tkinter import *
import time
import connection as connection
import tempfile
import os
import tkinter.messagebox as messagebox
from Prod_Return import ProdReturn
import random
# import cv2
# from pyzbar.pyzbar import decode


class Pos:
    def __init__(self, root, root_window):
        self.window = root
        self.dashboard = root_window
        self.window.title('MegaMart Automation')
        self.window.geometry('1280x700+43+0')
        self.window.resizable(False, False)
# ---------------------Variable Declaration-------------------------------------#
        self._contents = []
        self._date = StringVar()
        self._time = StringVar()
        self._day = StringVar()
        self.customer_name = StringVar()
        self.contact = StringVar()
        self.product_id = StringVar()
        self.product_name = StringVar()
        self.pro_cat = StringVar()
        self.unit_price = IntVar()
        self.ava_quantity = IntVar()
        self.quantity = IntVar()
        self.bill_no = StringVar()
        self.return_pid = StringVar()
# ---------------------Variable Declaration END-------------------------------------#
        mainframe1 = Frame(self.window, bg='teal', bd=2, relief=GROOVE)
        mainframe1.place(relwidth=1, relheight=1)

        mainframe2 = Frame(mainframe1, bg='white', bd=2, relief=GROOVE)
        mainframe2.place(relx=0.02, rely=0.025, relwidth=0.96, relheight=0.95)
        Label(mainframe2, text='MegaMart Automation\nBilling System', font=('Times New Roman', 18, 'bold'),
              bg='white', fg='black').place(relx=0.375, rely=0.05, relwidth=0.25, relheight=0.09)
        self.time_lbl = Label(mainframe2, text='Time: '+self._time.get(), font=('Times New Roman', 13), bg='white',
                              fg='black', anchor="w")
        self.time_lbl.place(relx=0.865, rely=0.04, relwidth=0.13, relheight=0.05)
        self.date_lbl = Label(mainframe2, text='Date: '+self._date.get(), font=('Times New Roman', 13),
                              bg='white', fg='black', anchor="w")
        self.date_lbl.place(relx=0.865, rely=0.09, relwidth=0.13, relheight=0.05)
        self.day_lbl = Label(mainframe2, text='Day: '+self._day.get(), font=('Times New Roman', 13),
                             bg='white', fg='black', anchor="w")
        self.day_lbl.place(relx=0.865, rely=0.14, relwidth=0.13, relheight=0.05)
# ---------------------------------------------------------------------------------------------------------------------#
        frame1 = LabelFrame(mainframe2, text='Customer Details', bd=2, bg='white', font=('Times New Roman', 13, 'bold'))
        frame1.place(relx=0.02, rely=0.2, relwidth=0.96, relheight=0.1)
        search_bill_lbl = Label(frame1, text='Bill Number:', font=('Times New Roman', 12, 'bold'),
                                bg='white', fg='black')
        search_bill_lbl.place(relx=0.006, rely=0.1, relwidth=0.08, relheight=0.8)
        entry1 = Entry(frame1, textvariable=self.bill_no, font=('Times New Roman', 12), bg='light grey', bd=2,
                       relief=GROOVE)
        entry1.place(relx=0.09, rely=0.17, relwidth=0.15, relheight=0.65)
        button1 = Button(frame1, font=('Times New Roman', 12, 'bold'), bd=2, relief=GROOVE, bg='red', fg='white',
                         cursor='hand2', text='Search', command=self.search_bill)
        button1.place(relx=0.25, rely=0.2, relwidth=0.07, relheight=0.6)
        cus_lbl = Label(frame1, text='Customer Name:', font=('Times New Roman', 12, 'bold'),
                        bg='white', fg='black')
        cus_lbl.place(relx=0.38, rely=0.1, relwidth=0.1, relheight=0.8)
        entry2 = Entry(frame1, textvariable=self.customer_name, font=('Times New Roman', 12), bg='light grey', bd=2,
                       relief=GROOVE)
        entry2.place(relx=0.49, rely=0.17, relwidth=0.15, relheight=0.63)
        contact_lbl = Label(frame1, text='Customer Contact:', font=('Times New Roman', 12, 'bold'),
                            bg='white', fg='black')
        contact_lbl.place(relx=0.71, rely=0.1, relwidth=0.13, relheight=0.8)
        entry3 = Entry(frame1, textvariable=self.contact, font=('Times New Roman', 12), bg='light grey', bd=2,
                       relief=GROOVE)
        entry3.place(relx=0.84, rely=0.17, relwidth=0.15, relheight=0.63)
# ---------------------------------------------------------------------------------------------------------------------#
        frame2 = LabelFrame(mainframe2, text='Products', bd=2, bg='white', font=('Times New Roman', 13, 'bold'))
        frame2.place(relx=0.02, rely=0.35, relwidth=0.43, relheight=0.6)
        lbl1 = Label(frame2, text='Product ID', font=('Times New Roman', 12), bg='white', fg='black', anchor="w")
        lbl1.place(relx=0.005, rely=0.03, relwidth=0.8, relheight=0.08)
        pid_entry = Entry(frame2, textvariable=self.product_id, font=('Times New Roman', 12), bg='light grey', bd=2,
                          relief=GROOVE)
        pid_entry.place(relx=0.005, rely=0.10, relwidth=0.6, relheight=0.066)
        vb = Button(frame2, font=('Times New Roman', 12, 'bold'), bd=2, relief=GROOVE, bg='brown', fg='white',
                    text='View Details', command=self.view_details)
        vb.place(relx=0.61, rely=0.10, relwidth=0.19, relheight=0.067)
        lbl2 = Label(frame2, text='Product Name:', font=('Times New Roman', 12), bg='white', fg='black', anchor="w")
        lbl2.place(relx=0.005, rely=0.18, relwidth=0.8, relheight=0.08)
        self.pna_entry = Entry(frame2, textvariable=self.product_name, font=('Times New Roman', 12), bg='light grey',
                               bd=2, relief=GROOVE, state=DISABLED)
        self.pna_entry.place(relx=0.005, rely=0.25, relwidth=0.8, relheight=0.066)
        lbl3 = Label(frame2, text='Unit Price:', font=('Times New Roman', 12),
                     bg='white', fg='black', anchor="w")
        lbl3.place(relx=0.005, rely=0.33, relwidth=0.8, relheight=0.08)
        self.up_entry = Entry(frame2, textvariable=self.unit_price, font=('Times New Roman', 12), bg='light grey', bd=2,
                              relief=GROOVE, state=DISABLED)
        self.up_entry.place(relx=0.005, rely=0.4, relwidth=0.8, relheight=0.066)
        lbl4 = Label(frame2, text='Available Quantity:', font=('Times New Roman', 12), bg='white',
                     fg='black', anchor="w")
        lbl4.place(relx=0.005, rely=0.48, relwidth=0.8, relheight=0.08)
        Entry(frame2, textvariable=self.ava_quantity, font=('Times New Roman', 12), bg='light grey', bd=2,
              relief=GROOVE, state=DISABLED).place(relx=0.005, rely=0.55, relwidth=0.8, relheight=0.066)
        lbl5 = Label(frame2, text='Quantity:', font=('Times New Roman', 12), bg='white', fg='black', anchor="w")
        lbl5.place(relx=0.005, rely=0.63, relwidth=0.8, relheight=0.08)
        Entry(frame2, textvariable=self.quantity, font=('Times New Roman', 12), bg='light grey', bd=2,
              relief=GROOVE).place(relx=0.005, rely=0.7, relwidth=0.8, relheight=0.066)
        self.adbtn = Button(frame2, font=('Times New Roman', 12, 'bold'), bd=2, relief=GROOVE, bg='red', fg='white',
                            cursor='hand2', text='Add', command=self.add, state=DISABLED)
        self.adbtn.place(relx=0.025, rely=0.8, relwidth=0.15, relheight=0.066)
        self.totbtn = Button(frame2, font=('Times New Roman', 12, 'bold'), bd=2, relief=GROOVE, bg='red', fg='white',
                             cursor='hand2', text='Total', command=self.total, state=DISABLED)
        self.totbtn.place(relx=0.225, rely=0.8, relwidth=0.15, relheight=0.066)
        self.receipt_btn = Button(frame2, font=('Times New Roman', 12, 'bold'), bd=2, relief=GROOVE, bg='red',
                                  cursor='hand2', fg='white', text='Receipt', command=self.receipt, state=NORMAL)
        self.receipt_btn.place(relx=0.42, rely=0.8, relwidth=0.15, relheight=0.066)
        Button(frame2, font=('Times New Roman', 12, 'bold'), bd=2, relief=GROOVE, bg='red', fg='white', text='Reset',
               cursor='hand2', state=NORMAL, command=self.reset).place(relx=0.61, rely=0.8,
                                                                       relwidth=0.15, relheight=0.066)
        Button(frame2, font=('Times New Roman', 12, 'bold'), bd=2, relief=GROOVE, bg='red', fg='white',
               cursor='hand2', text='Returns', command=self.pro_return).place(relx=0.80, rely=0.8,
                                                                              relwidth=0.15, relheight=0.066)
        self.print_btn = Button(frame2, font=('Times New Roman', 12, 'bold'), bd=2, relief=GROOVE, bg='gold', fg='white',
                                cursor='hand2', text='Print', command=self.print, state=DISABLED)
        self.print_btn.place(relx=0.35, rely=0.9, relwidth=0.3, relheight=0.08)

# ---------------------------------------------------------------------------------------------------------------------#
        frame3 = LabelFrame(mainframe2, text='Bill Generation', bd=2, bg='white', font=('Times New Roman', 13, 'bold'))
        frame3.place(relx=0.46, rely=0.35, relwidth=0.52, relheight=0.6)
        self.textbox = Text(frame3, font=('arial', 10))
        self.textbox.pack(fill=BOTH)
        self.window.bind("<Destroy>", self.on_destroy)
        self.welcome_bill()
        self.clock()

    def welcome_bill(self):
        self.textbox.delete('1.0', END)
        self.textbox.insert(END, '\t\t\t\tMegaMart Automation\n'
                                 '\t\t\t\tNawa Bazzar Kasur\n'
                                 '\t\t\t\tTelephone No: +92 345678910\n'
                                 '\t\t\t\tHelpline: 0800 78601')
        self.textbox.insert(END, f'\n\nBill Number: ')
        self.textbox.insert(END, f'\t\t\t\tCustomer Name: ')
        self.textbox.insert(END, f'\t\t\t\tContact No: ')
        self.textbox.insert(END, '\n'+'-'*156 + '\n Products\t\t\t\t\tQuantity\t\t\t\t'
                                 '\tUnit Price'+'\n'+'-'*156)

    def welcome_bill_extended(self):
        self.textbox.delete('1.0', END)
        self.textbox.insert(END, '\t\t\t\tMegaMart Automation\n'
                                 '\t\t\t\tNawa Bazzar Kasur\n'
                                 '\t\t\t\tTelephone No: +92 345678910\n'
                                 '\t\t\t\tHelpline: 0800 78601')
        self.textbox.insert(END, f'\n\nBill Number: {self.bill_no.get()}')
        self.textbox.insert(END, f'\t\t\t\tCustomer Name: {self.customer_name.get()}')
        self.textbox.insert(END, f'\t\t\t\tContact No: {self.contact.get()}')
        self.textbox.insert(END, '\n'+'-'*156 + '\n Products\t\t\t\t\tQuantity\t\t\t\t'
                                 '\tUnit Price'+'\n'+'-'*156)

    def search_bill(self):
        con = connection.connect_db()
        cur = con.cursor()
        query = 'SELECT `date` FROM `bills` WHERE `billno`="' + str(self.bill_no.get()) + '"'
        cur.execute(query)
        data = cur.fetchone()
        con.commit()
        if data is not None:
            try:
                with open(f'{self.bill_no.get()}.txt', 'r') as f:
                    text = f.read()
                    self.textbox.delete('1.0', END)
                    self.textbox.insert(END, text)
            except FileNotFoundError:
                messagebox.showerror('Error', f'Bill No {self.bill_no.get()} Might have deleted')
        else:
            messagebox.showerror('Error', f'Bill No {self.bill_no.get()} Does not Exist in Records')

    def add(self):
        if self.product_id.get() != '' or self.product_name.get() != '':
            if self.quantity.get() is not 0:
                self.textbox.insert(END, f'\n{self.product_name.get()}'
                                         f'  \t\t\t\t\t{self.quantity.get()}'
                                         f'    \t\t\t\t\t{self.unit_price.get()}')
                total = self.quantity.get()*self.unit_price.get()
                self._contents.append(total)
                profit = (5/100)*total
                con = connection.connect_db()
                cur = con.cursor()
                query = "INSERT INTO `salesreport` VALUES " \
                        "('','" + self._date.get() + "','" + self._time.get() + "', '" + self.product_id.get() + "', '" + str(
                           self.pro_cat.get()) + "', '" + str(self.quantity.get()) + "', '" + str(self.unit_price.get()) + "', '"+str(profit)+"')"
                cur.execute(query)
                con.commit()
                connection.close_con(con, cur)
                self.update_products()
                self.totbtn.config(state=NORMAL)
            else:
                messagebox.showwarning('Warning', 'Quantity should be valid')
        else:
            messagebox.showwarning('Warning', 'No Product Selected')

    @staticmethod
    def pro_return():
        top = Toplevel()
        top.grab_set()
        ProdReturn(top)
        top.mainloop()

    def total(self):
        total = sum(self._contents)
        self.textbox.insert(END, '\n'+'*'*125)
        self.textbox.insert(END, '\n'+'Total: '+' '*125 + f'{total}')
        self.print_btn.config(state=NORMAL)

    def receipt(self):
        if self.bill_no.get() != '':
            self.adbtn.config(state=NORMAL)
            self.welcome_bill_extended()
            self.receipt_btn.config(state=DISABLED)
        else:
            messagebox.showerror('Error', 'Bill No is Mandatory')

    def print(self):
        if self.bill_no.get() != '':
            q = self.textbox.get('1.0', 'end-1c')
            with open(f'{self.bill_no.get()}.txt', 'w') as f:
                f.write(q)
            filename = tempfile.mktemp('.txt')
            open(filename, 'w').write(q)
            os.startfile(filename, 'Print')
            try:
                con = connection.connect_db()
                cur = con.cursor()
                query = "INSERT INTO `bills` VALUES" \
                        " ('','"+self._date.get()+"','"+self._time.get()+"', '"+self.bill_no.get()+"')"
                cur.execute(query)
                con.commit()
                self.welcome_bill()
                self.reset()
            except Exception as Error:
                print(Error)
                messagebox.showerror('Error', 'Bill Not Saved')
        else:
            messagebox.showerror('Error', 'Bill No Required')

    def update_products(self):
        new_qty = self.ava_quantity.get() - self.quantity.get()
        con2 = connection.connect_db()
        cur2 = con2.cursor()
        query2 = "UPDATE `products` SET `qty`= '" + str(new_qty) + "' WHERE pid= '" + str(self.product_id.get()) + "'"
        cur2.execute(query2)
        con2.commit()

    def reset(self):
        self.product_name.set('')
        self.unit_price.set(0)
        self.product_id.set('')
        self.customer_name.set('')
        self.contact.set('')
        self.quantity.set(0)
        self.welcome_bill()
        self._contents = []
        self.ava_quantity.set(0)
        self.bill_no.set(f'{random.randrange(1, 10**4):04}')  # returns a 4 digit number from 1 to 10^4
        self.receipt_btn.config(state=NORMAL)

    def clock(self):
        self._time.set(time.strftime('%I:%M:%S %p'))
        self._day.set(time.strftime('%A'))
        self._date.set(time.strftime('%d-%m-%y'))
        self.time_lbl.config(text='Time: ' + str(self._time.get()))
        self.day_lbl.config(text='Day: ' + str(self._day.get()))
        self.date_lbl.config(text='Date: ' + str(self._date.get()))
        self.time_lbl.after(1000, self.clock)

    def view_details(self):
        try:
            con = connection.connect_db()
            cur = con.cursor()
            query = 'SELECT `pname`, `qty`, `unit_price`, `pro_cat` FROM `products` WHERE' \
                    ' `pid`="' + str(self.product_id.get()) + '"'
            cur.execute(query)
            data = cur.fetchone()
            con.commit()
        except Exception as Error:
            data = (None,)
            print(Error)
        if data is not None:
            self.product_name.set(data[0])
            self.ava_quantity.set(data[1])
            self.unit_price.set(data[2])
            self.pro_cat.set(data[3])
            self.quantity.set(1)
        else:
            messagebox.showerror('Error', 'Incorrect Product Id')

    def on_destroy(self, event):
        if event.widget == self.window:
            self.dashboard.deiconify()

    # def qr_reader(self):
    #     cap = cv2.VideoCapture(0)
    #     cap.set(3, 640)  # Width
    #     cap.set(4, 480)  # Height
    #     camera = True
    #     while camera is True:
    #         success, frame = cap.read()
    #         for code in decode(frame):
    #             print(code.data.decode('utf-8'))
    #             time.sleep(2)
    #         cv2.imshow('Testing....Barcode....Scan', frame)
    #         cv2.waitKey(1)


# if __name__ == '__main__':
#     app = Tk()
#     Pos(app)
#     app.mainloop()
