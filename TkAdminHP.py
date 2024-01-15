from tkinter import *
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import pandas as pd
import csv
import numpy as np
global next


def finish():
    root.quit()


def next():
    main_frame.destroy()
    global second_frame
    second_frame=Frame(root,bg="#3c8dbc", relief=GROOVE, borderwidth=10)
    second_frame.pack(pady=170)

    title = Label(second_frame, text='City Specific Analysis', font=('Arial', 16, 'bold'),fg="#A74AC7",borderwidth=10)
    title.pack(side='top', pady=30)

    # Create 5 buttons and added them to the frame
    Button(second_frame, text="Pune", font=("Arial", 20), bg="#728FCE", fg="white", width=20, height=30, bd=2, relief="solid",command=PuneAnalysis).pack(side=LEFT, pady=35, padx=25)
    Button(second_frame, text="Mumbai", font=("Arial", 20), bg="#728FCE", fg="white", width=20, height=30, bd=2, relief="solid",command=MumbaiAnalysis).pack(side=LEFT, pady=35, padx=15)
    Button(second_frame, text="Nashik", font=("Arial", 20), bg="#728FCE", fg="white", width=20, height=30, bd=2, relief="solid",command=NashikAnalysis).pack(side=LEFT, pady=35, padx=15)
    Button(second_frame, text="Nagpur", font=("Arial", 20), bg="#728FCE", fg="white", width=20, height=30, bd=2, relief="solid",command=NagpurAnalysis).pack(side=LEFT, pady=35, padx=15)
    Button(second_frame, text="Aurangabad", font=("Arial", 20), bg="#728FCE", fg="white", width=20, height=30, bd=2, relief="solid",command=AurangabadAnalysis).pack(side=LEFT, pady=35, padx=25)

def prev_cs():
    global second_frame
    second_frame=Frame(root,bg="#3c8dbc", relief=GROOVE, borderwidth=10)
    second_frame.pack(pady=170)

    title = Label(second_frame, text='City Specific Analysis', font=('Arial', 16, 'bold'),fg="#A74AC7",borderwidth=10)
    title.pack(side='top', pady=30)

    # Create 5 buttons and add them to the frame
    Button(second_frame, text="Pune", font=("Arial", 20), bg="#728FCE", fg="white", width=20, height=30, bd=2, relief="solid",command=PuneAnalysis).pack(side=LEFT, pady=35, padx=25)
    Button(second_frame, text="Mumbai", font=("Arial", 20), bg="#728FCE", fg="white", width=20, height=30, bd=2, relief="solid",command=MumbaiAnalysis).pack(side=LEFT, pady=35, padx=15)
    Button(second_frame, text="Nashik", font=("Arial", 20), bg="#728FCE", fg="white", width=20, height=30, bd=2, relief="solid",command=NashikAnalysis).pack(side=LEFT, pady=35, padx=15)
    Button(second_frame, text="Nagpur", font=("Arial", 20), bg="#728FCE", fg="white", width=20, height=30, bd=2, relief="solid",command=NagpurAnalysis).pack(side=LEFT, pady=35, padx=15)
    Button(second_frame, text="Aurangabad", font=("Arial", 20), bg="#728FCE", fg="white", width=20, height=30, bd=2, relief="solid",command=AurangabadAnalysis).pack(side=LEFT, pady=35, padx=25)



def prev_pune():
    pune_frame.destroy()
    prev_cs()

def prev_mumbai():
    mumbai_frame.destroy()
    prev_cs()

def prev_nashik():
    nashik_frame.destroy()
    prev_cs()

def prev_nagpur():
    nagpur_frame.destroy()
    prev_cs()

def prev_aurangabad():
    aurangabad_frame.destroy()
    prev_cs()



