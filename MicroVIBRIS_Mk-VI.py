"""
@doctype: python
@encoding: UTF-8
@author: SRP

SRP's Desktop Assistant V.I.B.R.I.S. Mark - VI Volume - 1

Some modules are to be installed by writing this line in PowerShell or Command Prompt-
-->   pip install -U speechRecognition, pyttsx3, pyaudio, pywin32, wikipedia, wolframalpha, playsound, psutil

If pip not working, follow steps from https://youtu.be/zYdHr-LxsJ0/

If error installing pyaudio, download its .whl file by searching pyaudio.whl, go to dowloaded directory, open terminal and try -->   pip install some_sort_of_name.whl

For Wolfram Alpha functions, get your own API from their website. Else, it will not work.

Do check the information from code.maxez.ml for compatibility and features.
#TheSRP
"""
import datetime
import random
from time import sleep
import speech_recognition
import pyttsx3
import os
import subprocess
import webbrowser
import playsound
import wikipedia
import wolframalpha
import smtplib
import psutil
import requests
name="SRP"
birthday="31 of December"
dob="31st of December 2004"
def me(res):
    if (res=="name"):
        speak(name)
        print(name)
    elif (res=="dob"):
        speak(dob)
        print(dob)
def apologise():
    apl1="Sorry for my technical disability. Hope you understand."
    apl2="I apologise for my technical error. You got to improve it."
    apl3="Forgive me, I hope someday I'd be the best!"
    apl=random.choice([apl1, apl2, apl3])
    speak(apl)
    print(apl)
def about(char):
    if (char=="vibris"):
        statement="Hey, I'm VIBRIS, the digital desktop assistance program made by and built for SRP. I love him 3000.\nVIBRIS stands for Virtual Intelligence Built for Rigid Interaction System, currently workinng as version - 'Mark - V'"
        speak(statement)
        print(statement)
    elif (char=="srp"):
        statement="SRP is my sire who made me and always feels that I'm his companion."
        speak(statement)
        print(statement)
def speak(text):
    engine=pyttsx3.init("sapi5")
    schema=engine.getProperty("voices")
    engine.setProperty("voice", schema[0].id)
    engine.setProperty("rate", 143)
    engine.say(text)
    engine.runAndWait()
def greet():
    htime=datetime.datetime.now().hour
    dtx=datetime.datetime.now().strftime("%dth of %B")
    if (htime >= 0) and (htime < 12):
        speak("Good Morning Sir!")
        print("Good Morning Sir!")
    elif (htime >= 12) and (htime < 17):
        speak("Good Afternoon Sir!")
        print("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")
        print("Good Evening Sir!")
    if (birthday == dtx):
        speak("Wish you a very Happy Birthday sir!")
        print("Wish you a very Happy Birthday sir!")
def okay():
    ok1="I'm all good sir!"
    ok2="I'm enjoying by assisting you sir!"
    ok3="I'm finding myself functioning with normal parameters!"
    ok4="Yes sir! All good!"
    ok5="sir, I'm always in joy!"
    ok6="I always boot into joy!"
    ok=random.choice([ok1, ok2, ok3, ok4, ok5, ok6])
    speak(ok)
    print(ok)
def say():
    speak("what should I speak sir?")
    read=input("What should I speak\n>>> ")
    speak(read)
def dt_time(func):
    date=datetime.datetime.now().strftime("%d of %B %Y")
    time=datetime.datetime.now().strftime("%H Hours and %M Minutes")
    if (func=="dtx"):
        dt_txt1="Sir, today it is " + date
        dt_txt2="This day, it is " + date
        dt_txt3="Sir, it is " + date
        dt_txt4="It is " + date
        dt_txt=random.choice([dt_txt1, dt_txt2, dt_txt3, dt_txt4])
        speak(dt_txt)
        print(dt_txt)
    elif (func=="tx"):
        tm_txt1="Sir, currently it is " + time
        tm_txt2="Right now it is " + time
        tm_txt3="On the clock it is " + time
        tm_txt4="Currently it is " + time
        tm_txt5="Now it's clocking " + time
        tm_txt=random.choice([tm_txt1, tm_txt2, tm_txt3, tm_txt4, tm_txt5])
        speak(tm_txt)
        print(tm_txt)
