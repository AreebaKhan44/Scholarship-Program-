#!/usr/bin/env python
# coding: utf-8

# In[2]:


from tkinter import*
from tkinter import messagebox
import tkinter as tk
from PIL import Image , ImageTk
import json

def log_in():
    screen = Tk()
    screen.geometry("500x600")
    screen.title("LOG IN")
    screen.configure(background = "purple")
    bg = ImageTk.PhotoImage(file ="b2.jpeg")
    img = Label(screen , image = bg)
    img.pack()
    

         ################## HEADING ###################
    heading = Label(text = "SINDH MADARSATUL ISLAM UNIVERSITY ",bg = 'indigo',fg = 'white')
    heading.place(x=180,y=5)
   

            ################# INFORMATION ################
    email = Label(text = "E-MAIL*", bg = 'indigo',fg = 'white',width = "30" , height = "1" )
    password = Label(text = "PASSSWORD *", bg = 'indigo',fg = 'white',width = "30" , height = "1" )
        

            ############### INFORMATION POSITIONS #############
    email.place(x= 5 , y = 60)
    password.place(x= 5 , y = 120)
    
    email = StringVar()
    password = StringVar()
    

             ################# ENTRY ################
    email_entry = Entry(textvariable = email , width = "40")
    password_entry = Entry(textvariable = password, width = "40",show="*")


            ############### ENTRY POSITION #############
    email_entry.place(x = 240 ,y = 60)
    password_entry.place(x = 240 ,y = 120)

            ############# BUTTONS MESSAGE ###############
    
    
    def login():
        with open('user.json','r') as f:
            dic = json.load(f)
        
        
        email_info = email.get()
        password_info = password.get()
        if email_info == "" or password_info == "":
            messagebox.showerror("Error", "All fields are required")
        
        elif dic["Email"] == email_info and dic["password"] == password_info:
            messagebox.showinfo("info", "successsfully logged in ")
            screen.destroy()
            registeration_form()
            
        else:
            messagebox.showerror("info", " Invalid user name or passsword")
            
        
    
           
         
    
    def cancel():
        result = messagebox.askyesno("Warning","Are you sure want to exit")
        if result:
            screen.destroy()
            MAIN_SCREEN()

    ########### BUTTONS ###############
    def delete():
        email_entry.delete(0, END)
        password_entry.delete(0, END)

    login = Button(screen,text = "LOG IN", command  = login, bg = 'indigo',fg = 'white')
    login.place(x= 280 , y = 200)
    clear = Button(screen,text = "CLEAR", command = delete , bg = 'indigo',fg = 'white')
    clear.place(x= 377 , y = 200)
    cancel = Button(screen,text = "HOME",command = cancel,bg = 'indigo',fg = 'white' )
    cancel.place(x= 330 , y = 200)
    screen.mainloop()
