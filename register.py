from tkinter import *
from PIL import ImageTk, Image
from tkinter.font import ROMAN


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("REGISTRATION ")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="gray")
        # background images
        #self.bground = ImageTk.PhotoImage(file="images/bg2.jpg")
        # bground = Label(self.root, image=self.bground).place(
        #   x=250, y=0, width=1000, relheight=1)
        # left images
        self.left = ImageTk.PhotoImage(file="images/background.jpg")
        bground = Label(self.root, image=self.left).place(
            x=80, y=100, width=400, height=500)

        # -----register frame-------
        frame1 = Frame(self.root, bg="white")
        frame1.place(x=480, y=100, width=700, height=500)
        title = Label(frame1, text="REGISTER HERE", font=(
            "times new roman", 20, "bold"), bg="white", fg="black").place(x=50, y=30)
        f_name = Label(frame1, text="first name".upper(), font=(
            "times new roman", 15, "bold"), bg="white", fg="blue").place(x=50, y=100)
        txt_fname = Entry(frame1, font=(
            "times new roman", 15), bg="lightgray").place(x=50, y=130, width=250)
        l_name = Label(frame1, text="last name".upper(), font=(
            "times new roman", 15, "bold"), bg="white", fg="blue").place(x=370, y=100)
        txt_lname = Entry(frame1, font=(
            "times new roman", 15), bg="lightgray").place(x=370, y=130, width=250)
        # ----secound layer------
        city_name = Label(frame1, text="city".upper(), font=(
            "times new roman", 15, "bold"), bg="white", fg="blue").place(x=50, y=160)
        txt_cityname = Entry(frame1, font=(
            "times new roman", 15), bg="lightgray").place(x=50, y=190, width=250)
        state_name = Label(frame1, text="state".upper(), font=(
            "times new roman", 15, "bold"), bg="white", fg="blue").place(x=370, y=160)
        txt_statename = Entry(frame1, font=(
            "times new roman", 15), bg="lightgray").place(x=370, y=190, width=250)
        # ----third layer------
        contat_no = Label(frame1, text="contact-no".upper(), font=(
            "times new roman", 15, "bold"), bg="white", fg="blue").place(x=50, y=270)
        txt_contact = Entry(frame1, font=(
            "times new roman", 15), bg="lightgray").place(x=50, y=190, width=250)
        email_name = Label(frame1, text="email".upper(), font=(
            "times new roman", 15, "bold"), bg="white", fg="blue").place(x=370, y=160)
        txt_emailname = Entry(frame1, font=(
            "times new roman", 15), bg="lightgray").place(x=370, y=190, width=250)


root = Tk()
obj = Register(root)
root.mainloop()