def web():
    ini_web1="Initialising Browsing mode\nSpecify the protocol."
    ini_web2="Loading URL Browsing Protocol\nBetter to specify browsing protocol."
    ini_web=random.choice([ini_web1, ini_web2])
    speak(ini_web)
    print(ini_web)
    web1="Enter the URL to be browsed\n>>> "
    web2="Put-in the URL for surfing\n>>> "
    web3="What URL you want to browse ?\n>>> "
    web4="fill the URL to be visited\n>>> "
    web5="Provide the URL below\n>>> "
    WEB=random.choice([web1, web2, web3, web4, web5])
    speak(WEB)
    url=input(WEB)
    web5="Opening..."
    web6="As you wish..."
    web7="Fire on the screen..."
    web8="Here you go"
    web9="I'm on it!..."
    web10="Loading it..."
    web11="Opening it..."
    web12=random.choice([web5, web6, web7, web8, web9, web10, web11])
    speak(web12)
    print(web12)
    try:
        webbrowser.open(url, new=2)
    except Exception as web_err:
        speak("Sorry Sir, my system is unable to launch the site.")
        print("Sorry Sir, my system is unable to launch the site.")
def sep_web(url):
    web5="Opening..."
    web6="As you wish..."
    web7="Fire on the screen..."
    web8="Here you go"
    web9="I'm on it!..."
    web10="Loading it..."
    web11="Opening it..."
    web12=random.choice([web5, web6, web7, web8, web9, web10, web11])
    speak(web12)
    print(web12)
    try:
        webbrowser.open(url, new=2)
    except Exception as web_err:
        speak("Sorry Sir, my system is unable to launch the site.")
        print("Sorry Sir, my system is unable to launch the site.")
def dice():
    dicenote1="Yes Sir rolling a dice..."
    dicenote2="Okay rolling a dice..."
    dicenote3="Dice's bein' rolled..."
    dicenote4="As you wish rolling dice..."
    DICENOTE=random.choice([dicenote1, dicenote2, dicenote3, dicenote4])
    speak(DICENOTE)
    print(DICENOTE)
    sleep(1)
    diceout=random.choice(["1", "2", "3", "4", "5", "6"])
    diceout1="On the top, it is" + diceout
    diceout2="The outcome is" + diceout
    diceout3="The result is" + diceout
    diceout4="Sir got" + diceout
    DICEOUT=random.choice([diceout1, diceout2, diceout3])
    speak(DICEOUT)
    print(DICEOUT)
def coin():
    coinnote1="Yes Sir tossing a coin..."
    coinnote2="Okay tossing a coin..."
    coinnote3="Alright coin is being tossed..."
    coinnote4="As you wish getting coin tossed..."
    COINNOTE=random.choice([coinnote1, coinnote2, coinnote3, coinnote4])
    speak(COINNOTE)
    print(COINNOTE)
    sleep(1)
    coinout=random.choice(["Heads", "Tails"])
    coinout1="On the top, it is" + coinout
    coinout2="The outcome is" + coinout
    coinout3="Tthe result is" + coinout
    coinout4="Sir got" + coinout
    COINOUT=random.choice([coinout1, coinout2, coinout3, coinout4])
    speak(COINOUT)
    print(COINOUT)
