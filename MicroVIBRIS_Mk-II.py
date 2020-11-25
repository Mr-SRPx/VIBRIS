#SRP's A.I. VIBRIS Mark - II
import datetime as dtx
import time as tx
import random as rdm
import webbrowser as web
def guider() :
    guide="\vYou can try - 'time', 'date', 'timer', 'wish or greet', 'dice roll',\n 'coin toss', 'google, facebook, youtube, any site browsing or surfing', 'bye for shutdown'\nYou can ask talk for these in any of your way.\nE.g. 'What is the time' or'show me the time' anything will work for all"
    print(guide)
def time() :
    tm=dtx.datetime.now().strftime("%H : %M")
    tm1="\vRight now, it is", tm
    tm2="\vCurrently, it is", tm
    tm3="\vAt this point of time, it is clocking", tm
    TM=rdm.choice([tm1, tm2, tm3])
    print(*TM)
def timer() :
    tmrnote="\vTimer protocol is being initialised. But it just shows a text for end."
    print(tmrnote)
    tx.sleep(1)
    tmr1="\vBoss, for how much seconds you wanna set the timer ? :- "
    tmr2="\vBoss, please enter the number of seconds for interval of the timer :- "
    tmr3="\vPlease put-in the time in seconds for setting the timer :- "
    tmr=rdm.choice([tmr1, tmr2, tmr3])
    interval=int(input(tmr))
    tx.sleep(1)
    print("Ready.")
    tx.sleep(1)
    print("Steady.")
    tx.sleep(1)
    print("Go!")
    tx.sleep(interval)
    print("Time's up! "*5)
def okay() :
    ok1="\vI'm all good boss!"
    ok2="\vI'm enjoying by assisting you boss!"
    ok3="\vI'm finding myself functioning with normal parameters!"
    ok=rdm.choice([ok1, ok2, ok3])
    print(ok)
def date() :
    dt=dtx.datetime.today().strftime("%d - %m - %Y")
    dt1="\vToday, it is", dt
    dt2="\vThis day, it is", dt
    DT=rdm.choice([dt1, dt2])
    print(*DT)
def greeter() :
    htm=dtx.datetime.now().hour
    if (htm >= 0 and htm < 12):
        print("\vGood Morning Boss!")
    elif (htm >= 12 and htm <5):
        print("\vGood Afternoon Boss!")
    else:
        print("\vGood Evening Boss!")
def dice() :
    dicenote1="\vYes boss, rolling a dice..."
    dicenote2="\vOkay boss, rolling a dice..."
    dicenote3="\vAlright boss, dice's bein' rolled..."
    DICENOTE=rdm.choice([dicenote1, dicenote2, dicenote3])
    print(DICENOTE)
    tx.sleep(1)
    diceout=rdm.choice(["1", "2", "3", "4", "5", "6"])
    diceout1="\vOn the top, it is",diceout
    diceout2="\vBoss, The outcome is",diceout
    diceout3="\vBoss, the result is",diceout
    DICEOUT=rdm.choice([diceout1, diceout2, diceout3])
    print(*DICEOUT)
def coin() :
    coinnote1="\vYes boss, tossing a coin..."
    coinnote2="\vOkay boss, tossing a coin..."
    coinnote3="\vAlright boss, coin is being tossed..."
    COINNOTE=rdm.choice([coinnote1, coinnote2, coinnote3])
    print(COINNOTE)
    tx.sleep(1)
    coinout=rdm.choice(["Heads", "Tails"])
    coinout1="\vOn the top, it is",coinout
    coinout2="\vBoss, the outcome is",coinout
    coinout3="\vBoss, the result is",coinout
    COINOUT=rdm.choice([coinout1, coinout2, coinout3])
    print(*COINOUT)
def google() :
    gnote1="\vHere you go!"
    gnote2="\vAs you wish boss!"
    gnote3="\vFire on the screen!"
    gnote=rdm.choice([gnote1, gnote2, gnote3])
    print(gnote)
    tx.sleep(1)
    web.open_new_tab("https://www.google.co.in")
def fb() :
    gnote1="\vHere you go!"
    gnote2="\vAs you wish boss!"
    gnote3="\vFire on the screen!"
    gnote=rdm.choice([gnote1, gnote2, gnote3])
    print(gnote)
    tx.sleep(1)
    web.open_new_tab("https://www.facebook.com")
def yt() :
    gnote1="\vHere you go!"
    gnote2="\vAs you wish boss!"
    gnote3="\vFire on the screen!"
    gnote=rdm.choice([gnote1, gnote2, gnote3])
    print(gnote)
    tx.sleep(1)
    web.open_new_tab("https://www.youtube.com")
def surf() :
    url=input("\vEnter the web URL (along with transfer protocol; press enter after browsing.) :- ")
    web.open_new_tab(url)
