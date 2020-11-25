"""
# SRP's AI V.I.B.R.I.S. Mark - III

To intsall pyttsx3 module, run 'pip install -U pyttsx3==2.71' in Command Prompt or Power Shell.

If pip not working, follow steps from https://youtu.be/zYdHr-LxsJ0/

Do check the information from code.maxez.ml for compatibility and features.
"""
import pyttsx3
import datetime
import time as timex
import random
import webbrowser
import os
def guider():
    guide="You can try - 'time', 'date', 'timer', 'wish or greet', 'dice roll',\n'coin toss', 'google, facebook, youtube, any site browsing or surfing','about you or about me', 'open app', 'if said stupid then apologises','make me speak what you want', 'bye for shutdown'\nYou can ask or talk for these in any of your way.\nExample- 'What is the time' or'show me the time' anything will work for all"
    speak(guide)
    print(guide)
def speak(text):
    engine=pyttsx3.init("sapi5")
    voiceover=engine.getProperty("voices")
    engine.setProperty("voice", voiceover[1].id)
    engine.setProperty("rate", 145)
    engine.say(text)
    engine.runAndWait()
def about_vibris():
    intro="I am VIBRIS, a micro-AI program made by Mr. SRP.\nMy script is made using Python. I am a text-based virtual assistant version - \'Mark III\'"
    speak(intro)
    print(intro)
    about="\nVIBRIS stands for \"Very Intelligent But Recyclic Interaction System\".\nThese acronym was made by Mr.SRP in 2020 when he was building me.\nThat's all about me."
    speak(about)
    print(about)
def greet():
    htimex=int(datetime.datetime.now().hour)
    if (htimex >= 0) and (htimex < 12):
        speak("Good Morning Boss!")
        print("Good Morning Boss!")
    elif (htimex >= 12) and (htimex < 17):
        speak("Good Afternoon Boss!")
        print("Good Afternoon Boss!")
    else:
        speak("Good Evening Boss!")
        print("Good Evening Boss!")
def date():
    dt_d=datetime.datetime.now().strftime("%d of")
    dt_m=int(datetime.datetime.now().strftime("%m"))
    dt_y=datetime.datetime.now().strftime("%Y")
    if (dt_m == 1):
        dt_M="January"
    elif (dt_m == 2):
        dt_M="February"
    elif (dt_m == 3):
        dt_M="March"
    elif (dt_m == 4):
        dt_M="April"
    elif (dt_m == 5):
        dt_M="May"
    elif (dt_m == 6):
        dt_M="June"
    elif (dt_m == 7):
        dt_M="July"
    elif (dt_m == 8):
        dt_M="August"
    elif (dt_m == 9):
        dt_M="September"
    elif (dt_m == 10):
        dt_M="October"
    elif (dt_m == 11):
        dt_M="November"
    else:
        dt_M="December"
    dt=dt_d,dt_M,",",dt_y
    dtimex1="Today it is"
    dtimex2="This day it is"
    dtimex3="Boss, the date is"
    dtimex4="Currently it is"
    dtimex=random.choice([dtimex1, dtimex2, dtimex3, dtimex4])
    Dtimex=dtimex, *dt
    speak(Dtimex)
    print(*Dtimex)
def time():
    timex=datetime.datetime.now().strftime("%H : %M")
    tmx1="Right now it is",timex
    tmx2="Currently it is",timex
    tmx3="At this point of time it is",timex
    tmx4="Now it is clocking",timex
    tmx5="Boss, the time is"
    TMX=random.choice([tmx1, tmx2, tmx3, tmx4, tmx5])
    speak(TMX)
    print(*TMX)
def web():
    ini_web1="Initialising URL Browsing Protocol\nyou can set the browsing protocol"
    ini_web2="Loading URL Browsing Protocol\nbetter to specify browsing protocol"
    ini_web=random.choice([ini_web1, ini_web2])
    speak(ini_web)
    print(ini_web)
    timex.sleep(1)
    web1="Please enter the URL to be browsed\n>>> "
    web2="Put-in the URL for surfing\n>>> "
    web3="What URL you want to browse ?\n>>> "
    web4="Boss, fill the URL to be visited\n>>> "
    web5="Provide the URL below\n>>> "
    WEB=random.choice([web1, web2, web3, web4, web5])
    speak(WEB)
    url=input(WEB)
    timex.sleep(0.5)
    web5="Yes boss, opening..."
    web6="As you wish boss..."
    web7="Okay, fire on the screen..."
    web8="Here you go"
    web9="I'm on it!..."
    web10="Loading it..."
    web11="Opening it..."
    web12=random.choice([web5, web6, web7, web8, web9, web10, web11])
    speak(web12)
    print(web12)
    webbrowser.open(url, new=2)