def sign_up_form():
    sign_up = Tk()
    win_width = sign_up.winfo_screenwidth()
    win_height= sign_up.winfo_screenheight()
    sign_up.geometry(f"{win_width}x{win_height}")
    sign_up.title("SIGNUP FORM")
    sign_up.configure(background="PURPLE")
    
    HEADING = Label(sign_up, text ="*SIGNUP FORM*",font = ("bold","20","italic"),bg="PURPLE", fg="WHITE").place(x=500, y=1)
    label1 = Label(sign_up, text="FIRST NAME", fg="black",width="15").place(x=300, y=90)
    label2 = Label(sign_up, text="LAST NAME ", fg="black",width="15").place(x=640, y=90)
    label3 = Label(sign_up, text="GENDER", fg="black",width="15").place(x=300, y=140)
    label4 = Label(sign_up, text="DATE OF BIRTH", fg="black",width="15").place(x=640, y=140)
    label5 = Label(sign_up, text="EMAIL ADDRESS", fg="black",width="15").place(x=300, y=190)
    label6 = Label(sign_up, text="EDUCATION",fg="black",width="15").place(x=640,y=190)
    label7 = Label(sign_up, text="CREATE PASSWORD",fg="black",width="15").place(x=300, y=240)
    label1 = StringVar()
    label2 = StringVar()
    label3 = StringVar()
    label4 = StringVar()
    label5 = StringVar()
    label6 = StringVar()
    label7 = StringVar()
    
    entry1 = Entry(sign_up,text=label1, width="30").place(x=430,y=90)
    entry2 = Entry(sign_up,text=label2, width="30").place(x=770,y=90)
    entry3 = Entry(sign_up,text=label3, width="30").place(x=430,y=140)
    entry4 = Entry(sign_up,text=label4, width="30").place(x=770,y=140)
    entry5 = Entry(sign_up,text=label5, width="30").place(x=430,y=190)
    entry6 = Entry(sign_up,text=label6, width="30").place(x=770,y=190)
    entry7 = Entry(sign_up,text=label7, width="30").place(x=430,y=240)

    
    def signup():
        
        fname = label1.get()
        lname = label2.get()
        gender = label3.get()
        dob = label4.get()
        email = label5.get()
        education = label6.get()
        password = label7.get()
        with open('user.json','r') as f:
            dc = json.load(f)
       
        
        if fname == ""or lname==""or gender==""or dob== ""or email==""or education==""or password=="" :
            messagebox.showerror("Error",'All fields are required')
        elif email == dc["Email"]:
                            messagebox.showerror("Error","This email is already exist")
        else:
            dic = {"Email":email,"password":password,"First name":fname,"last name":lname,
                  "Gender":gender,"Date of birth":dob,"Education":education}
            with open("user.json",'w') as f:
                   json.dump(dic,f)
                
            result=messagebox.showinfo("confirmation","SIGNUP COMPLETE")
            sign_up.destroy()
            MAIN_SCREEN()
            
           
    def exit():
        result=messagebox.askquestion("confirmation","are you sure")
        if(result=="yes"):
            sign_up.destroy()
            MAIN_SCREEN()
    #CREATE BUTTONS
    SIGNUP = Button(sign_up,text = "SIGNUP", command = signup, bg = 'indigo',fg = 'white',width="20",height="2").place(x=400,y=350 )
    exit = Button(sign_up,text = "EXIT", command = exit, bg = 'indigo',fg = 'white',width="20",height="2").place(x=600, y=350)

    sign_up.mainloop()
