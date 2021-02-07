from tkinter import *
import tkinter as ttk
window = Tk()
lable = Label(window, text = "Choose the report you want to check its result", fg='violet', font=('Cooper Black',40))
lable.pack()
window.title("Your monthly analysis checker")
'''rate'''
def rate3():
    import matplotlib.pyplot as plt
    doctor = ['Endocrinologist', 'Urologist', 'Nephrologists']
    sugg = [90, 60, 50]
    plt.bar(doctor, sugg)
    plt.show()
def rate4():
    import matplotlib.pyplot as plt
    doctor = ['Endocrinologist', 'Urologist', 'Nephrologists', 'Podiatrist', 'Nutritionist', 'Cardiologist',
              'Ophthalmologist']
    sugg = [90, 60, 50, 50, 80, 30, 30]
    c = ['blue', 'orange', 'teal', 'navy', 'pink', 'violet', 'green']
    plt.barh(doctor, sugg, 0.7, color=c)
    plt.ylabel("Specialist Doctors", color="red")
    plt.xlabel("Suggestion percentage", color="green")
    plt.title("The suggested doctors", color="orange")
    plt.show()
def rate2():
    import matplotlib.pyplot as plt
    doctor = ['gynecologist', 'Endocrinologist', 'Andrologist']
    sugg = [0, 60, 90]
    c2 = ['teal', 'violet', 'pink']
    plt.ylabel("Suggestion percentage", color="red")
    plt.xlabel("Specialist Doctors", color="green")
    plt.title("The suggested doctors", color="orange")
    plt.bar(doctor, sugg, color=c2)
    plt.show()
def rate():
    import matplotlib.pyplot as plt
    doctor = ['gynecologist', 'Endocrinologist', 'Andrologist']
    sugg = [90, 60, 0]
    c1 = ['teal', 'violet', 'pink']
    plt.ylabel("Suggestion percentage", color="red")
    plt.xlabel("Specialist Doctors", color="green")
    plt.title("The suggested doctors", color="orange")
    plt.bar(doctor, sugg, color=c1)
    plt.show()

#fsh hormone
def no():
    d = float(input("type your FSH report\n"))
    if float(0) <= d <= float(4.0):
        print("you are doing well!")
    elif d < float(0) or d > int(4.0):
        print("I suggest you to visit an OB/GYN or a gynecologist \n"
              "Gynecologists are doctors who specialize in women's health,\n "
              "with a focus on the female reproductive system.\n"
              "They deal with a wide range of issues, including obstetrics,\n"
              "or pregnancy and childbirth, menstruation and fertility issues,\n "
              "sexually transmitted infections (STIs), hormone disorders, and others.\n")
        rate()
def yes():
    d1 = float(input("enter your FSH report\n"))
    if int(4.7) <= d1 <= float(21.5):
        print("you are doing well")
    elif d1 <= int(4.7) or d1 > float(21.5):
        print("During each menstrual cycle, there is a rise in follicle stimulating hormone secretion \n"
              " in the first half of the cycle that stimulates follicular growth in the ovary. \n "
              "After ovulation the ruptured follicle forms a corpus luteum that produces high levels of. "
              "\n "
              "Therefore,you may suffer from those changes in your FSH \n"
              "**by the way**, I suggest you to visit an OB/GYN or a gynecologist \n"
              "Gynecologists are doctors who specialize in women's health, \n "
              "with a focus on the female reproductive system.\n"
              "They deal with a wide range of issues, including obstetrics, \n "
              "or pregnancy and childbirth, menstruation and fertility issues, \n "
              "sexually transmitted infections (STIs), hormone disorders, and others. \n ")
        rate()

def no2():
    d2 = float(input("type your FSH report\n"))
    if float(0.3) <= d2 <= float(10.0):
        print("you are doing well!")
    elif d2 < float(0.3) or d2 > int(10.0):
        print("I suggest you to visit an OB/GYN or a gynecologist \n"
              "Gynecologists are doctors who specialize in women's health,\n "
              "with a focus on the female reproductive system.\n"
              "They deal with a wide range of issues, including obstetrics,\n"
              "or pregnancy and childbirth, menstruation and fertility issues,\n "
              "sexually transmitted infections (STIs), hormone disorders, and others.\n")
        rate()
    else:
        print("please enter a valid answer")