def sep_web(url):
    web5="Yes boss, opening..."
    web6="As you wish boss..."
    web7="Okay, fire on the screen..."
    web8="Here you go"
    web9="I'm on it!..."
    web10="Loading it..."
    web11="Opening it..."
    web12=random.choice([web5, web6, web7, web8, web9, web10, web11])
    speak(web12)
    print(web12)
    webbrowser.open(url, new=2)
def dice() :
    dice_ini1="Initialising Virtual Dice Roll Protocol..."
    dice_ini2="Loading Virtual Dice Roll Protocol..."
    dice_ini=random.choice([dice_ini1, dice_ini2])
    speak(dice_ini)
    print(dice_ini)
    dicenote1="Yes boss, rolling a dice..."
    dicenote2="Okay boss, rolling a dice..."
    dicenote3="Alright boss, dice's bein' rolled..."
    dicenote4="As you wish, rolling dice..."
    DICENOTE=random.choice([dicenote1, dicenote2, dicenote3, dicenote4])
    speak(DICENOTE)
    print(DICENOTE)
    timex.sleep(1)
    diceout=random.choice(["1", "2", "3", "4", "5", "6"])
    diceout1="On the top, it is",diceout
    diceout2="Boss, The outcome is",diceout
    diceout3="Boss, the result is",diceout
    diceout4="Boss, got",diceout
    DICEOUT=random.choice([diceout1, diceout2, diceout3])
    speak(DICEOUT)
    print(*DICEOUT)
def coin() :
    coin_ini1="Initialising Virtual Coin Toss Protocol..."
    coin_ini2="Loading Virtual Coin Toss Protocol..."
    coin_ini=random.choice([coin_ini1, coin_ini2])
    speak(coin_ini)
    print(coin_ini)
    coinnote1="Yes boss, tossing a coin..."
    coinnote2="Okay boss, tossing a coin..."
    coinnote3="Alright boss, coin is being tossed..."
    coinnote4="As you wish, getting coin tossed..."
    COINNOTE=random.choice([coinnote1, coinnote2, coinnote3, coinnote4])
    speak(COINNOTE)
    print(COINNOTE)
    timex.sleep(1)
    coinout=random.choice(["Heads", "Tails"])
    coinout1="On the top, it is",coinout
    coinout2="Boss, the outcome is",coinout
    coinout3="Boss, the result is",coinout
    coinout4="Boss, got",coinout
    COINOUT=random.choice([coinout1, coinout2, coinout3, coinout4])
    speak(COINOUT)
    print(*COINOUT)
def okay() :
    ok1="I'm all good boss!"
    ok2="I'm enjoying by assisting you boss!"
    ok3="I'm finding myself functioning with normal parameters!"
    ok4="Yaa Boss! All good!"
    ok5="Boss, I'm always in joy!"
    ok6="I always boot into joy!"
    ok=random.choice([ok1, ok2, ok3, ok4, ok5, ok6])
    speak(ok)
    print(ok)
def timer() :
    timer_ini1="Initialising Timer Protocol, shows time left on screen..."
    timer_ini2="Loading Timer Protocol, shows time left on screen..."
    timer_ini=random.choice([timer_ini1, timer_ini2])
    speak(timer_ini)
    print(timer_ini)
    term_1="Put in the number of seconds\n>>> "
    term_2="Insert the number of seconds\n>>> "
    term_3="Provide time in seconds for timer\n>>> "
    term_4=random.choice([term_1, term_2, term_3])
    speak(term_4)
    term=int(input(term_4))
    timex.sleep(2)
    speak("Get.")
    print("Get.")
    speak("Set.")
    print("Set.")
    speak("Go!")
    print("Go.")
    while (term != 0):
        print(term)
        term -= 1
        timex.sleep(1)
    speak("Time's Up! Time's Up! Time's Up!")
    print("Time's up! "*3)
