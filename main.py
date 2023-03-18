import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2
import pandas as pd


class FirstPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        load = Image.open("imp3.jpg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)

        border = tk.LabelFrame(self, text='Login', bg='ivory', bd=20, font=("Arial", 20))
        border.pack(fill="both", expand="yes", padx=130, pady=130)

        L1 = tk.Label(border, text="Username", font=("Arial Bold", 15), bg='ivory')
        L1.place(x=50, y=20)
        T1 = tk.Entry(border, width=30, bd=5)
        T1.place(x=180, y=20)

        L2 = tk.Label(border, text="Password", font=("Arial Bold", 15), bg='ivory')
        L2.place(x=50, y=80)
        T2 = tk.Entry(border, width=30, show='*', bd=5)
        T2.place(x=180, y=80)

        def verify():
            try:
                with open("LoginPass.txt", "r") as f:
                    info = f.readlines()
                    i = 0
                    for e in info:
                        u, p = e.split(",")
                        if u.strip() == T1.get() and p.strip() == T2.get():
                            controller.show_frame(SecondPage)
                            i = 1
                            break
                    if i == 0:
                        messagebox.showinfo("Error", "Please provide correct username and password!!")
            except:
                messagebox.showinfo("Error", "Please provide correct username and password!!")

        B1 = tk.Button(border, text="Submit", font=("Arial", 15), command=verify)
        B1.place(x=320, y=115)

        def register():
            window = tk.Tk()
            window.resizable(0, 0)
            window.configure(bg="light pink")
            window.title("Register")
            l1 = tk.Label(window, text="Username:", font=("Arial Bold", 15),bg="light pink")
            l1.place(x=10, y=10)
            t1 = tk.Entry(window, width=30, bd=5)
            t1.place(x=200, y=10)

            l2 = tk.Label(window, text="Password:", font=("Arial Bold", 15), bg="light pink")
            l2.place(x=10, y=60)
            t2 = tk.Entry(window, width=30, show="*", bd=5)
            t2.place(x=200, y=60)

            l3 = tk.Label(window, text="Confirm Password:", font=("Arial Bold", 15),bg="light pink")
            l3.place(x=10, y=110)
            t3 = tk.Entry(window, width=30, show="*", bd=5)
            t3.place(x=200, y=110)

            def check():
                if t1.get() != "" or t2.get() != "" or t3.get() != "":
                    if t2.get() == t3.get():
                        with open("LoginPass.txt", "a") as f:
                            f.write(t1.get() + "," + t2.get() + "\n")
                            messagebox.showinfo("Welcome", "You are registered successfully!!")

                    else:
                        messagebox.showinfo("Error", "Your password didn't get match!!")
                else:
                    messagebox.showinfo("Error", "Please fill the complete field!!")

            b1 = tk.Button(window, text="Sign In", font=("Arial", 15), bg="#ffc22a", command=check)
            b1.place(x=170, y=150)



            window.geometry("470x220")
            window.mainloop()

        B2 = tk.Button(self, text="Register", bg="dark orange", font=("Arial", 15), command=register)
        B2.place(x=650, y=20)




class SecondPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        load1 = Image.open("imp4.jpg")
        resized = load1.resize((800, 500), Image.ANTIALIAS)
        photo1 = ImageTk.PhotoImage(resized)
        label = tk.Label(self, image=photo1)
        label.image = photo1
        label.place(x=0, y=0)

        def StudentRegister():
            window = tk.Tk()
            window.resizable(0, 0)
            window.configure(bg="deep sky blue")
            window.title("StudentRegister")
            l1 = tk.Label(window, text="Name:", font=("Arial", 15), bg="deep sky blue")
            l1.place(x=10, y=10)
            t1 = tk.Entry(window, width=30, bd=5)
            t1.place(x=200, y=10)


            l2 = tk.Label(window, text="ID:", font=("Arial", 15), bg="deep sky blue")
            l2.place(x=10, y=60)
            t2 = tk.Entry(window, width=30, bd=5)
            t2.place(x=200, y=60)

            l3 = tk.Label(window, text="Phone Number:", font=("Arial", 15), bg="deep sky blue")
            l3.place(x=10, y=110)
            t3 = tk.Entry(window, width=30, bd=5)
            t3.place(x=200, y=110)

            l4 = tk.Label(window, text="Upload an Image:", font=("Arial", 15), bg="deep sky blue")
            l4.place(x=10, y=160)

            def save():
                while True:
                    if t1.get() != "" and t2.get() != "" and t3.get() != "":
                        with open("StudentRegister.txt", "a") as f:
                            f.write(t1.get() + "," + t2.get() + "," + t3.get() + "\n")
                            messagebox.showinfo("Saved","Student Info saved successfully!!")
                    else:
                        messagebox.showinfo("Error", "please enter the values")

                    break

            def saveimg():
                cam = cv2.VideoCapture(0)

                cv2.namedWindow("test")

                name = (t1.get())
                id = (t2.get())
                phone = (t3.get())
                while True:
                    ret, frame = cam.read()
                    if not ret:
                        print("failed to grab frame")
                        break
                    cv2.imshow("Taking Image", frame)

                    k = cv2.waitKey(1)
                    if k % 256 == 27:
                        # ESC pressed
                        print("Escape hit, closing...")
                        break
                    elif k % 256 == 32:
                        # SPACE pressed
                        cv2.imwrite("Images/" + name + "," + id + "," + phone + ".jpg", frame)
                        #cv2.imwrite(img_name, frame)
                        print("Image taken")
                        break

                cam.release()

                cv2.destroyAllWindows()

            Button = tk.Button(window, text= "Load Image", font=("Arial", 15), command=saveimg)
            Button.place(x=200, y=160)

            Button = tk.Button(window, text= "Save", font=("Arial", 15), command=save)
            Button.place(x=430, y=205)

            window.geometry("500x250")
            window.mainloop()

        Button = tk.Button(self, text="Student Register", width=20,font=("Arial", 20), command=StudentRegister)
        Button.place(x=250, y=100)

        def Takeattendance():
            import os
            import cv2
            import numpy as np
            import face_recognition
            from datetime import datetime

            path = 'Images'
            images = []
            classNames = []
            myList = os.listdir(path)

            # To Loop Throgh all images
            for cls in myList:
                curImg = cv2.imread(f'{path}/{cls}')
                images.append(curImg)
                classNames.append(os.path.splitext(cls)[0])
            print(classNames)

            def FindEncodings(Images):
                encodeList = []
                for img in Images:
                    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                    encode = face_recognition.face_encodings(img)[0]
                    encodeList.append(encode)
                return encodeList

            def markAttendence(name):
                with open('Attendence/Attendance.csv', 'r+') as f:
                    myDataList = f.readline()
                    nameList = []
                    namesplit = name.split(',')
                    for line in myDataList:
                        entry = line.split(',')
                        nameList.append(entry[0])
                    if name not in nameList[0]:
                        now = datetime.now()
                        tString = now.strftime('%H:%M:%S')
                        dtstring = now.strftime('%d-%m-%Y')
                        f.writelines(f'\n{namesplit[1]},{namesplit[0]},{namesplit[2]},{tString},{dtstring}')

            encodeListKnown = FindEncodings(images)
            print("Encodeing completed")

            cam = cv2.VideoCapture(0)

            while True:
                success, img = cam.read()
                imgS = cv2.resize(img, (0, 0), None, 1, 1)
                imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

                faceLoc = face_recognition.face_locations(imgS)
                encodeCur = face_recognition.face_encodings(imgS, faceLoc)

                for encodeFace, FaceLoc in zip(encodeCur, faceLoc):
                    matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
                    faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
                    print(faceDis)
                    matchIndex = np.argmin(faceDis)

                    if matches[matchIndex]:
                        name = classNames[matchIndex]
                        splitname = name.split(",")
                        print(splitname[0])
                        y1, x2, y2, x1 = FaceLoc
                        y1, x2, y2, x1 = y1 * 1, x2 * 1, y2 * 1, x1 * 1
                        cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
                        cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (255, 0, 0), cv2.FILLED)
                        cv2.putText(img, splitname[0], (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                        markAttendence(name)
                k = cv2.waitKey(1)
                if k % 256 == 27:
                    # ESC pressed
                    print("Escape hit, closing...")
                    break

                cv2.imshow('Web Cam', img)
                cv2.waitKey(1)


        Button = tk.Button(self, text="Take Attendance",width=20, font=("Arial", 20), command=Takeattendance)
        Button.place(x=250, y=180)

        Button = tk.Button(self, text="Show Attendance",width=20, font=("Arial", 20), command=lambda: controller.show_frame(ThirdPage))
        Button.place(x=250, y=270)

        Button = tk.Button(self, text="QUIT", font=("Arial", 15),command=lambda: controller.show_frame(FirstPage))
        Button.place(x=650, y=380)


class ThirdPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        l1 = tk.Label(self, text="Please Enter ID :", font=("Arial", 20))
        l1.place(x=80, y=150)
        t1 = tk.Entry(self, width=20, bd=5,font=('Arial 20'))
        t1.place(x=300, y=150)

        def database():
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

           # df.to_csv('Attendance.csv')

            # here starts the calculation or calcukating students attendance and stuff
            df = pd.concat(map(pd.read_csv, glob.glob("Dates" + "/*.csv")))  # big data frame of all attendance record

            id_number = str(t1.get())  # getting id number

            pre_att = df['ID'].value_counts()[id_number]  # gets count or occurences of student attendance
            csv_files = glob.glob("Dates" + "/*.csv")  # list of csv files in dates folder
            tot_lec = len(csv_files)  # count of csv files in folder
            print(pre_att)
            print(f"The attendance percentage of student with id number : {id_number} is {pre_att * 100 / tot_lec}%")
            percent = pre_att * 100 / tot_lec
            percent = str(percent)


            L1 = tk.Label(self, text=percent, width=15, font=("Arial Bold", 20))
            L1.place(x=430, y=260)

        def record():

            database()


        def a():

            os.system("python database.py")


        def a1():
            os.system("python textdate.py")

        Button = tk.Button(self, text=" ", width=20, font=("Arial", 20))
        Button.place(x=420, y=250)

        Button = tk.Button(self, text="Percentage Of Student ",width=20, font=("Arial", 20), command=record)
        Button.place(x=80, y=250)

        Button = tk.Button(self, text="Show DataBase",width=20, font=("Arial", 20), command=a)
        Button.place(x=420, y=350)

        Button = tk.Button(self, text="Show Date",width=20, font=("Arial", 20), command=a1)
        Button.place(x=80, y=350)

        Button = tk.Button(self, text="BACK", font=("Arial", 15), command=lambda: controller.show_frame(SecondPage))
        Button.place(x=50, y=10)


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a window
        window = tk.Frame(self)
        window.pack()

        window.grid_rowconfigure(0, minsize=500)
        window.grid_columnconfigure(0, minsize=800)

        self.frames = {}
        for F in (FirstPage, SecondPage,ThirdPage):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(FirstPage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()

app = Application()

app.maxsize(1080, 720)
app.mainloop()
