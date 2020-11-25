#SRP's A.I. VIBRIS
#This Is V.I.B.R.I.S. 'Mark - I'
#UsePyCompiler
#ContributeSuggestions
#FLOSS
from datetime import date
import time as timex
import datetime
import webbrowser
htime=datetime.datetime.now().strftime("%H")
print("Hello User!")
timex.sleep(2.5)
intro="Hey, I am V.I.B.R.I.S., a micro-AI program made by Mr. SRP.\nMy neural framework is made using Python. I am a text-based virtual assistant version - \'Mark -1\'"
about="\nV.I.B.R.I.S. stands for \"Very Intelligent But Recyclonic Interaction System\".\nThese acronym was made by Mr.SRP in 2020 when he ws building me.\nThat's all about me."
print(intro)
timex.sleep(2)
print("That is how I give my introduction.")
timex.sleep(2.5)
print("Loading set-up ...")
timex.sleep(2)
name=str(input("First of all, Please let me know your name : "))
timex.sleep(0.5)
age=int(input("Okay, tell me your age : "))
gen=input("Lastly, enter your gender\n(\'m\' for male and \'f\' for female) : ")
date=date.today()
time=datetime.datetime.now().strftime("%H:%M")
print("Alright", name, ", Intializing command in-take and response systems ...")
timex.sleep(3)
print("Okay, we are all set. here is a guide.\nYou should not use uppercase and try to type in simple manner. Some commands are in the directory. You can add your commands and set elif")
timex.sleep(0.5)
if (gen=="m") :
    resp=" sir!"
    gender="male"
elif (gen=="f") :
    resp=" mam!"
    gender="female"
if (age>=18) :
    vote="\nYou are eligible to vote."
else :
    vote="\nYou aren't eligible to vote."