def yes2():
    d3 = float(input("enter your FSH report\n"))
    if int(4.7) <= d3 <= float(21.5):
        print("you are doing well")
    elif d3 <= int(4.7) or d3 > float(21.5):
        print("During each menstrual cycle, there is a rise in follicle stimulating hormone secretion \n"
              " in the first half of the cycle that stimulates follicular growth in the ovary. \n "
              "After ovulation the ruptured follicle forms a corpus luteum that produces high levels of. "
              "\n "
              "Therefore,you may suffer from those changes in your FSH \n"
              "**by the way**, I suggest you to visit an OB/GYN or a gynecologist \n"
              "Gynecologists are doctors who specialize in women's health, \n "
              "with a focus on the female reproductive system.\n"
              "They deal with a wide range of issues, including obstetrics, \n "
              "or pregnancy and childbirth, menstruation and fertility issues, \n "
              "sexually transmitted infections (STIs), hormone disorders, and others. \n ")
        rate()
def choice1():
            d4 = float(input("type your FSH report\n"))
            if float(4.7) <= d4 <= float(21.5):
                print("you are doing well!")
            elif d4 < float(4.7) or d4 > int(21.5):
                print("During each menstrual cycle, there is a rise in follicle stimulating hormone secretion \n"
                      " in the first half of the cycle that stimulates follicular growth in the ovary. \n "
                      "After ovulation the ruptured follicle forms a corpus luteum that produces high levels of. "
                      "\n "
                      "Therefore,you may suffer from those changes in your FSH \n"
                      "I suggest you to visit an OB/GYN or a gynecologist \n"
                      "Gynecologists are doctors who specialize in women's health,\n "
                      "with a focus on the female reproductive system.\n"
                      "They deal with a wide range of issues, including obstetrics,\n"
                      "or pregnancy and childbirth, menstruation and fertility issues,\n "
                      "sexually transmitted infections (STIs), hormone disorders, and others.\n")
                rate()
def choice2():
            d5 = float(input("type your FSH report\n"))
            if float(25.8) <= d5 <= float(134.8):
                print("you are doing well!")
            elif d5 < float(25.8) or d5 > int(134.8):
                print("for very high FSH levels is that you are beginning menopause. Because you have fewer\n "
                      "remaining follicles,\n "
                      " your body produces less of a hormone called Inhibin B,\n"
                      " which is responsible for keeping FSH levels down\n"
                      "**BY THE WAY*** I suggest you to visit an OB/GYN or a gynecologist \n"
                      "Gynecologists are doctors who specialize in women's health,\n "
                      "with a focus on the female reproductive system.\n"
                      "They deal with a wide range of issues, including obstetrics,\n"
                      "or pregnancy and childbirth, menstruation and fertility issues,\n "
                      "sexually transmitted infections (STIs), hormone disorders, and others.\n")
                rate()
            else:
                print("please enter a valid answer")
                check_again()
def fsh_female():
    age = int(input("what's your age?\n"))
    if age <= 11:
        lable3= Label(window, text = "Do you have menstrual cycle" , fg = 'Red', font=('Cooper Black',30))
        lable3.pack()
        x3 = IntVar()
        x4 = IntVar()
        checkboxno = Checkbutton(window,
                                 text="no",
                                 onvalue=1,
                                 offvalue=0,
                                 variable=x3,
                                 command=no,
                                 font=('Arial', 20))
        checkboxno.pack()
        checkboxyes = Checkbutton(window,
                                  text="yes",
                                  onvalue=1,
                                  offvalue=0,
                                  variable=x4,
                                  command=yes,
                                  font=('Arial', 20))
        checkboxyes.pack()
        window.mainloop()
    elif 11 < age <= 17:
        lable8= Label(window, text = "Are you menstruating now?" , fg = 'Red', font=('Cooper Black',30))
        lable8.pack()
        x5 = IntVar()
        x6 = IntVar()
        checkboxno2 = Checkbutton(window,
                                  text="no",
                                  onvalue=1,
                                  offvalue=0,
                                  variable=x5,
                                  command=no2,
                                  font=('Arial', 20))
        checkboxno2.pack()
        checkboxyes2 = Checkbutton(window,
                                   text="yes",
                                   onvalue=1,
                                   offvalue=0,
                                   variable=x6,
                                   command=yes2,
                                   font=('Arial', 20))
        checkboxyes2.pack()
        window.mainloop()



    else:
        print("please choose one condition")
        x7 = IntVar()
        x8 = IntVar()
        checkboxchoice1 = Checkbutton(window,
                                 text="I am still menstrauting",
                                 onvalue=1,
                                 offvalue=0,
                                 variable=x7,
                                 command=choice1,
                                 font=('Arial', 20))
        checkboxchoice1.pack()
        checkboxchoice2 = Checkbutton(window,
                                  text="I have reached the menopause",
                                  onvalue=1,
                                  offvalue=0,
                                  variable=x8,
                                  command=choice2,
                                  font=('Arial', 20))
        checkboxchoice2.pack()
        window.mainloop()