def apologise():
    apl1="I am sorry boss! It is due to my technical disability. Hope you understand."
    apl2="Boss, I apologise for my technical error. My developer is trying to improve me."
    apl3="Please forgive me. SRP will try to improve me. Can contact him."
    apl=random.choice([apl1, apl2, apl3])
    speak(apl)
    print(apl)
def off():
    off1="Okay, boss. I appreciate your time for me. Shutting myself down..."
    off2="Alright boss. As you wish! Terminating VIBRIS program..."
    off3="Thanks for your time boss. Quitting VIBRIS program..."
    OFF=random.choice([off1, off2, off3])
    speak(OFF)
    print(OFF)
def say():
    speak("what should I speak boss ?")
    read=input("What should I speak\n>>> ")
    speak(read)
def error():
    err1="Oh no, an error occured! Maybe there's a typing mistake or beyond my scope of working."
    err2="Oops, something went wrong. Maybe there's a typing mistake or beyond my scope of working."
    err3="Oh! There's an error. There can be typing mistake or far by my ability, or both."
    err4="Sorry boss, error raised. Probable chances of typing mistake or uncompatible work, or both."
    err=random.choice([err1, err4, err3, err2])
    speak(err)
    print(err)
def AI_Engine():
    speak("Initialising Set-Up Protocol...")
    print("Initialising Set-Up Protocol...")
    speak("First of all, Please let me know your name")
    name=str(input("First of all, Please let me know your name\n>>> "))
    speak("So now tell me your age")
    age=int(input("So now tell me your age\n>>> "))
    if (age > 103) :
        speak("Sorry, I'm not a fool, restarting A.I.")
        print("Sorry, I'm not a fool, restarting AI")
        timex.sleep(1)
        AI_Engine()
    else:
        speak("Now finally, Put-in your gender")
        gen=input("Finally, Enter your Gender\n>>> ")
        if ("f" in gen) or ("female" in gen) or ("F" in gen) or ("Female" in gen) or ("FEMALE" in gen) or ("Femaline" in gen) or ("femaline" in gen) or ("FEMALINE" in gen):
            gender="female"
        elif ("m" in gen) or ("male" in gen) or ("M" in gen) or ("Male" in gen) or ("MALE" in gen) or ("masculine" in gen) or ("Masculine" in gen) or ("MASCULINE" in gen):
            gender="male"
        else:
            gender="unknown"
        if (age >= 18):
            vote="You are eligible to vote."
        else:
            vote="You are not eligible to vote."
        def about_usr():
            abt_usr1="You are my boss whose name is",name,"You are",age,"years old and thus",vote,"Your gender is",gender,
            abt_usr2="Your name is",name,"Your age is",age,"So,",vote,"Lastly, your gender is",gender,
            abt_usr3="From Set-Up Protocol, Your name is",name,"Your age is",age,"So,",vote,"Lastly, your gender is",gender,
            abt_USR=random.choice([abt_usr1, abt_usr2, abt_usr3])
            speak(abt_USR)
            print(*abt_USR)
        speak("Insert the title of your most used app to recall it")
        app_title=input("Insert the title of your most used app to recall it\n>>> ")
        app_title=app_title.lower()
        speak("Insert the path of your most used application")
        app_path=input("Insert the path of shortcut of your most used application\n>>> ")
        lx=name,", Now Initialising Command In-Take And Response Systems"
        speak(lx)
        print("Now Initialising Command In-Take And Response Systems...")
        timex.sleep(1)
        def app():
            app_inf1="Yes boss, loading..."
            app_inf2="As you wish boss, opening..."
            app_inf3="Alright, loading..."
            app_inf=random.choice([app_inf1, app_inf2, app_inf3])
            speak(app_inf)
            print(app_inf)
            os.startfile(app_path)
        while (True):
            cmd_a=1
            cmd_b=2
            cmd_c=3
            cmd_d=4
            cmd_e=5
            cmd_x=int(random.choice([cmd_a, cmd_b, cmd_c, cmd_d, cmd_e]))
            if (cmd_x == 1):
                speak("How can I help you boss ?")
                cmd=input("How can I help you boss ? (Type 'guide' for some guide)\n>>> ")
            elif (cmd_x == 2):
                speak("Gimme your command boss")
                cmd=input("Gimme your command boss (Type 'guide' for some guide)\n>>> ")
            elif (cmd_x == 3):
                speak("Boss, what you are looking for ?")
                cmd=input("Boss, what you are looking for ? (Type 'guide' for some guide)\n>>> ")
            elif (cmd_x == 4):
                speak("What's your command for me boss ?")
                cmd=input("What's your command for me boss ? (Type 'guide' for some guide)\n>>> ")
            else:
                speak("Enter your command boss")
                cmd=input("Enter your command boss (Type 'guide' for some guide)\n>>> ")
            cmd=cmd.lower()
            if ("about" in cmd) and ("me" in cmd or "boss" in cmd):
                about_usr()
            elif ("about" in cmd or "who" in cmd or "what" in cmd) and ("you" in cmd or "vibris" in cmd):
                about_vibris()
            elif ("about" in cmd) and ("me" in cmd or "boss" in cmd):
                about_usr()
            elif ("who" in cmd) and (name in cmd):
                about_usr()
            elif ("date" in cmd) or ("day" in cmd):
                date()
            elif ("timer" in cmd):
                timer()
            elif ("time" in cmd) or ("clock" in cmd):
                time()
            elif ("guide" in cmd) or ("help" in cmd):
                guider()
            elif ("speak" in cmd) or ("say" in cmd):
                say()
            elif ("wish" in cmd) or ("greet" in cmd):
                greet()
            elif ("google" in cmd):
                sep_web("https://www.google.co.in/")
            elif ("facebook" in cmd) or ("fb" in cmd):
                sep_web("https://www.facebook.com/")
            elif ("youtube" in cmd) or ("yt" in cmd):
                sep_web("https://www.youtube.com/")
            elif ("maxez" in cmd):
                sep_web("http://code.maxez.ml")
            elif ("surf" in cmd) or ("browse" in cmd) or ("internet" in cmd):
                web()
            elif ("how" in cmd or "ok" in cmd) and ("you" in cmd):
                okay()
            elif ("dice" in cmd):
                dice()
            elif ("coin" in cmd) or ("toss" in cmd):
                coin()
            elif ("you" in cmd) and ("stupid" in cmd or "idiot" in cmd or "dumb" in cmd):
                apologise()
            elif (app_title in cmd):
                app()
            elif ("bye" in cmd) or ("shut" in cmd and "down" in cmd):
                off()
                break
            else:
                error()