def app_open(app_name):
    vs_code="C:\\Users\\srpx3\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    browser="C:\\Program Files (x86)\\Google\\Chrome\\Application"
    python="C:\\Users\\srpx3\\AppData\\Local\\Programs\\Python\\Python38-32\\pythonw.exe"
    calculator="C:\\VIBRIS\\shortcuts\\calculator.lnk"
    camtasia="C:\\VIBRIS\\shortcuts\\camtasia.lnk"
    camtasiarec="C:\\VIBRIS\\shortcuts\\camtasiarec.lnk"
    msmail="C:\\VIBRIS\\shortcuts\\mail.lnk"
    groovemusic="C:\\VIBRIS\\shortcuts\\music.lnk"
    saavn="C:\\VIBRIS\\shortcuts\\saavn.lnk"
    news="C:\\VIBRIS\\shortcuts\\news.lnk"
    powershell="C:\\VIBRIS\\shortcuts\\powershell.lnk"
    store="C:\\VIBRIS\\shortcuts\\store.lnk"
    weather="C:\\VIBRIS\\shortcuts\\weather.lnk"
    whatsapp="C:\\VIBRIS\\shortcuts\\whatsapp.lnk"
    wordpad="C:\\VIBRIS\\shortcuts\\wordpad.lnk"
    word="C:\VIBRIS\shortcuts\word.lnk"
    excel="C:\VIBRIS\shortcuts\excel.lnk"
    task_manager="C:\\VIBRIS\\shortcuts\\task_manager.lnk"
    explorer="Explorer.exe"
    app_note1="As you wish sir!"
    app_note2="Opening it!"
    app_note3="I'm on it!"
    app_note4="Fire on the screen!"
    app_note5="Here you go"
    app_note=random.choice([app_note1, app_note2, app_note3, app_note4, app_note5])
    if (app_name=="vs_code"):
        speak(app_note)
        print(app_note)
        try:
            os.startfile(vs_code)
        except Exception as app_open_error:
            speak("Sir, I am unable to initialize it!")
            print("Sir, I am unable to initialize it!")
    elif (app_name=="browser"):
        speak(app_note)
        print(app_note)
        try:
            os.startfile(browser)
        except Exception as app_open_error:
            speak("Sir, I am unable to initialize it!")
            print("Sir, I am unable to initialize it!")
    elif (app_name=="task_manager"):
        speak(app_note)
        print(app_note)
        try:
            os.startfile(task_manager)
        except Exception as app_open_error:
            speak("Sir, I am unable to initialize it!")
            print("Sir, I am unable to initialize it!")
    elif (app_name=="python"):
        speak(app_note)
        print(app_note)
        try:
            os.startfile(python)
        except Exception as app_open_error:
            speak("Sir, I am unable to initialize it!")
            print("Sir, I am unable to initialize it!")
    elif (app_name=="saavn"):
        speak(app_note)
        print(app_note)
        try:
            os.startfile(saavn)
        except Exception as app_open_error:
            speak("Sir, I am unable to initialize it!")
            print("Sir, I am unable to initialize it!")
    elif (app_name=="explorer"):
        speak(app_note)
        print(app_note)
        try:
            os.startfile(explorer)
        except Exception as app_open_error:
            speak("Sir, I am unable to initialize it!")
            print("Sir, I am unable to initialize it!")
    elif (app_name=="calculator"):
        speak(app_note)
        print(app_note)
        try:
            os.startfile(calculator)
        except Exception as app_open_error:
            speak("Sir, I am unable to initialize it!")
            print("Sir, I am unable to initialize it!")
    elif (app_name=="camtasia"):
        speak(app_note)
        print(app_note)
        try:
            os.startfile(camtasia)
        except Exception as app_open_error:
            speak("Sir, I am unable to initialize it!")
            print("Sir, I am unable to initialize it!")
    elif (app_name=="camtasiarec"):
        speak(app_note)
        print(app_note)
        try:
            os.startfile(camtasiarec)
        except Exception as app_open_error:
            speak("Sir, I am unable to initialize it!")
            print("Sir, I am unable to initialize it!")
    elif (app_name=="mail"):
        speak(app_note)
        print(app_note)
        try:
            os.startfile(msmail)
        except Exception as app_open_error:
            speak("Sir, I am unable to initialize it!")
            print("Sir, I am unable to initialize it!")
    elif (app_name=="music"):
        speak(app_note)
        print(app_note)
        try:
            speak("Enjoy your music sir!")
            os.startfile(groovemusic)
        except Exception as app_open_error:
            speak("Sir, I am unable to initialize it!")
            print("Sir, I am unable to initialize it!")
    elif (app_name=="news"):
        speak(app_note)
        print(app_note)
        try:
            os.startfile(news)
        except Exception as app_open_error:
            speak("Sir, I am unable to initialize it!")
            print("Sir, I am unable to initialize it!")
    elif (app_name=="powershell"):
        speak(app_note)
        print(app_note)
        try:
            os.startfile(powershell)
        except Exception as app_open_error:
            speak("Sir, I am unable to initialize it!")
            print("Sir, I am unable to initialize it!")
    elif (app_name=="store"):
        speak(app_note)
        print(app_note)
        try:
            os.startfile(store)
        except Exception as app_open_error:
            speak("Sir, I am unable to initialize it!")
            print("Sir, I am unable to initialize it!")
    elif (app_name=="weather"):
        speak(app_note)
        print(app_note)
        try:
            os.startfile(weather)
        except Exception as app_open_error:
            speak("Sir, I am unable to initialize it!")
            print("Sir, I am unable to initialize it!")
    elif (app_name=="whatsapp"):
        speak(app_note)
        print(app_note)
        try:
            os.startfile(whatsapp)
        except Exception as app_open_error:
            speak("Sir, I am unable to initialize it!")
            print("Sir, I am unable to initialize it!")
    elif (app_name=="wordpad"):
        speak(app_note)
        print(app_note)
        try:
            os.startfile(wordpad)
        except Exception as app_open_error:
            speak("Sir, I am unable to initialize it!")
            print("Sir, I am unable to initialize it!")
    elif (app_name=="word"):
        speak(app_note)
        print(app_note)
        try:
            os.startfile(word)
        except Exception as app_open_error:
            speak("Sir, I am unable to initialize it!")
            print("Sir, I am unable to initialize it!")
    elif (app_name=="excel"):
        speak(app_note)
        print(app_note)
        try:
            os.startfile(excel)
        except Exception as app_open_error:
            speak("Sir, I am unable to initialize it!")
            print("Sir, I am unable to initialize it!")