def fsh_male():
    age2 = int(input("what's your age?\n"))
    if age2 <= 12:
        q2 = float(input("type your FSH report\n"))
        if int(0) <= q2 <= float(0.5):
            print("you are doing well!")
        elif q2 > float(0.5) or q2 < int(0):
            print("I suggest you seeing an Andrologist (Andrologists are the male equivalent of \n"
                  " gynecologists, focusing entirely on male reproductive issues ")
            rate2()
        else:
            print("enter a valid answer")
            check_again()
    elif 12 < age2 <= 17:
        q2 = float(input("type your FSH report\n"))
        if int(0.3) <= q2 <= float(10.0):
            print("you are doing well!")
        elif q2 > float(0.3) or q2 < int(10.0):
            print("I suggest you seeing an Andrologist (Andrologists are the male equivalent of \n"
                  " gynecologists, focusing entirely on male reproductive issues ")
            rate2()
        else:
            print("enter a valid answer")
            check_again()
    else:
        q2 = float(input("type your FSH report\n"))
        if int(1.5) <= q2 <= float(12.4):
            print("you are doing well!")
        elif q2 > float(1.5) or q2 < int(12.4):
            print("I suggest you seeing an Andrologist (Andrologists are the male equivalent of \n"
                  " gynecologists, focusing entirely on male reproductive issues ")
            rate2()
        else:
            print("enter a valid answer")
            check_again()
def female_fsh():
    if (x.get() == 1):
        print(fsh_female())
def male_fsh():
    if x2.get() == 1:
        print(fsh_male())
def gender_fsh():
    lable2=Label(window, text="Choose your gender", font= ('Cooper Black', 30), fg= 'blue')
    lable2.pack()
    checkbutton = Checkbutton(window,
                          text="female",
                          onvalue=1,
                          offvalue=0,
                          variable=x,
                          command=female_fsh,
                          font=('Arial', 20))
    checkbutton.pack()
    checkbutton2 = Checkbutton(window,
                           text="male",
                           onvalue=1,
                           offvalue=0,
                           variable=x2,
                           command=male_fsh,
                           font=('Arial', 20))
    checkbutton2.pack()
    window.mainloop()

#prolactin
def no3():
  p = float(input("Type your prolactin report\n"))
  if 2 <= p <=29:
    print("You're doing well")
  else:
    print("I suggest you to visit an OB/GYN or a gynecologist \n"
              "Gynecologists are doctors who specialize in women's health,\n "
              "with a focus on the female reproductive system.\n"
              "They deal with a wide range of issues, including obstetrics,\n"
              "or pregnancy and childbirth, menstruation and fertility issues,\n "
              "sexually transmitted infections (STIs), hormone disorders, and others.\n")
    rate()
def yes3():
    p2 = float(input("Type your prolactin report\n"))
    if 10 <= p2 <=209:
       print("You're doing well")
    else:
        print("I suggest you to visit an OB/GYN or a gynecologist \n"
              "Gynecologists are doctors who specialize in women's health,\n "
              "with a focus on the female reproductive system.\n"
              "They deal with a wide range of issues, including obstetrics,\n"
              "or pregnancy and childbirth, menstruation and fertility issues,\n "
              "sexually transmitted infections (STIs), hormone disorders, and others.\n")
        rate()