pod=int(2)
while (pod>0) :
    #CmdDirectory
    inp=input("Enter Your command! : ")
    a="what is my name"
    b="tell my name"
    c="show my name"
    d="tell my age"
    e="what is my age"
    f="show my age"
    g="tell something about me"
    h="about me"
    i="tell about me"
    j="what is the date"
    k="what is today's date"
    l="show me the date"
    m="what is the time"
    n="tell me the time"
    o="what is on the clock"
    p="show me the time"
    q="who are you"
    r="about you"
    s="about V.I.B.R.I.S."
    t="about Vibris"
    u="about vibris"
    v="perform a calculation"
    w="do a calculation"
    x="calculation"
    y="calculator"
    z="perform a calc"
    a1="do a calc"
    a2="make a calculation"   
    a3="goodbye"
    a4="bye"
    a5="end"
    a6="terminate"
    a7="open google"
    a8="load google"
    a9="open youtube"
    a10="load youtube"
    b1="open a website"
    b2="browse a website"
    b3="load a website"
    if (inp==a):
        print("your name is ", name, resp)
    elif (inp==b):
        print("your name is ", name, resp)
    elif (inp==c):
        print("your name is ", name, resp)
    elif (inp==d):
        print("It is", age, resp)
    elif (inp==e):
        print("It is", age, resp)
    elif (inp==f):
        print("It is", age, resp)
    elif (inp==g):
        print("Your name is " , name, "Your gender is ", gender, "\n Your age is " , age, vote, "\n You are currently using me and I'm feeling good. :)")
    elif (inp==h):
        print("Your name is " , name, "Your gender is ", gender, "\n Your age is " , age, vote, "\n You are currently using me and I'm feeling good. :)")
    elif (inp==i):
        print("Your name is " , name, "Your gender is ", gender, "\n Your age is " , age, vote, "\n You are currently using me and I'm feeling good. :)")
    elif (inp==j):
        print("Today's date is ", date, resp)
    elif (inp==k):
        print("Today's date is ", date, resp)
    elif (inp==l):
        print("Today's date is ", date, resp)
    elif (inp==m):
        print("Right now, it is ", time, resp)
    elif (inp==n):
        print("Right now, it is ", time, resp)
    elif (inp==o):
        print("Right now, it is ", time, resp)
    elif (inp==p):
        print("Right now, it is ", time, resp)
    elif (inp==q):
        print(intro, about)
    elif (inp==r):
        print(intro, about)
    elif (inp==s):
        print(intro, about)
    elif (inp==t):
        print(intro, about)
    elif (inp==u):
        print(intro, about)
    elif (inp==v) :
        print("Usage -\n1) \'+\' for addition\n2) \'-\' for subtraction\n3) \'*\' for multiplication\n4) \'/\' for division\n5) All operators are based on python. You can also use braces.")
        timex.sleep(1)
        calc=float(input("  Enter your calculation : "))
        print("You answer is :- ", calc)
    elif (inp==w) :
        print("Usage -\n1) \'+\' for addition\n2) \'-\' for subtraction\n3) \'*\' for multiplication\n4) \'/\' for division\n5) All operators are based on python. You can also use braces.")
        timex.sleep(1)
        calc=float(input("  Enter your calculation : "))
        print("You answer is :- ", calc)
    elif (inp==x) :
        print("Usage -\n1) \'+\' for addition\n2) \'-\' for subtraction\n3) \'*\' for multiplication\n4) \'/\' for division\n5) All operators are based on python. You can also use braces.")
        timex.sleep(1)
        calc=float(input("  Enter your calculation : "))
        print("You answer is :- ", calc)
    elif (inp==y) :
        print("Usage -\n1) \'+\' for addition\n2) \'-\' for subtraction\n3) \'*\' for multiplication\n4) \'/\' for division\n5) All operators are based on python. You can also use braces.")
        timex.sleep(1)
        calc=float(input("  Enter your calculation : "))
        print("You answer is :- ", calc)
    elif (inp==z) :
        print("Usage -\n1) \'+\' for addition\n2) \'-\' for subtraction\n3) \'*\' for multiplication\n4) \'/\' for division\n5) All operators are based on python. You can also use braces.")
        timex.sleep(1)
        calc=float(input("  Enter your calculation : "))
        print("You answer is :- ", calc)
    elif (inp==a1) :
        print("Usage -\n1) \'+\' for addition\n2) \'-\' for subtraction\n3) \'*\' for multiplication\n4) \'/\' for division\n5) All operators are based on python. You can also use braces.")
        timex.sleep(1)
        calc=float(input("  Enter your calculation : "))
        print("You answer is :- ", calc)
    elif (inp==a2) :
        print("Usage -\n1) \'+\' for addition\n2) \'-\' for subtraction\n3) \'*\' for multiplication\n) \'/\' for division\n5) All operators are based on python. You can also use braces.")
        timex.sleep(1)
        calc=float(input("  Enter your calculation : "))
        print("You answer is :- ", calc)
    elif (inp==a3) :
        pod=int(0)
        timex.sleep(1)
        print("Okay, bye! Thanks for using me.")
    elif (inp==a4) :
        pod=int(0)
        timex.sleep(1)
        print("Okay, bye! Thanks for using me.")
    elif (inp==a5) :
        pod=int(0)
        timex.sleep(1)
        print("Okay, bye! Thanks for using me.")
    elif (inp==a6) :
        pod=int(0)
        timex.sleep(1)
        print("Okay, bye! Thanks for using me.")
    elif (inp==a7) :
        print("Here you go.")
        timex.sleep(1)
        webbrowser.open('https://www.google.co.in', new=2)
    elif (inp==a8) :
        print("Get. Set. Go.")
        timex.sleep(1)
        webbrowser.open('https://www.google.co.in', new=2)
    elif (inp==a9) :
        print("Here you go.")
        timex.sleep(1)
        webbrowser.open('https://www.youtube.com', new=2)
    elif (inp==a10) :
        print("Get. Set. Go.")
        timex.sleep(1)
        webbrowser.open('https://www.youtube.com', new=2)
    elif (inp==b1) :
        url=input("Enter your desired URL/Web Address : ")
        print("Here you go.")
        timex.sleep(1)
        webbrowser.open(url, new=2)
    elif (inp==b2) :
        url=input("Enter your desired URL/Web Address : ")
        print("Here you go.")
        timex.sleep(1)
        webbrowser.open(url, new=2)
    elif (inp==b3) :
        url=input("Enter your desired URL/Web Address : ")
        print("Here you go.")
        timex.sleep(1)
        webbrowser.open(url, new=2)
    else :
        print("Sorry, something went wrong, I can't understand. Maybe there is a typing error or beyond the scope of my working.")