def app_close():
    app_note1="Okay, Closing app..."
    app_note2="Alright! Killing app..."
    app_note3="Ya, exiting..."
    app_note=random.choice([app_note1, app_note2, app_note3])
    if (app_name=="vs_code"):
        applet="Code.exe"
    elif (app_name=="chrome"):
        applet="chrome.exe"
    elif (app_name=="python"):
        applet="pythonw.exe"
    elif (app_name=="calculator"):
        applet="calculator.exe"
    elif (app_name=="saavn"):
        applet="Saavn.exe"
    elif (app_name=="camtasiarec"):
        applet="CamRecorder.exe"
    elif (app_name=="camtasia"):
        applet="CamtasiaStudio.exe"
    elif (app_name=="mail"):
        applet="HxOutlook.exe"
    elif (app_name=="music"):
        applet="Music.UI.exe"
    elif (app_name=="news"):
        applet="Microsoft.Msn.News.exe"
    elif (app_name=="powershell"):
        applet="powershell.exe"
    elif (app_name=="store"):
        applet="WinStore.App.exe"
    elif (app_name=="weather"):
        applet="Microsoft.Msn.Weather.exe"
    elif (app_name=="wordpad"):
        applet="wordpad.exe"
    elif (app_name=="msword"):
        applet="Word.exe"
    elif (app_name=="msexcel"):
        applet="Excel.exe"
    elif (app_name=="whatsapp"):
        applet="WhatsApp.exe"
    elif (app_name=="explorer"):
        applet="explorer.exe"
    elif (app_name=="task manager"):
        applet="Taskmgr.exe"
    speak(app_note)
    print(app_note)
    command="TASKKILL /F /IM " + applet
    try:
        os.system(command)
    except Exception as close_err:
        speak("Sorry sir, unable to close that!")
        print("Sorry sir, unable to close that!")
def ext_py(component):
    if (component=="timer"):
        os.startfile("C:\\VIBRIS\\extended_files\\timer.py")
    elif (component=="alarm"):
        os.startfile("C:\\VIBRIS\\extended_files\\alarm.py")
def status(var):
    if (var=="cpu"):
        cpu_val=psutil.cpu_percent()
        cpu_note1="The consumption of CPU is at", cpu_val, "%"
        cpu_note2="CPU usage level is at", cpu_val, "%"
        cpu_note=random.choice([cpu_note1, cpu_note2])
        speak(cpu_note)
        print(*cpu_note)
    elif (var=="ram"):
        ram_val=psutil.virtual_memory()
        ram_percent=float(ram_val.percent)
        ram_prcnt=str(ram_val.percent)
        if (ram_percent <= 35.0):
            condition=" Performance is excellent."
        elif (ram_percent > 35.0) and (ram_percent <= 50.0):
            condition=" Performance is satisfactory."
        elif (ram_percent > 50.0) and (ram_percent <= 65.0):
            condition=" Performance is good."
        elif (ram_percent > 65.0) and (ram_percent < 80.0):
            condition=" Performance is moderate."
        else:
            condition=" Performance is critical."
        if (ram_percent >= 80.0):
            ram_lvl1="The consumption of RAM is at " + ram_prcnt + "%" + condition
            ram_lvl2="RAM usage is at " + ram_prcnt + "%" + condition
            ram_lvl=random.choice([ram_lvl1, ram_lvl2])
            speak(ram_lvl)
            print(ram_lvl)
            speak("Should I eject the interface to free the RAM ?")
            print("Should I eject the interface to free the RAM?")
            ej_conf=listen()
            if ("yes" in ej_conf) or ("yep" in ej_conf) or ("yeah" in ej_conf):
                ej_note1="Okay, disabling the UI..."
                ej_note2="Ejecting the interface..."
                ej_note=random.choice([ej_note1, ej_note2])
                speak(ej_note)
                print(ej_note)
                try:
                    playsound.playsound("C:/VIBRIS/music/eject.mp3")
                    os.system("TASKKILL /F /IM Rainmeter.exe")
                except Exception as ej_err:
                    speak("Sorry sir, unable to eject the interface!")
                    print("Sorry sir, unable to eject the interface!")
            else:
                speak("Okay, cancelling...")
                print("Okay, cancelling...")
                exit
        else:
            ram_lvl1="The consumption of RAM is at " + ram_prcnt + "%." + condition
            ram_lvl2="RAM usage is at " + ram_prcnt + "%." + condition
            ram_lvl=random.choice([ram_lvl1, ram_lvl2])
            speak(ram_lvl)
            print(ram_lvl)
