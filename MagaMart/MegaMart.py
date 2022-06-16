from tkinter import *
from PIL import Image, ImageTk
from subprocess import Popen
import subprocess
# import os
from check import Check


def process_exists(process_name):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    process = subprocess.Popen(call, shell=True, stdout=subprocess.PIPE)
    output, err = process.communicate()  # use built in check_output right away
    last_line = str(output).strip().split('\r\n')[-1]   # check in last line for process name
    return last_line.lower().startswith(process_name.lower())  # because Fail message could be translated


def search_panel():
    from search_panel import SearchPanel
    top = Toplevel()
    window.withdraw()
    SearchPanel(top, window)
    top.mainloop()


def pos_panel():
    from pos import Pos
    top = Toplevel()
    top.grab_set()
    Check(top, window, Pos)
    top.mainloop()


def stock_management():
    from inventory import Inventory
    top = Toplevel()
    top.grab_set()
    Check(top, window, Inventory)
    top.mainloop()


def sales_report():
    from reports import Reports
    top = Toplevel()
    top.grab_set()
    Check(top, window, Reports)
    top.mainloop()


def hover_effect(event):
    if event.widget == button1:
        button1.config(bg='purple')
    if event.widget == button2:
        button2.config(bg='purple')
    if event.widget == button3:
        button3.config(bg='purple')
    if event.widget == button4:
        button4.config(bg='purple')


def hover_effect_leave(event):
    if event.widget == button1:
        button1.config(bg='#ff8080')
    if event.widget == button2:
        button2.config(bg='#ff8080')
    if event.widget == button3:
        button3.config(bg='#ff8080')
    if event.widget == button4:
        button4.config(bg='#ff8080')


def start_db():
    if process_exists('mysqld.exe'):
        print('Database is Ready')
    else:
        Popen(r'C:\xampp\mysql_start.bat')


def setting_panel():
    from settings import PasswordRecovery
    top = Toplevel()
    top.grab_set()
    PasswordRecovery(top)
    top.mainloop()


def manual():
    pass


def refresh():
    pass


def about():
    pass


def privacy_policy():
    pass


def categories():
    from categories import Categories
    top = Toplevel()
    top.grab_set()
    Categories(top)
    top.mainloop()


def on_destroy(event):
    pass
    # if event.widget == window:
    #     print(process_exists('mysqld.exe'))
    #     if process_exists('mysqld.exe'):
    #         os.system("taskkill /f /im mysqld.exe")
    #     else:
    #         print('Database Shutdown Failed')


window = Tk()
window.title('MegaMart Management')
window.geometry('1080x624+143+60')
window.resizable(False, False)
# -----------------------------Menu------------------------------------#
menu = Menu(window)
window.config(menu=menu)
file_menu = Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Refresh", command=refresh)
# file_menu.add_command(label="Open", command=OpenFile)
file_menu.add_command(label="Exit", command=window.destroy)

help_menu = Menu(menu)
menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="Manual", command=manual)
help_menu.add_command(label="Privacy Policy", command=privacy_policy)
help_menu.add_command(label="About", command=about)

setting_menu = Menu(menu)
menu.add_cascade(label="Setting", menu=setting_menu)
setting_menu.add_command(label="Categories", command=categories)
# -----------------------------Menu------------------------------------#
im = Image.open("Images/mainbg.jpg")
photo_img = ImageTk.PhotoImage(im)
im2 = Image.open("Images/settings.png")
setting_btn = ImageTk.PhotoImage(im2)
message = 'All Rights Reserved :: MegaMart Automation 2021'
mainframe = Frame(window)
mainframe.place(relwidth=1, relheight=1)
bg = Label(mainframe, image=photo_img).place(relwidth=1, relheight=1)
title_Lbl = Label(mainframe, text='MegaMart Automation', font=('Times New Roman', 16, 'bold'), bg='#009933',
                  fg='white').place(relx=0, rely=0, relwidth=1, relheight=0.08)
button1 = Button(mainframe, bg='#ff8080', fg='white', font=('Times New Roman', 18, 'bold'),
                 text='Search', command=search_panel)
button1.place(relx=0.25, rely=0.25, relwidth=0.24, relheight=0.24)
button1.bind('<Enter>', hover_effect)
button1.bind('<Leave>', hover_effect_leave)
button2 = Button(mainframe, bg='#ff8080', fg='white', font=('Times New Roman', 18, 'bold'), cursor='hand2',
                 text='Point Of Sale', command=pos_panel)
button2.place(relx=0.51, rely=0.25, relwidth=0.24, relheight=0.24)
button2.bind('<Enter>', hover_effect)
button2.bind('<Leave>', hover_effect_leave)
button3 = Button(mainframe, bg='#ff8080', fg='white', font=('Times New Roman', 18, 'bold'),
                 text='Stocks Management', command=stock_management)
button3.bind('<Enter>', hover_effect)
button3.bind('<Leave>', hover_effect_leave)
button3.place(relx=0.25, rely=0.51, relwidth=0.24, relheight=0.24)
button4 = Button(mainframe, bg='#ff8080', fg='white', font=('Times New Roman', 18, 'bold'), cursor='hand2',
                 text='Sales Report', command=sales_report)
button4.place(relx=0.51, rely=0.51, relwidth=0.24, relheight=0.24)
button4.bind('<Enter>', hover_effect)
button4.bind('<Leave>', hover_effect_leave)
footer_Lbl = Label(mainframe, text=message, font=('Times New Roman', 12, 'italic'), bg='black',
                   fg='white').place(relx=0, rely=0.93, relwidth=1, relheight=0.07)
set_button = Button(mainframe, image=setting_btn, cursor='hand2', command=setting_panel, bg='white', bd=0)
set_button.place(relx=0.95, rely=0.1, relwidth=0.038, relheight=0.068)
start_db()
window.bind("<Destroy>", on_destroy)
window.mainloop()
