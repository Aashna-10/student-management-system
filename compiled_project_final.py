from tkinter import *
import pandas as pd
from tkinter import scrolledtext
from functools import partial
from tkinter import ttk
import matplotlib.pyplot as plt
from tkinter import messagebox
import numpy as np
from PIL import ImageTk, Image
import mysql.connector as msql
main = Tk()
main.geometry('400x300')
main.title('Main Page')
b1 = Button(main, text = 'Student Login', command = lambda: stu(main)).grid(row = 0, column = 0)
b2 = Button(main, text = 'Teacher Login', command = lambda: teach(main)).grid(row = 0, column = 1)
def teach(main):
    main.withdraw()
    mycon = msql.connect(host = 'localhost', user = 'root', passwd = 'Aashna!10',database = 'ip_project')
    login_info = pd.read_sql("select * from login_info ;", mycon)
    teacher_info = pd.read_sql("select * from teacher_info ;", mycon)
    class_details = pd.read_sql("select * from class_details;", mycon)

    n = 0
#designing the window
    root = Toplevel(main)
    root.geometry('400x300')
    root.title('Login Page')

#creating username part
    userl = Label(root, text = 'Username: ' )
    userl.grid(row = 0, column = 0, pady = 2)
    user = StringVar()
#name = StringVar()
    usere = Entry(root, textvariable = user)

    usere.grid(row = 0,column = 1)

