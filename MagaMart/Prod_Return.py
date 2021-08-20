from tkinter import *
import connection as connection
import tkinter.messagebox as messagebox


class ProdReturn:
    def __init__(self, root):
        self.rm = root
        self.rm.geometry('350x150')
        self.rm.title('Product Return Menu')
        self.rm.resizable(False, False)
        self.return_pid = StringVar()
        self.product_qty = IntVar()
        self.product_qty.set(1)
        main_win = Frame(self.rm,  bg='white', bd=2, relief=GROOVE)
        main_win.place(relwidth=1, relheight=1)
        lbl1 = Label(main_win, text='Product ID', font=('Times New Roman', 12, 'bold'), bg='white', anchor="w")
        lbl1.place(relx=0.01, rely=0.02, relwidth=0.9, relheight=0.16)
        pid_ret = Entry(main_win, textvariable=self.return_pid, font=('Times New Roman', 12), bg='light grey', bd=2,
                        relief=RIDGE)
        pid_ret.place(relx=0.02, rely=0.19, relwidth=0.9, relheight=0.16)
        lbl2 = Label(main_win, text='Product Quantity', font=('Times New Roman', 12, 'bold'), bg='white', anchor="w")
        lbl2.place(relx=0.01, rely=0.36, relwidth=0.9, relheight=0.16)
        entry2 = Entry(main_win, textvariable=self.product_qty, font=('Times New Roman', 12), bg='light grey', bd=2,
                       relief=RIDGE)
        entry2.place(relx=0.02, rely=0.53, relwidth=0.9, relheight=0.16)
        vb = Button(main_win, font=('Times New Roman', 12, 'bold'), bd=2, relief=GROOVE, bg='light grey',
                    text='Return', command=self.action_prod_return)
        vb.place(relx=0.3, rely=0.79, relwidth=0.4, relheight=0.17)

    def action_prod_return(self):
        if self.return_pid.get() == '' and self.product_qty.get() == 0:
            messagebox.showwarning('Warning', 'All Fields Required')
        else:
            # check previous value
            con = connection.connect_db()
            cur = con.cursor()
            query = "SELECT `qty` FROM `products` WHERE `pid` = '"+str(self.return_pid.get())+"'"
            cur.execute(query)
            prev_qty = cur.fetchone()
            con.commit()
            connection.close_con(con, cur)
            if prev_qty:
                new_qty = int(prev_qty[0]) + self.product_qty.get()
            else:
                new_qty = self.product_qty.get()
            # updating value
            con2 = connection.connect_db()
            cur2 = con2.cursor()
            query2 = "UPDATE `products` SET `qty`= '"+str(new_qty)+"' WHERE pid= '"+str(self.return_pid.get())+"'"
            cur2.execute(query2)
            con2.commit()
            # closing connections
            messagebox.showinfo('Success', 'Product Returned Successfully')
            connection.close_con(con2, cur2)
            self.clear()

    def clear(self):
        self.product_qty.set(1)
        self.return_pid.set('')


if __name__ == '__main__':
    app = Tk()
    ProdReturn(app)
    app.mainloop()
