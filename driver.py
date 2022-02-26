from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

import sqlite3

#Main screen
root = Tk()
root.title("Login")
root.geometry("512x384")
root.iconbitmap('icon_eul.ico')
root.resizable(width=False, height=False)
bg_image = PhotoImage(file = "eul_bg1.png")


bg_label = Label(root,image= bg_image)
bg_label.place(x=0,y=0)


#Create canvas
canvas = Canvas(root,width=512,height = 384)
canvas.pack(fill="both",expand = True)

#Set image in canvas
canvas.create_image(0,0,image=bg_image,anchor="nw")

#Login Entry boxes
u_name = Entry(root, width=30)
u_name.place(x=182,y=150)
p_word = Entry(root, width=30)
p_word.place(x=182,y=180,)

#login entry box labels
canvas.create_text(140,160,text = "Username",font=("Franklin Gothic Demi",10))
canvas.create_text(140,190,text = "Password",font=("Franklin Gothic Demi",10))
canvas.create_text(140,230, text = "Login as",font=("Franklin Gothic Demi",10))
lg_arg = ""
def select(event):
    global lg_arg
    if selection.get() == 'Student':
       lg_arg = selection.get() 
    elif selection.get() == 'Instructor':
        lg_arg = selection.get() 
    elif selection.get() == 'Faculty coordinator':
        lg_arg = selection.get()

        

def login():
    global lg_arg 
    conn = sqlite3.connect('university_.db')
    c = conn.cursor()
    User_n = u_name.get()
    Pass = p_word.get()
    if lg_arg == 'Student':
        c.execute("""SELECT username,password
                     FROM student_login 
                     WHERE username = :value1 
                     AND password = :value2""",
                     {'value1':User_n,'value2':Pass})
        results = c.fetchall()
        if results:
            login = True

        else:
            login = False
        if login == True:
            student_screen(User_n)
            p_word.delete(0,END)
        if login == False:
            error = Label(root,text='Email or username is wrong',fg ='red')
            u_name.delete(0,END)
            p_word.delete(0,END)
            error.place(x = 182,y=250)

    elif lg_arg == 'Instructor':
        c.execute("""SELECT username,password
                     FROM instructor_login 
                     WHERE username = :value1 
                     AND password = :value2""",
                     {'value1':User_n,'value2':Pass})
        results = c.fetchall()
        if results:
            login = True
        else:
            login = False
        if login == True:
            instructor_screen(User_n)
            p_word.delete(0,END)
        if login == False:
            error = Label(root,text='Email or username is wrong',fg ='red')
            u_name.delete(0,END)
            p_word.delete(0,END)
            error.place(x = 182,y=250)

    elif lg_arg == 'Faculty coordinator' :
        c.execute("""SELECT username,password
                     FROM fadmin_login 
                     WHERE username = :value1 
                     AND password = :value2""",
                     {'value1':User_n,'value2':Pass})
        results = c.fetchall()
        if results:
            login = True

        else:
            login = False
        if login == True:
            fadminscreen(User_n)
            p_word.delete(0,END)
        if login == False:
            error = Label(root,text='Email or username is wrong',fg ='red')
            u_name.delete(0,END)
            p_word.delete(0,END)
            error.place(x = 182,y=250)
    conn.close()
    
selection = StringVar()
selection.set("pick one")
drop = OptionMenu(root,selection,"Student","Instructor","Faculty coordinator",command=select)
drop.place(x=182,y=210)
 

submit_btn = Button(root,text="Login",command = login, height= 0, width =10)
submit_btn.place(x = 182,y=280)
submit_btn.bind("selection",select)



