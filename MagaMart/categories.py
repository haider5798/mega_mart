from tkinter import *
import json
from PIL import Image, ImageTk
from subprocess import Popen
import tkinter.messagebox as messagebox
import connection as connection


class Categories:
    def __init__(self, roots):
        self.window = roots
        self.window.title('Password Recovery')
        self.window.geometry('335x250+520+319')
        self.window.resizable(False, False)

        # ------------------------------Variable Declaration--------------------------------------
        self.cat_name = StringVar()
        self.cat_pro_per = IntVar()
        self.cat_id = StringVar()

        # ------------------------------Variable Declaration--------------------------------------
        # bullet = "\u2022"     # Show Bullets In Entry Field
        mainframe = Frame(self.window, bg='white', bd=0, relief=GROOVE)
        mainframe.place(relwidth=1, relheight=1)

        # .............................................................................................. #
        entryframe = Frame(mainframe, bg='white')
        entryframe.place(rely=0.1, relwidth=1, relheight=0.72)
        title_lbl = Label(entryframe, text='Category Id',
                          font=('Times New Roman', 11), bg='white', justify=LEFT)
        title_lbl.grid(row=1, column=0, sticky=W, padx=5)
        entry1 = Entry(entryframe, width=30, textvariable=self.cat_id, font=('Times New Roman', 12),
                       bd=2, relief=GROOVE, bg='light grey')
        entry1.grid(row=2, column=0, pady=1, padx=5, sticky=W)
        Button(entryframe, width=8, font=('Times New Roman', 10), bd=2, relief=RIDGE, cursor='hand2',
               text='Search', command=self.search).grid(row=2, column=1, pady=1, sticky=NW)
        title_lbl = Label(entryframe, text='Category Name',
                          font=('Times New Roman', 11), bg='white', justify=LEFT)
        title_lbl.grid(row=3, column=0, sticky=W, padx=5)
        entry2 = Entry(entryframe, width=40, textvariable=self.cat_name, font=('Times New Roman', 12),
                       bd=2, relief=GROOVE, bg='light grey')
        entry2.grid(row=4, column=0, pady=1, padx=5, columnspan=2)
        title_lbl = Label(entryframe, text='Profit Percentage',
                          font=('Times New Roman', 11), bg='white', justify=LEFT)
        title_lbl.grid(row=5, column=0, sticky=W, padx=5)
        entry3 = Entry(entryframe, width=40, textvariable=self.cat_pro_per, font=('Times New Roman', 12),
                       bd=2, relief=GROOVE, bg='light grey')
        entry3.grid(row=6, column=0, pady=1, padx=5, columnspan=2)

        # .............................................................................................. #
        btnframe = Frame(mainframe, bg='white')
        btnframe.place(rely=0.78, relwidth=1, relheight=0.13)
        Button(btnframe, font=('Times New Roman', 12), bd=2, relief=RIDGE, cursor='hand2',
               text='Add', command=self.add).place(relx=0.025, relwidth=0.3, relheight=1)
        Button(btnframe, font=('Times New Roman', 12), bd=2, relief=RIDGE, cursor='hand2',
               text='Update', command=self.update).place(relx=0.35, relwidth=0.3, relheight=1)
        Button(btnframe, font=('Times New Roman', 12), bd=2, relief=RIDGE, cursor='hand2',
               text='Delete', command=self.delete).place(relx=0.675, relwidth=0.3, relheight=1)
        self.res_lbl = Label(mainframe, text='', font=('Times New Roman', 11), bg='white')
        self.res_lbl.place(rely=0.92, relwidth=1)

    def add(self):
        if self.cat_id.get() != '' and self.cat_name.get() != '' and self.cat_pro_per.get() != 0:
            con1 = connection.connect_db()
            cur1 = con1.cursor()
            cur1.execute('SELECT * FROM `category` WHERE `cat_id` = "' + self.cat_id.get() + '"')
            row = cur1.fetchone()
            if row is not None:
                messagebox.showerror('Error', 'Product ID Already Exist')
            else:
                con = connection.connect_db()
                cur = con.cursor()
                query = "INSERT INTO `category` VALUES " \
                        "('','" + self.cat_id.get() + "','" + self.cat_name.get() + "', '" + str(self.cat_pro_per.get()) + "')"
                cur.execute(query)
                con.commit()
                self.clear()
                self.res_lbl.config(text='Process Successful', fg='green')

        else:
            self.res_lbl.config(text='All Fields Required', fg='red')

    def delete(self):
        if self.cat_id.get() != '' and self.cat_name.get() != '' and self.cat_pro_per.get() != 0:
            con = connection.connect_db()
            cur = con.cursor()
            query = 'DELETE FROM `category` WHERE `cat_id`="' + self.cat_id.get() + '"'
            cur.execute(query)
            con.commit()
            self.clear()
            self.res_lbl.config(text='Process Successful', fg='green')
        else:
            self.res_lbl.config(text='No Product Selected', fg='red')

    def update(self):
        if self.cat_id.get() != '' and self.cat_name.get() != '' and self.cat_pro_per.get() != 0:
            con2 = connection.connect_db()
            cur2 = con2.cursor()
            query2 = 'UPDATE `category` SET' \
                     '`cat_name`="' + self.cat_name.get() + '", `profit`="' \
                     + str(self.cat_pro_per.get()) + '" WHERE `cat_id` = "' + self.cat_id.get() + '"'
            cur2.execute(query2)
            con2.commit()
            connection.close_con(con2, cur2)
            self.clear()
            self.res_lbl.config(text='Process Successful', fg='green')

        else:
            self.res_lbl.config(text='All Fields Required', fg='red')

    def clear(self):
        self.cat_name.set('')
        self.cat_id.set('')
        self.cat_pro_per.set(0)
        self.res_lbl.config(text='')

    def search(self):
        if self.cat_id.get() != '':
            try:
                con = connection.connect_db()
                cur = con.cursor()
                query = 'SELECT `cat_name`, `profit` FROM `category` WHERE' \
                        ' `cat_id`="' + str(self.cat_id.get()) + '"'
                cur.execute(query)
                data = cur.fetchone()
                con.commit()
            except Exception as Error:
                data = None
                print(Error)
            if data is not None:
                self.cat_name.set(data[0])
                self.cat_pro_per.set(data[1])
            else:
                messagebox.showerror('Error', 'ID Does not exists')
        else:
            messagebox.showerror('Error', 'Please Enter ID')