def PuneAnalysis():
    second_frame.destroy()

    global pune_frame
    pune_frame = Frame(root)
    pune_frame.pack(expand=True, fill=BOTH)

    city_filter = df['City'] == 'Pune'
    city_df = df[city_filter]

    region_counts = city_df.groupby('Region').size().reset_index(name='counts')
    regions = region_counts['Region'].tolist()
    counts = region_counts['counts'].tolist()

    Tow_counts = city_df.groupby('Type of Waste').size().reset_index(name='counts')
    Towp = Tow_counts['Type of Waste'].tolist()
    Tow_counts = Tow_counts['counts'].tolist()

    fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(20, 9.1))

    colors = ["#2554C7", "#728FCE", "#78C7C7", "#50EBEC", "#7FFFD4", "#CFECEC", "#AFEEEE", "#8EEBEC", "#CCFFFF"]
    axs[0].bar(regions, counts, color=colors)
    axs[0].set_title('Waste Reported')
    axs[0].set_xticklabels(regions, rotation=60)


    colors = ["#7FFFD4", "#50EBEC", "#78C7C7", "#728FCE", "#2554C7"]
    axs[1].pie(Tow_counts, labels=Towp, autopct='%1.1f%%', startangle=90, colors=colors)
    axs[1].axis('equal')
    axs[1].set_title('Type Of Waste Reported')

    canvas = FigureCanvasTkAgg(fig, master=pune_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

    plt.suptitle("Pune Specific Analysis", fontsize=14, fontweight='bold')
    plt.subplots_adjust(wspace=0.4)

    button_frame = Frame(pune_frame)
    button_frame.pack(pady=10)

    prev_button = Button(button_frame, text="City Specific", font=("Arial bold", 16), fg="white", bg="#3c8dbc", padx=20, borderwidth=0, command=prev_pune)
    prev_button.grid(row=0, column=0, padx=410)

    end_button = Button(button_frame, text="Exit ", font=("Arial bold", 16), fg="white", bg="#3c8dbc", padx=20,  borderwidth=0, command=finish)
    end_button.grid(row=0, column=1, padx=410)


def MumbaiAnalysis():
    second_frame.destroy()

    global mumbai_frame
    mumbai_frame = Frame(root)
    mumbai_frame.pack(expand=True, fill=BOTH)

    city_filter = df['City'] == 'Mumbai'
    city_df = df[city_filter]

    region_counts = city_df.groupby('Region').size().reset_index(name='counts')
    regions = region_counts['Region'].tolist()
    counts = region_counts['counts'].tolist()

    Tow_counts = city_df.groupby('Type of Waste').size().reset_index(name='counts')
    Towm = Tow_counts['Type of Waste'].tolist()
    Tow_counts = Tow_counts['counts'].tolist()

    fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(20, 9.1))

    colors = ["#2554C7", "#728FCE", "#78C7C7", "#50EBEC", "#7FFFD4", "#CFECEC", "#AFEEEE", "#8EEBEC", "#CCFFFF"]
    axs[0].bar(regions, counts, color=colors)
    axs[0].set_title('Waste Reported')
    axs[0].set_xticklabels(regions, rotation=60)


    colors = ["#7FFFD4", "#50EBEC", "#78C7C7", "#728FCE", "#2554C7"]
    axs[1].pie(Tow_counts, labels=Towm, autopct='%1.1f%%', startangle=90, colors=colors)
    axs[1].axis('equal')
    axs[1].set_title('Type Of Waste Reported')

    canvas = FigureCanvasTkAgg(fig, master=mumbai_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

    plt.suptitle("Mumbai Specific Analysis", fontsize=14, fontweight='bold')
    plt.subplots_adjust(wspace=0.4)

    button_frame = Frame(mumbai_frame)
    button_frame.pack(pady=10)

    prev_button = Button(button_frame, text="City Specific", font=("Arial bold", 16), fg="white", bg="#3c8dbc", padx=20, borderwidth=0, command=prev_mumbai)
    prev_button.grid(row=0, column=0, padx=410)

    end_button = Button(button_frame, text="Exit", font=("Arial bold", 16), fg="white", bg="#3c8dbc", padx=20,  borderwidth=0, command=finish)
    end_button.grid(row=0, column=1, padx=410)



def NashikAnalysis():
    second_frame.destroy()

    global nashik_frame
    nashik_frame = Frame(root)
    nashik_frame.pack(expand=True, fill=BOTH)

    city_filter = df['City'] == 'Nashik'
    city_df = df[city_filter]

    region_counts = city_df.groupby('Region').size().reset_index(name='counts')
    regions = region_counts['Region'].tolist()
    counts = region_counts['counts'].tolist()

    Tow_counts = city_df.groupby('Type of Waste').size().reset_index(name='counts')
    Towm = Tow_counts['Type of Waste'].tolist()
    Tow_counts = Tow_counts['counts'].tolist()

    fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(20, 9.1))

    colors = ["#2554C7", "#728FCE", "#78C7C7", "#50EBEC", "#7FFFD4", "#CFECEC", "#AFEEEE", "#8EEBEC", "#CCFFFF"]
    axs[0].bar(regions, counts, color=colors)
    axs[0].set_title('Waste Reported')
    axs[0].set_xticklabels(regions, rotation=60)


    colors = ["#7FFFD4", "#50EBEC", "#78C7C7", "#728FCE", "#2554C7"]
    axs[1].pie(Tow_counts, labels=Towm, autopct='%1.1f%%', startangle=90, colors=colors)
    axs[1].axis('equal')
    axs[1].set_title('Type Of Waste Reported')

    canvas = FigureCanvasTkAgg(fig, master=nashik_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

    plt.suptitle("Nashik Specific Analysis", fontsize=14, fontweight='bold')
    plt.subplots_adjust(wspace=0.4)

    button_frame = Frame(nashik_frame)
    button_frame.pack(pady=10)

    prev_button = Button(button_frame, text="City Specific", font=("Arial bold", 16), fg="white", bg="#3c8dbc", padx=20, borderwidth=0, command=prev_nashik)
    prev_button.grid(row=0, column=0, padx=410)

    end_button = Button(button_frame, text="Exit", font=("Arial bold", 16), fg="white", bg="#3c8dbc", padx=20,  borderwidth=0, command=finish)
    end_button.grid(row=0, column=1, padx=410)

def NagpurAnalysis():
    second_frame.destroy()

    global nagpur_frame
    nagpur_frame = Frame(root)
    nagpur_frame.pack(expand=True, fill=BOTH)

    city_filter = df['City'] == 'Nagpur'
    city_df = df[city_filter]

    region_counts = city_df.groupby('Region').size().reset_index(name='counts')
    regions = region_counts['Region'].tolist()
    counts = region_counts['counts'].tolist()

    Tow_counts = city_df.groupby('Type of Waste').size().reset_index(name='counts')
    Towm = Tow_counts['Type of Waste'].tolist()
    Tow_counts = Tow_counts['counts'].tolist()

    fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(20, 9.1))

    colors = ["#2554C7", "#728FCE", "#78C7C7", "#50EBEC", "#7FFFD4", "#CFECEC", "#AFEEEE", "#8EEBEC", "#CCFFFF"]
    axs[0].bar(regions, counts, color=colors)
    axs[0].set_title('Waste Reported')
    axs[0].set_xticklabels(regions, rotation=60)


    colors = ["#7FFFD4", "#50EBEC", "#78C7C7", "#728FCE", "#2554C7"]
    axs[1].pie(Tow_counts, labels=Towm, autopct='%1.1f%%', startangle=90, colors=colors)
    axs[1].axis('equal')
    axs[1].set_title('Type Of Waste Reported')

    canvas = FigureCanvasTkAgg(fig, master=nagpur_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

    plt.suptitle("Nagpur Specific Analysis", fontsize=14, fontweight='bold')
    plt.subplots_adjust(wspace=0.4)

    button_frame = Frame(nagpur_frame)
    button_frame.pack(pady=10)

    prev_button = Button(button_frame, text="City Specific", font=("Arial bold", 16), fg="white", bg="#3c8dbc", padx=20, borderwidth=0, command=prev_nagpur)
    prev_button.grid(row=0, column=0, padx=410)

    end_button = Button(button_frame, text="Exit", font=("Arial bold", 16), fg="white", bg="#3c8dbc", padx=20,  borderwidth=0, command=finish)
    end_button.grid(row=0, column=1, padx=410)


def AurangabadAnalysis():
    second_frame.destroy()

    global aurangabad_frame
    aurangabad_frame = Frame(root)
    aurangabad_frame.pack(expand=True, fill=BOTH)

    city_filter = df['City'] == 'Aurangabad'
    city_df = df[city_filter]

    region_counts = city_df.groupby('Region').size().reset_index(name='counts')
    regions = region_counts['Region'].tolist()
    counts = region_counts['counts'].tolist()

    Tow_counts = city_df.groupby('Type of Waste').size().reset_index(name='counts')
    Towm = Tow_counts['Type of Waste'].tolist()
    Tow_counts = Tow_counts['counts'].tolist()

    fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(20, 9.1))

    colors = ["#2554C7", "#728FCE", "#78C7C7", "#50EBEC", "#7FFFD4", "#CFECEC", "#AFEEEE", "#8EEBEC", "#CCFFFF"]
    axs[0].bar(regions, counts, color=colors)
    axs[0].set_title('Waste Reported')
    axs[0].set_xticklabels(regions, rotation=60)


    colors = ["#7FFFD4", "#50EBEC", "#78C7C7", "#728FCE", "#2554C7"]
    axs[1].pie(Tow_counts, labels=Towm, autopct='%1.1f%%', startangle=90, colors=colors)
    axs[1].axis('equal')
    axs[1].set_title('Type Of Waste Reported')

    canvas = FigureCanvasTkAgg(fig, master=aurangabad_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

    plt.suptitle("Aurangabad Specific Analysis", fontsize=14, fontweight='bold')
    plt.subplots_adjust(wspace=0.4)

    button_frame = Frame(aurangabad_frame)
    button_frame.pack(pady=10)

    prev_button = Button(button_frame, text="City Specific", font=("Arial bold", 16), fg="white", bg="#3c8dbc", padx=20, borderwidth=0, command=prev_aurangabad)
    prev_button.grid(row=0, column=0, padx=410)

    end_button = Button(button_frame, text="Exit", font=("Arial bold", 16), fg="white", bg="#3c8dbc", padx=20,  borderwidth=0, command=finish)
    end_button.grid(row=0, column=1, padx=410)




root=Tk()
root.state('zoomed')
main_frame = Frame(root)
main_frame.pack(expand=True, fill=BOTH)

df = pd.read_csv("D:\coding\Python\my_csv_file.csv")

A = df['City'].value_counts()
Cities = list(dict(A))
No_compl = (A.tolist())

B = df['Type of Waste'].value_counts()
Tow = list(dict(B))
count = B.tolist()

fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(20, 9.1))

color=["#2554C7","#728FCE","#78C7C7","#50EBEC","#7FFFD4"]
axs[0].bar(Cities[0:6], No_compl[0:], color=color)
axs[0].set_title('Waste Reported')


color=["#7FFFD4","#50EBEC","#78C7C7","#728FCE","#2554C7"]
axs[1].pie(count, labels=Tow, autopct='%1.1f%%', startangle=90,colors=color)
axs[1].axis('equal')
axs[1].set_title('Type Of Waste Reported')

canvas = FigureCanvasTkAgg(fig, master=main_frame)
canvas.draw()
canvas.get_tk_widget().pack()

plt.suptitle("Overall Analysis", fontsize=14, fontweight='bold')

plt.subplots_adjust(wspace=0.4)

my_button = Button(main_frame, text="City Specific", font=("Arial bold", 16), fg="white", bg="#3c8dbc", padx=20, pady=10, borderwidth=0, command=next).pack(padx=30,side=BOTTOM, anchor="e")

root.mainloop()