#create password part
    passl = Label(root, text = 'Password: ')
    passl.grid(row = 1,column = 0, pady = 2)
    passw = StringVar()
    passe = Entry(root,  textvariable = passw,show = '*')
    passe.grid(row = 1, column = 1)

    def fn(a,b):
        if (a.get(), b.get()) not in zip(login_info['username'].values, login_info['password'].values):
            error = Label(root, text = 'invalid username or password')
            error.grid(row = 5, column = 1)
        else :
            root.withdraw()
            root2(user)
            root.update()
            root.deiconify

    def root2(user) :
    
        root2 = Toplevel(root)
        root2.geometry('400x300')
        root2.title('Welcome')
        welcomelabel = Label(root2, text = ('Welcome' )).grid(row = 0, column = 0)
        b = []
        c = []
        e= []
        n = 0
        for (i,j) in teacher_info.iterrows():
            a = list(j)
            b.append(a)
        for (i,j) in class_details.iterrows():
            k = list(j)
            c.append(k)
        for (i,j) in class_details.iteritems():
            t = list(j)
            e.append(t)
            d = e[3:]
    
        for i in b:
            ll = []
            if user.get() in i:
                welcomelabel = Label(root2, text = ('Welcome '+  i[1] ), pady = 10, fg = 'blue').grid(row = 0, column = 0)
                if i[3] is not None:
                    class_teacher=i[3]
                    ll.append(i[3])
                    
                    
                    for j in c:
                            if i[0] in j :
                            
                                if i[0] != j[2]:
                                    non_class_teacher=j[1]
                                    ll.append(j[1])
                                    
                                    n = n + 1
                    v = StringVar()
                    button = ttk.Combobox(root2, width = 27, textvariable = v)
                    button['values'] = ll
                    button.grid(column = 1, row = 1)
                    button.current()
                    labell = Label(root2, text = 'Select Class: ').grid(row = 1, column = 0)
                    
                    
                    bbb = Button(root2, text = 'Enter' ,command = lambda: root3(v.get(), root2, user)).grid(row = 2, column = 1)
                elif i[3] is None:
                    for j in c:
                            if i[0] in j :
                            
                                 if i[0] != j[2] :
                                    ll.append(j[1])
                                    
                                    n = n + 1
                    v = StringVar()
                    button = ttk.Combobox(root2, width = 27, textvariable = v)
                    button['values'] = ll
                    button.grid(column = 1, row = 5)
                    button.current()
                    bbb = Button(root2, text = 'Enter', command = lambda: root3(v.get(), root2, user)).grid(row = 6, column = 1)
            else:
                pass
    
        
        root2.mainloop()
    def root3(variable, root2, user):
        
        root3 = Toplevel()
        root3.geometry('400x300')
        root3.title('Process')
        sturec = Button(root3, text = 'View Particular Student Record',command = lambda: root4(variable, root3)).grid(row = 0, column =0)
        upsyl = Button(root3, text = 'Update Syllabus', command = lambda: root7(variable, user)).grid(row = 1, column = 0)
        
        root3.mainloop()

    
    def root4(variable,root3):
        
        root4 = Toplevel()
        root4.geometry('700x500')
        root4.title('Student Record')
        name_var = StringVar()
        admn = StringVar()
        ttt = Label(root4, text = 'Enter roll no of student to view record: ').grid(row = 0, column = 0)
        ggg = Label(root4, text = 'Enter admission no of student to view record: ').grid(row = 1, column = 0)
        tt = Entry(root4, textvariable = name_var).grid(row = 0, column = 1)
        gg = Entry(root4, textvariable = admn).grid(row = 1, column = 1)

        record = pd.read_sql("select * from " + variable + ' ;', mycon)

        button_submit = Button(root4, text = "Enter", command = lambda: root5(name_var.get(),variable,root4, admn)).grid(row = 2, column = 1)
    
        root4.mainloop()
    def root5(name_var, variable, root4,admn):
        root4.withdraw()
        root5 = Toplevel()
        root5.geometry('500x300')
        root5.title('Student Record')
    
        record = pd.read_sql("select * from " + variable + ' ;', mycon)
        stu = []
        for (i,j) in record.iteritems():
            a = list(j)
            stu.append(a)
    
        for i in stu[0]:
        
       
            if i == int(name_var):
                subjects = list(record.columns)
                v = StringVar()
                button2 = ttk.Combobox(root5, width = 27, textvariable = v)
                button2['values'] = subjects
                button2.grid(column = 1, row = 0)
                button2.current()
                labelll = Label(root5, text = 'Select column to edit: ').grid(row = 0, column = 0)
                bu = Button(root5, text = 'Enter',command = lambda: root6(v, variable, name_var, root5, admn)).grid(row = 2, column = 1)
            
        root5.mainloop()
    def root6(v, variable, name_var, root5, admn):
        root5.withdraw()
        root6 = Toplevel()
        root6.geometry('400x300')
        root6.title('Student Record')
        l = Label(root6, text = 'New Value: '). grid(row = 1, column = 0)
        table = pd.read_sql('select ' + str(v.get()) + ' from ' + variable + '  where roll_no = ' + str(name_var) + ';', mycon)
        ll = Label(root6, text = 'Current Value: ' + str(table.values[0][0])). grid(row = 0, column = 0)
        marks = IntVar()
        e = Entry(root6, textvariable = marks).grid(row = 1, column = 1)
        b = Button(root6, text = 'Enter', command = lambda: up(marks, variable,v, name_var, root6, admn)). grid(row = 2, column = 1)
        root6.mainloop()

    def up(m, variable,v, name_var, root6, admn):
         
         root6.withdraw()
         root8 = Toplevel()
         root8.geometry('400x300')
         root8.title('Success')
         ll = Label(root8, text = 'UPDATED SUCCESSFULLY!!').grid(row = 0, column = 0)
         
         cursor = mycon.cursor()
         cursor.execute('update ' + variable + ' set ' + str(v.get()) +' = ' + str(m.get()) + ' where roll_no = ' + str(name_var) + ';' )
         if str(v.get()) == 'Physics_score':
             cursor.execute('update stu_phy_marks set ut_1 = ' + str(m.get()) + ' where admn_no = ' + str(admn.get()) + ' ;')
         elif str(v.get()) == 'Maths_score':
             cursor.execute('update stu_math_marks set ut_1 = ' + str(m.get()) + ' where admn_no = ' + str(admn.get()) + ' ;')
         elif str(v.get()) == 'ip_score':
             cursor.execute('update stu_ip_marks set ut_1 = ' + str(m.get()) + ' where admn_no = ' + str(admn.get()) + ' ;')
         else:
            pass
         mycon.commit()
         root8.mainloop()
    
    def root7(variable, user):
        
        root7 = Toplevel()
        root7.geometry('400x300')
        root7.title('Chapters')
        cb1 = IntVar()  
        cb2 = IntVar()
        cb3 = IntVar()
        cb4 = IntVar()
        cb5 = IntVar()
        cb6 = IntVar()
        button1 = Checkbutton(root7, text = "Chap 1", variable = cb1,onvalue = 1,offvalue = 0,height = 2,width = 10).grid(row = 1, column = 1)
        button2 = Checkbutton(root7, text = "Chap 2", variable = cb2,onvalue = 1,offvalue = 0,height = 2,width = 10).grid(row = 2, column = 1)
        button3 = Checkbutton(root7, text = "Chap 3", variable = cb3,onvalue = 1,offvalue = 0,height = 2,width = 10).grid(row = 3, column = 1)
        button4 = Checkbutton(root7, text = "Chap 4", variable = cb4,onvalue = 1,offvalue = 0,height = 2,width = 10).grid(row = 4, column = 1)
        button5 = Checkbutton(root7, text = "Chap 5", variable = cb5,onvalue = 1,offvalue = 0,height = 2,width = 10).grid(row = 5, column = 1)
        button6 = Checkbutton(root7, text = "Chap 6", variable = cb6,onvalue = 1,offvalue = 0,height = 2,width = 10).grid(row = 6, column = 1)
        
        bb = Button(root7, text = 'Enter',  command = lambda: root8(cb1, cb2, cb3, cb4, cb5, cb6, variable, user)).grid(row = 7, column = 1)
    
        root7.mainloop()
    def root8(cb1, cb2, cb3, cb4, cb5, cb6,variable, user):
        
        lst = [cb1.get(), cb2.get(), cb3.get(), cb4.get(), cb5.get(), cb6.get()]
        nn = 0
        m = 0

        for i in lst:
            if int(i) == 1:
                nn = nn + 1
           
            else:
                m = m + 1
        plt.pie([nn,m], labels = ['Chapters done','Chapters left'], autopct = '%1.1f%%')
        plt.title('Syllabus Progress')
        plt.savefig('/Users/aashna_ased/Desktop/' + variable + str(user.get())+ '.pdf')
        plt.show()
    
    
            
        
    buu = Button(root, text = 'Login', command=lambda:fn(user, passw))
    buu.grid(row = 4, column = 1)
    root.mainloop()

