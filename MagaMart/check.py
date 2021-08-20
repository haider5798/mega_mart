from tkinter import *
import json
import tkinter.messagebox as messagebox


class Check:
    def __init__(self, roots, parent, target):
        self.window = roots
        self.parent = parent
        self.target = target
        self.window.title('Login')
        self.window.geometry('325x130+520+319')
        self.window.resizable(False, False)
        self.password = StringVar()
        # bullet = "\u2022"     # Show Bullets In Entry Field
        mainframe = Frame(self.window, bg='white', bd=0, relief=GROOVE)
        mainframe.place(relwidth=1, relheight=1)
        title_lbl = Label(mainframe, text='The Program Requires a User Authentication\n\nEnter Your Password Here',
                          font=('Times New Roman', 10), bg='white', justify=LEFT)
        title_lbl.place(relx=0.1, rely=0, relwidth=0.9, relheight=0.4)
        entry1 = Entry(mainframe, textvariable=self.password, font=('Times New Roman', 10),
                       show='*', bd=2, relief=GROOVE)
        entry1.place(relx=0.2, rely=0.45, relwidth=0.63, relheight=0.18)
        button1 = Button(mainframe, font=('Times New Roman', 12), bd=2, relief=RIDGE,
                         text='Ok', command=self.pos_panel)
        button1.place(relx=0.35, rely=0.7, relwidth=0.3, relheight=0.2)

    def pos_panel(self):
        with open('password.json') as file:
            data = json.load(file)
            current_pass = data['password']
        file.close()
        if self.password.get() == current_pass:
            app = Toplevel()
            self.target(app, self.parent)
            self.parent.withdraw()
            self.window.destroy()
        else:
            messagebox.showerror('Error', 'Password You Entered Is Incorrect')


# if __name__ == '__main__':
#     root = Tk()
#     Check(root)
#     root.mainloop()