def power(power_action):
    power_note1="Doing it! Goodbye!"
    power_note2="As you wish! Goodbye!"
    power_note3="Okay, I'm on it! Goodbye"
    power_note4="Goodbye! Powering off!."
    power_note=random.choice([power_note1, power_note2, power_note3, power_note4])
    if (power_action == "reboot"):
        speak("Are you sure to reboot ?")
        print("Are you sure to reboot ?")
        reboot_conf=listen()
        if ("yes" in reboot_conf) or ("yep" in reboot_conf):
            speak(power_note)
            print(power_note)
            playsound.playsound("C:/VIBRIS/music/eject.mp3")
            os.system("reboot now")
        else:
            speak("Deactivating power configuration protocol")
            print("Deactivating Power Configuration Protocol")
            exit
    elif (power_action == "lock"):
        speak("Are you sure to enter lockscreen ?")
        print("Are you sure to enter lockscreen ?")
        lock_conf=listen()
        if ("yes" in lock_conf) or ("yep" in lock_conf):
            speak(power_note)
            print(power_note)
            subprocess.call("rundll32.exe user32.dll, LockWorkStation")
        else:
            speak("Deactivating power retuning...")
            print("Deactivating Power retuning...")
            exit
    elif (power_action == "halt"):
        speak("Are you sure to shutdown the system ?")
        print("Are you sure to shutdown the system ?")
        halt_conf=listen()
        if ("yes" in halt_conf) or ("yep" in halt_conf):
            speak(power_note)
            print(power_note)
            print("Quitting V.I.B.R.I.S. framework...")
            playsound.playsound("C:/VIBRIS/music/eject.mp3")
            os.system("shutdown /s /t 1")
        else:
            speak("Deactivating power retuning...")
            print("Deactivating Power retuning...")
            exit
    elif (power_action=="suspend"):
        speak("Are you sure to sign-out ?")
        print("Are you sure to sign-out ?")
        halt_conf=listen()
        if ("yes" in halt_conf) or ("yep" in halt_conf):
            speak(power_note)
            print(power_note)
            print("Quitting V.I.B.R.I.S. framework...")
            playsound.playsound("C:/VIBRIS/music/eject.mp3")
            os.system("shutdown -l")
def listen():
    rec=speech_recognition.Recognizer()
    with speech_recognition.Microphone() as src:
        playsound.playsound("C:/VIBRIS/music/wake-up.wav")
        print("Hearing...")
        rec.pause_threshold=1
        audio=rec.listen(src)
    try:
        print("Recognising the words...")
        query=rec.recognize_google(audio, language="en-in")
        print(f"You said :- {query}\n")
        playsound.playsound("C:/VIBRIS/music/action.wav")
        query=query
    except Exception as repeat:
        speak("Sorry, pardon please...")
        print("Sorry, pardon please...")
        query="retrial_x"
    if (query=="retrial_x"):
        listen()
    return(query)
def wfalpha():
    wfa_inp1="What's your query ?"
    wfa_inp2="Tell me your query!"
    wfa_inp3="For what query should I search?"
    wfa_inp=random.choice([wfa_inp1, wfa_inp2, wfa_inp3])
    speak(wfa_inp)
    inp=listen()
    keylet1="LE85EY-AKJVVJWX9H"
    keylet2="LE85EY-4UYQYRJ6YX"
    keylet=random.choice([keylet1, keylet2])
    client=wolframalpha.Client(keylet)
    port=client.query(inp)
    try:
        speak("Accessing Wolfram Alpha")
        print("Scanning Wolfram Alpha Servers...")
        result=next(port.results).text
        wfa_conf_txt1="Found results, shall I speak it for you ?"
        wfa_conf_txt2="Got it, Need me to speak results?"
        wfa_conf_txt=random.choice([wfa_conf_txt1, wfa_conf_txt2])
        speak(wfa_conf_txt)
        print(wfa_conf_txt)
        wfa_conf=listen().lower()
        if ("no" in wfa_conf) or ("nope" in wfa_conf):
            print(result)
        else:
            print(result)
            speak(result)
    except Exception as wfa_error:
        print(wfa_error)
        wfa_err1="Sorry , Wolfram Alpha Servers denied."
        wfa_err2="The connection to Wolfram Alpha failed."
        wfa_err=random.choice([wfa_err1, wfa_err2])
        speak(wfa_err)
        print(wfa_err)
def off():
    off1="Okay, thanks for time, terminating myself..."
    off2="As you wish! Terminating VIBRIS program..."
    off3="Thanks for your time, Deactivating VIBRIS..."
    off4="As you wish! Ejecting myself..."
    OFF=random.choice([off1, off2, off3, off4])
    speak(OFF)
    print(OFF)
    playsound.playsound("C:/VIBRIS/music/eject.mp3")