def prolactin_female():
  lable4 = Label(window, text="Are you pregnant", fg='green', font=('Cooper Black', 30))
  lable4.pack()
  x9 = IntVar()
  x10 = IntVar()
  checkboxno3 = Checkbutton(window,
                                 text="no",
                                 onvalue=1,
                                 offvalue=0,
                                 variable=x9,
                                 command=no3,
                                 font=('Arial', 20))
  checkboxno3.pack()
  checkboxyes3 = Checkbutton(window,
                                  text="yes",
                                  onvalue=1,
                                  offvalue=0,
                                  variable=x10,
                                  command=yes3,
                                  font=('Arial', 20))
  checkboxyes3.pack()
  window.mainloop()
def prolactin_male():
  p3 = float(input("Type your prolactin report\n"))
  if 2 <= p3 <= 18:
    print("you are doing well!")
  else:
    print("I suggest you seeing an Andrologist (Andrologists are the male equivalent of \n"
                  " gynecologists, focusing entirely on male reproductive issues")
    rate2()
def femaleprolactin():
    if (pro.get() == 1):
        print(prolactin_female())
def maleprolactin():
    if (pro2.get() == 1):
        print(prolactin_male())
def gender_prolactin():
    checkbutton = Checkbutton(window,
                          text="female",
                          onvalue=1,
                          offvalue=0,
                          variable=pro,
                          command=femaleprolactin,
                          font=('Arial', 20))
    checkbutton.pack()
    checkbutton2 = Checkbutton(window,
                           text="male",
                           onvalue=1,
                           offvalue=0,
                           variable=pro2,
                           command=maleprolactin,
                           font=('Arial', 20))
    checkbutton2.pack()
    window.mainloop()

#sugar
fast = IntVar()
hours = IntVar()
fast2 = IntVar()
hours2 = IntVar()
def fasting_normal():
    v = float(input("Enter your blood sugar report in mmol/L value\n"))
    if v < 100:
        print("you have a good health!")
    else:
        print("you may be suffering from some problem, thus visiting a doctor will be the best solution for you.\n"
              "here are some specialist in diagnosing your case\n"
              "1- Endocrinologists: specialize in the glands of the endocrine (hormone) system, you may need to see\n "
              "an endocrinologist early on for a more precise diagnosis, or later (if there is any disease)\n"
              "2- Urologist: is a physician who specializes in diseases of the urinary tract. This doctor will help you in discovering any\n"
              "problems in your urine that may be associated with your blood sugar report\n"
              "3- Nephrologists: is a doctor who specializes in taking care of the kidneys. kidney associated with your body fluid concentration\n"
              "therefore, maybe you have some problems with your kidney that affects your blood sugar result")
        rate3()
def hours_normal():
    v2 = float(input("Enter your blood sugar report in mg/dL value\n"))
    if v2 < 140:
        print("you have a good health!")
    else:
        print("you may be suffering from some problem, thus visiting a doctor will be the best solution for you.\n"
              "here are some specialist in diagnosing your case\n"
              "1- Endocrinologists: specialize in the glands of the endocrine (hormone) system, you may need to see\n "
              "an endocrinologist early on for a more precise diagnosis, or later (if there is any disease)\n"
              "2- Urologist: is a physician who specializes in diseases of the urinary tract. This doctor will help you in discovering any\n"
              "problems in your urine that may be associated with your blood sugar report\n"
              "3- Nephrologists: is a doctor who specializes in taking care of the kidneys. kidney associated with your body fluid concentration\n"
              "therefore, maybe you have some problems with your kidney that affects your blood sugar result")
        rate3()

    if (fast2.get() == 1):
        print(fasting_diabetic())
    if (hours2.get() == 1):
        print(hours_diabetic())
