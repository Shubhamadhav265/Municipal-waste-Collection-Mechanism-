from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import smtplib
import tkinter.messagebox as tmsg
import Personal_info
import csv
from email.message import EmailMessage
import ssl
global lbx, frame1, selected_place, email_body_entry, n, email, frame2


def send_message():
    global email
    if selected_place == "Shivaji Nagar":
        email = "shubhamadhav265@gmail.com"
    elif selected_place == "Kondhwa":
        email = "shubhamadhav265@gmail.com"
    elif selected_place == "Bandra":
        email = "shubhamadhav265@gmail.com"
    elif selected_place == "MIDC":
        email = "shubhamadhav265@gmail.com"

    address_info = email
    email_body_info = email_body_entry.get()

    msg = EmailMessage()
    msg.set_content(email_body_info)
    msg['Subject'] = "MAIL FROM GARBAGE PORTAL"
    msg['From'] = Personal_info.sender_email
    msg['To'] = address_info
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
        # server.set_debuglevel(1)
        server.login(Personal_info.sender_email, Personal_info.sender_password)
        server.sendmail(Personal_info.sender_email,
                        address_info, msg.as_string())
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        server.close()
    tmsg.showinfo("You the Contributor", "Your Message sent successfully")
    Button(frame2, text="Exit", font="Serif 12 bold", command=exit, padx=20, bg="light green") \
        .pack(padx=30, side=BOTTOM, anchor="e")