def detect():
    xurl="http://216.58.192.142"
    try:
        quad=requests.get(xurl, timeout=5)
        speak("Active Internet Detected! We are online and ready.")
        print("Internet Connection Detected! We are online and ready")
    except requests.ConnectionError:
        speak("Internet connection isn't reachable! System is offline!")
        print("The internet connection isn't reachable! System is offline!")
def on():
    playsound.playsound("C:/VIBRIS/music/timer_beep.mp3")
    greet()
    speak("Welcome back! Initialising VIBRIS Systems")
    print("Welcome back! Initialising VIBRIS Systems...")
    sleep(1.5)
    speak("All checked!")
    print("All checked!")
    speak("Deploying Virtual UI...")
    print("Deploying Virtual UI...")
    playsound.playsound("C:/VIBRIS/music/activating.mp3")
    os.startfile("C:\\Program Files\\Rainmeter\\Rainmeter.exe")
    status("ram")
    speak("Detecting Internet Connection...")
    print("Detecting Internet Connection...")
    sleep(1)
    detect()
def mail():
    speak("Whom to send the email ?")
    print("Whom to send the email ?")
    receive=listen()
    if ("me" in receive) or ("srp" in receive):
        receiver="srp@maxez.ml"
    elif ("friend" in receive) or ("shivang"):
        receiver="shiwanggb@gmail.com"
    elif ("dad" in receive):
        receiver="pvshridhar02@gmail.com"
    speak("What shall be the content sir ?")
    print("What shall be the content sir ?")
    content=listen()
    try:
        server=smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login("srpx31@gmail.com", "zxfpwmj1860")
        server.sendmail("srpx31@gmail.com", receiver, content)
        server.close()
        speak("Email sent successfully!")
    except Exception as mail_err:
        speak("I'm sorry, unable to send mail at the moment!")
        print("I'm sorry, unable to send mail at the moment!")
        print(mail_err)
def boredom():
    speak("Choose a boredom repellant option - Play YouTube, Play Music, Play online games ?")
    print("Choose a boredom repellant option - Play YouTube, Play Music, Play online games ?")
    act=listen()
    if ("youtube" in act):
        speak("Okay!")
        print("Okay!")
        sep_web("https://www.youtube.com/")
    elif ("music" in act):
        speak("Okay!")
        print("Okay!")
        app_open("music")
    elif ("games" in act):
        speak("Okay!")
        print("Okay!")
        sep_web("https://www.miniclip.com/")
