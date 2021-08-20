from tkinter import *
from tkinter import ttk
import tkinter.messagebox as messagebox
import connection as connection


class Inventory:
    def __init__(self, args, root):
        self.window = args
        self.dashboard = root
        self.window.title('MMA')
        self.window.geometry('1280x700+43+0')
        self.window.resizable(False, False)
        style = ttk.Style()
        style.theme_use('clam')
        # ---------------------Variable Declaration-------------------------------------#
        self.search_item = StringVar()
        self.categories = [
            'Select',
            'Cosmetics',
            'Grocery',
            'Medicine',
        ]
        # ...............................................................................................................................................

        main_frame = Frame(self.window, bd=2, relief=GROOVE)
        main_frame.place(x=0, y=0, relwidth=1, relheight=1)
        r_title = Frame(self.window, bd=4, relief=GROOVE)
        r_title.place(relwidth=1, relheight=0.15)
        self.Tab_Title = Label(r_title, text='MegaMart Automation', font=('Castellar', 14, 'bold'), fg='brown', pady=5)
        self.Tab_Title.place(relx=0, rely=0, relwidth=1, relheight=1)

        b_frame = Frame(main_frame)
        b_frame.place(relx=0, rely=0.15, relwidth=1, relheight=0.85)

        # .................................................................................................#

        d_frame = Frame(b_frame, bd=2, relief=GROOVE)
        d_frame.place(relx=0, rely=0, relwidth=0.4, relheight=1)

        data_lbl_frame = Frame(d_frame, bd=2, relief=GROOVE)
        data_lbl_frame.place(relx=0.1, rely=0.02, relwidth=0.8, relheight=0.1)

        self.Nt_lbl = Label(data_lbl_frame, text='Data Entry', font=('Times New Roman', 18, 'bold'))
        self.Nt_lbl.place(rely=0, relwidth=1, relheight=1)

        # .............................................DATA FRAME....................................................#

        data_frame = Frame(d_frame)
        data_frame.place(relx=0.04, rely=0.12, relwidth=0.92, relheight=0.9)
        self.pid = StringVar()
        self.N_lbl = Label(data_frame, text='Product id', font=('Times New Roman', 14), padx=4, pady=3)
        self.N_lbl.grid(row=1, column=0, pady=3, sticky=W)
        self.N_entry = Entry(data_frame, width=57, textvariable=self.pid, font=('Times New Roman', 12),
                             bd=2, relief=GROOVE).grid(row=2, column=0)
        self.pname = StringVar()
        self.FN_lbl = Label(data_frame, text='Product Name', font=('Times New Roman', 14), padx=4, pady=3)
        self.FN_lbl.grid(row=3, column=0, pady=3, sticky=W)
        self.FN_entry = Entry(data_frame, width=57, textvariable=self.pname, font=('Times New Roman', 12),
                              bd=2, relief=GROOVE).grid(row=4, column=0)
        self.pcategory = StringVar()
        self.L_ID_lbl = Label(data_frame, text='Product Category', font=('Times New Roman', 14), padx=4, pady=3)
        self.L_ID_lbl.grid(row=5, column=0, pady=3, sticky=W)
        self.L_ID_entry = ttk.Combobox(data_frame, width=55, textvariable=self.pcategory, font=('Times New Roman', 12))
        self.L_ID_entry['values'] = 'Select Category'
        self.L_ID_entry.grid(row=6, column=0)
        self.L_ID_entry.current(0)

        self.unitprice = IntVar()
        self.DESIGNATION_lbl = Label(data_frame, text='Unit Price', font=('Times New Roman', 14), padx=4, pady=3)
        self.DESIGNATION_lbl.grid(row=7, column=0, pady=3, sticky=W)
        self.DESIGNATION_entry = Entry(data_frame, width=57, textvariable=self.unitprice,
                                       font=('Times New Roman', 12), bd=2, relief=GROOVE).grid(row=8, column=0)
        self.quantity = IntVar()
        self.MS_lbl = Label(data_frame, text='Quantity', font=('Times New Roman', 14), padx=4, pady=3)
        self.MS_lbl.grid(row=9, column=0, pady=3, sticky=W)

        self.MS_entry = Entry(data_frame, width=57, textvariable=self.quantity, font=('Times New Roman', 12),
                              bd=2, relief=GROOVE)
        self.MS_entry.grid(row=10, column=0)

        self.location = StringVar()
        self.ADD_lbl = Label(data_frame, text='Address', font=('Times New Roman', 14), padx=4, pady=3)
        self.ADD_lbl.grid(row=11, column=0, pady=3, sticky=W)
        self.ADD_entry = Entry(data_frame, width=57, textvariable=self.location, font=('Times New Roman', 12), bd=2,
                               relief=GROOVE)
        self.ADD_entry.grid(row=12, column=0, columnspan=2)

        # ...............................................................................................
        b_d_frame = LabelFrame(d_frame, text='Controls', font=('Bell MT', 13, 'bold'))
        b_d_frame.place(relx=0.04, rely=0.78, relwidth=0.92, relheight=0.15)

        self.Button_Reg = Button(b_d_frame, text='Add', width=10, pady=4, font=('Bell MT', 12, 'bold'),
                                 cursor='hand2', command=self.add, bg='brown', fg='white').grid(row=1, column=0,
                                                                                                padx=3, pady=7)

        self.Button_Upd = Button(b_d_frame, text='Update', width=10, pady=4, font=('Bell MT', 12, 'bold'),
                                 cursor='hand2', command=self.update, bg='brown', fg='white').grid(row=1, column=1)

        self.Button_Cl = Button(b_d_frame, text='Clear', width=10, pady=4, font=('Bell MT', 12, 'bold'), cursor='hand2',
                                command=self.clear, bg='brown', fg='white').grid(row=1, column=2, padx=3)

        self.Button_Del = Button(b_d_frame, text='Delete', width=10, pady=4, font=('Bell MT', 12, 'bold'),
                                 cursor='hand2', command=self.delete, bg='brown', fg='white').grid(row=1, column=3)

        self.res_lbl = Label(d_frame, text='', font=('Times New Roman', 13), fg='Red')
        self.res_lbl.place(relx=0.2, rely=0.95, relwidth=0.6, relheight=0.03)
        # ............................................................................................
        right_frame = Frame(b_frame)
        right_frame.place(relx=0.4, rely=0, relwidth=0.6, relheight=1)

        b_s_frame = Frame(right_frame, bd=2, relief=GROOVE)
        b_s_frame.place(relx=0, rely=0, relwidth=1, relheight=0.1)
        # ..........................................................................................................
        search_button_frame = Frame(b_s_frame)
        search_button_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.EUI_lbl = Label(search_button_frame, text='Enter Product ID',
                             font=('Times New Roman', 14)).grid(row=1, column=0, pady=5, padx=5, sticky=W)
        self.EUI_entry = Entry(search_button_frame, width=20, font=('Times New Roman', 14),
                               textvariable=self.search_item).grid(row=1, column=1, padx=10, pady=4)

        self.EUI_Button = Button(search_button_frame, width=10, font=('Times New Roman', 14), bg='brown', fg='white',
                                 text='Search', command=self.search).grid(row=1, column=2, padx=8, pady=7)
        self.Clear_v_Button = Button(search_button_frame, width=10, font=('Times New Roman', 14), bg='brown',
                                     fg='white', text='Clear', command=lambda: self.search_item.set(''))
        self.Clear_v_Button.grid(row=1, column=3, padx=8)
        self.Show_all_Button = Button(search_button_frame, width=10, font=('Times New Roman', 14), bg='brown',
                                      fg='white', text='Show All', command=self.show_all).grid(row=1, column=4, padx=8)
        # ..........................................................................................................
        View_Frame = Frame(right_frame)
        View_Frame.place(relx=0, rely=0.1, relwidth=1, relheight=0.9)

        scroll_x = Scrollbar(View_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(View_Frame, orient=VERTICAL)
        self.user_view = ttk.Treeview(View_Frame, columns=('pid', 'pname', 'category', 'unitprice',
                                                           'quantity', 'location'),
                                      xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.configure(command=self.user_view.xview)
        scroll_y.configure(command=self.user_view.yview)
        self.user_view.heading('pid', text='PID')
        self.user_view.heading('pname', text='Product Name')
        self.user_view.heading('category', text='Category')
        self.user_view.heading('unitprice', text='UnitPrice')
        self.user_view.heading('quantity', text='Quantity')
        self.user_view.heading('location', text='Location')
        self.user_view['show'] = 'headings'
        self.user_view.column('pid', width=100)
        self.user_view.column('pname', width=150)
        self.user_view.column('category', width=100)
        self.user_view.column('unitprice', width=100)
        self.user_view.column('quantity', width=100)
        self.user_view.column('location', width=200)
        self.user_view.pack(fill=BOTH, expand=1)
        self.user_view.bind("<ButtonRelease-1>", self.get_data)
        self.fetch_ud()
        self.window.bind("<Destroy>", self.on_destroy)
        self.get_category()

    # # ........................................................................................................
    def fetch_ud(self):
        try:
            con = connection.connect_db()
            cur = con.cursor()
            cur.execute(
                'SELECT `pid`, `pname`, `pro_cat`, `unit_price`, `qty`, `location` FROM `products`')
            rows = cur.fetchall()
            self.user_view.delete(*self.user_view.get_children())
            if len(rows) != 0:
                for row in rows:
                    self.user_view.insert('', END, values=row)
                con.commit()
            connection.close_con(con, cur)
        except Exception as Error:
            print(Error)

    def get_data(self, event):
        cur_row = self.user_view.focus()
        content = self.user_view.item(cur_row)
        row = content['values']
        con = connection.connect_db()
        cur = con.cursor()
        if row:
            cur.execute("SELECT * FROM `products` WHERE `pid` = '" + row[0] + "'")
            row = cur.fetchall()
            print(row)
            con.close()
            if row:
                convert_row = list(row[0])
                self.pid.set(convert_row[1])
                self.pname.set(convert_row[2])
                self.pcategory.set(convert_row[3])
                self.unitprice.set(convert_row[4])
                self.quantity.set(convert_row[5])
                self.location.set(convert_row[6])

    def add(self):
        if self.pid.get() != '' and self.pname.get() != '' and self.pcategory.get() != '' and self.unitprice.get() != 0 and self.quantity.get() != 0 and self.location.get() != '':
            con1 = connection.connect_db()
            cur1 = con1.cursor()
            cur1.execute('SELECT * FROM `products` WHERE `pid` = "' + self.pid.get() + '"')
            row = cur1.fetchone()
            if row is not None:
                messagebox.showerror('Error', 'Product ID Already Exist')
            else:
                con = connection.connect_db()
                cur = con.cursor()
                query = "INSERT INTO `products` VALUES " \
                        "('','" + self.pid.get() + "','" + self.pname.get() + "', '" + self.pcategory.get() + "', '" + str(
                    self.unitprice.get()) + "', '" + str(self.quantity.get()) + "', '" + self.location.get() + "')"
                cur.execute(query)
                con.commit()
                self.fetch_ud()
                self.clear()
                self.res_lbl.config(text='Process Successful', fg='green')
        else:
            self.res_lbl.config(text='All Fields Required', fg='red')

    def delete(self):
        if self.pid.get() != '' and self.pname.get() != '' and self.pcategory.get() != '' and self.unitprice.get() != 0 and self.quantity.get() != 0 and self.location.get() != '':
            con = connection.connect_db()
            cur = con.cursor()
            query = 'DELETE FROM `products` WHERE `pid`="' + self.pid.get() + '"'
            cur.execute(query)
            con.commit()
            self.clear()
            self.fetch_ud()
            self.res_lbl.config(text='Process Successful', fg='green')
        else:
            self.res_lbl.config(text='No Product Selected', fg='red')

    def update(self):
        if self.pid.get() != '' and self.pname.get() != '' and self.pcategory.get() != '' and self.unitprice.get() != 0 and self.quantity.get() != 0 and self.location.get() != '':
            con1 = connection.connect_db()
            cur1 = con1.cursor()
            query1 = 'SELECT `sno` FROM `products` WHERE `pid`="' + str(self.pid.get()) + '"'
            cur1.execute(query1)
            sno = cur1.fetchone()
            con1.commit()
            con2 = connection.connect_db()
            cur2 = con2.cursor()
            query2 = 'UPDATE `products` SET' \
                     '`pid`="' + self.pid.get() + '", `pname`="' + self.pname.get() + '", `pro_cat`="' + self.pcategory.get() + '",`unit_price`="' + str(
                self.unitprice.get()) + '",`qty`="' + str(
                self.quantity.get()) + '",`location`="' + self.location.get() + '" WHERE `sno` = "' + str(sno[0]) + '" '
            cur2.execute(query2)
            con2.commit()
            connection.close_con(con1, cur1)
            connection.close_con(con2, cur2)
            self.fetch_ud()
            self.clear()
            self.res_lbl.config(text='Process Successful', fg='green')
        else:
            self.res_lbl.config(text='All Fields Required', fg='red')

    def clear(self):
        self.pname.set('')
        self.pid.set('')
        self.quantity.set(0)
        self.unitprice.set(0)
        self.location.set('')
        self.pcategory.set('Select')
        self.search_item.set('')
        self.res_lbl.config(text='')

    def show_all(self):
        self.fetch_ud()

    def get_category(self):
        con = connection.connect_db()
        cur = con.cursor()
        cur.execute('SELECT `cat_name` FROM `category`')
        rows = cur.fetchall()
        print(rows)
        self.L_ID_entry['values'] = rows

    def search(self):
        if self.search_item.get() != '':
            con = connection.connect_db()
            cur = con.cursor()
            cur.execute(
                'SELECT `pid`, `pname`, `pro_cat`, `unit_price`, `qty`,'
                ' `location` FROM `products` WHERE `pid`="' + self.search_item.get() + '"')
            rows = cur.fetchall()
            if len(rows) != 0:
                self.user_view.delete(*self.user_view.get_children())
                for row in rows:
                    self.user_view.insert('', END, values=row)
                con.commit()
            con.close()
        else:
            messagebox.showwarning('Warning', 'Nothing to Search')

    def on_destroy(self, event):
        if event.widget == self.window:
            self.dashboard.deiconify()

# if __name__ == '__main__':
#     app = Tk()
#     Inventory(app)
#     app.mainloop()