def stu(main):
    my_w = Tk()
    my_w.geometry("500x500")  # Size of the login window
    my_w.title('Login to Student Management')

    #Connect to MySQL database
    try:
            conn = msql.connect(host="localhost", user="root", password = 'Aashna!10', database="ip_project")
            if conn.is_connected():
                cursor = conn.cursor()
                
    except Error as e:
            print("Error while connecting to MySQL", e)
    
    #Login details    

    #Fill the frame with the label and input button and radio buttons

    email= Entry(my_w, width=30)
    email.grid(row=1, column=2, padx=20, pady=(10,0))

    password= Entry(my_w, width=30, show = '*')
    password.grid(row=2, column=2)

    email_label= Label(my_w, text="Email")
    email_label.grid(row=1, column=1)

    password_label= Label(my_w, text="Password:")
    password_label.grid(row=2, column=1)
    email.focus()


    
    login_btn = Button(my_w,text="Login", command= lambda: click_login())
    login_btn.grid(row=6,column=0,columnspan=2,pady=10, padx=10, ipadx=100)
    
    def click_login():
        global sequence_no
        global stu_section_var



        cursor = conn.cursor()

        #Search for the correct login email + password
        email_id_var= email.get()
        password_var= password.get()
        

        #Search for the email and password
        

        q = "SELECT * FROM new_students WHERE email= %(val_email)s AND password=%(val_password)s "
        params = {'val_email':email_id_var, 'val_password':password_var}
        cursor.execute(q, params)
        records=cursor.fetchall()
        #print(type(records))
        
        flag_var=1
        #Loop through record in list
        try:
            for record in records:
                
                if (email_id_var == str(record[6]) and password_var==str(record[7])):
                    
                    sequence_no=str(record[0])  #the admin_no of the student is int
                    stu_section_var=str(record[8])  #the section of the student is varchar
                    flag_var=0
                    messagebox.showinfo("Successful Login into Student Management","Welcome ")

                    #Display the next frame after successful login
                    disp_main_menu_list()
                else:

                    if flag_var==0:
                        print('Record found so do not reject')    
                    else:
                        flag_var==1
                        print('Record not found ')

            if flag_var==1:
                messagebox.showinfo("Unsuccessful Login Attempt", "Incorrect login/email or password, try again")

        except e:
            print(' Exception Record not found :'+ e)
        email.delete(0,END)
        password.delete(0,END)
        email.focus()
    
    def disp_main_menu_list():
        global editor
        global frame1
        global frame2
        global frame3
        global frame4

        editor=Tk()
        editor.title=('Main Menu')
        editor.geometry('1700x1000')
        
  
        

        global f_name_editor
        global l_name_editor
        global address_editor

        global prof_btn
        global res_btn
        global class_btn

        #Dashboard frame - Frame1
        frame1=LabelFrame(editor,bg="red")

        #Create dashboard buttons
        prof_btn=Button(frame1, text="Student Profile",command=fn_profile_display)
        prof_btn.grid(row=7,column=0,columnspan=1,pady=10, padx=10, ipadx=137)

        res_btn=Button(frame1, text="Results          ",command=fn_results_display)
        res_btn.grid(row=8,column=0,columnspan=1,pady=10, padx=10, ipadx=137)

        class_btn=Button(frame1, text="Class records  ",command=fn_classroom_display)
        class_btn.grid(row=9,column=0,columnspan=1,pady=10, padx=10, ipadx=137)

        #Row10
        exit_btn=Button(frame1, text="Logout           ",command=fn_logout)
        exit_btn.grid(row=10,column=0,columnspan=1,pady=10, padx=10, ipadx=137)
        frame1.pack(side="top", fill="both")
   

    def fn_logout():
        editor.destroy()
    
    def fn_results_display():

   
        if res_btn["state"] == NORMAL:
            res_btn["state"] = DISABLED
        else:
            res_btn["state"] = NORMAL

        #Create Frame4
        frame4=LabelFrame(editor)



        Admin_no_label= Label(frame4, text="    Admin no:")
        Admin_no_label.grid(row=12, column=2,sticky=W)

        UT1_label= Label(frame4, text="   UT1:")
        UT1_label.grid(row=12, column=3,sticky=W)

        UT2_label= Label(frame4, text="   UT2:")
        UT2_label.grid(row=12, column=4,sticky=W)

        midterm_label= Label(frame4, text="  MIDTERM:")
        midterm_label.grid(row=12, column=5,sticky=W)

        UT3_label= Label(frame4, text="   UT3:")
        UT3_label.grid(row=12, column=6,sticky=W)

        UT4_label= Label(frame4, text="   UT4:")
        UT4_label.grid(row=12, column=7,sticky=W)

        finals_label= Label(frame4, text="  FINALS:")
        finals_label.grid(row=12, column=8,sticky=W)

        chartMath_btn=Button(frame4, text="Chart_Link",command=lambda: Math_chart_link())
        chartMath_btn.grid(row=13,column=12,columnspan=1,pady=10, padx=10, ipadx=50)

        #Search for logged in students Math marks
        q = "SELECT * FROM stu_math_marks WHERE admn_no= %(val_admin_no)s "
        params = {'val_admin_no':sequence_no}
        cursor.execute(q, params)

        records=cursor.fetchall()
        
        #Loop through record in list
        i=13
        for record in records:

            rows = []
            x=2
            j=0
            

            cols = []

            for j in range(7):

                e = Entry(frame4,width=8,relief=GROOVE)

                e.grid(row=i, column=x, sticky=NSEW)

                e.insert(END,  (record[j]))
                
                x+=1
                cols.append(e)
            i+=1    

            rows.append(cols)



        Admin_no_label= Label(frame4, text="Subject     MATH ")
        Admin_no_label.grid(row=13, column=0)


        #Computer IP marks

        q = "SELECT * FROM stu_ip_marks WHERE admn_no= %(val_admin_no)s "
        params = {'val_admin_no':sequence_no}
        cursor.execute(q, params)
        records=cursor.fetchall()        

        #Loop through record in list
        i=14
        for record in records:

            rows = []
            x=2
            j=0            

            cols = []

            for j in range(7):

                e = Entry(frame4,width=8,relief=GROOVE)

                e.grid(row=i, column=x, sticky=NSEW)

                e.insert(END,  (record[j]))
                
                x+=1
                cols.append(e)
            i+=1    

            rows.append(cols)

        Admin_no_label= Label(frame4, text="Subject           IP ")
        Admin_no_label.grid(row=14, column=0)

        chartIP_btn=Button(frame4, text="Chart_Link",command=lambda: IP_chart_link())
        chartIP_btn.grid(row=14,column=12,columnspan=1,pady=10, padx=10, ipadx=50)


        #Physics Marks
        
        q = "SELECT * FROM stu_phy_marks WHERE admn_no= %(val_admin_no)s "
        params = {'val_admin_no':sequence_no,'val_section':stu_section_var}
        cursor.execute(q, params)
        records=cursor.fetchall()

        #Loop through record in list
        i=15
        for record in records:

            rows = []
            x=2
            j=0


            cols = []

            for j in range(7):

                e = Entry(frame4,width=8,relief=GROOVE)

                e.grid(row=i, column=x, sticky=NSEW)

                e.insert(END,  (record[j]))
                
                x+=1
                cols.append(e)
            i+=1    

            rows.append(cols)

        Admin_no_label= Label(frame4, text="Subject   Physics ")
        Admin_no_label.grid(row=15, column=0)


        chartPhy_btn=Button(frame4, text="Chart_Link",command=lambda: Phy_chart_link())
        chartPhy_btn.grid(row=15,column=12,columnspan=1,pady=10, padx=10, ipadx=50)


        frame4.pack()
  
    
    def Math_chart_link():
        import matplotlib 
        
        q = "SELECT * FROM stu_math_marks WHERE admn_no= %(val_admin_no)s "
        params = {'val_admin_no':sequence_no}
        cursor.execute(q, params)
        records=cursor.fetchall()
        print('Math marks :', records)

        dev_y=[]
        if records:
            
            for record in records:
                dev_y.insert(0,int(record[1])/40 *100)
                dev_y.insert(1,int(record[2])/40 *100)
                dev_y.insert(2,int(record[3])/80 *100)
                dev_y.insert(3,int(record[4])/40 *100)
                dev_y.insert(4,int(record[5])/40 *100)
                dev_y.insert(5,int(record[6])/80 *100)

            print('dev_y records ')
            print(dev_y)

            exam_x=['UT1','UT2',  'MidTerm','UT3', 'UT4', 'Final']
            Mathaverage_y=[62,74,78,86,84,81]
            plt.ylabel("Math marks")
            plt.title("Exam wise")

            plt.plot(exam_x, dev_y, color='g',marker='.', label='Student '+ str(sequence_no))

            #Class Average Plot
            plt.plot(exam_x, Mathaverage_y, color='#444444', linewidth=3, linestyle='--', marker='o', label='Math-Class Median')

            plt.legend()

            #To set the padding right for different monitor screen types
            plt.tight_layout()

            #to save the plot as a .png file in the current directory
            plt.savefig('/Users/aashna_ased/Desktop/graph'+'.pdf')
            plt.show()  
        else:
            print('No Math data to plot for student')

    def IP_chart_link():
        
        #c.execute("SELECT * FROM stu_ip_marks WHERE oid=" + str(sequence_no))
        q = "SELECT * FROM stu_ip_marks WHERE admn_no= %(val_admin_no)s "
        params = {'val_admin_no':sequence_no}
        cursor.execute(q, params)
        records=cursor.fetchall()
        print('IP marks :', records)
        dev_y=[]
        if records:
            #Loop through record in list
            for record in records:
                dev_y.insert(0,int(record[1])/40 *100)
                dev_y.insert(1,int(record[2])/40 *100)
                dev_y.insert(2,int(record[3])/80 *100)
                dev_y.insert(3,int(record[4])/40 *100)
                dev_y.insert(4,int(record[5])/40 *100)
                dev_y.insert(5,int(record[6])/80 *100)

            #Ploting Style
            plt.xkcd()

            IPaverage_y=[72,76,73,83,81,90]
            exam_x=['UT1','UT2',  'MidTerm','UT3', 'UT4', 'Final']

            plt.ylabel("IP marks")
            plt.title("Exam wise")

            plt.plot(exam_x, dev_y,marker='.',label='Student '+ str(sequence_no))

            #Class Average Plot for IP
            plt.plot(exam_x, IPaverage_y, color='#444444', linewidth=3, linestyle='--',marker='o', label='IP-Class Median')

            plt.legend()

            #To set the padding right for different monitor screen types
            plt.tight_layout()

            #to save the plot as a .png file in the current directory
            plt.savefig('/Users/aashna_ased/Desktop/graph'+'.pdf')

            plt.show()
        else:
            print('No IP data to plot for student')


    def Phy_chart_link():
        
        q = "SELECT * FROM stu_phy_marks WHERE admn_no= %(val_admin_no)s  "
        params = {'val_admin_no':sequence_no}
        cursor.execute(q, params)
        records=cursor.fetchall()
        print('Physics marks :', records)
        dev_y=[]
        if records:
            #Loop through record in list
            for record in records:
                dev_y.insert(0,int(record[1])/40 *100)
                dev_y.insert(1,int(record[2])/40 *100)
                dev_y.insert(2,int(record[3])/80 *100)
                dev_y.insert(3,int(record[4])/40 *100)
                dev_y.insert(4,int(record[5])/40 *100)
                dev_y.insert(5,int(record[6])/80 *100)


            #Ploting Style
            plt.style.use('fivethirtyeight')

            Phyaverage_y=[72,74,73,80,84,82]
            exam_x=['UT1','UT2',  'MidTerm','UT3', 'UT4', 'Final']

            plt.ylabel("Marks")
            plt.title("Exam wise")

            plt.plot(exam_x, dev_y,marker='.',  label='Student '+ str(sequence_no))

            #Class Average Plot for Physics
            plt.plot(exam_x, Phyaverage_y,color='#444444', linewidth=3, linestyle='--', marker='o', label='Physics-Class Median')

            plt.legend()

            #To set the padding right for different monitor screen types
            plt.tight_layout()

            #to save the plot as a .png file in the current directory
            plt.savefig('/Users/aashna_ased/Desktop/graph'+'.pdf')
            plt.show()
        else:
            print('No Physics data to plot for student')



    def fn_classroom_display():

        editor.title=('View Student profile')
        editor.geometry('1700x1000')



        global f_name_editor
        global l_name_editor
        global Admin_no_editor
        global rank_editor      
        global section_editor
        global class_teacher_editor

        if class_btn["state"] == NORMAL:
            class_btn["state"] = DISABLED
        else:
            class_btn["state"] = NORMAL


        #Frame3
        frame3=LabelFrame(editor)

       #Class Rank

        rank_label= Label(frame3, text="Rank:")
        rank_label.grid(row=14, column=0, sticky=W)

        Admin_no_label= Label(frame3, text="Admin_no:")
        Admin_no_label.grid(row=14, column=1, sticky=W)

        f_name_label= Label(frame3, text="First Name:")
        f_name_label.grid(row=14, column=2, sticky=W)

        l_name_label= Label(frame3, text="Last Name:")
        l_name_label.grid(row=14, column=3, sticky=W)  

        section_label= Label(frame3, text="Section:")
        section_label.grid(row=14, column=4, sticky=W)

        class_teacher_label= Label(frame3, text="Class_teacher:")
        class_teacher_label.grid(row=14, column=5, sticky=W)


        
        q = "SELECT * FROM new_students WHERE section= %(val_section)s "
        params = {'val_section':stu_section_var}
        cursor.execute(q, params)
        records=cursor.fetchall()

        
        #Loop through record in list
        i=15
        for record in records:

            rows = []
            x=0
            j=0

            cols = []

            for j in range(6):

                e = Entry(frame3,width=8,relief=GROOVE)

                e.grid(row=i, column=j, sticky=NSEW)

                e.insert(END,  (record[j]))


                cols.append(e)
            i+=1    
            x+=1    
            rows.append(cols)

        frame3.pack()



    def fn_profile_display():

        #Row12
        global editor
        global frame1
        global frame2
        global frame3
        global frame4
        #editor=Tk()
        editor.title=('View Student profile')
        editor.geometry('1700x1000')

        global f_name_editor
        global l_name_editor
        global gender_editor
        global DOB_editor      
        global address_editor
        global contact_num_editor
        global email_editor
        global admin_editor
        global section_editor



        if prof_btn["state"] == NORMAL:
            prof_btn["state"] = DISABLED
        else:
            prof_btn["state"] = NORMAL

        #Frame 2
        frame2=LabelFrame(editor)


        f_name_editor= Entry(frame2, width=30)
        f_name_editor.grid(row=12, column=1, padx=20, pady=(10,0))
        
        gender_editor= Entry(frame2, width=30)
        gender_editor.grid(row=13, column=1)
        DOB_editor= Entry(frame2, width=30)
        DOB_editor.grid(row=14, column=1)
        address_editor= Entry(frame2, width=30)
        address_editor.grid(row=15, column=1)
        contact_num_editor= Entry(frame2, width=30)
        contact_num_editor.grid(row=16, column=1)
        email_editor= Entry(frame2, width=30)
        email_editor.grid(row=17, column=1)
        admin_editor= Entry(frame2, width=30)
        admin_editor.grid(row=19, column=1)
        section_editor= Entry(frame2, width=30)
        section_editor.grid(row=18, column=1)

        #Search for logged in student's profile data
        q = "SELECT * FROM new_students WHERE admn_no= %(val_admin_no)s AND section=%(val_section)s "
        params = {'val_admin_no':sequence_no, 'val_section':stu_section_var}
        cursor.execute(q, params)
        records=cursor.fetchall()
        
        #Loop through record in list
        for record in records:
            f_name_editor.insert(0,record[1])
            
            gender_editor.insert(0,record[2])
            DOB_editor.insert(0,record[3])
            address_editor.insert(0,record[4])
            contact_num_editor.insert(0,record[5])
            email_editor.insert(0,record[6])
            admin_editor.insert(0,record[0])
            section_editor.insert(0,record[8])



        f_name_label= Label(frame2, text="First Name:")
        f_name_label.grid(row=12, column=0)


        gender_label= Label(frame2, text="Gender:")
        gender_label.grid(row=13, column=0)

        DOB_label= Label(frame2, text="DOB:")
        DOB_label.grid(row=14, column=0)

        address_label= Label(frame2, text="Address:")
        address_label.grid(row=15, column=0)

        contact_num_label= Label(frame2, text="Contact Number:")
        contact_num_label.grid(row=16, column=0)

        email_label= Label(frame2, text="Email:")
        email_label.grid(row=17, column=0)

        admin_label= Label(frame2, text="Admin No:")
        admin_label.grid(row=19, column=0)

        section_label= Label(frame2, text="Section:")
        section_label.grid(row=18, column=0)

        frame2.pack()
   


main.mainloop()