on()
def process_engine():
    while(True):
        while(True):
            print("Hit Enter to speak.") 
            runlet=input()
            if (runlet==""):
                cmd=listen()
                cmd=cmd.lower()
                break
            else:
                continue
        if ("about" in cmd) and ("me" in cmd or "boss" in cmd or "srp" in cmd):
            about("srp")
        elif ("about" in cmd or "who" in cmd) and ("you" in cmd):
            about("vibris")
        elif ("who" in cmd) and (name in cmd):
            about("srp")
        elif ("date" in cmd) or ("day" in cmd):
            dt_time("dtx")
        elif ("timer" in cmd):
            ext_py("timer")
        elif ("time" in cmd) or ("clock" in cmd):
            dt_time("tx")
        elif ("speak" in cmd) or ("say" in cmd):
            say()
        elif ("wish" in cmd) or ("greet" in cmd):
            greet()
        elif ("google" in cmd):
            sep_web("https://www.google.co.in/")
        elif ("tutor" in cmd) or ("aakash digital" in cmd):
            sep_web("https://www.digital.aakash.ac.in/")
        elif ("youtube" in cmd) or ("yt" in cmd):
            sep_web("https://www.youtube.com/")
        elif ("my site" in cmd):
            sep_web("http://code.maxez.ml")
        elif ("quora" in cmd):
            sep_web("https://www.quora.com/")
        elif ("stackoverflow" in cmd):
            sep_web("https://www.stackoverflow.com")
        elif ("open" in cmd or "launch" in cmd or "load" in cmd) and("browser" in cmd):
            app_open("browser")
        elif ("surf" in cmd) or ("browse" in cmd):
            web()
        elif ("how" in cmd or "ok" in cmd) and ("you" in cmd):
            okay()
        elif ("dice" in cmd):
            dice()
        elif ("coin" in cmd) or ("toss" in cmd):
            coin()
        elif ("you" in cmd) and("connect" in cmd):
            detect()
        elif ("you" in cmd) and ("online" in cmd):
            detect()
        elif ("detect" in cmd or "verify" in cmd) and ("internet" in cmd):
            detect()
        elif ("ram" in cmd):
            status("ram")
        elif ("cpu" in cmd):
            status("cpu")
        elif ("system" in cmd) and ("work" in cmd):
            status("ram")
            status("cpu")
        elif ("alarm" in cmd):
            ext_py("alarm")
        elif ("you" in cmd) and ("stupid" in cmd or "idiot" in cmd or "dumb" in cmd):
            apologise()
        elif ("wikipedia" in cmd):
            speak("Searching...")
            print("Searching...")
            query=cmd.replace("wikipedia ", "")
            result=wikipedia.summary(query, sentences=2)
            rel1="From Wikipedia -"
            rel2="According to wikipedia -"
            rel=random.choice([rel1, rel2])
            speak(rel)
            print(rel)
            speak(result)
            print(result)
        elif ("wolfram" in cmd) or ("search" in cmd):
            wfalpha()
        elif ("mail" in cmd) and ("post" in cmd or "send" in cmd):
            mail()
        elif ("open" in cmd or "launch" in cmd or "load" in cmd) and ("mail" in cmd):
            app_open("mail")
        elif ("open" in cmd or "launch" in cmd or "load" in cmd) and ("visual studio" in cmd or "vs" in cmd) and ("code" in cmd):
            app_open("vs_code")
        elif ("close" in cmd or "exit" in cmd or "quit" in cmd or "kill" in cmd) and ("visual studio" in cmd or "vs" in cmd) and ("code" in cmd):
            app_close("vs_code")
        elif ("open" in cmd or "launch" in cmd or "load" in cmd) and ("task manager" in cmd):
            app_open("task_manager")
        elif ("close" in cmd or "exit" in cmd or "quit" in cmd or "kill" in cmd) and ("task manager" in cmd):
            app_close("task_manager")
        elif ("open" in cmd or "launch" in cmd or "load" in cmd) and ("file explorer" in cmd or "file manager" in cmd):
            app_open("explorer")
        elif ("close" in cmd or "exit" in cmd or "quit" in cmd or "kill" in cmd) and ("file explorer" in cmd or "file manager" in cmd):
            speak("You need to manually close the file explorer.")
            print("You need to manually close the file explorer.")
        elif ("open" in cmd or "launch" in cmd or "load" in cmd) and ("calaculate" in cmd or "calculation" in cmd or "calculator" in cmd):
            app_open("calculator")
        elif ("close" in cmd or "exit" in cmd or "quit" in cmd or "kill" in cmd) and ("calaculate" in cmd or "calculation" in cmd or "calculator" in cmd):
            app_close("calculator")
        elif ("open" in cmd or "launch" in cmd or "load" in cmd) and ("record" in cmd and "screen" in cmd) or ("camtasia recorder" in cmd):
            app_open("camtasiarec")
        elif ("close" in cmd or "exit" in cmd or "quit" in cmd or "kill" in cmd) and ("record" in cmd and "screen" in cmd) or ("camtasia recorder" in cmd):
            app_close("camtasiarec")
        elif ("open" in cmd or "launch" in cmd or "load" in cmd) and ("camtasia" in cmd):
            app_open("camtasia")
        elif ("close" in cmd or "exit" in cmd or "quit" in cmd or "kill" in cmd) and ("camtasia" in cmd):
            app_close("camtasia")
        elif ("open" in cmd or "launch" in cmd or "load" in cmd) and ("groove music" in cmd):
            app_open("music")
        elif ("close" in cmd or "exit" in cmd or "quit" in cmd or "kill" in cmd) and ("groove music" in cmd):
            app_close("music")
        elif ("open" in cmd or "launch" in cmd or "load" in cmd) and ("music" in cmd or "saavn" in cmd):
            app_open("saavn")
        elif ("close" in cmd or "exit" in cmd or "quit" in cmd or "kill" in cmd) and ("music" in cmd or "saavn" in cmd):
            app_close("saavn")
        elif ("open" in cmd or "launch" in cmd or "load" in cmd) and ("news" in cmd):
            app_open("news")
        elif ("close" in cmd or "exit" in cmd or "quit" in cmd or "kill" in cmd) and ("news" in cmd):
            app_close("news")
        elif ("open" in cmd or "launch" in cmd or "load" in cmd) and ("powershell" in cmd):
            app_open("powershell")
        elif ("close" in cmd or "exit" in cmd or "quit" in cmd or "kill" in cmd) and ("powershell" in cmd):
            app_close("powershell")
        elif ("open" in cmd or "launch" in cmd or "load" in cmd) and ("store" in cmd):
            app_open("store")
        elif ("close" in cmd or "exit" in cmd or "quit" in cmd or "kill" in cmd) and ("store" in cmd):
            app_close("store")
        elif ("open" in cmd or "launch" in cmd or "load" in cmd) and ("weather" in cmd):
            app_open("weather")
        elif ("close" in cmd or "exit" in cmd or "quit" in cmd or "kill" in cmd) and ("weather" in cmd):
            app_close("weather")
        elif ("open" in cmd or "launch" in cmd or "load" in cmd) and ("whatsapp" in cmd):
            app_open("whatsapp")
        elif ("close" in cmd or "exit" in cmd or "quit" in cmd or "kill" in cmd) and ("whatsapp" in cmd):
            app_close("whatsapp")
        elif ("open" in cmd or "launch" in cmd or "load" in cmd) and ("python" in cmd or "idle" in cmd):
            app_open("python")
        elif ("close" in cmd or "exit" in cmd or "quit" in cmd or "kill" in cmd) and ("python" in cmd or "idle" in cmd):
            app_close("python")
        elif ("open" in cmd or "launch" in cmd or "load" in cmd) and ("wordpad" in cmd):
            app_open("wordpad")
        elif ("close" in cmd or "exit" in cmd or "quit" in cmd or "kill" in cmd) and ("wordpad" in cmd):
            app_close("wordpad")
        elif ("open" in cmd or "launch" in cmd or "load" in cmd) and ("chrome" in cmd):
            app_open("browser")
        elif ("close" in cmd or "exit" in cmd or "quit" in cmd or "kill" in cmd) and ("chrome" in cmd):
            app_close("chrome")
        elif ("bored" in cmd):
            boredom()
        elif ("who is " in cmd) and (name not in cmd):
            speak("Searching...")
            print("Searching...")
            query=cmd.replace("who is ", "")
            result=wikipedia.summary(query, sentences=2)
            rel1="From Wikipedia -"
            rel2="According to wikipedia -"
            rel=random.choice([rel1, rel2])
            speak(rel)
            print(rel)
            speak(result)
            print(result)
        elif ("you" in cmd) and ("happy" in cmd):
            okay()
        elif ("shutdown" in cmd) or ("power off" in cmd) or ("halt" in cmd):
            power("halt")
        elif ("reboot" in cmd) or ("restart" in cmd):
            power("reboot")
        elif ("lock" in cmd):
            power("lock")
        elif ("sign out" in cmd) or ("log out" in cmd) or ("log off" in cmd):
            power("suspend")
        elif ("eject" in cmd or "throw" in cmd or "deactivate" in cmd or "remove" in cmd) and ("ui" in cmd or "interface" in cmd):
            ej_note1="Okay, disabling the UI..."
            ej_note2="As you wish, ejecting the interface..."
            ej_note=random.choice([ej_note1, ej_note2])
            speak(ej_note)
            print(ej_note)
            try:
                playsound.playsound("C:/VIBRIS/music/eject.mp3")
                os.system("TASKKILL /F /IM Rainmeter.exe")
            except Exception as ej_err:
                speak("Sorry, unable to eject the interface!")
                print("Sorry, unable to eject the interface!")
        elif ("goodbye" in cmd) or ("eject" in cmd and "vibris" in cmd):
            off()
            break
        else:
            try:
                inp=cmd
                keylet1="LE85EY-AKJVVJWX9H"
                keylet2="LE85EY-4UYQYRJ6YX"
                keylet=random.choice([keylet1, keylet2])
                client=wolframalpha.Client(keylet)
                port=client.query(inp)
                try:
                    speak("Approaching the servers of Wolfram Alpha")
                    print("Approaching the servers of Wolfram Alpha")
                    result=next(port.results).text
                    wfa_conf_txt1="Found results, shall I speak it for you ?"
                    wfa_conf_txt2="Got it, Need me to speak results ?"
                    wfa_conf_txt=random.choice([wfa_conf_txt1, wfa_conf_txt2])
                    speak(wfa_conf_txt)
                    print(wfa_conf_txt)
                    wfa_conf=listen().lower()
                    if ("no" in wfa_conf) or ("nope" in wfa_conf):
                        print(result)
                    else:
                        print(result)
                        speak(result)
                except Exception as wfa_error:
                    print(wfa_error)
                    wfa_err1="Unable to access Wolfram Alpha Servers."
                    wfa_err2="I am sorry, connection to servers failed."
                    wfa_err=random.choice([wfa_err1, wfa_err2])
                    print(wfa_err)
            except Exception as e:
                try:
                    speak("Searching...")
                    print("Searching...")
                    query=cmd
                    result=wikipedia.summary(query, sentences=2)
                    rel1="From Wikipedia -"
                    rel2="According to wikipedia -"
                    rel=random.choice([rel1, rel2])
                    speak(rel)
                    print(rel)
                    speak(result)
                    print(result)
                except Exception as final_err:
                    speak("Sorry, unable to find that!")
                    print("Sorry, unable to find that!")
process_engine()