def switch(): 
    power=input("Do you want to activate V.I.B.R.I.S. ?\n>>> ")
    if ("y" in power) or ("Y" in power) or ("yes" in power) or ("YES" in power) or ("Yes" in power) or ("Yep" in power) or ("yep" in power) or ("YEP" in power) :
        print("+------------------------------------------------+\n|          ___    ____     ____     ___   ____   |\n|\      /   |    |    \   |    \     |   /       |\n| \    /    |    |____/   |____/     |   \____   |\n|  \  /     |    |    \   |    \     |        \  |\n|   \/  *  _|_ * |____/ * |     \ * _|_ * ____/ *|\n|                                                |\n+------------------------------------------------+")
        timex.sleep(3)
        print("Checking Control Services    ...     [Checked]")
        speak("Warning!\nDon't type anything wherever input is not given, it breaks the program\nIf asked integer value, then only add integer value.")
        print("Warning!\nDon't type anything wherever input is not given, it breaks the program\nIf asked integer value, then only add integer value.")
        speak("Activating A.I. Engine...")
        print("Activating A.I. Engine...")
        timex.sleep(1)
        greet()
        intro="I am VIBRIS, a micro-AI program made by Mr. SRP.\nMy script is made using Python. I am a text-based virtual assistant version - \'Mark III\'"
        speak(intro)
        print(intro)
        speak("That is how I give my introduction.")
        print("That is how I give my introduction.")
        timex.sleep(2.5)
        AI_Engine()
    elif ("n" in power) or ("N" in power) or ("no" in power) or ("No" in power) or ("NO" in power) or ("Nope" in power) or ("nope" in power) or ("NOPE" in power) :
        exit
    else :
        switch()
switch()