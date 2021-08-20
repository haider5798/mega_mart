from tkinter import *
import json
from PIL import Image, ImageTk
from subprocess import Popen
import tkinter.messagebox as messagebox


class PasswordRecovery:
    def __init__(self, roots):
        self.window = roots
        self.window.title('Password Recovery')
        self.window.geometry('335x250+520+319')
        self.window.resizable(False, False)
        self.current_password = StringVar()
        self.new_password = StringVar()
        self.repeat_new_password = StringVar()
        # bullet = "\u2022"     # Show Bullets In Entry Field
        mainframe = Frame(self.window, bg='white', relief=GROOVE)
        mainframe.place(relwidth=1, relheight=1)
        # .............................................................................................. #

        entryframe = Frame(mainframe, bg='white')
        entryframe.place(rely=0.02, relwidth=1, relheight=0.72)
        title_lbl = Label(entryframe, text='Current Password',
                          font=('Times New Roman', 11, 'bold'), bg='white', justify=LEFT)
        title_lbl.grid(row=1, column=0, sticky=W, padx=5)
        entry1 = Entry(entryframe, width=40, textvariable=self.current_password, font=('Times New Roman', 12),
                       show='*', bd=2, relief=GROOVE, bg='light grey')
        entry1.grid(row=2, column=0, pady=5, padx=5)
        title_lbl = Label(entryframe, text='New Password',
                          font=('Times New Roman', 11, 'bold'), bg='white', justify=LEFT)
        title_lbl.grid(row=3, column=0, sticky=W, padx=5)
        entry2 = Entry(entryframe, width=40, textvariable=self.new_password, font=('Times New Roman', 12),
                       show='*', bd=2, relief=GROOVE, bg='light grey')
        entry2.grid(row=4, column=0, pady=5)
        title_lbl = Label(entryframe, text=' Confirm New Password',
                          font=('Times New Roman', 11, 'bold'), bg='white', justify=LEFT)
        title_lbl.grid(row=5, column=0, sticky=W)
        entry3 = Entry(entryframe, width=40, textvariable=self.repeat_new_password, font=('Times New Roman', 12),
                       show='*', bd=2, relief=GROOVE, bg='light grey')
        entry3.grid(row=6, column=0, pady=5)
        # .............................................................................................. #
        btnframe = Frame(mainframe, bg='white')
        btnframe.place(rely=0.76, relwidth=1, relheight=0.13)
        button1 = Button(btnframe, font=('Times New Roman', 12), bd=2, relief=RIDGE, cursor='hand2',
                         text='Ok', command=self.recovery)
        button1.place(relx=0.03, relwidth=0.455, relheight=1)
        button1 = Button(btnframe, font=('Times New Roman', 12), bd=2, relief=RIDGE, cursor='hand2',
                         text='Cancel', command=self.window.destroy)
        button1.place(relx=0.515, relwidth=0.455, relheight=1)

    def recovery(self):
        with open('password.json') as file:
            data = json.load(file)
            current_pass = data['password']
        file.close()
        if self.current_password.get() == current_pass and self.new_password.get() == self.repeat_new_password.get():
            data['password'] = self.new_password.get()
            file = open("password.json", "w+")
            file.write(json.dumps(data))
            file.close()
            messagebox.showinfo('Success', 'Password Changed Successfully')
            self.reset()
        else:
            messagebox.showwarning('Warning', 'Wrong Current Password or Mismatched New Password')

    def reset(self):
        self.new_password.set('')
        self.current_password.set('')
        self.repeat_new_password.set('')


if __name__ == '__main__':
    root = Tk()
    PasswordRecovery(root)
    root.mainloop()