def registeration_form():
    form = Tk()
    win_width = form.winfo_screenwidth()
    win_height= form.winfo_screenheight()
    form.geometry(f"{win_width}x{win_height}")
    form.title("SCHOLARSHIP FORM")
    form.configure(background="purple")
    def save_info():
        ######################## USING GET FUNCTION ######################
        FIRST_NAME_info = FIRST_NAME.get() 
        LAST_NAME_info = LAST_NAME.get() 
        DATE_OF_BIRTH_info = DATE_OF_BIRTH.get() 
        GENDER_info = GENDER.get() 
        MARITAL_STATUS_info = MARITAL_STATUS.get() 
        RELIGION_info = RELIGION.get() 
        NATIONALITY_info = NATIONALITY.get()
        CNIC_NO_info = CNIC_NO.get()
        CURRENT_ADDRESS_info = CURRENT_ADDRESS.get() 
        PERMANENT_ADDRESS_info = PERMANENT_ADDRESS.get() 
        MOBILE_NUMBER_info = MOBILE_NUMBER.get() 
        PHONE_NUMBER_info = PHONE_NUMBER.get() 
        EMAIL_ADDRESS_info = EMAIL_ADDRESS.get() 
        FATHER_NAME_info = FATHER_NAME.get()
        FATHER_MOBILE_NUMBER_info = FATHER_MOBILE_NUMBER.get() 
        FATHER_EMAIL_ADDRESS_info = FATHER_EMAIL_ADDRESS.get() 
        FATHER_CNIC_NO_info = FATHER_CNIC_NO.get() 
        FATHER_OCCUPATION_info = FATHER_OCCUPATION.get() 
        MOTHER_NAME_info = MOTHER_NAME.get() 
        MOTHER_MOBILE_NUMBER_info = MOTHER_MOBILE_NUMBER.get() 
        MOTHER_EMAIL_ADDRESS_info = MOTHER_EMAIL_ADDRESS.get() 
        MOTHER_CNIC_NO_info = MOTHER_CNIC_NO.get() 
        MOTHER_OCCUPATION_info = MOTHER_OCCUPATION.get() 
        SCHOOL_NAME_info = SCHOOL_NAME.get() 
        SCHOOL_DEGREE_info = SCHOOL_DEGREE.get() 
        SCHOOL_TOTAL_MARKS_info = SCHOOL_TOTAL_MARKS.get()
        SCHOOL_MARKS_OBTAINED_info = SCHOOL_MARKS_OBTAINED.get() 
        SCHOOL_PERCENTAGE_info = SCHOOL_PERCENTAGE.get() 
        COLLEGE_NAME_info = COLLEGE_NAME.get() 
        COLLEGE_DEGREE_info = COLLEGE_DEGREE.get()
        COLLEGE_TOTAL_MARKS_info = COLLEGE_TOTAL_MARKS.get() 
        COLLEGE_MARKS_OBTAINED_info = COLLEGE_MARKS_OBTAINED.get() 
        COLLEGE_PERCENTAGE_info = COLLEGE_PERCENTAGE.get()
        
        if FIRST_NAME_info == "" or LAST_NAME_info == "" or DATE_OF_BIRTH_info == "" or GENDER_info == "" or MARITAL_STATUS_info == "" or RELIGION_info == "" or NATIONALITY_info == "" or CNIC_NO_info == "" or CURRENT_ADDRESS_info == "" or PERMANENT_ADDRESS_info == "" or MOBILE_NUMBER_info == "" or PHONE_NUMBER_info == "" or EMAIL_ADDRESS_info == "" or FATHER_NAME_info == "" or FATHER_MOBILE_NUMBER_info == "" or FATHER_EMAIL_ADDRESS_info == "" or FATHER_CNIC_NO_info == "" or  FATHER_OCCUPATION_info == "" or MOTHER_NAME_info == "" or  MOTHER_MOBILE_NUMBER_info == "" or MOTHER_EMAIL_ADDRESS_info == "" or MOTHER_CNIC_NO_info == "" or MOTHER_OCCUPATION_info == "" or SCHOOL_NAME_info == "" or SCHOOL_DEGREE_info == "" or SCHOOL_TOTAL_MARKS_info == "" or SCHOOL_MARKS_OBTAINED_info == "" or SCHOOL_PERCENTAGE_info == "" or COLLEGE_NAME_info == "" or COLLEGE_DEGREE_info == "" or COLLEGE_TOTAL_MARKS_info == "" or COLLEGE_MARKS_OBTAINED_info == "" or COLLEGE_PERCENTAGE_info == "":
            messagebox.showerror("Error",'All fields are required')
        else:
    ####################### SAVING DATA IN TEXT FILE ######################### 
            file = open("scholarship_form.txt","w")
            file.write("YOUR FIRST NAME:" + FIRST_NAME_info)
            file.write("\n")
            file.write("YOUR LAST NAME:" + LAST_NAME_info)
            file.write("\n")
            file.write("YOUR GENDER:" + GENDER_info)
            file.write("\n")
            file.write("YOUR DATE OF BIRTH:" + str(DATE_OF_BIRTH_info))
            file.write("\n")
            file.write("YOUR MARITAL STATUS:" + MARITAL_STATUS_info)
            file.write("\n")
            file.write("YOUR RELIGION:" + RELIGION_info)
            file.write("\n")
            file.write("YOUR NATIONALITY:" + NATIONALITY_info)
            file.write("\n")
            file.write("YOUR CNIC NO:" + str(CNIC_NO_info))
            file.write("\n")
            file.write("YOUR CURRENT ADDRESS:" + CURRENT_ADDRESS_info)
            file.write("\n")
            file.write("YOUR PERMANENT ADDRESS:" + PERMANENT_ADDRESS_info)
            file.write("\n")
            file.write("YOUR MOBILE NUMBER:" + str(MOBILE_NUMBER_info))
            file.write("\n")
            file.write("YOUR PHONE NUMBER:" + str(PHONE_NUMBER_info))
            file.write("\n")
            file.write("YOUR EMAIL ADDRESS:" + EMAIL_ADDRESS_info)
            file.write("\n")
            file.write("YOUR FATHER NAME:" + FATHER_NAME_info)
            file.write("\n")
            file.write("YOUR FATHER MOBILE NUMBER:" + str(FATHER_MOBILE_NUMBER_info))
            file.write("\n")
            file.write("YOUR FATHER EMAIL ADDRESS:" + FATHER_EMAIL_ADDRESS_info)
            file.write("\n")
            file.write("YOUR FATHER CNIC NO:" + str(FATHER_CNIC_NO_info))
            file.write("\n")
            file.write("YOUR FATHER OCCUPATION:" + FATHER_OCCUPATION_info)
            file.write("\n")
            file.write("YOUR MOTHER NAME:" + MOTHER_NAME_info)
            file.write("\n")
            file.write("YOUR MOTHER MOBILE NUMBER:" + str(MOTHER_MOBILE_NUMBER_info))
            file.write("\n")
            file.write("YOUR MOTHER EMAIL ADDRESS:" + MOTHER_EMAIL_ADDRESS_info)
            file.write("\n")
            file.write("YOUR MOTHER CNIC NO:" + str(MOTHER_CNIC_NO_info))
            file.write("\n")
            file.write("YOUR MOTHER OCCUPATION:" + MOTHER_OCCUPATION_info)
            file.write("\n")
            file.write("YOUR SCHOOL NAME:" + SCHOOL_NAME_info)
            file.write("\n")
            file.write("YOUR SCHOOL DEGREE:" + SCHOOL_DEGREE_info)
            file.write("\n")
            file.write("YOUR SCHOOL TOTAL MARKS:" + str(SCHOOL_TOTAL_MARKS_info))
            file.write("\n")
            file.write("YOUR SCHOOL MARKS OBTAINED:" + str(SCHOOL_MARKS_OBTAINED_info))
            file.write("\n")
            file.write("YOUR SCHOOL PERCENTAGE:" + str(SCHOOL_PERCENTAGE_info))
            file.write("\n")
            file.write("YOUR COLLEGE NAME:" + COLLEGE_NAME_info)
            file.write("\n")
            file.write("YOUR COLLEGE DEGREE:" + COLLEGE_DEGREE_info)
            file.write("\n")
            file.write("YOUR COLLEGE TOTAL MARKS:" + str(COLLEGE_TOTAL_MARKS_info))
            file.write("\n")
            file.write("YOUR COLLEGE MARKS OBTAINED:" + str(COLLEGE_MARKS_OBTAINED_info))
            file.write("\n")
            file.write("YOUR COLLEGE PERCENTAGE:" + str(COLLEGE_PERCENTAGE_info))
    
            file.close()
            result=messagebox.askyesno("confirmation","IF YOU PROVIDE A WRONG AND MISS INFORMATION YOUR FORM WILL BE REJECTED")
            if result:
                form.destroy()
                record = Tk()
                win_width = record.winfo_screenwidth()
                win_height= record.winfo_screenheight()
                record.geometry(f"{win_width}x{win_height}")
                record.title("SCHOLARSHIP FORM")
                record.configure(background="purple")
                HEADING = Label(record, text = "*UNDERGRADUATE SCHOLARSHIP FORM",font = ("bold","20","italic"),bg= "indigo" , fg="green").place(x=350, y=1)
                HEADING2 = Label(record, text = f"Dear {FIRST_NAME_info}  { LAST_NAME_info} your form has been submitted successfully",font = ("bold","10","italic"),
                                 bg= 'indigo' , fg="white").place(x=200, y=200)
                def log_out():
                    result = messagebox.askyesno("log out", "Are you sure want to log out")
                    if result:
                        record.destroy()
                    
                submit = Button(record,text = "LOG OUT", command = log_out ,fg= "white",
                                bg = "indigo" ,width="30",height="2").place(x=200,y=750 )
                
                
                
                