def error() :
    err1="\vOh no, an error occured! Maybe there's a typing mistake or beyond my scope of working."
    err2="\vOops, something went wrong. Maybe there's a typing mistake or beyond my scope of working."
    err3="\vOh! There's an error. There can be typing mistake or far by my ability, or both."
    err=rdm.choice([err1, err2, err3])
    print(err)
def AI_engine():
    print("+------------------------------------------------+\n|          ___    ____     ____     ___   ____   |\n|\      /   |    |    \   |    \     |   /       |\n| \    /    |    |____/   |____/     |   \____   |\n|  \  /     |    |    \   |    \     |        \  |\n|   \/  *  _|_ * |____/ * |     \ * _|_ * ____/ *|\n|                                                |\n+------------------------------------------------+")
    tx.sleep(3)
    print("\vChecking Control Services    ...     [Checked]")
    tx.sleep(1)
    print("Warning!\nDon't type anything wherever input is not given, it breaks the program\nif asked integer value, then only add integer value.")
    print("\vActivating A.I. Engine...")
    tx.sleep(1)
    greeter()
    intro="\vI am V.I.B.R.I.S., a micro-AI program made by Mr. SRP.\nMy script is made using Python. I am a text-based virtual assistant version - \'Mark -II\'"
    about="\nV.I.B.R.I.S. stands for \"Very Intelligent But Recyclic Interaction System\".\nThese acronym was made by Mr.SRP in 2020 when he ws building me.\nThat's all about me."
    print(intro)
    tx.sleep(3)
    print("\vThat is how I give my introduction.")
    tx.sleep(2.5)
    def func():
        print("\vLoading set-up ...")
        tx.sleep(2)
        name=str(input("\vFirst of all, Please let me know your name :- "))
        tx.sleep(0.5)
        age=int(input("\vOkay, tell me your age :- "))
        if (age >103) :
            print("Sorry, I'm not a fool, restarting AI")
            func()
        else :
            gen=input("\vLastly, enter your gender\n(\'m\' for male and \'f\' for female) :- ")
            if (gen=="m") :
                gender="male"
            elif (gen=="f"):
                gender="female"
            else :
                gender="unknown"
            if (age >= 18) :
                vote="You are eligible to vote."
            else :
                vote="You are not eligible to vote."
            def about_usr():
                abt_usr1="\vYou are my boss whose name is",name,".\nYou are",age,"years old and thus",vote,"\nYour gender is",gender,"."
                abt_usr2="\vYour name is",name,".\nYour age is",age,"\nSo,",vote,"\nLastly, your gender is",gender,"."
                abt_USR=rdm.choice([abt_usr1, abt_usr2])
                print(*abt_USR)
            print("\vAlright",name,", Initialising Command in-take and Response System...")
            tx.sleep(2)
            print("\vOkay, we are all-set, please input only in lowercase and expanded forms.")
            tx.sleep(0.5)
            guider()
            tx.sleep(1)
            def engine() :
                while(True) :
                    inp1="\vHow can I help you boss ?"
                    inp2="\vGimme a command"
                    inp3="\vEnter your command"
                    inp4="\vPut your order"
                    INP=rdm.choice([inp1, inp2, inp3, inp4])
                    inp=input(INP+"\n(type guide for some guide) :- ")
                    if ("how" in inp or "ok" in inp or "okay" in inp) and ("you" in inp) :
                        okay()
                    elif ("guide" in inp) :
                        guider()
                    elif ("timer" in inp) :
                        timer()
                    elif ("date" in inp) and ("day" in inp) :
                        date()
                    elif ("greet" in inp) or ("wish" in inp) :
                        greeter()
                    elif ("dice" in inp) :
                        dice()
                    elif ("coin" in inp) :
                        coin()
                    elif ("google" in inp) :
                        google()
                    elif ("facebook" in inp) and ("fb" in inp) :
                        fb()
                    elif ("youtube" in inp) and ("yt" in inp) :
                        yt()
                    elif ("bye" in inp) or ("goodbye" in inp) :
                        print("\vOkay boss, goodbye!")
                        break
                    elif ("surf" in inp) or ("browse" in inp) :
                        surf()
                    elif ("time" in inp) :
                        time()
                    elif ("about" in inp) and ("you" in inp or "VIBRIS" in inp) :
                        print(intro)
                        tx.sleep(3)
                        print(about)
                    elif ("about" in inp) and ("me" in inp or"boss" in inp) :
                        about_usr()
                    else :
                        error()
            engine()
    func()
def run() :
    power=input("Do you want to activate V.I.B.R.I.S. ?\n('y' for yes and 'n' for no) :- ")
    if (power=="y") :
        AI_engine()
    elif (power=="n") :
        exit
    else :
        run()
run()