def hours_diabetic():
    v3 = float(input("Enter your blood sugar report in mg/dL value\n"))
    if 200 <= v3:
        print("you are doing well!!")
    else:
        print("you may be suffering from some problem, thus visiting a doctor will be the best solution for you.\n"
              "here are some specialist in diagnosing your case\n"
              "1- Endocrinologists: While your diabetes journey likely will begin with a primary care provider, you may need to see an\n "
              "endocrinologist early on for a more precise diagnosis, or later as the disease progresses\n"
              "2- Urologist: is a physician who specializes in diseases of the urinary tract. This doctor will help you in discovering any\n"
              "problems in your urine that may be associated with your blood sugar report\n"
              "3- Nephrologist: care for the kidneys, two bean-shaped organs in the mid-back that remove toxins from the blood.\n "
              "Diabetes is a major risk factor for developing kidney disease\n"
              "4- Podiatrist :These feet specialists can help diabetics manage foot health, which is a common problem. Patients with\n" 
               "poorly controlled blood sugar levels are more likely to develop a condition called diabetic neuropathy\n" 
               "that disrupts how the nerves in the feet and lower legs communicate with the brain.\n"
              "5- Dietitian or Nutritionist: Controlling your diet is a major component of effectively managing diabetes,\n" 
              "and for that reason, you may need to work with a dietitian or nutritionist\n" 
             " to make sure you're getting the right balance of nutrients while tightly controlling your blood sugar levels."
              "Cardiologist : Because they share so many risk factors, heart disease and diabetes often go hand-in-hand, and as\n"
              " a result, many diabetics end up seeing a cardiologist, or \n"
              " heart specialist, at some point during the course of their treatment\n"
              "6- Ophthalmologist: Eye care becomes critical for diabetic patients because over time,\n"
              "elevated blood sugar levels can damage the retina and other delicate structures in the eye\n")
        rate4()
def fasting_diabetic():
    v4 = float(input("Enter your blood sugar report in mg/dL value\n"))
    if 126 <= v4:
        print("you are doing well!!")
    else:
        print("you may be suffering from some problem, thus visiting a doctor will be the best solution for you.\n"
              "here are some specialist in diagnosing your case\n"
              "1- Endocrinologists: While your diabetes journey likely will begin with a primary care provider, you may need to see an\n "
              "endocrinologist early on for a more precise diagnosis, or later as the disease progresses\n"
              "2- Urologist: is a physician who specializes in diseases of the urinary tract. This doctor will help you in discovering any\n"
              "problems in your urine that may be associated with your blood sugar report\n"
              "3- Nephrologist: care for the kidneys, two bean-shaped organs in the mid-back that remove toxins from the blood.\n "
              "Diabetes is a major risk factor for developing kidney disease\n"
              "4- Podiatrist :These feet specialists can help diabetics manage foot health, which is a common problem. Patients with\n" 
               "poorly controlled blood sugar levels are more likely to develop a condition called diabetic neuropathy\n" 
               "that disrupts how the nerves in the feet and lower legs communicate with the brain.\n"
              "5- Dietitian or Nutritionist: Controlling your diet is a major component of effectively managing diabetes,\n" 
              "and for that reason, you may need to work with a dietitian or nutritionist\n" 
             " to make sure you're getting the right balance of nutrients while tightly controlling your blood sugar levels."
              "Cardiologist : Because they share so many risk factors, heart disease and diabetes often go hand-in-hand, and as\n"
              " a result, many diabetics end up seeing a cardiologist, or \n"
              " heart specialist, at some point during the course of their treatment\n"
              "Eye care becomes critical for diabetic patients because over time, "
              "6- Ophthalmologist: elevated blood sugar levels can damage the retina and other delicate structures in the eye\n")
        rate4()
def yesfast():
    if (fast.get() == 1):
            print(fasting_normal())
def yeshours():
    if (hours.get() == 1):
            print(hours_normal())
def yesfast2():
    if (fast2.get() == 1):
            print(fasting_diabetic())
def yeshours2():
    if (hours2.get() == 1):
            print(hours_diabetic())