###################### CREATING LABELS ####################

    HEADING = Label(form, text = "*UNDERGRADUATE SCHOLARSHIP FORM",font = ("bold","20","italic"),fg="green").place(x=350, y=1)
    PERSONAL_INFORMATION = Label(form, text = "PERSONAL INFORMATION(*required)",fg="blue2").place(x=50, y=50)
    label1 = Label(form, text="FIRST NAME", fg="black",bg = "grey",width="15").place(x=60, y=90)
    label2 = Label(form, text="LAST NAME ", fg="black",bg = "grey",width="15").place(x=400, y=90) 
    label3 = Label(form, text="DATE OF BIRTH ", fg="black",bg = "grey",width="15").place(x=740, y=90)
    label4 = Label(form, text="GENDER", fg="black",bg = "grey",width="15").place(x=1080, y=90)
    label5 = Label(form, text="MARITAL STATUS", fg="black",bg = "grey",width="15").place(x=60, y=140)
    label6 = Label(form, text="RELIGION", fg="black",bg = "grey",width="15").place(x=400, y=140)
    label7 = Label(form, text="NATIONALITY", fg="black",bg = "grey",width="15").place(x=740, y=140)
    label8 = Label(form, text="CNIC NO:",fg="black",bg = "grey",width="15").place(x=1080,y=140)
    label9 = Label(form, text="CURRENT ADDRESS",fg="black",bg = "grey",width="15").place(x=60, y=190)
    label10 = Label(form, text="PERMANENT ADDRESS",fg="black",bg = "grey",width="20").place(x=780, y=190)
    CONTACT_INFORMATION = Label(form,text = "CONTACT INFORMATION(*required)", fg="blue2").place(x=50, y=230)
    label11 = Label(form, text="MOBILE NUMBER",fg="black",bg = "grey",width="15").place(x=60,y=270)
    label12 = Label(form, text="PHONE NUMBER",fg="black",bg = "grey",width="15").place(x=400, y=270)
    label13 = Label(form, text="EMAIL ADDRESS", fg="black",bg = "grey",width="15").place(x=740,y=270)
    FATHER_INFORMATION = Label(form, text="FATHER'S INFORMATION(*required)", fg="blue2").place(x=50, y=310)
    label14 = Label(form, text="FATHER'S NAME", fg="black",bg = "grey",width="15").place(x=60, y=350)
    label15 = Label(form, text="MOBILE NUMBER",fg="black",bg = "grey",width="15").place(x=400, y=350)
    label16 = Label(form, text="EMAIL ADDRESS", fg="black",bg = "grey",width="15").place(x=740,y=350)
    label17 = Label(form, text="CNIC NO:",fg="black",bg = "grey",width="15").place(x=60,y=400)
    label18 = Label(form, text="OCCUPATION:",fg="black",bg = "grey",width="15").place(x=400,y=400)
    MOTHER_INFORMATION = Label(form, text="MOTHER'S INFORMATION(*required)", fg="blue2").place(x=50, y=440)
    label19 = Label(form, text="MOTHER'S NAME ", fg="black",bg = "grey",width="15").place(x=60, y=480)
    label20 = Label(form, text="MOBILE NUMBER",fg="black",bg = "grey",width="15").place(x=400, y=480)
    label21 = Label(form, text="EMAIL ADDRESS", fg="black",bg = "grey",width="15").place(x=740,y=480)
    label22 = Label(form, text="CNIC NO:",fg="black",bg = "grey",width="15").place(x=60,y=520)
    label23 = Label(form, text="OCCUPATION:",fg="black",bg = "grey",width="15").place(x=400,y=520)
    EDUCATIONAL_INFORMATION = Label(form, text="EDUCATIONAL INFORMATION(*required)", fg="blue2").place(x=50, y=560)
    label24 = Label(form, text="SCHOOL NAME:",fg="black",bg = "grey",width="15").place(x=60,y=600)
    label25 = Label(form, text="DEGREE:",fg="black",bg = "grey",width="15").place(x=400,y=600)
    label26 = Label(form, text="TOTAL MARKS:",fg="black",bg = "grey",width="15").place(x=740,y=600)
    label27 = Label(form, text="MARKS OBTAINED:",fg="black",bg = "grey",width="15").place(x=1080,y=600)
    label28 = Label(form, text="PERCENTAGE:",fg="black",bg = "grey",width="15").place(x=60,y=650)
    label29 = Label(form, text="COLLEGE NAME:",fg="black",bg = "grey",width="15").place(x=400,y=650)
    label30 = Label(form, text="DEGREE:",fg="black",bg = "grey",width="15").place(x=740,y=650)
    label31 = Label(form, text="TOTAL MARKS:",fg="black",bg = "grey",width="15").place(x=1080,y=650)
    label32 = Label(form, text="MARKS OBTAINED:",fg="black",bg = "grey",width="15").place(x=60,y=700)
    label33 = Label(form, text="PERCENTAGE:",fg="black",bg = "grey",width="15").place(x=400,y=700)


    FIRST_NAME = StringVar()
    LAST_NAME = StringVar()
    DATE_OF_BIRTH = StringVar()
    GENDER = StringVar()
    MARITAL_STATUS = StringVar()
    RELIGION = StringVar()
    NATIONALITY = StringVar()
    CNIC_NO = IntVar()
    CURRENT_ADDRESS = StringVar()
    PERMANENT_ADDRESS = StringVar()
    MOBILE_NUMBER = StringVar()
    PHONE_NUMBER = StringVar()
    EMAIL_ADDRESS = StringVar()
    FATHER_NAME = StringVar()
    FATHER_MOBILE_NUMBER = StringVar()
    FATHER_EMAIL_ADDRESS = StringVar()
    FATHER_CNIC_NO = StringVar()
    FATHER_OCCUPATION = StringVar()
    MOTHER_NAME = StringVar()
    MOTHER_MOBILE_NUMBER = StringVar()
    MOTHER_EMAIL_ADDRESS = StringVar()
    MOTHER_CNIC_NO = StringVar()
    MOTHER_OCCUPATION = StringVar()
    SCHOOL_NAME = StringVar()
    SCHOOL_DEGREE = StringVar()
    SCHOOL_TOTAL_MARKS = StringVar()
    SCHOOL_MARKS_OBTAINED = StringVar()
    SCHOOL_PERCENTAGE = StringVar()
    COLLEGE_NAME = StringVar()
    COLLEGE_DEGREE = StringVar()
    COLLEGE_TOTAL_MARKS = StringVar()
    COLLEGE_MARKS_OBTAINED = StringVar()
    COLLEGE_PERCENTAGE = StringVar()

