import os
from colorama import init
from termcolor import colored
import random
from time import sleep
import wmi
import speech_recognition as sr
import webbrowser
import pyttsx3

os.system('color 3F')

init()

'''0 = Black       8 = Gray
    1 = Blue        9 = Light Blue
    2 = Green       A = Light Green
    3 = Aqua        B = Light Aqua
    4 = Red         C = Light Red
    5 = Purple      D = Light Purple
    6 = Yellow      E = Light Yellow
    7 = White       F = Bright White'''

colors = None
bacg = "on_magenta"
adre = "on_red"
latte = ['bold', 'dark', 'underline', 'blink', 'reverse', 'concealed']
atte = ['dark']

def speakText(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def alexa():
    with sr.Microphone() as source:
        r = sr.Recognizer() ; sleep(0.2)
        print(colored("\n                                                               ", None, "on_cyan")+colored(" listening... ", colors, adre, atte))
        
        try:
            audio_text = r.listen(source)
            speak_text = r.recognize_google(audio_text)
            lower_speak_text = speak_text.lower()
            print("\n"+colored("                                                               ", None, "on_cyan")+colored(" "+lower_speak_text+" ", colors, adre, atte))
            print(colored("", None, "on_cyan"))
            return lower_speak_text
        except:
            ac8 = "\n Sorry, I did not get that "
            print(colored(ac8, colors, bacg, atte)); speakText(ac8) ; sleep(1)

nameList = []

def starting():
    aa1 = " Hi i am aaka "
    print(colored(aa1, colors, bacg, atte)) ; speakText(aa1)
    aa2 = "\n the bot " 
    print(colored(aa2, colors, bacg, atte)) ; speakText(aa2) ; sleep(1)

def ask_name():
    
    aa3 = "\n Whats your name? "
    print(colored(aa3, colors, bacg, atte)) ; speakText(aa3)
    name = alexa() ; sleep(0.5)
    
    if (name == None):
        ask_name()    
    else:
        nameList.append(name)    
        weicome_string_list = (
            "\n Hi "+nameList[0]+" nice to meet you " ,
            "\n What a wonderful day "+nameList[0]+" " ,
            "\n welcome "+nameList[0]+" " ,
            "\n Hey "+nameList[0]+" i am very exciting to talk to you " ,
            "\nWhats up! "+nameList[0] ,
            "\n "+nameList[0]+"! "+"I dont hear this name in my whole life " , 
            "\n Hey "+nameList[0]+" I belive you will like it "
        )
        aa4 = random.choice(weicome_string_list)
        print(colored(aa4, colors, bacg, atte)) ; speakText(aa4) ; sleep(0.5)
        aa5 = "\n I am in a devloping process "
        print(colored(aa5, colors, bacg, atte)) ; speakText(aa5) ; sleep(0.6)
        aa6 = "\n So i am providing you a list from \n you can select an option "
        print(colored(aa6, colors, bacg, atte)) ; speakText(aa6) ; sleep(1)
    
starting()
ask_name()

def sal():
    aa7 = "\n Enter time "
    print(colored(aa7, colors, bacg, atte)) ; speakText(aa7)
    def hour():
        aa8 = "\n Hours : "
        print(colored(aa8, colors, bacg, atte)) ; speakText(aa8)
        hours = alexa()
        if(hours == None):
            hour()
        else:    
            hours = str(hours)
            def mint():
                aa9 = "\n Minutes : "
                print(colored(aa9, colors, bacg, atte)) ; speakText(aa9)
                minutes = alexa()
                if(minutes == None):
                    mint()
                else:     
                    minutes = str(minutes) ; sleep(0.6)
                    ab1 = "\n Alarm set on "+hours+":"+minutes+" "
                    print(colored(ab1, colors, bacg, atte)) ; speakText(ab1) ; sleep(2)
            mint()    
    hour()

def trch(percent):
    brightness = int(percent)
    c = wmi.WMI(namespace="wmi")
    method = c.WmiMonitorBrightnessMethods()[0]
    method.WmiSetBrightness(brightness, 0)
    if(brightness == 100): 
        ab4 = "\n Maxed the brightness "
        print(colored(ab4, colors, bacg, atte)) ; speakText(ab4)
    if(brightness == 0):
        ab5 = "\n Reduced the brightness "
        print(colored(ab5, colors, bacg, atte)) ; speakText(ab5)    


def srhg():
    ab2 = "\n Tell me what you want to search or say exit to quit : "
    print(colored(ab2, colors, bacg, atte)) ; speakText(ab2)
    search_string = alexa() ; sleep(1)
    if(search_string == None):
        srhg()
    elif(search_string == "exit"):
        ad7 = "\n Quiting.. "
        print(colored(ad7, colors, bacg, atte)) ; speakText(ad7)    
    else:    
        search_string = str(search_string)
        url = "https://www.google.com.tr/search?q={}".format(search_string)
        webbrowser.open_new_tab(url) ; sleep(3)

def url_opner(url):
    urll = url
    webbrowser.open_new_tab(urll)
    ad6 = "\n Opening... "
    print(colored(ad6, colors, bacg, atte)) ; speakText(ad6) ; sleep(3)

def opnste():
    ad2 = "\n Select from these "
    print(colored(ad2, colors, bacg, atte)) ; speakText(ad2) ; sleep(0.2)
    print(colored("", None, "on_cyan"))
    ad4 = "\n>> Wikipedia \n>> Youtube \n>> Facebook \n>> Instagram \n>> Linkedin \n>> Register for vaccine \n>> Aadhar card \n>> Pan card \n>> Passport \n>> Driving licence"
    print(colored(ad4, colors, bacg, atte))
    print(colored(" ", colors, bacg, atte)) ; sleep(0.3)
    ad3 = "\n Or say exit to quit "
    print(colored(ad3, colors, bacg, atte)) ; speakText(ad3)
    utren = alexa() 
    condn = ["wikipedia", "youtube", "facebook", "instagram", "linkedin", "vaccine", "aadhar", "pan", "passport", "driving", "exit"]

    def findstr():
        if(utren == None):
            app()
        else:
            try:    
                for el in condn:
                    id = utren.find(el)
                    if(id != -1):
                        return el
            except TypeError:
                ac9 = "\n Invalid option "
                print(colored(ac9, colors, bacg, atte)) ; speakText(ac9)
                opnste()

    slct = findstr() ; sleep(0.4)           

    if(slct == None):
        opnste()
    elif(slct == "exit"):
        ad8 = "\n Closing... "
        print(colored(ad8, colors, bacg, atte)) ; speakText(ad8) ; sleep(0.6)    
    elif(slct == "wikipedia"):
        url_opner("https://en.wikipedia.org/wiki/Main_Page")
        opnste()
    elif(slct == "driving"):
        url_opner("https://parivahan.gov.in/parivahan/en/content/driving-licence-0")
        opnste()
    elif(slct == "youtube"):
        url_opner("https://www.youtube.com/")
        opnste()        
    elif(slct == "facebook"):
        url_opner("https://www.facebook.com/")
        opnste()
    elif(slct == "instagram"):
        url_opner("https://www.instagram.com/")
        opnste()
    elif(slct == "linkedin"):
        url_opner("https://in.linkedin.com/")
        opnste()
    elif(slct == "vaccine"):
        url_opner("https://selfregistration.cowin.gov.in/")
        opnste()
    elif(slct == "aadhar"):
        url_opner("https://uidai.gov.in/")
        opnste()
    elif(slct == "pan"):
        url_opner("https://www.onlineservices.nsdl.com/paam/endUserRegisterContact.html")
        opnste()
    elif(slct == "passport"):
        url_opner("https://www.passportindia.gov.in/AppOnlineProject/welcomeLink#")
        opnste()
    else:
        ad5 = "\n Invalid option "
        print(colored(ad5, colors, bacg, atte)) ; speakText(ad5) ; sleep(0.5)
        opnste()    

def teljok():
    ac4 = (
        "\n Yesterday I saw a guy spill all his Scrabble letters on the road. I asked him, 'What???s the word on the street?' " ,
        "\n Hear about the new restaurant called Karma? " ,
        "\n A woman in labor suddenly shouted, 'Shouldn???t! Wouldn???t! Couldn???t! Didn???t! Can???t!' " ,
        "\n A bear walks into a bar and says, 'Give me a whiskey and ??? cola.' " ,
        "\n What do Alexander the Great and Winnie the Pooh have in common? Same middle name. " ,
        "\n I was horrified when my wife told me that my six-year-old son wasn't actually mine. Apparently I need to pay more attention during school pick-up. " ,
        "\n What is the opposite of a croissant? A happy uncle. " ,
        "\n If April showers bring May flowers, what do May flowers bring? Pilgrims. " ,
        "\n Which branch of the military accepts toddlers? The infantry. " ,
        "\n Did you know you can actually listen to the blood in your veins? You just have to listen varicosely. " ,
        "\n Though I enjoy the sport, I could never date a tennis player. Love means nothing to them. " ,
        "\n I have a joke about time travel, but I'm not gonna share it. You guys didn't like it. " ,
        "\n What's the opposite of irony? Wrinkly. " ,
        "\n I was kidnapped by mimes once. They did unspeakable things to me. " ,
        "\n Got a PS5 for my little brother. Best trade I've ever done! " ,
        "\n What do the movies Titanic and The Sixth Sense have in common? Icy dead people. " ,
        "\n I finally decided to sell my vacuum cleaner. All it was doing was gathering dust! " ,
        "\n When you die, what part of the body dies last? The pupils???they dilate. " ,
        "\n A friend of mine went bald years ago, but still carries around an old comb. He just can't part with it "
    )
    ac5 = random.choice(ac4)
    print(colored(ac5, colors, bacg, atte)) ; speakText(ac5)

def whatname():
    print("\n"+colored(nameList[0], colors, bacg, atte)) ; speakText("your name is "+nameList[0])

def ordfod():
    ab8 = "\n Coming soon... "
    print(colored(ab8, colors, bacg, atte)) ; speakText(ab8) ; sleep(2)

def boktaxi():
    ab9 = "\n Coming soon... "
    print(colored(ab9, colors, bacg, atte)) ; speakText(ab9) ; sleep(2)

def finsh():
    ac1 = "\n Closing... "
    print(colored(ac1, colors, bacg, atte)) ; speakText(ac1)
    ac2 = "\n Thank you for using our app " 
    print(colored(ac2, colors, bacg, atte)) ; speakText(ac2) ; sleep(2)
    print("---")

rem_que_list = []
rem_ans_list = []

def rember():
    ad1 = "\n Ok tell me what i remberer for you like age, mothers name, meeting time etc "
    print(colored(ad1, colors, bacg, atte)) ; speakText(ad1)
    def inner():
        remember_que = alexa() ; sleep(0.6)
        if(remember_que == None):
            inner()
        else:    
            rem_que_list.append(remember_que)
            ad2 = "\n Ok what is your "+remember_que+"? "
            print(colored(ad2, colors, bacg, atte)) ; speakText(ad2)
            def pinner():
                tex_rememberd = alexa() ; sleep(0.7)
                if(tex_rememberd == None):
                    pinner()
                else:    
                    rem_ans_list.append(tex_rememberd)
                    ad3 = "\n Ok i will remember that for you "
                    print(colored(ad3, colors, bacg, atte)) ; speakText(ad3)
            pinner()       
    inner()    

def repl_remb(n):    
    ad4 = rem_ans_list[n]
    print("\n"+colored(ad4, colors, bacg, atte)) ; speakText(str(ad4)) ; sleep(2)

def gtu():
    try:
        rem_que_list[0]
        return True
    except IndexError:
        return False    



def app():
    print(colored("                               \n                          ", None, "on_cyan"))
    ab3 = "\n>> Set alarm \n>> On the torch \n>> Off the torch \n>> Search on google \n>> Tell me a joke \n>> Order food \n>> Book a ride \n>> What is my name \n>> Remember \n>> Open site \n\n Say 'exit' to close the app " ; sleep(0.2)
    print(colored(ab3, colors, bacg, atte))
    talk = alexa()

    def srt():
        if(talk == None):
            app()
        else:
            try:    
                for el in rem_que_list:
                    idt = talk.find(el)
                    if(idt != -1):
                        return el
            except TypeError:
                ac9 = "\n Invalid option "
                print(colored(ac9, colors, bacg, atte)) ; speakText(ac9)
                app()                            

    nlle = srt()

    condn = ["alarm", "on", "off", "google", "joke", "food", "ride", "name", "remember", "site", "exit", nlle]

    def findstr():
        if(talk == None):
            app()
        else:
            try:    
                for el in condn:
                    id = talk.find(el)
                    if(id != -1):
                        return el
            except TypeError:
                ac9 = "\n Invalid option "
                print(colored(ac9, colors, bacg, atte)) ; speakText(ac9)
                app()                                  

    speech = findstr()

    if(speech == None):
        app()
    elif(speech == "exit"):
        finsh()    
    elif(speech == "alarm"):
        sal()
        app()
    elif(speech == "on"):
        trch(100) ; sleep(2)
        app()
    elif(speech == "google"):
        srhg() ; sleep(2)
        app()  
    elif(speech == "joke"):
        teljok() ; sleep(2)
        app()    
    elif(speech == "ride"):
        boktaxi()
        app()
    elif(speech == "food"):
        ordfod()
        app()
    elif(speech == "off"):
        trch(0) ; sleep(2)
        app()
    elif(speech == "name"):
        whatname()
        app()
    elif(speech == "remember"):
        rember() ; sleep(2)
        app()
    elif(speech == "site"):
        opnste()
        app()
    elif(gtu()):
        try:
            if(speech == nlle):
                for i in range(len(rem_que_list)):
                    if(rem_que_list[i] == nlle):
                        repl_remb(i)
                        app()
            elif(speech == "exit"):
                finsh()    
        except IndexError:
            print("close..")    
    else:
        ac9 = "\n Invalid option "
        print(colored(ac9, colors, bacg, atte)) ; speakText(ac9)
        app()        
    
            
    

app()


'''if(speech == "what is my "+rem_que_list[0]):
                repl_remb(0) 
                app()          
            elif(speech == "what is my "+rem_que_list[1]):
                repl_remb(1)
                app()
            elif(speech == "what is my "+rem_que_list[2]):
                repl_remb(2)
                app()
            elif(speech == "what is my "+rem_que_list[3]):
                repl_remb(3)
                app()        '''
