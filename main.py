from tkinter import *
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage


class QR_Generator:
    def __init__(self, root):
        self.root = root
        # for width,height,left_margin and up_margin respectively
        self.root.geometry("900x550+200+100")
        # for the heading
        self.root.title("QR Code Generator || Developed by stunner007")
        # will not let user to change the size of the window
        self.root.resizable(False, False)

        title = Label(self.root, text="QR Code Generator", font=(
            "times new roman", 40), bg='dark blue', fg='yellow', anchor='w').place(x=0, y=0, relwidth=1)
        # at the anchor tag use w for west and e for east allignment of the heading

        # ******Variables*******
        self.var_stu_ID = StringVar()
        self.var_stu_name = StringVar()
        self.var_stu_DOB = StringVar()
        self.var_stu_Dept = StringVar()

        # ******Heading of the app*****
        name_frame = Frame(self.root, bd=4, relief=RIDGE, bg='skyblue')
        name_frame.place(x=50, y=100, width=450, height=400)

        name_title = Label(name_frame, text=" Student Details ", font=(
            "times new roman", 30), bg='orange', fg='blue')
        name_title.place(x=0, y=0, relwidth=1)

        # Defining the name of the columns
        label_studentID = Label(name_frame, text="Enter Student ID ", font=(
            "times new roman", 15, 'bold'), bg='skyblue').place(x=20, y=70)
        label_studentName = Label(name_frame, text="Enter Student Name ", font=(
            "times new roman", 15, 'bold'), bg='skyblue').place(x=20, y=120)
        label_studentDOB = Label(name_frame, text="Student Date of Birth ", font=(
            "times new roman", 15, 'bold'), bg='skyblue').place(x=20, y=170)
        label_studentDept = Label(name_frame, text="Student Department ", font=(
            "times new roman", 15, 'bold'), bg='skyblue').place(x=20, y=220)

        # Taking the
        text_studentID = Entry(name_frame, font=(
            "times new roman", 15), textvariable=self.var_stu_ID, bg='lightblue').place(x=225, y=70)
        text_studentName = Entry(name_frame, font=(
            "times new roman", 15), textvariable=self.var_stu_name, bg='lightblue').place(x=225, y=120)
        text_studentDOB = Entry(name_frame, font=(
            "times new roman", 15), textvariable=self.var_stu_DOB, bg='lightblue').place(x=225, y=170)
        text_studentDept = Entry(name_frame, font=(
            "times new roman", 15), textvariable=self.var_stu_Dept, bg='lightblue').place(x=225, y=220)

        btn_generate = Button(name_frame, text='Generate QR', command=self.generate, font=(
            "times new roman", 15, 'bold'), bg='green', fg='pink').place(x=100, y=275)
        btn_Clear = Button(name_frame, text='Clear', command=self.clear, font=(
            "times new roman", 15, 'bold'), bg='green', fg='purple').place(x=270, y=275)

        self.msg = ''
        self.lbl_msg = Label(name_frame, text=self.msg, font=(
            "times new roman", 20, 'bold'), bg='white', fg='green')
        self.lbl_msg.place(x=0, y=340, relwidth=1)

        # Student qr code frame
        qr_frame = Frame(self.root, bd=4, relief=RIDGE, bg='skyblue')
        qr_frame.place(x=550, y=100, height=400, width=300)

        student_qrtitle = Label(qr_frame, text=" Student QR Code ", font=(
            "times new roman", 25), bg='orange', fg='blue')
        student_qrtitle.place(x=0, y=0, relwidth=1)

        self.qr_code = Label(qr_frame, text='QR Code \nNot Generated', font=(
            "times new roman", 15), bg='grey', fg='blue', bd=1, relief=RIDGE)
        self.qr_code.place(x=50, y=100, width=180, height=180)

    def clear(self):
        self.var_stu_ID.set('')
        self.var_stu_name.set('')
        self.var_stu_DOB.set('')
        self.var_stu_Dept.set('')
        self.msg = ''
        self.lbl_msg.config(text=self.msg)
        self.qr_code.config(image='')

    def generate(self):
        if self.var_stu_ID.get() == '' or self.var_stu_name.get() == '' or self.var_stu_DOB.get() == '' or self.var_stu_Dept.get() == '':
            self.msg = 'All fields are required.'
            self.lbl_msg.config(text=self.msg, fg='red')
        else:
            qr_data = (
                f"Student ID: {self.var_stu_ID.get()}\nStudent Name: {self.var_stu_name.get()}\nStudent DOB: {self.var_stu_DOB.get()}\nStudent Department: {self.var_stu_Dept.get()}")
            qr_code=qrcode.make(qr_data)
            qr_code=resizeimage.resize_cover(qr_code,[180,180])
            qr_code.save("QR_"+str(self.var_stu_ID.get())+'.png')

            # ******QR code image Update******
            self.im=ImageTk.PhotoImage(qr_code)
            self.qr_code.config(image=self.im)
            # ********Updating notification*******
            self.msg = 'QR Generated Successfully!!!'
            self.lbl_msg.config(text=self.msg, fg='green')


root = Tk()
obj = QR_Generator(root)
root.mainloop()