#################### CREATING ENTRIES #####################

    entry1 = Entry(form,textvariable=FIRST_NAME, width="30").place(x=190,y=90)
    entry2 = Entry(form,textvariable=LAST_NAME, width="30").place(x=530,y=90)
    entry3 = Entry(form,textvariable=DATE_OF_BIRTH, width="30").place(x=870,y=90)
    entry4 = Entry(form,textvariable=GENDER, width="30").place(x=1210,y=90)
    entry5 = Entry(form,textvariable=MARITAL_STATUS, width="30").place(x=190,y=140)
    entry6 = Entry(form,textvariable=RELIGION, width="30").place(x=530,y=140)
    entry7 = Entry(form,textvariable=NATIONALITY, width="30").place(x=870,y=140)
    entry8= Entry(form,textvariable=CNIC_NO, width="30").place(x=1210,y=140)
    entry9 = Entry(form,textvariable=CURRENT_ADDRESS, width="95").place(x=190,y=190)
    entry10 = Entry(form,textvariable=PERMANENT_ADDRESS, width="95").place(x=940,y=190)        
    entry11 = Entry(form,textvariable=MOBILE_NUMBER, width="30").place(x=190,y=270)
    entry12 = Entry(form,textvariable=PHONE_NUMBER, width="30").place(x=530,y=270)
    entry13 = Entry(form,textvariable=EMAIL_ADDRESS, width="35").place(x=870,y=270)
    entry14 = Entry(form,textvariable=FATHER_NAME, width="30").place(x=190,y=350)
    entry15 = Entry(form,textvariable=FATHER_MOBILE_NUMBER, width="30").place(x=530,y=350)
    entry16 = Entry(form,textvariable=FATHER_EMAIL_ADDRESS, width="30").place(x=870,y=350)
    entry17 = Entry(form,textvariable=FATHER_CNIC_NO, width="30").place(x=190,y=400)
    entry18 = Entry(form,textvariable=FATHER_OCCUPATION, width="30").place(x=530,y=400)
    entry19 = Entry(form,textvariable=MOTHER_NAME, width="30").place(x=190,y=480)
    entry20 = Entry(form,textvariable=MOTHER_MOBILE_NUMBER, width="30").place(x=530,y=480)
    entry21 = Entry(form,textvariable=MOTHER_EMAIL_ADDRESS, width="35").place(x=870,y=480)
    entry22 = Entry(form,textvariable=MOTHER_CNIC_NO, width="30").place(x=190,y=520)
    entry23 = Entry(form,textvariable=MOTHER_OCCUPATION, width="30").place(x=530,y=520)
    entry24 = Entry(form,textvariable=SCHOOL_NAME, width="30").place(x=190,y=600)
    entry25 = Entry(form,textvariable=SCHOOL_DEGREE, width="30").place(x=530,y=600)
    entry26 = Entry(form,textvariable=SCHOOL_TOTAL_MARKS, width="30").place(x=870,y=600)
    entry27 = Entry(form,textvariable=SCHOOL_MARKS_OBTAINED, width="30").place(x=1210,y=600)
    entry28 = Entry(form,textvariable=SCHOOL_PERCENTAGE, width="30").place(x=190,y=650)
    entry29 = Entry(form,textvariable=COLLEGE_NAME, width="30").place(x=530,y=650)
    entry30 = Entry(form,textvariable=COLLEGE_DEGREE, width="30").place(x=870,y=650)
    entry31 = Entry(form,textvariable=COLLEGE_TOTAL_MARKS, width="30").place(x=1210,y=650)
    entry32 = Entry(form,textvariable=COLLEGE_MARKS_OBTAINED, width="30").place(x=190,y=700)
    entry33 = Entry(form,textvariable=COLLEGE_PERCENTAGE, width="30").place(x=530,y=700)
    
   
     #################### CALLING FUNCTIONS ####################
    def exit():
        result=messagebox.askquestion("confirmation","are you sure want to exit")
        if(result=="yes"):
            form.destroy()
            MAIN_SCREEN()
        
        

    #################### CREATING BUTTONS #####################
    submit = Button(form,text = "submit", command = save_info,fg= "white",bg = "indigo" ,width="30",height="2").place(x=200,y=750 )
    exit = Button(form,text = "exit", command = exit,fg = "white",bg = "indigo" ,width="30",height="2").place(x=440, y=750)
    
    form.mainloop()

