from tkinter import *
from tkcalendar import Calendar
import pandas as pd
from tkinter import messagebox

def showdates(strDate):
    # Youtube Link: https://www.youtube.com/watch?v=PgLjwl6Br0k

    import tkinter as tk
    from tkinter import filedialog, messagebox, ttk

    # initalise the tkinter GUI
    root = tk.Tk()

    root.geometry("800x500")  # set the root dimensions
    root.pack_propagate(False)  # tells the root to not let the widgets inside it determine its size.
    root.resizable(0, 0)  # makes the root window fixed in size.

    # Frame for TreeView
    frame1 = tk.LabelFrame(root, text="Excel Data")
    frame1.place(height=300, width=800)

    # Frame for open file dialog
    file_frame = tk.LabelFrame(root, text="Open File")
    file_frame.place(height=100, width=400, rely=0.66, relx=0.24)

    # Buttons

    button2 = tk.Button(file_frame, text="Load File", command=lambda: Load_excel_data())
    button2.place(rely=0.2, relx=0.40)


    ## Treeview Widget
    tv1 = ttk.Treeview(frame1)
    tv1.place(relheight=1, relwidth=1)  # set the height and width of the widget to 100% of its container (frame1).

    treescrolly = tk.Scrollbar(frame1, orient="vertical",
                               command=tv1.yview)  # command means update the yaxis view of the widget
    treescrollx = tk.Scrollbar(frame1, orient="horizontal",
                               command=tv1.xview)  # command means update the xaxis view of the widget
    tv1.configure(xscrollcommand=treescrollx.set,
                  yscrollcommand=treescrolly.set)  # assign the scrollbars to the Treeview Widget
    treescrollx.pack(side="bottom", fill="x")  # make the scrollbar fill the x axis of the Treeview widget
    treescrolly.pack(side="right", fill="y")  # make the scrollbar fill the y axis of the Treeview widget



    def Load_excel_data():
        """If the file selected is valid this will load the file into the Treeview"""
        file_path = strDate
        print(file_path)
        try:
            excel_filename = r"{}".format(file_path)
            if excel_filename[-4:] == ".csv":
                df = pd.read_csv(excel_filename)
            else:
                df = pd.read_excel(excel_filename)

        except ValueError:
            tk.messagebox.showerror("Information", "The file you have chosen is invalid")
            return None
        except FileNotFoundError:
            tk.messagebox.showerror("Information", f"No such file as {file_path}")
            return None

        clear_data()
        tv1["column"] = list(df.columns)
        tv1["show"] = "headings"
        for column in tv1["columns"]:
            tv1.heading(column, text=column)  # let the column heading = column name

        df_rows = df.to_numpy().tolist()  # turns the dataframe into a list of lists
        for row in df_rows:
            tv1.insert("", "end",
                       values=row)  # inserts each list into the treeview. For parameters see https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.insert
        return None

    def clear_data():
        tv1.delete(*tv1.get_children())
        return None

    root.mainloop()



# creating an object of tkinter

tkobj = Tk()

# setting up the geomentry

tkobj.geometry("400x400")
tkobj.title("Calendar picker")
#creating a calender object

tkc = Calendar(tkobj,selectmode = "day",year=2022,month=10,date=25,date_pattern="DD-MM-YYYY")

#display on main window
tkc.pack(pady=40)

# getting date from the calendar

def fetch_date():
    dates.config(text = "Selected Date is: " + tkc.get_date())

#add button to load the date clicked on calendar

but = Button(tkobj,text="Select Date",command=fetch_date, bg="black", fg='white')
#displaying button on the main display
but.pack()
#Label for showing date on main display
dates = Label(tkobj,text="",bg='black',fg='white')
dates.pack(pady=20)


def a():
    import numpy as np  # importing essential packages
    import pandas as pd
    from datetime import date  # Import date class from datetime module
    import glob  # used for getting the data or record of student

    df = pd.read_csv('Attendence/Attendance.csv')  # TO OPEN A CSV where attendance is market

    df = df.dropna(axis=0)  # TO DROP OR REMOVE NAN or NULL Value
    today = date.today()  # getting todays date
    today = str(today.strftime("%d-%m-%Y"))

    df.drop(df[df['Date'] != today].index, inplace=True)  # not today ones should be removed

    df.sort_values(by=['ID', 'Time'], inplace=True)  # sorting

    df.drop_duplicates(subset=['ID'], keep='first', inplace=True)  # REMOVING DUPLICATES

    df.reset_index(inplace=True, drop=True)  # RESETING INDEX

    df.to_csv("Dates/" + today + ".csv", index=False)

    # to clear ated.csv as attendance is already sorted

    df = df.iloc[0:0]

    # df.to_csv('Attendace.csv')

    # here starts the calculation or calcukating students attendance and stuff
    df = pd.concat(map(pd.read_csv, glob.glob("Dates" + "/*.csv")))  # big data frame of all attendance record

    date = tkc.get_date()
    try:
        df = pd.read_csv('Dates/' + date + '.csv')
        showdates('Dates/' + date + '.csv')
        print(df)
    except:
        print("No file Found")
        messagebox.showinfo("Error", "No Data found on that date")



but = Button(tkobj,text="show attendace",command=a, bg="black", fg='white')
#displaying button on the main display
but.pack()
#starting the object
tkobj.mainloop()