def no4():
    lable5 = Label(window, text="choose your case when you get this result", fg='blue', font=('Cooper Black', 30))
    lable5.pack()
    checkboxfast = Checkbutton(window,
                                 text="fasting",
                                 onvalue=1,
                                 offvalue=0,
                                 variable=fast,
                                 command=yesfast,
                                 font=('Arial', 20))
    checkboxfast.pack()
    checkboxhours = Checkbutton(window,
                                  text="after 2 hours from eating",
                                  onvalue=1,
                                  offvalue=0,
                                  variable=hours,
                                  command=yeshours,
                                  font=('Arial', 20))
    checkboxhours.pack()
    window.mainloop()
def yes4():
    lable6 = Label(window, text="choose your case when you get this result", fg='blue', font=('Cooper Black', 30))
    lable6.pack()
    checkboxfast = Checkbutton(window,
                               text="fasting",
                               onvalue=1,
                               offvalue=0,
                               variable=fast2,
                               command=yesfast2,
                               font=('Arial', 20))
    checkboxfast.pack()
    checkboxhours = Checkbutton(window,
                                text="after 2 hours from eating",
                                onvalue=1,
                                offvalue=0,
                                variable=hours2,
                                command=yeshours2,
                                font=('Arial', 20))
    checkboxhours.pack()
    window.mainloop()
def which():
    print("Do you have diabetes?")
    d = IntVar()
    d2 = IntVar()
    d3 = IntVar()
    checkboxno3 = Checkbutton(window,
                                 text="no",
                                 onvalue=1,
                                 offvalue=0,
                                 variable=d,
                                 command=no4,
                                 font=('Arial', 20))
    checkboxno3.pack()
    checkboxyes2 = Checkbutton(window,
                                  text="yes",
                                  onvalue=1,
                                  offvalue=0,
                                  variable=d2,
                                  command=yes4,
                                  font=('Arial', 20))
    checkboxyes2.pack()
    checkboxno4 = Checkbutton(window,
                                  text="I don't know",
                                  onvalue=1,
                                  offvalue=0,
                                  variable=d3,
                                  command=no4,
                                  font=('Arial', 20))
    checkboxno4.pack()
    window.mainloop()

#T3
def T3_female():
  tt = float(input("Type your T3 report\n"))
  if 80 < tt < 200:
    print("You're doing well")
  else:
    print("I suggest you to visit an OB/GYN or a gynecologist \n"
              "Gynecologists are doctors who specialize in women's health, \n "
              "with a focus on the female reproductive system.\n"
              "They deal with a wide range of issues, including obstetrics, \n "
              "or pregnancy and childbirth, menstruation and fertility issues, \n "
              "sexually transmitted infections (STIs), hormone disorders, and others. \n")
    rate()
def T3_male():
  tt2 = float(input("Type your T3 report\n"))
  if 80 < tt2 < 200:
    print("You're doing well")
  else:
    print("I suggest you seeing an Andrologist (Andrologists are the male equivalent of \n"
                  " gynecologists, focusing entirely on male reproductive issues ")
    rate2()
def maleT3():
    if (t2.get() == 1):
        print(T3_male())
def femaleT3():
    if (t3.get() == 1):
        print(T3_female())
def gender_t3():
    checkt23 = Checkbutton(window,
                          text="female",
                          onvalue=1,
                          offvalue=0,
                          variable=t,
                          command=femaleT3,
                          font=('Arial', 20))
    checkt23.pack()
    checkt33 = Checkbutton(window,
                           text="male",
                           onvalue=1,
                           offvalue=0,
                           variable=t2,
                           command=maleT3,
                           font=('Arial', 20))
    checkt33.pack()
    window.mainloop()

#T4
def T4_female():
  f = float(input("Type your T4 report\n"))
  if 5 < f < 12:
    print("You're doing well")
  else:
    print("I suggest you to visit an OB/GYN or a gynecologist \n"
              "Gynecologists are doctors who specialize in women's health, \n "
              "with a focus on the female reproductive system.\n"
              "They deal with a wide range of issues, including obstetrics, \n "
              "or pregnancy and childbirth, menstruation and fertility issues, \n "
              "sexually transmitted infections (STIs), hormone disorders, and others. \n")
    rate()
def T4_male():
  m = float(input("type your T4 report\n"))
  if 5 < m < 12:
    print("You're doing well")
  else:
    print("I suggest you seeing an Andrologist (Andrologists are the male equivalent of \n"
                  " gynecologists, focusing entirely on male reproductive issues ")
    rate2()