def student_screen(Uname):
    root.withdraw()
    screen1 = Toplevel(root)
    
    
    screen1.title('Student')
    screen1.geometry('900x690+0+0')
    screen1.iconbitmap('icon_eul.ico')
    screen1.config(bg="Light Blue",bd=6)
    screen1.resizable(width=False, height=False)

    Title_Frame = LabelFrame(screen1,bd=2,width=900,height=70,padx=54,pady=80,bg = "Blue",relief = FLAT
        ,font =('Helvetica',33),text=" European University of Lefke Student Portal ",fg='White')
    Title_Frame.pack(side=TOP)



    Info_Frame = Frame(screen1,bd=6,width=350,height=500,padx=5,pady=8,bg = "Ghost White",relief = RIDGE)
    Info_Frame.pack(side=LEFT)
    Info_Frame.pack_propagate(0)

    Display_Frame = LabelFrame(screen1,bd=2,width=450,height=500,padx=54,pady=8,bg = "Ghost White",
        font =('Calibiri',20),relief = RIDGE,text='Information Tab')
    Display_Frame.pack(side=RIGHT)
    Display_Frame.grid_propagate(0)

    Picture_Frame = Frame(Info_Frame,bd=6,width=160,height=160,bg = "Ghost White",relief = RIDGE)
    Picture_Frame.pack()
    
    #===========================================================Student details frame=====================
    def logout():
        screen1.withdraw()
        root.deiconify()
        messagebox.showinfo(' ','Logout Successful')


    def getcourse():
        
        listbox.delete(0,END)
        conn = sqlite3.connect('university_.db')
        c = conn.cursor()
        c.execute("""SELECT DISTINCT course.title
                     FROM course,student_login,takes
                     WHERE takes.ID = :value AND
                    takes.course_id = course.course_id """,{'value':ID})  
        for subjects in c.fetchall():
            listbox.insert(END," ".join(subjects),str(""))
        c.close()
    def changepassword():

        p_screen = Toplevel(screen1)
        p_screen.title('Change Password')
        p_screen.geometry('300x300+0+0')
        p_screen.iconbitmap('icon_eul.ico')
        p_screen.config(bg="Light Blue",bd=6)
        p_screen.resizable(width=False, height=False)


        entry_frame = Frame(p_screen,bd=6,width=250,height=250,padx=5,pady=8,bg = "Ghost White",relief = RIDGE)
        entry_frame.grid(row=0,column=0,sticky="")
        entry_frame.grid_propagate(0)
        p_screen.grid_rowconfigure(0,weight=1)
        p_screen.grid_columnconfigure(0,weight=1)

        old_entry = Entry(entry_frame,font=("arial",8),width=20)
        old_entry.place(x = 100,y=100)
       

        new_entry = Entry(entry_frame,font=("arial",8),width=20)
        new_entry.place(x = 105,y=150)
        
        info_label = Label(entry_frame,font=("arial",11,'bold'),text = "Enter old Password first",bg="Ghost White")
        info_label.place(x = 40,y=30)

        new_label = Label(entry_frame,font=("arial",10),text = "New Password ",bg="Ghost White")
        new_label.place(x = 8,y=150)

        old_label = Label(entry_frame,font=("arial",10),text = "Old Password ",bg="Ghost White")
        old_label.place(x = 8,y=100)


        def confirm():
            value = ID
            conn = sqlite3.connect('university_.db')
            c = conn.cursor()
            c.execute("SELECT password FROM student_login WHERE student_login.username = :user",{'user':u_name.get()})
            
            result = c.fetchone()
            for items in result:
                if old_entry.get() == items:
                    confirm = True
                else:
                    confirm = False
            conn.close()
            if confirm == True:
               conn = sqlite3.connect('university_.db')
               c = conn.cursor()
               c.execute("UPDATE student_login SET password = :pass WHERE ID = :userid",{'pass':new_entry.get(),'userid':value})
               conn.commit()
               messagebox.showinfo('','Password changed successfully')
               p_screen.withdraw()

            if confirm == False:
                messagebox.showinfo('','Old password does not match')
                new_entry.delete(0,END)
            conn.close()


        submit_btn = Button(entry_frame,text="Confirm",height= 0, width =10,command=confirm)
        submit_btn.place(x = 100,y=190)
    def enter():
        listbox.delete(0,END)
        course_ = select_course.get()
        conn = sqlite3.connect('university_.db')
        c = conn.cursor()
        listbox.insert(END,"Course Participants",str(""))
        if course_:
            c.execute("""SELECT student.name 
                        FROM student,takes
                        WHERE course_id = :c
                        AND student.ID = takes.ID""",{'c':course_})
            for std in c.fetchall():
                listbox.insert(END,str("------------------")," ".join(std),str(""))
        c.close()

    #===========================================================Buttons================================================
    logout_btn = Button(screen1,text="Logout",height= 0, width =10,command=logout)
    logout_btn.place(x = 800,y=650)

    update_btn = Button(Info_Frame,text="Change Password",height= 0, width =20,command = changepassword)
    update_btn.place(x = 10,y=450)

    details_btn = Button(Info_Frame,text="Enter",height= 0, width =10,bg="red",command = enter)
    details_btn.place(x = 130,y=380)

    info_btn = Button(Info_Frame,text="Courses",height= 0, width =10,command = getcourse)
    info_btn.place(x = 30,y=280)

    #===========================================================Labels and Entry widgets================================================
    conn = sqlite3.connect('university_.db')
    c = conn.cursor()
    c.execute("""SELECT course_id FROM takes,student_login 
                WHERE student_login.username = :selectuname 
                AND takes.ID = student_login.ID""",{'selectuname':Uname})
    courses = []
    for crs in c.fetchall():
        courses.extend(crs)

    select_course = StringVar()
    select_course.set("Select Course")
    crs_drop = OptionMenu(Info_Frame,select_course,*courses)
    crs_drop.place(x=30,y=350)
    
    crs_label = Label(Info_Frame,font=("arial",10),text = "See Course Participants",padx=2,pady=2,bg="Ghost White",fg="blue")
    crs_label.place(x=70,y=320)
    conn.close()



    #===========================================================Variables=====================
    conn = sqlite3.connect('university_.db')
    c = conn.cursor()
    global ID
    c.execute("""SELECT student.name FROM student,student_login WHERE student.ID = student_login.ID
                AND student_login.username = :user""",{'user':Uname})
    for item in c.fetchone ():
        Name = item

    c.execute("""SELECT student.dept_name FROM student,student_login WHERE student.ID = student_login.ID
                AND student_login.username = :user""",{'user':Uname})
    for item in c.fetchone ():
        d_name = item

    c.execute("""SELECT student .ID FROM student,student_login WHERE student.ID = student_login.ID
                AND student_login.username = :user""",{'user':Uname})
    for item in c.fetchone ():
        ID = item
    conn.close()
    #===========================================================Student details frame=====================

    ID_label = Label(Info_Frame,font=("arial",13,'bold'),text = "ID : " + str(ID),anchor='w',padx=2,pady=5,bg="Ghost White")
    ID_label.pack(fill='both')


    name_label = Label(Info_Frame,font=("arial",13,'bold'),text = "Name : " + str(Name),anchor='w',padx=2,pady=5,bg="Ghost White")
    name_label.pack(fill='both')

    d_name_label = Label(Info_Frame,font=("arial",13,'bold'),text = "Department : " + str(d_name),anchor='w',padx=2,pady=5,bg="Ghost White")
    d_name_label.pack(fill='both')


    #===========================================================Student details frame=====================
    scrollbar =  Scrollbar(Display_Frame) 
    scrollbar.grid(row=0,column=1,sticky = 'ns')

    listbox = Listbox(Display_Frame,width = 60, height=26,yscrollcommand = scrollbar.set)
    listbox.grid(row=0,column=0)
    scrollbar.config(command = listbox.yview)