def submit():
    global selected_place, email_body_entry, frame2
    selected_place = lbx.get(ACTIVE)

    data = [[f"{var.get()}", f"{n}", f"{selected_place}"]]
    # define the name of the CSV file
    filename = 'my_csv_file.csv'
    with open(filename, 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        for row in data:
            csv_writer.writerow(row)
    print(f"{filename} Updated successfully!")

    frame2 = Frame(root)
    frame2.pack(fill=BOTH)
    Label(frame2, text=f"Problem: {var.get()}    Place: {selected_place},{n}", font="lucid 15", bg="green", fg="white",
          anchor="nw").pack(fill=BOTH, pady=5)
    email_body_field = Label(frame2, text="Details: ", font="lucid 20 bold")
    email_body_field.pack(anchor="nw", pady=5)
    email_body_entry = Entry(frame2, width=120, font="lucid 13")
    email_body_entry.insert(
        END, f"Problem-{var.get()}\t Place-{selected_place},{n}\t Exact address-\t Exact details-")
    email_body_entry.pack(anchor="nw", pady=5)

    Button(frame2, text="Send Email", font="lucid 18 ", command=send_message, bg="green", fg="white")\
        .pack(padx=5, pady=5, anchor="nw")


def address1():
    list1 = ["Shivaji Nagar", "Katraj", "Kondhwa", "Yewalewadi", "Viman Nagar", "Kothrud", "Hadapsar",
             "Bavdhan Budruk", "Baner", "Vishrantwadi", "Warje"]
    global lbx, n
    n = "Pune"
    lbx = Listbox(frame1)
    lbx.grid(row=2, column=0, padx=20, pady=10)
    for b in sorted(list1):
        lbx.insert(END, b)
    Button(frame1, text="Submit", command=submit).grid(row=3, column=0, pady=5)


def address2():
    list2 = ["Bandra", "Parle", "Andheri", "Juhu", "Navi Mumbai", "Pawai", "Vile Parle", "Dahisar", "Model Town",
             "Jogeshwari", "Kandivali", "Santacruz"]
    global lbx, n
    n = "Mumbai"
    lbx = Listbox(frame1)
    lbx.grid(row=2, column=1, padx=20, pady=10)
    for b in sorted(list2):
        lbx.insert(END, b)
    Button(frame1, text="Submit", command=submit).grid(row=3, column=1, pady=5)


def address3():
    list3 = ["Sharanpur Road", "Sharda Nagar", "Sawarkar Nagar", "Shramik Nagar", "Tidke Nagar", "Tilak Road",
             "Pathardi Gaon", "Sharanpur Road", "Satpur", "Shalimar", "Indira Nagar"]
    global lbx, n
    n = "Nashik"
    lbx = Listbox(frame1)
    lbx.grid(row=2, column=2, padx=20, pady=10)
    for b in sorted(list3):
        lbx.insert(END, b)
    Button(frame1, text="Submit", command=submit).grid(row=3, column=2, pady=5)


def address4():
    list4 = ["Mahal", "Sitabuldi", "Dhantoli", "Itwari", "Ganesh Peth Colony", "Mominpura", "Dharampeth",
             "Ramdaspeth", "Gandhibagh", "Seminary Hills", "Wardhaman Nagar",
             "Ajni", "Ashok Nagar", "Lakadganj"]
    global lbx, n
    n = "Nagpur"
    lbx = Listbox(frame1)
    lbx.grid(row=2, column=3, padx=20, pady=10)
    for b in sorted(list4):
        lbx.insert(END, b)
    Button(frame1, text="Submit", command=submit).grid(row=3, column=3, pady=5)


def address5():
    list5 = ["MIDC", "Deolai", "Padegoan", "Kanchanwadi", "Paithan", "Satara Parisar", "Waluj", "CIDCO", "Gangapur",
             "Nirala Bazar", "Shendra MIDC", "Beed Bypass Padegoan", "Bidkin", "Samarth Nagar", "Usmanpura", "Vaijapur",
             "Tuljapur", "Chikalthana", "Karmad", "Kannad", "Mustafabad", "Pisadevi", "Sillod", "Sulibhanjan"]
    global lbx, n
    n = "Aurangabad"
    lbx = Listbox(frame1)
    lbx.grid(row=2, column=4, padx=20, pady=10)
    for b in sorted(list5):
        lbx.insert(END, b)
    Button(frame1, text="Submit", command=submit).grid(row=3, column=4, pady=5)


def new_window():
    main_frame.destroy()
    second_frame.destroy()

    global frame1
    frame1 = Frame(root, bg="light green", relief=GROOVE, borderwidth=5)
    frame1.pack(fill=BOTH)

    Label(frame1, text="Select your City", font="Lucid 18",
          bg="green", fg="white").grid(row=0, column=2)

    pune_button = Button(frame1, image=pune1, command=address1)
    mumbai_button = Button(frame1, image=mumbai1, command=address2)
    nashik_button = Button(frame1, image=nashik1, command=address3)
    nagpur_button = Button(frame1, image=nagpur1, command=address4)
    aurangabad_button = Button(frame1, image=aurangabad1, command=address5)

    pune_button.grid(row=1, column=0, padx=12, pady=16)
    mumbai_button.grid(row=1, column=1, padx=12, pady=16)
    nashik_button.grid(row=1, column=2, padx=12, pady=16)
    nagpur_button.grid(row=1, column=3, padx=12, pady=16)
    aurangabad_button.grid(row=1, column=4, padx=12, pady=16)


def instruction():
    tmsg.showinfo("You The Contributor", "Instructions: \n"
                                         "1. Firstly select your problem\n"
                                         "2. Go to next page and select your city\n"
                                         "3. Select your region and Submit\n"
                                         "4. Add exact address and submit your response")


root = Tk()
root.state("zoomed")
root.title("You The Contributor")

# scrollbar
main_frame = Frame(root)
main_frame.pack(expand=1, fill=BOTH)

my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

my_scrollbar = ttk.Scrollbar(
    main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(
    scrollregion=my_canvas.bbox('all')))

second_frame = Frame(my_canvas)

my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
# scrollbar

image = Image.open("Add a heading.png")
image = image.resize((1525, 350), Image.Resampling.LANCZOS)
photo = ImageTk.PhotoImage(image)
Label(second_frame, image=photo).pack()

Label(second_frame, text="About Us",
      font="Serif 18 bold", padx=10).pack(anchor="nw")
Label(second_frame, text="This is the Portal of the Government of India, designed, developed and hosted to inform "
                         "related to cleanliness.", font="Aerial-black 14", padx=10).pack(anchor="nw")
Label(second_frame, text="This is our co-work to make our environment eco-friendly and green", font="Aerial-black 14",
      padx=10).pack(anchor="nw")
Label(second_frame, text="History",
      font="Serif 18 bold", padx=10).pack(anchor="nw")
Label(second_frame, text="The Portal has been developed as a Mission Mode Project (MMP).The portal was launched in "
                         "June 2022 for 5 years.", font="Aerial-black 14", padx=10).pack(anchor="nw")
Label(second_frame, text="Objective / Vision",
      font="Serif 18 bold", padx=10).pack(anchor="nw")
Label(second_frame, text="The objective behind the Portal is to provide a single window access to services being "
                         "provided by you the contributor.", font="Aerial-black 14", padx=10).pack(anchor="nw")
Label(second_frame, text="The objective behind the Portal is to provide a single window access to services being "
                         "provided by you the contributor.", font="Aerial-black 14", padx=10).pack(anchor="nw")
Label(second_frame, text="Main objective of this Portal is to clean your surrounding and make it Garbage free.",
      font="Aerial-black 14", padx=10).pack(anchor="nw")
Label(second_frame, text="We have to protect our mother earth as this is the only habitual place for our humans Mars "
                         "is yet to become habitual.", font="Aerial-black 14", padx=10).pack(anchor="nw")
Label(second_frame, text="We have to make our Earth suitable for our future generation.", font="Aerial-black 14",
      padx=10).pack(anchor="nw")
Label(second_frame, text="So please do your contribution and let gather together to make our EARTH beautiful. ",
      font="Aerial-black 14", padx=10).pack(anchor="nw")


Button(second_frame, text="How to Use?", command=instruction, font="Serif 12 bold", bg="sky blue", fg="red",
       relief="groove").pack(padx=10, pady=10, anchor="nw")

Label(second_frame, text="Select your Problem",
      font="Aerial 14 bold", padx=10, pady=10).pack(anchor="nw")
List = ["E-Waste", "Dead Animal", "Bio-Medical", "Household waste", "Other"]
var = StringVar()
var.set("Not selected")
for i in range(0, 5):
    radio = Radiobutton(
        second_frame, text=List[i], font="Serif 16 ", value=List[i], variable=var, padx=10, pady=10)
    radio.pack(padx=10, side=LEFT, anchor="w")

Button(second_frame, text="Next", font="Serif 12 bold", command=new_window,
       padx=20, bg="light green").pack(padx=30, side=BOTTOM, anchor="n")

pune1 = Image.open("Pune.png")
mumbai1 = Image.open("Mumbai.png")
nashik1 = Image.open("Nashik.png")
nagpur1 = Image.open("Nagpur.png")
aurangabad1 = Image.open("Aurangabad.png")
resized1 = pune1.resize((150, 150), Image.Resampling.LANCZOS)
resized2 = mumbai1.resize((150, 150), Image.Resampling.LANCZOS)
resized3 = nashik1.resize((150, 150), Image.Resampling.LANCZOS)
resized4 = nagpur1.resize((150, 150), Image.Resampling.LANCZOS)
resized5 = aurangabad1.resize((150, 150), Image.Resampling.LANCZOS)

pune1 = ImageTk.PhotoImage(resized1)
mumbai1 = ImageTk.PhotoImage(resized2)
nashik1 = ImageTk.PhotoImage(resized3)
nagpur1 = ImageTk.PhotoImage(resized4)
aurangabad1 = ImageTk.PhotoImage(resized5)

# image1 = Image.open("Thank You for Contributing.png")
# image1 = image1.resize((1525, 200), Image.Resampling.LANCZOS)
# photo1 = ImageTk.PhotoImage(image1)

root.mainloop()
