from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox as messagebox
import connection as connection


class SearchPanel:
    def __init__(self, arg, window):
        self.root = arg
        self.root_window = window
        self.root.title('MMA Search Panel')
        self.root.geometry('1080x624+143+60')
        self.root.resizable(False, False)
        im = Image.open("Images/searchbg.jpg")
        self.photo_img = ImageTk.PhotoImage(im)
        self.product = StringVar()
        self.product.set('Enter Product Id . . . .')
        self.mainframe = Frame(self.root)
        self.mainframe.place(relwidth=1, relheight=1)
        bg = Label(self.mainframe, image=self.photo_img)
        bg.place(relwidth=1, relheight=1)
        lbl = Label(self.mainframe, text='MegaMart Automation', font=('Times New Roman', 16, 'bold'),
                    bg='Gold', fg='black')
        lbl.place(relx=0.275, rely=0.05, relwidth=0.45, relheight=0.08)
        search_frame = Frame(self.mainframe)
        search_frame.place(relx=0.2, rely=0.25, relwidth=0.6, relheight=0.07)
        Button(search_frame, bg='green', fg='white', font=('Times New Roman', 13, 'bold'), text='Search',
               cursor='hand2', bd=4, relief=GROOVE, command=self.search).place(relx=0.8, rely=0, relwidth=0.2, relheight=1)
        entry1 = Entry(search_frame, textvariable=self.product, font=('Times New Roman', 14), bd=2, relief=RIDGE)
        entry1.place(relx=0, rely=0, relwidth=0.8, relheight=1)
        entry1.bind('<FocusIn>', self.clear)
        Button(self.mainframe, bg='teal', fg='white', font=('Times New Roman', 14), text='Go Back', cursor='hand2',
               command=self.dashboard).place(relx=0.02, rely=0.92, relwidth=0.12, relheight=0.055)
        self.root.bind("<Destroy>", self.on_destroy)

    def dashboard(self):
        self.root.destroy()

    def search(self):
        print(self.product.get())
        if self.product.get() == 'Enter Product Id . . . .' or self.product.get() == '':
            messagebox.showwarning('Warning', 'Nothing to Search')
        else:
            con = connection.connect_db()
            cur = con.cursor()
            query = 'SELECT `location` FROM `products` WHERE `pid`="'+str(self.product.get())+'"'
            cur.execute(query)
            data = cur.fetchone()
            con.commit()
            if data is not None:
                messagebox.showinfo('Info', f'Product {self.product.get()} is at {data[0]}')
            else:
                data = (None,)
                messagebox.showwarning('Warning', 'Wrong Product Id')

    def clear(self, event):
        self.product.set('')

    def on_destroy(self, event):
        if event.widget == self.root:
            self.root_window.deiconify()


# if __name__ == '__main__':
#     app = Tk()
#     SearchPanel(app)
#     app.mainloop()