def instructor_screen(Uname):
    root.withdraw()
    screen1 = Toplevel(root)


    screen1.title('Instructor')
    screen1.geometry('1200x690+0+0')
    screen1.iconbitmap('icon_eul.ico')
    screen1.config(bg="Light Blue",bd=6)
    screen1.resizable(width=False, height=False)

    Title_Frame = LabelFrame(screen1,bd=2,width=1200,height=70,padx=54,pady=80,bg = "Blue",relief = FLAT,
                            text="European University of Lefke Instructor Portal",fg='white',
                            font=('Helvetica',43))
    Title_Frame.pack(side=TOP)
    Title_Frame.grid_propagate(0)
        

    Info_Frame = Frame(screen1,bd=6,width=320,height=500,padx=2,pady=8,bg = "Ghost White",relief = RIDGE)
    Info_Frame.pack(side=LEFT)
    Info_Frame.pack_propagate(0)

    Display_Frame = LabelFrame(screen1,bd=2,width=400,height=500,padx=10,pady=8,bg = "Ghost White",
    font =('Calibiri',20),relief = RIDGE,text='Information Tab')
    Display_Frame.pack(side=RIGHT)
    Display_Frame.grid_propagate(0)

    Registration_Frame = LabelFrame(screen1,bd=2,width=380,height=500,padx=65,pady=100,bg = "Ghost White",
                font =('Calibiri',20),relief = RIDGE,text='Student Registration')
    Registration_Frame.place(x=360,y=125)
    Registration_Frame.grid_propagate(0)

    Picture_Frame = Frame(Info_Frame,bd=6,width=160,height=160,bg = "Ghost White",relief = RIDGE)
    Picture_Frame.pack()
    Picture_Frame.pack_propagate(0)

    pp = PhotoImage(file = "pp.png")
    pp_label = Label(Picture_Frame,image=pp)
    pp_label.pack()

    #===========================================================Button Functions=====================
    def getcourse():
        global ID
        value= ID
        listbox.delete(0,END)
        conn = sqlite3.connect('C:/Users/Dumebi Nwanze/Documents/SMSystem/university_.db')
        c = conn.cursor()
        c.execute("""SELECT DISTINCT course.title
                    FROM course,student_login,teaches
                    WHERE teaches.ID = :value AND
                    teaches.course_id = course.course_id """,{'value':ID})  
        for subjects in c.fetchall():
            listbox.insert(END," ".join(subjects),str(""))
        conn.close()

    def logout():
        screen1.withdraw()
        root.deiconify()
        messagebox.showinfo(' ','Logout Successful')


    def register():
        conn = sqlite3.connect('C:/Users/Dumebi Nwanze/Documents/SMSystem/university_.db')
        c = conn.cursor()
        
        c.execute("""INSERT INTO takes
                    VALUES (:id,:c_id,:sec_id,:semester,:year,"NULL")""",
                    {'id':Std_ID.get(),
                    'c_id':select_course.get(),
                    'sec_id':sec_ID.get(),
                    'semester':semester.get(),
                    'year':year.get()})
        conn.commit()
        messagebox.showinfo("","Student was registered successfully")
        Std_ID.delete(0,END)
        sec_ID.delete(0,END)
        semester.delete(0,END)
        year.delete(0,END)
        conn.close()
    def changepassword():

        p_screen = Toplevel(screen1)
        p_screen.title('Change Password')
        p_screen.geometry('300x300+0+0')
        p_screen.iconbitmap('icon_eul.ico')
        p_screen.config(bg="Light Blue",bd=6)
        p_screen.resizable(width=False, height=False)


        entry_frame = Frame(p_screen,bd=6,width=250,height=250,padx=5,pady=8,bg = "Ghost White",relief = RIDGE)
        entry_frame.grid(row=0,column=0,sticky="")
        entry_frame.grid_propagate(0)
        p_screen.grid_rowconfigure(0,weight=1)
        p_screen.grid_columnconfigure(0,weight=1)

        old_entry = Entry(entry_frame,font=("arial",8),width=20)
        old_entry.place(x = 100,y=100)
       

        new_entry = Entry(entry_frame,font=("arial",8),width=20)
        new_entry.place(x = 105,y=150)
        
        info_label = Label(entry_frame,font=("arial",11,'bold'),text = "Enter old Password first",bg="Ghost White")
        info_label.place(x = 40,y=30)

        new_label = Label(entry_frame,font=("arial",10),text = "New Password ",bg="Ghost White")
        new_label.place(x = 8,y=150)

        old_label = Label(entry_frame,font=("arial",10),text = "Old Password ",bg="Ghost White")
        old_label.place(x = 8,y=100)

        def confirm():
            value = ID
            conn = sqlite3.connect('university_.db')
            c = conn.cursor()
            c.execute("SELECT password FROM instructor_login WHERE instructor_login.username = :user",{'user':u_name.get()})
            
            result = c.fetchone()
            for items in result:
                if old_entry.get() == items:
                    confirm = True
                else:
                    confirm = False
            conn.close()
            if confirm == True:
               conn = sqlite3.connect('university_.db')
               c = conn.cursor()
               c.execute("UPDATE instructor_login SET password = :pass WHERE ID = :userid",{'pass':new_entry.get(),'userid':value})
               conn.commit()
               messagebox.showinfo('','Password changed successfully')
               p_screen.withdraw()

            if confirm == False:
                messagebox.showinfo('','Old password does not match')
                new_entry.delete(0,END)
            conn.close()
        submit_btn = Button(entry_frame,text="Confirm",height= 0, width =10,command=confirm)
        submit_btn.place(x = 100,y=190)
    def enter():
        listbox.delete(0,END)
        course_ = course_select.get()
        conn = sqlite3.connect('university_.db')
        c = conn.cursor()
        listbox.insert(END,"Course Details",str(""))
        if course_:
            c.execute("""SELECT title
                        FROM course
                        WHERE course_id = :c """,{'c':course_})
            for std in c.fetchall():
                listbox.insert(END,str("------------------")," ".join(std),str(""))
        c.close()

    #===========================================================Buttons================================================
    logout_btn = Button(screen1,text="Logout",height= 0, width =10,command=logout)
    logout_btn.place(x = 1100,y=650)

    update_btn = Button(Info_Frame,text="Change Password",height= 0, width =20,command=changepassword)
    update_btn.place(x = 10,y=450)

    details_btn = Button(Info_Frame,text="Enter",height= 0, width =10,command=enter)
    details_btn.place(x = 130,y=390)

    info_btn = Button(Info_Frame,text="View Courses",height= 0, width =10,command = getcourse)
    info_btn.place(x = 30,y=280)
    #===========================================================Labels and Entry widgets================================================
    conn = sqlite3.connect('university_.db')
    c = conn.cursor()
    c.execute("""SELECT course_id FROM teaches,instructor_login 
                WHERE instructor_login.username = :selectuname 
                AND teaches.ID = instructor_login.ID""",{'selectuname':Uname})
    courses = []
    for crs in c.fetchall():
        courses.extend(crs)

    course_select = StringVar()
    course_select.set("Select Course")
    crs_drop = OptionMenu(Info_Frame,course_select,*courses)
    crs_drop.place(x=30,y=350)
    
    crs_label = Label(Info_Frame,font=("arial",10),text = "See Course Details",padx=2,pady=2,bg="Ghost White",fg="blue")
    crs_label.place(x=30,y=320)

    #===========================================================Variables=====================

    conn = sqlite3.connect('university_.db')
    c = conn.cursor()
    global ID
    c.execute("""SELECT instructor.name FROM instructor,instructor_login WHERE instructor.ID = instructor_login.ID
                AND instructor_login.username = :user""",{'user':Uname})
    for item in c.fetchone ():
        Name = item

    c.execute("""SELECT instructor.dept_name FROM instructor,instructor_login WHERE instructor.ID = instructor_login.ID
                AND instructor_login.username = :user""",{'user':Uname})
    for item in c.fetchone ():
        d_name = item

    c.execute("""SELECT instructor.ID FROM instructor,instructor_login WHERE instructor.ID = instructor_login.ID
                AND instructor_login.username = :user""",{'user':Uname})
    for item in c.fetchone ():
        ID = item
    conn.close()

    #===========================================================Info frame=====================

    ID_label = Label(Info_Frame,font=("arial",13,'bold'),text = "ID : " + str(ID),anchor='w',padx=2,pady=2,bg="Ghost White")
    ID_label.pack(fill='both')


    name_label = Label(Info_Frame,font=("arial",13,'bold'),text = "Name : " + str(Name),anchor='w',padx=2,pady=2,bg="Ghost White")
    name_label.pack(fill='both')

    d_name_label = Label(Info_Frame,font=("arial",13,'bold'),text = "Department : " + str(d_name),anchor='w',padx=2,pady=2,bg="Ghost White")
    d_name_label.pack(fill='both')


    #===========================================================Student details frame=====================
    scrollbar =  Scrollbar(Display_Frame) 
    scrollbar.grid(row=0,column=1,sticky = 'ns')

    listbox = Listbox(Display_Frame,width = 60, height=26,yscrollcommand = scrollbar.set)
    listbox.grid(row=0,column=0)
    scrollbar.config(command = listbox.yview)

    #===========================================================Registration frame=====================



    Std_ID_label = Label(Registration_Frame,font=("arial",10,'bold'),text = "Student ID ",padx=10,pady=10,bg="Ghost White")
    Std_ID_label.grid(row=0,column=0)

    Std_ID = Entry(Registration_Frame,font=("arial",8),width=20)
    Std_ID.grid(row=0,column=1)

    course_ID_label = Label(Registration_Frame,font=("arial",10,'bold'),text = "Course ID ",padx=10,pady=10,bg="Ghost White")
    course_ID_label.grid(row=1,column=0)

    conn = sqlite3.connect('C:/Users/Dumebi Nwanze/Documents/SMSystem/university_.db')
    c = conn.cursor()
    c.execute("SELECT course_id FROM course")
    courses = []
    for crs in c.fetchall():
        courses.extend(crs)

    select_course = StringVar()
    select_course.set("Select Course")
    course_ID= OptionMenu(Registration_Frame,select_course,*courses)
    course_ID.grid(row=1,column=1,padx=20)
    conn.close()

    sec_ID_label = Label(Registration_Frame,font=("arial",10,'bold'),text = "Section ID ",padx=10,pady=10,bg="Ghost White")
    sec_ID_label.grid(row=2,column=0)

    sec_ID = Entry(Registration_Frame,font=("arial",8),width=20)
    sec_ID.grid(row=2,column=1)

    semester_label = Label(Registration_Frame,font=("arial",10,'bold'),text = "Semester ",padx=10,pady=10,bg="Ghost White")
    semester_label.grid(row=3,column=0)

    semester = Entry(Registration_Frame,font=("arial",8),width=20)
    semester.grid(row=3,column=1)

    year_label = Label(Registration_Frame,font=("arial",10,'bold'),text = "Year",padx=10,pady=10,bg="Ghost White")
    year_label.grid(row=4,column=0)

    year = Entry(Registration_Frame,font=("arial",8),width=20)
    year.grid(row=4,column=1)

    register_btn = Button(Registration_Frame,text="Register",height= 0, width =10,command = register)
    register_btn.grid(row=5,column=1,pady=30)