def femaleT4():
    if (tt3.get() == 1):
        print(T4_female())
def maleT4():
    if (tt4.get() == 1):
        print(T4_male())
def gender_t4():
    checkbuttont4 = Checkbutton(window,
                          text="female",
                          onvalue=1,
                          offvalue=0,
                          variable=tt3,
                          command=femaleT4,
                          font=('Arial', 20))
    checkbuttont4.pack()
    checkbuttont42 = Checkbutton(window,
                           text="male",
                           onvalue=1,
                           offvalue=0,
                           variable=tt4,
                           command=maleT4,
                           font=('Arial', 20))
    checkbuttont42.pack()
    window.mainloop()

#Tsh
def Tsh_male():
  m3 = float(input("type your T4 report\n"))
  if 0.5 < m3 < 5:
    print("You're doing well")
  else:
    print("I suggest you seeing an Andrologist (Andrologists are the male equivalent of \n"
                  " gynecologists, focusing entirely on male reproductive issues ")
    rate2()
def Tsh_female():
  m4 = float(input("Type your T4 report\n"))
  if 5 < m4 < 12:
    print("You're doing well")
  else:
    print("I suggest you to visit an OB/GYN or a gynecologist \n"
              "Gynecologists are doctors who specialize in women's health, \n "
              "with a focus on the female reproductive system.\n"
              "They deal with a wide range of issues, including obstetrics, \n "
              "or pregnancy and childbirth, menstruation and fertility issues, \n "
              "sexually transmitted infections (STIs), hormone disorders, and others. \n")
    rate()
def maletsh():
    if (ss.get() == 1):
        print(Tsh_male())
def femaletsh():
    if (s.get() == 1):
        print(Tsh_female())
def gender_tsh():
    checkbuttontsh = Checkbutton(window,
                          text="female",
                          onvalue=1,
                          offvalue=0,
                          variable=s,
                          command=femaletsh,
                          font=('Arial', 20))
    checkbuttontsh.pack()
    checkbuttontsh = Checkbutton(window,
                           text="male",
                           onvalue=1,
                           offvalue=0,
                           variable=ss,
                           command=maletsh,
                           font=('Arial', 20))
    checkbuttontsh2.pack()
    window.mainloop()

t = IntVar()
t2 = IntVar()
tt3 = IntVar()
tt4 = IntVar()
s = IntVar()
ss = IntVar()
x = IntVar()
x2 = IntVar()
r = IntVar()
r2 = IntVar()
pro = IntVar()
pro2 = IntVar()
g = IntVar()
g2 = IntVar()
t3 = IntVar()
t4 = IntVar()
tsh = IntVar()
sugar = IntVar()


checkfsh = Checkbutton(window,
                          text="FSH",
                          onvalue=1,
                          offvalue=0,
                          variable=g,
                          command=gender_fsh,
                          font=('Arial', 26))
checkfsh.pack()
checkprolactin = Checkbutton(window,
                           text="Prolactin",
                           onvalue=1,
                           offvalue=0,
                           variable=g2,
                           command=gender_prolactin,
                           font=('Arial', 26))
checkprolactin.pack()
checkt3 = Checkbutton(window,
                           text="T3",
                           onvalue=1,
                           offvalue=0,
                           variable=t3,
                           command=gender_t3,
                           font=('Arial', 26))
checkt3.pack()
checkt4 = Checkbutton(window,
                           text="T4",
                           onvalue=1,
                           offvalue=0,
                           variable=t4,
                           command=gender_t4,
                           font=('Arial', 26))
checkt4.pack()
checktsh = Checkbutton(window,
                           text="TSH",
                           onvalue=1,
                           offvalue=0,
                           variable=tsh,
                           command=gender_tsh,
                           font=('Arial', 26))
checktsh.pack()
checksugar = Checkbutton(window,
                           text="Blood sugar",
                           onvalue=1,
                           offvalue=0,
                           variable=sugar,
                           command=which,
                           font=('Arial', 26))
checksugar.pack()
window.mainloop()