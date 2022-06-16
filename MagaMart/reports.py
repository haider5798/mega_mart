from tkinter import *
from tkinter import ttk
import connection as connection
import time
from tkinter import messagebox


class Reports:
    def __init__(self, window, parent):
        self.window = window
        self.dashboard = parent
        self.window.title('MMR')
        self.window.geometry('720x620+323+50')
        self.window.resizable(False, False)
        style = ttk.Style()
        style.theme_use('clam')

        # .....................................VARIABLE DECLARATION.......................................#
        self.date_time = StringVar()
        self.date_time.set(time.strftime('%d-%m-%y'))
        self.grocery_profit = IntVar()
        self.cosmetics_profit = IntVar()
        self.medicine_profit = IntVar()
        self.cosmetics_sales = IntVar()
        self.medicine_sales = IntVar()
        self.grocery_sales = IntVar()
        self.cosmetics_profit_percentage = StringVar()
        self.cosmetics_profit_percentage.set('0%')
        self.grocery_profit_percentage = StringVar()
        self.grocery_profit_percentage.set('0%')
        self.medicine_profit_percentage = StringVar()
        self.medicine_profit_percentage.set('0%')

        # .....................................MAINFRAME.................................................#
        main_frame = Frame(self.window, bd=2, relief=GROOVE)
        main_frame.place(x=0, y=0, relwidth=1, relheight=1)
        r_title = Frame(self.window, bd=4, relief=GROOVE)
        r_title.place(relwidth=1, relheight=0.1)
        self.Tab_Title = Label(r_title, text='MegaMart Sales Report', font=('Times New Roman', 14, 'bold'), bg='brown',
                               fg='white', pady=5)
        self.Tab_Title.place(relx=0, rely=0, relwidth=1, relheight=1)

        # .....................................VIEW FRAME.................................................#
        view_frame = Frame(main_frame, bd=2, relief=GROOVE)
        view_frame.place(relx=0, rely=0.1, relwidth=1, relheight=0.6)

        scroll_x = Scrollbar(view_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(view_frame, orient=VERTICAL)
        self.user_view = ttk.Treeview(view_frame, columns=('date', 'time', 'pid', 'pro_cat', 'qty',
                                                           'unit_price', 'profit'),
                                      xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.configure(command=self.user_view.xview)
        scroll_y.configure(command=self.user_view.yview)
        self.user_view.heading('date', text='Date')
        self.user_view.heading('time', text='Time')
        self.user_view.heading('pid', text='Product ID')
        self.user_view.heading('pro_cat', text='Product Category')
        self.user_view.heading('qty', text='Quantity')
        self.user_view.heading('unit_price', text='Unit Price')
        self.user_view.heading('profit', text='Profit')
        self.user_view['show'] = 'headings'
        self.user_view.column('date', width=100)
        self.user_view.column('time', width=100)
        self.user_view.column('pid', width=100)
        self.user_view.column('pro_cat', width=120)
        self.user_view.column('qty', width=100)
        self.user_view.column('unit_price', width=80)
        self.user_view.column('profit', width=80)
        self.user_view.pack(fill=BOTH, expand=1)
        self.fetch_ud()

        # .....................................CALCULATION FRAME.................................................#
        calculation_frame = Frame(main_frame, bd=2, relief=GROOVE)
        calculation_frame.place(relx=0, rely=0.7, relwidth=1, relheight=0.3)

        self.lbl1 = Label(calculation_frame, text='Total Sales', font=('Times New Roman', 14), padx=4, pady=3)
        self.lbl1.grid(row=2, column=0, pady=3, padx=3, sticky=W)
        self.lbl1 = Label(calculation_frame, text='Profit Percentages', font=('Times New Roman', 14), padx=4, pady=3)
        self.lbl1.grid(row=3, column=0, pady=3, padx=3, sticky=W)
        self.lbl1 = Label(calculation_frame, text='Total Profits', font=('Times New Roman', 14), padx=4, pady=3)
        self.lbl1.grid(row=4, column=0, pady=3, padx=3, sticky=W)

        self.lbl1 = Label(calculation_frame, text='Grocery', font=('Times New Roman', 14), padx=4, pady=3)
        self.lbl1.grid(row=1, column=1, pady=3, padx=5)
        self.entry1 = Entry(calculation_frame, width=20, textvariable=self.grocery_sales, font=('Times New Roman', 12),
                            bd=2, relief=GROOVE).grid(row=2, column=1, padx=10)
        self.entry11 = Entry(calculation_frame, width=20, textvariable=self.grocery_profit_percentage,
                             font=('Times New Roman', 12), bd=2, relief=GROOVE).grid(row=3, column=1, padx=10)
        self.entry12 = Entry(calculation_frame, width=20, textvariable=self.grocery_profit,
                             font=('Times New Roman', 12), bd=2, relief=GROOVE).grid(row=4, column=1, padx=10)
        self.lbl2 = Label(calculation_frame, text='Cosmetics', font=('Times New Roman', 14), padx=4, pady=3)
        self.lbl2.grid(row=1, column=2, pady=3, padx=10)
        self.entry2 = Entry(calculation_frame, width=20, textvariable=self.cosmetics_sales,
                            font=('Times New Roman', 12), bd=2, relief=GROOVE).grid(row=2, column=2, padx=10)
        self.entry21 = Entry(calculation_frame, width=20, textvariable=self.cosmetics_profit_percentage,
                             font=('Times New Roman', 12), bd=2, relief=GROOVE).grid(row=3, column=2, padx=10)
        self.entry22 = Entry(calculation_frame, width=20, textvariable=self.cosmetics_profit,
                             font=('Times New Roman', 12), bd=2, relief=GROOVE).grid(row=4, column=2, padx=10)
        self.lbl3 = Label(calculation_frame, text='Medicine', font=('Times New Roman', 14), padx=4, pady=3)
        self.lbl3.grid(row=1, column=3, pady=3, padx=10)
        self.entry3 = Entry(calculation_frame, width=20, textvariable=self.medicine_sales, font=('Times New Roman', 12),
                            bd=2, relief=GROOVE).grid(row=2, column=3, padx=10)
        self.entry31 = Entry(calculation_frame, width=20, textvariable=self.medicine_profit_percentage,
                             font=('Times New Roman', 12),
                             bd=2, relief=GROOVE).grid(row=3, column=3, padx=10)
        self.entry32 = Entry(calculation_frame, width=20, textvariable=self.medicine_profit,
                             font=('Times New Roman', 12),
                             bd=2, relief=GROOVE).grid(row=4, column=3, padx=10)
        btn = Button(calculation_frame, text='Generate Report', bd=2, relief=GROOVE,
                     font=('Times New Roman', 12, 'bold'), fg='white', bg='grey', command=self.report_gen)
        btn.grid(row=5, column=3, padx=12)
        self.profit_per()
        self.window.bind("<Destroy>", self.on_destroy)
        self.cal_profit()

    def fetch_ud(self):
        try:
            con = connection.connect_db()
            cur = con.cursor()
            cur.execute(
                'SELECT `date`, `time`, `pid`, `pro_cat`, `qty`, `unit_price`, `profit` FROM `salesreport`')
            rows = cur.fetchall()
            if len(rows) != 0:
                self.user_view.delete(*self.user_view.get_children())
                for row in rows:
                    self.user_view.insert('', END, values=row)
                con.commit()
            connection.close_con(con, cur)
        except Exception as Error:
            print(Error)

    def profit_per(self):
        con = connection.connect_db()
        cur = con.cursor()
        cur.execute(
            'SELECT `cat_name`, `profit` FROM `category`')
        rows = cur.fetchall()
        if rows:
            self.grocery_profit_percentage.set(str(rows[0][1])+'%')
            self.cosmetics_profit_percentage.set(str(rows[1][1])+'%')
            self.medicine_profit_percentage.set(str(rows[2][1])+'%')
        con1 = connection.connect_db()
        cur1 = con1.cursor()
        cur1.execute(
            'SELECT COUNT(*) FROM `salesreport` WHERE `pro_cat`= "Grocery"')
        gro_itm = cur1.fetchone()
        if gro_itm is not None:
            self.grocery_sales.set(gro_itm[0])
        con2 = connection.connect_db()
        cur2 = con2.cursor()
        cur2.execute(
            'SELECT COUNT(*) FROM `salesreport` WHERE `pro_cat`= "Medicine"')
        med_itm = cur2.fetchone()
        if med_itm is not None:
            self.medicine_sales.set(med_itm[0])
        con3 = connection.connect_db()
        cur3 = con1.cursor()
        cur3.execute(
            'SELECT COUNT(*) FROM `salesreport` WHERE `pro_cat`= "Cosmetics"')
        cos_itm = cur3.fetchall()
        if cos_itm is not None:
            self.cosmetics_sales.set(cos_itm[0])
        connection.close_con(con1, cur1)
        connection.close_con(con2, cur2)
        connection.close_con(con3, cur3)

    def cal_profit(self):
        con1 = connection.connect_db()
        cur1 = con1.cursor()
        cur1.execute('SELECT SUM(profit) FROM `salesreport` WHERE `pro_cat`= "Grocery"')
        gro_itm = cur1.fetchone()
        if gro_itm is None:
            self.grocery_profit.set(0)
        else:
            self.grocery_profit.set(gro_itm[0])
        con2 = connection.connect_db()
        cur2 = con2.cursor()
        cur2.execute(
            'SELECT SUM(profit) FROM `salesreport` WHERE `pro_cat`= "Medicine"')
        med_itm = cur2.fetchone()
        if med_itm is None:
            self.medicine_profit.set(0)
        else:
            self.medicine_profit.set(med_itm[0])
        con3 = connection.connect_db()
        cur3 = con1.cursor()
        cur3.execute(
            'SELECT SUM(profit) FROM `salesreport` WHERE `pro_cat`= "Cosmetics"')
        cos_itm = cur3.fetchall()
        if cos_itm is None:
            self.cosmetics_profit.set(0)
        else:
            self.cosmetics_profit.set(cos_itm[0])
        connection.close_con(con1, cur1)
        connection.close_con(con2, cur2)
        connection.close_con(con3, cur3)

    def on_destroy(self, event):
        if event.widget == self.window:
            self.dashboard.deiconify()

    def report_gen(self):
        con1 = connection.connect_db()
        cur1 = con1.cursor()
        query = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'salesreport'"
        cur1.execute(query)
        column_name = cur1.fetchall()
        con = connection.connect_db()
        cur = con.cursor()
        cur.execute('SELECT * FROM `salesreport`')
        rows = cur.fetchall()
        if rows:
            with open(f'static/reports/{self.date_time.get()}.csv', 'w') as f:
                for column in column_name:
                    f.write(column[0]+',')
                f.write('\n')
                for row in rows:
                    for element in row:
                        f.write(str(element)+',')
                    f.write('\n')
                f.close()
            messagebox.showinfo('Success', 'Report Generated Successfully')
        else:
            messagebox.showerror('Error', 'No Record Found')

        connection.close_con(con, cur)


if __name__ == '__main__':
    app = Tk()
    Reports(app)
    app.mainloop()