def fadminscreen(Uname):


    root.withdraw()
    screen1 = Toplevel(root)


    screen1.title('Faculty Administrator')
    screen1.geometry('1350x690+0+0')
    screen1.iconbitmap('icon_eul.ico')
    screen1.config(bg="Light Blue")
    screen1.resizable(width=False, height=False)

    Title_Frame = LabelFrame(screen1,bd=2,width=1350,height=70,padx=10,pady=7,bg = "Blue",relief = FLAT)
    Title_Frame.grid(row=0,column=0,columnspan=3)
    Title_Frame.pack_propagate(0)
        
    Title_label = Label(Title_Frame,text="European University of Lefke Faculty Administrator Portal",font = ('Arial',34,'bold'),fg='white',bg='blue')
    Title_label.pack()

    Info_Frame = Frame(screen1,bd=4,width=400,height=280,padx=20,pady=8,bg = "Ghost White",relief = RIDGE)
    Info_Frame.grid(row=1,column=0,padx=5)
    Info_Frame.pack_propagate(0)

    addTeacher_Frame = LabelFrame(screen1,bd=2,width=400,height=300,padx=20,pady=10,bg = "Ghost White",
                                   font =('Calibiri',15),relief = RIDGE,text='Add Instructor')
    addTeacher_Frame.grid(row=1,column=1,padx=5,pady=10)
    addTeacher_Frame.grid_propagate(0)

    addStudent_Frame = LabelFrame(screen1,bd=2,width=400,height=300,padx=20,pady=10,bg = "Ghost White",
                font =('Calibiri',15),text='Student Registration')
    addStudent_Frame.grid(row=1,column=2,padx=5,pady=10)
    addStudent_Frame.grid_propagate(0)

    addAdvisor_Frame = LabelFrame(screen1,bd=2,width=400,height=270,padx=70,pady=70,bg = "Ghost White",relief = RIDGE,
                                    font =('Calibiri',15),text='Assign Advisor')
    addAdvisor_Frame.grid(row=3,column=0,padx=5)
    addAdvisor_Frame.grid_propagate(0)


    setInstructor_Frame = LabelFrame(screen1,bd=2,width=400,height=270,padx=20,pady=5,bg = "Ghost White",relief = RIDGE,
                                          font =('Calibiri',15),text='Assign Instructor')
    setInstructor_Frame.grid(row=3,column=1,padx=5)
    setInstructor_Frame.grid_propagate(0)


    addCourse_Frame = LabelFrame(screen1,bd=2,width=400,height=270,padx=50,pady=20,bg = "Ghost White",relief = RIDGE,
                                     font =('Calibiri',15),text='Add Course')
    addCourse_Frame.grid(row=3,column=2,padx=5)
    addCourse_Frame.grid_propagate(0)


    Picture_Frame = Frame(Info_Frame,bd=2,width=120,height=120,bg = "Ghost White",relief = RIDGE)
    Picture_Frame.pack(side=LEFT)
    Picture_Frame.pack_propagate(0)      

    pp = PhotoImage(file = "pp.png")
    pp_label = Label(Picture_Frame,image=pp)
    pp_label.pack()

    Sinfo_Frame = Frame(Info_Frame,bd=2,width=360,height=200,bg = "Ghost White",relief = FLAT,pady=50)
    Sinfo_Frame.pack(side=RIGHT)
    Sinfo_Frame.grid_propagate(0)  
    #------------------------------------------Functions-----------------------------------

    def logout():
        screen1.withdraw()
        root.deiconify()
        messagebox.showinfo(' ','Logout Successful')

    def addStudent():
        conn = sqlite3.connect('C:/Users/Dumebi Nwanze/Documents/SMSystem/university_.db')
        c = conn.cursor()
        c.execute("""INSERT INTO student 
                     VALUES (:id,:name,:dept,"NULL")""",
                     {'id':Std_ID.get(),
                     'name':Std_Name.get(),
                     'dept':std_dept.get()})
        conn.commit()
        conn.close()
        conn = sqlite3.connect('C:/Users/Dumebi Nwanze/Documents/SMSystem/university_.db')
        c = conn.cursor()
        c.execute("""INSERT INTO student_login 
                     VALUES (:user,:pass,:id,:name)""",
                     {'user':Std_usern.get(),
                     'pass':Std_pass.get(),
                     'id':Std_ID.get(),
                     'name':Std_Name.get()})
        messagebox.showinfo('','Insertion Success')
        Std_ID.delete(0,END)
        Std_Name.delete(0,END)
        Std_dept.delete(0,END)
        Std_usern.delete(0,END)
        Std_pass.delete(0,END)
        conn.commit()
        conn.close()

    def delStudent():
        conn = sqlite3.connect('C:/Users/Dumebi Nwanze/Documents/SMSystem/university_.db')
        c = conn.cursor()
        c.execute("""DELETE FROM student 
                     WHERE ID = :id """,
                     {'id':Std_ID.get()})
        conn.commit()
        conn.close()
        conn = sqlite3.connect('C:/Users/Dumebi Nwanze/Documents/SMSystem/university_.db')
        c = conn.cursor()
        c.execute("""DELETE FROM student_login 
                     WHERE ID = :id """,
                     {'id':Std_ID.get()})
        messagebox.showinfo('','Deletion Success')
        Std_ID.delete(0,END)
        Std_Name.delete(0,END)
        Std_dept.delete(0,END)
        Std_usern.delete(0,END)
        Std_pass.delete(0,END)
        conn.commit()
        conn.close()

    def addInstructor():
        conn = sqlite3.connect('C:/Users/Dumebi Nwanze/Documents/SMSystem/university_.db')
        c = conn.cursor()
        c.execute("""INSERT INTO instructor 
                     VALUES (:id,:name,:dept,"NULL")""",
                     {'id':Ins_ID.get(),
                     'name':Ins_Name.get(),
                     'dept':ins_dept.get()})
        conn.commit()
        conn.close()
        conn = sqlite3.connect('C:/Users/Dumebi Nwanze/Documents/SMSystem/university_.db')
        c = conn.cursor()
        c.execute("""INSERT INTO instructor_login 
                     VALUES (:user,:pass,:id,:name)""",
                     {'user':Ins_usern.get(),
                     'pass':Ins_pass.get(),
                     'id':Ins_ID.get(),
                     'name':Ins_Name.get()})
        messagebox.showinfo('','Insertion Success')
        Ins_ID.delete(0,END)
        Ins_Name.delete(0,END)
        Ins_dept.delete(0,END)
        Ins_usern.delete(0,END)
        Ins_pass.delete(0,END)
        conn.commit()
        conn.close()


    def delInstructor():
        conn = sqlite3.connect('C:/Users/Dumebi Nwanze/Documents/SMSystem/university_.db')
        c = conn.cursor()
        c.execute("""DELETE FROM instuctor 
                     WHERE ID = :id """,
                     {'id':Ins_ID.get()})
        conn.commit()
        conn.close()
        conn = sqlite3.connect('C:/Users/Dumebi Nwanze/Documents/SMSystem/university_.db')
        c = conn.cursor()
        c.execute("""DELETE FROM instructor_login 
                     WHERE ID = :id """,
                     {'id':Ins_ID.get()})
        messagebox.showinfo('','Deletion Success')
        Ins_ID.delete(0,END)
        Ins_Name.delete(0,END)
        Ins_dept.delete(0,END)
        Ins_usern.delete(0,END)
        Ins_pass.delete(0,END)
        conn.commit()
        conn.close()

    def addCourse():
        conn = sqlite3.connect('C:/Users/Dumebi Nwanze/Documents/SMSystem/university_.db')
        c = conn.cursor()
        c.execute("""INSERT INTO course
                     VALUES (:id,:title,:dept,:cred)""",
                     {'id':Course_id.get(),
                     'title':Course_title.get(),
                     'dept':course_dept.get(),
                     'cred':credit.get()})
        messagebox.showinfo('','Insertion Success')
        Course_id.delete(0,END)
        Course_title.delete(0,END)
        Course_dept.delete(0,END)
        credit.delete(0,END)
        conn.commit()
        conn.close()


    def delCourse():
        conn = sqlite3.connect('C:/Users/Dumebi Nwanze/Documents/SMSystem/university_.db')
        c = conn.cursor()
        c.execute("""DELETE FROM course
                     WHERE course_id = :id""",
                     {'id':Course_id.get()})
        messagebox.showinfo('','Deletion Success')
        Course_id.delete(0,END)
        Course_title.delete(0,END)
        Course_dept.delete(0,END)
        credit.delete(0,END)
        conn.commit()
        conn.close()

    def AssignAdvisor():
        conn = sqlite3.connect('C:/Users/Dumebi Nwanze/Documents/SMSystem/university_.db')
        c = conn.cursor()
        c.execute("""INSERT INTO advisors
                     VALUES (:sid,:iid)""",
                     {'sid':AStd_ID.get(),
                     'iid':AIns_ID.get()})
        messagebox.showinfo('','Insertion Success')
        AStd_ID.delete(0,END)
        AIns_ID.delete(0,END)
        conn.commit()
        conn.close()

    def RemoveAdvisor():
        conn = sqlite3.connect('C:/Users/Dumebi Nwanze/Documents/SMSystem/university_.db')
        c = conn.cursor()
        c.execute("""DELETE FROM advisors
                     WHERE s_ID = :sid AND i_ID = :iid""",
                     {'sid': AStd_ID.get(),
                     'iid':AIns_ID.get()})
        messagebox.showinfo('','Deletion Success')
        AStd_ID.delete(0,END)
        AIns_ID.delete(0,END)
        conn.commit()
        conn.close()

    def AssignInstructor():
        conn = sqlite3.connect('C:/Users/Dumebi Nwanze/Documents/SMSystem/university_.db')
        c = conn.cursor()
        c.execute("""INSERT INTO teaches
                     VALUES (:id,:cid,:sec_id,:sem,:y)""",
                     {'id':Inst_ID.get(),
                     'cid':courseID.get(),
                     'sec_id':section.get(),
                     'sem':semester.get(),
                     'y':year})
        messagebox.showinfo('','Insertion Success')
        Inst_ID.delete(0,END)
        Icourse_ID.delete(0,END)
        section.delete(0,END)
        semester.delete(0,END)
        year.delete(0,END)
        conn.commit()
        conn.close()

    def RemoveInstructor():
        conn = sqlite3.connect('C:/Users/Dumebi Nwanze/Documents/SMSystem/university_.db')
        c = conn.cursor()
        c.execute("""DELETE FROM teaches
                     WHERE ID = :id AND course_id = :cid 
                     AND sec_id = :sec_Id AND semester = :sem AND year = :y)""",
                     {'id':Inst_ID.get(),
                     'cid':courseID.get(),
                     'sec_Id':section.get(),
                     'sem':semester.get(),
                     'y':year})
        messagebox.showinfo('','Deletion Success')
        Inst_ID.delete(0,END)
        Icourse_ID.delete(0,END)
        section.delete(0,END)
        semester.delete(0,END)
        year.delete(0,END)
        conn.commit()
        conn.close()
    #------------------------------------------Add Student---------------------------------

    Std_ID_label = Label(addStudent_Frame,font=("arial",10,'bold'),text = "Student ID ",padx=10,pady=10,bg="Ghost White")
    Std_ID_label.grid(row=0,column=0)

    Std_ID = Entry(addStudent_Frame,font=("arial",8),width=20)
    Std_ID.grid(row=0,column=1)  

    Std_Name_label = Label(addStudent_Frame,font=("arial",10,'bold'),text = "Student Name ",padx=10,pady=10,bg="Ghost White")
    Std_Name_label.grid(row=1,column=0)

    Std_Name = Entry(addStudent_Frame,font=("arial",8),width=20)
    Std_Name.grid(row=1,column=1)

    Std_dept_label = Label(addStudent_Frame,font=("arial",10,'bold'),text = "Department ",padx=10,pady=10,bg="Ghost White")
    Std_dept_label.grid(row=2,column=0)

    conn = sqlite3.connect('C:/Users/Dumebi Nwanze/Documents/SMSystem/university_.db')
    c = conn.cursor()
    c.execute("SELECT dept_name FROM department")
    courses = []
    for crs in c.fetchall():
        courses.extend(crs)

    std_dept = StringVar()
    std_dept.set("Select Course")
    Std_dept = OptionMenu(addStudent_Frame,std_dept,*courses)
    Std_dept.grid(row=2,column=1,padx=20)
    conn.close()

    Std_usern_label = Label(addStudent_Frame,font=("arial",10,'bold'),text = "Username ",padx=10,pady=10,bg="Ghost White")
    Std_usern_label.grid(row=3,column=0)

    Std_usern = Entry(addStudent_Frame,font=("arial",8),width=20)
    Std_usern.grid(row=3,column=1)

    Std_pass_label = Label(addStudent_Frame,font=("arial",10,'bold'),text = "Password ",padx=10,pady=10,bg="Ghost White")
    Std_pass_label.grid(row=4,column=0)

    Std_pass = Entry(addStudent_Frame,font=("arial",8),width=20)
    Std_pass.grid(row=4,column=1)

    addStudent_btn = Button(addStudent_Frame,text="Add Student",height= 0, width =10,command=addStudent)
    addStudent_btn.grid(row=5,column=0,pady=5)
    delStudent_btn = Button(addStudent_Frame,text="Delete Student",height= 0, width =12,command = delStudent)
    delStudent_btn.grid(row=5,column=1,pady=5)


    #------------------------------------------Add Instructor---------------------------------
    Ins_ID_label = Label(addTeacher_Frame,font=("arial",10,'bold'),text = "Instructor ID ",padx=10,pady=10,bg="Ghost White")
    Ins_ID_label.grid(row=0,column=0)

    Ins_ID = Entry(addTeacher_Frame,font=("arial",8),width=20)
    Ins_ID.grid(row=0,column=1)

    Ins_Name_label = Label(addTeacher_Frame,font=("arial",10,'bold'),text = "Instructor Name ",padx=10,pady=10,bg="Ghost White")
    Ins_Name_label.grid(row=1,column=0)

    Ins_Name = Entry(addTeacher_Frame,font=("arial",8),width=20)
    Ins_Name.grid(row=1,column=1)

    Ins_dept_label = Label(addTeacher_Frame,font=("arial",10,'bold'),text = "Department ",padx=10,pady=10,bg="Ghost White")
    Ins_dept_label.grid(row=2,column=0)

    conn = sqlite3.connect('C:/Users/Dumebi Nwanze/Documents/SMSystem/university_.db')
    c = conn.cursor()
    c.execute("SELECT dept_name FROM department")
    courses = []
    for crs in c.fetchall():
        courses.extend(crs)

    ins_dept = StringVar()
    ins_dept .set("Select Course")
    Ins_dept = OptionMenu(addTeacher_Frame,ins_dept,*courses)
    Ins_dept.grid(row=2,column=1,padx=20)
    conn.close()

    Ins_usern_label = Label(addTeacher_Frame,font=("arial",10,'bold'),text = "Username ",padx=10,pady=10,bg="Ghost White")
    Ins_usern_label.grid(row=3,column=0)

    Ins_usern = Entry(addTeacher_Frame,font=("arial",8),width=20)
    Ins_usern.grid(row=3,column=1)

    Ins_pass_label = Label(addTeacher_Frame,font=("arial",10,'bold'),text = "Password ",padx=10,pady=10,bg="Ghost White")
    Ins_pass_label.grid(row=4,column=0)

    Ins_pass = Entry(addTeacher_Frame,font=("arial",8),width=20)
    Ins_pass.grid(row=4,column=1)

    addIns_btn = Button(addTeacher_Frame,text="Add Instructor",height= 0, width =15,command = addInstructor)
    addIns_btn.grid(row=5,column=0,pady=5)
    delIns_btn = Button(addTeacher_Frame,text="Delete Instructor",height= 0, width =15,command = delInstructor)
    delIns_btn.grid(row=5,column=1,pady=5)


    #------------------------------------------Add Advisor---------------------------------

    AIns_ID_label = Label(addAdvisor_Frame,font=("arial",10,'bold'),text = "Advisor ID ",padx=10,pady=10,bg="Ghost White")
    AIns_ID_label.grid(row=0,column=0)

    Ins_ID = Entry(addAdvisor_Frame,font=("arial",8),width=20)
    Ins_ID.grid(row=0,column=1)

    AStd_ID_label = Label(addAdvisor_Frame,font=("arial",10,'bold'),text = "Student ID ",padx=10,pady=10,bg="Ghost White")
    AStd_ID_label.grid(row=1,column=0)

    AStd_ID = Entry(addAdvisor_Frame,font=("arial",8),width=20)
    AStd_ID.grid(row=1,column=1)

    addAdvisor_btn = Button(addAdvisor_Frame,text="Assign Advisor",height= 0, width =15,command = AssignAdvisor)
    addAdvisor_btn.grid(row=3,column=0,pady=30)

    remAdvisor_btn = Button(addAdvisor_Frame,text="Remove Advisor",height= 0, width =15,command = RemoveAdvisor)
    remAdvisor_btn.grid(row=3,column=1,pady=30)

    #------------------------------------------Add Course---------------------------------


    Course_title_label = Label(addCourse_Frame,font=("arial",10,'bold'),text = "Course Title ",padx=10,pady=10,bg="Ghost White")
    Course_title_label.grid(row=0,column=0)

    Course_title = Entry(addCourse_Frame,font=("arial",8),width=20)
    Course_title.grid(row=0,column=1)

    Course_id_label = Label(addCourse_Frame,font=("arial",10,'bold'),text = "Course ID",padx=10,pady=10,bg="Ghost White")
    Course_id_label.grid(row=1,column=0)

    Course_id = Entry(addCourse_Frame,font=("arial",8),width=20)
    Course_id.grid(row=1,column=1)

    Course_dept_label = Label(addCourse_Frame,font=("arial",10,'bold'),text = "Department ",padx=10,pady=10,bg="Ghost White")
    Course_dept_label.grid(row=2,column=0)

    conn = sqlite3.connect('C:/Users/Dumebi Nwanze/Documents/SMSystem/university_.db')
    c = conn.cursor()
    c.execute("SELECT dept_name FROM department")
    courses = []
    for crs in c.fetchall():
        courses.extend(crs)

    course_dept = StringVar()
    course_dept .set("Select Course")
    Course_dept = OptionMenu(addCourse_Frame,course_dept,*courses)
    Course_dept.grid(row=2,column=1,padx=20)
    conn.close()

    credit_label = Label(addCourse_Frame,font=("arial",10,'bold'),text = "Course Credit ",padx=10,pady=10,bg="Ghost White")
    credit_label.grid(row=3,column=0)

    credit = Entry(addCourse_Frame,font=("arial",8),width=20)
    credit.grid(row=3,column=1)


    addCourse_btn = Button(addCourse_Frame,text="Add Course",height= 0, width =15,command = addCourse)
    addCourse_btn.grid(row=4,column=0,pady=30)
    delCourse_btn = Button(addCourse_Frame,text="Delete Course",height= 0, width =15,command = delCourse)
    delCourse_btn.grid(row=4,column=1,pady=30)


    #------------------------------------------Set Instructor---------------------------------

    Inst_ID_label = Label(setInstructor_Frame,font=("arial",10,'bold'),text = "Instructor ID ",padx=10,pady=10,bg="Ghost White")
    Inst_ID_label.grid(row=0,column=0)

    Inst_ID = Entry(setInstructor_Frame,font=("arial",8),width=20)
    Inst_ID.grid(row=0,column=1)

    Icourse_ID_label = Label(setInstructor_Frame,font=("arial",10,'bold'),text = "Course ID ",padx=10,pady=10,bg="Ghost White")
    Icourse_ID_label.grid(row=1,column=0)

    conn = sqlite3.connect('C:/Users/Dumebi Nwanze/Documents/SMSystem/university_.db')
    c = conn.cursor()
    c.execute("SELECT course_id FROM course")
    courses = []
    for crs in c.fetchall():
        courses.extend(crs)

    courseID = StringVar()
    courseID.set("Select Course")
    Icourse_ID = OptionMenu(setInstructor_Frame,courseID,*courses)
    Icourse_ID.grid(row=1,column=1,padx=20)
    conn.close()

    section_label = Label(setInstructor_Frame,font=("arial",10,'bold'),text = "Section",padx=10,pady=10,bg="Ghost White")
    section_label.grid(row=2,column=0)

    section = Entry(setInstructor_Frame,font=("arial",8),width=20)
    section.grid(row=2,column=1)

    addInst_btn = Button(setInstructor_Frame,text="Assign Instructor",height= 0, width =15,command = AssignInstructor)
    addInst_btn.grid(row=5,column=0,pady=5)
    delInst_btn = Button(setInstructor_Frame,text="Remove Instructor",height= 0, width =15,command = RemoveInstructor)
    delInst_btn.grid(row=5,column=1,pady=5)

    semester_label = Label(setInstructor_Frame,font=("arial",10,'bold'),text = "Semester",padx=10,pady=10,bg="Ghost White")
    semester_label.grid(row=3,column=0)

    semester = Entry(setInstructor_Frame,font=("arial",8),width=20)
    semester.grid(row=3,column=1)

    year_label = Label(setInstructor_Frame,font=("arial",10,'bold'),text = "Year",padx=10,pady=10,bg="Ghost White")
    year_label.grid(row=4,column=0)

    year = Entry(setInstructor_Frame,font=("arial",8),width=20)
    year.grid(row=4,column=1)

    #===========================================================Info frame=====================
    conn = sqlite3.connect('university_.db')
    c = conn.cursor()
    c.execute("""SELECT faculty_admin.name FROM faculty_admin,fadmin_login WHERE faculty_admin.ID = fadmin_login.ID
                AND fadmin_login.username = :user""",{'user':Uname})
    for item in c.fetchone ():
        Name = item

    c.execute("""SELECT faculty_admin.dept_name FROM faculty_admin,fadmin_login WHERE faculty_admin.ID = fadmin_login.ID
                AND fadmin_login.username = :user""",{'user':Uname})
    for item in c.fetchone ():
        d_name = item

    c.execute("""SELECT faculty_admin.ID FROM faculty_admin,fadmin_login WHERE faculty_admin.ID = fadmin_login.ID
                AND fadmin_login.username = :user""",{'user':Uname})
    for item in c.fetchone ():
        ID = item
    conn.close()

    ID_label = Label(Sinfo_Frame,font=("arial",10,'bold'),text = "ID : " + str(ID),anchor='w',bg="Ghost White")
    ID_label.pack(fill='both')


    name_label = Label(Sinfo_Frame,font=("arial",10,'bold'),text = "Name : " + str(Name),anchor='w',bg="Ghost White")
    name_label.pack(fill='both')

    d_name_label = Label(Sinfo_Frame,font=("arial",10,'bold'),text = "Department : " + str(d_name),anchor='w',bg="Ghost White")
    d_name_label.pack(fill='both')
    
    logout_btn = Button(screen1,text="Logout",height= 0, width =10,bg='red',fg='white',command=logout)
    logout_btn.grid(row=2,column=0,sticky='Nw',padx=26)


    
root.mainloop()  