def MAIN_SCREEN():
     
##########################                 L O G        I N               #############################################
    def LOG_IN():
        main_screen.destroy()
        log_in()
        

        
##########################             S   I  G  N         U   P          ####################################################
    def SIGN_UP():
        main_screen.destroy()
        sign_up_form()
        
        
    
##########################         R E G I S T R A T I O N    F O R M     ########################################
    def REGISTRATION_FORM():
        main_screen.destroy()
        registeration_form()
        
        
###################################### M  A  I  N     M  E  N  U #################################################
    def HOME():
        radSelected = radValues.get()
        if radSelected == 1:
            LOG_IN()
        
        
        elif radSelected == 2:
            SIGN_UP()
        
       
        elif radSelected == 3:
            def cancel():
                result = messagebox.askyesno("Warning","Are you sure want to exit")
                if result:
                    main_screen.destroy()
            cancel()
        else:
            print("sorry")
        
    main_screen = Tk()
    main_screen.geometry('586x400')
    main_screen.configure(background='purple')
    main_screen.title("       M A I N    M E N U      "  )
    HEADING = Label(main_screen, text = "WELCOME TO SMIU SCHOLARSHIP PORTAL",
                   font = ("bold","20","italic"),fg="green").place(x=0, y=0)
    bg = ImageTk.PhotoImage(file ="b1.jpg")
    img = Label(main_screen , image = bg)
    img.place(x=53,y=60)
    radValues = IntVar()

    rad1 = Radiobutton(main_screen, text="LOG IN",bg= 'indigo',fg = 'white' , variable=radValues, value=1, command=HOME)
    rad1.place(x=200,y=100)
    rad2 = Radiobutton(main_screen, text="SIGN UP",bg= 'indigo',fg = 'white' , variable=radValues, value=2, command=HOME)
    rad2.place(x=200,y=150)
    rad3 = Radiobutton(main_screen, text="EXIT",bg= 'indigo',fg = 'white' , variable=radValues, value=3, command=HOME)
    rad3.place(x=200,y=200)
    
        
        
    ###########     M A I N        L O O P  ###############
    main_screen.mainloop()


# In[5]:


MAIN_SCREEN()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[50]:





# In[ ]:





# In[ ]:




