from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter.messagebox as tmsg
import subprocess
global lbx, frame1, selected_place, email_body_entry, n, email, frame2 

def destroy_root():
    root.destroy()

def login_done():
    subprocess.Popen(['python', 'TkAdminHP.py'])

root = Tk()

root.title("Login Page")
root.state("zoomed")

bg_image = Image.open("bg_image.jpg")
bg_image = bg_image.resize((1300, 450), Image.ANTIALIAS)
bg_image = ImageTk.PhotoImage(bg_image)

bg_label = Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=0.5)

admin_login_frame = Frame(root, bg="white")
admin_login_frame.place(relx=0.3, rely=0.6, relwidth=0.4, relheight=0.3)

admin_login_label = Label(admin_login_frame, text="Admin Login", font=("Arial", 14), bg="white")
admin_login_label.pack(pady=10)
admin_username_label = Label(admin_login_frame, text="Username", font=("Arial", 12), bg="white")
admin_username_label.pack()
admin_username_entry = Entry(admin_login_frame, font=("Arial", 12))
admin_username_entry.pack(pady=5)
admin_password_label = Label(admin_login_frame, text="Password", font=("Arial", 12), bg="white")
admin_password_label.pack()
admin_password_entry = Entry(admin_login_frame, font=("Arial", 12), show="*")
admin_password_entry.pack(pady=5)


def login():
    
    global login_failed_label
    global login_successful_label
    
    if admin_username_entry.get() == "admin" and admin_password_entry.get() == "123456":

        login_successful_label = Label(root, text="Login Successful!", font=("Arial", 14), fg="green")
        login_successful_label.place(relx=0.5, rely=0.9, anchor="center")
        login_done()
        root.after(5000, root.destroy)
        # destroy_root()
    else:

        login_failed_label = Label(root, text="Invalid Credentials. Try Again.", font=("Arial", 14), fg="red")
        login_failed_label.place(relx=0.5, rely=0.9, anchor="center")
        root.after(2000, login_failed_label.destroy)
        return
    
    
        
login_button = Button(admin_login_frame, text="Login", font=("Arial", 12), bg="white", command=login)
login_button.place(relx=0.5, rely=0.9, anchor="center")

root.mainloop()

