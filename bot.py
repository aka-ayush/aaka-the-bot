from colorama import init
from termcolor import colored
import random
from time import sleep
import wmi
import speech_recognition as sr
import webbrowser
import pyttsx3
import os

os.system('color 70')

init()

'''0 = Black       8 = Gray
    1 = Blue        9 = Light Blue
    2 = Green       A = Light Green
    3 = Aqua        B = Light Aqua
    4 = Red         C = Light Red
    5 = Purple      D = Light Purple
    6 = Yellow      E = Light Yellow
    7 = White       F = Bright White'''

colors = ('red', 'yellow', 'green', 'cyan', 'blue', 'magenta')
bacg = "on_white"
latte = ['bold', 'dark', 'underline', 'blink', 'reverse', 'concealed']
atte = ['dark']

def speakText(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def alexa():
    with sr.Microphone() as source:
        r = sr.Recognizer() ; sleep(0.2)
        print(colored("\n                                                               listening...", random.choice(colors), bacg, atte))
        
        try:
            audio_text = r.listen(source)
            speak_text = r.recognize_google(audio_text)
            lower_speak_text = speak_text.lower()
            print(colored("                                                               "+lower_speak_text, random.choice(colors), bacg, atte))
            print(colored("", random.choice(colors), bacg))
            return lower_speak_text
        except:
            ac8 = "Sorry, I did not get that"
            print(colored(ac8, random.choice(colors), bacg, atte)); speakText(ac8) ; sleep(1)

nameList = []

def starting():
    aa1 = "Hi i am aaka"
    print(colored(aa1, random.choice(colors), bacg, atte)) ; speakText(aa1)
    aa2 = "the bot" 
    print(colored(aa2, random.choice(colors), bacg, atte)) ; speakText(aa2) ; sleep(1)

def ask_name():
    
    aa3 = "Whats your name?"
    print(colored(aa3, random.choice(colors), bacg, atte)) ; speakText(aa3)
    name = alexa() ; sleep(0.5)
    
    if (name == None):
        ask_name()    
    else:
        nameList.append(name)    
        weicome_string_list = (
            "hi "+nameList[0]+" nice to meet you" ,
            "what a wonderful day "+nameList[0] ,
            "welcome "+nameList[0] ,
            "hey "+nameList[0]+" i am very exciting to talk to you" ,
            "whats up! "+nameList[0] ,
            nameList[0]+"! "+"i dont hear this name in my whole life" , 
            "hey "+nameList[0]+" i belive you will like it bro"
        )
        aa4 = random.choice(weicome_string_list)
        print(colored(aa4, random.choice(colors), bacg, atte)) ; speakText(aa4) ; sleep(0.5)
        aa5 = "I am in a devloping process"
        print(colored(aa5, random.choice(colors), bacg, atte)) ; speakText(aa5) ; sleep(0.6)
        aa6 = "So i am providing you a list from \nyou can select an option"
        print(colored(aa6, random.choice(colors), bacg, atte)) ; speakText(aa6) ; sleep(1)
    
starting()
ask_name()

def sal():
    aa7 = "Enter time"
    print(colored(aa7, random.choice(colors), bacg, atte)) ; speakText(aa7)
    aa8 = "Hours : "
    print(colored(aa8, random.choice(colors), bacg, atte)) ; speakText(aa8)
    hours = alexa()
    hours = str(hours)
    aa9 = "Minutes : "
    print(colored(aa9, random.choice(colors), bacg, atte)) ; speakText(aa9)
    minutes = alexa() 
    minutes = str(minutes) ; sleep(0.6)
    ab1 = "Alarm set on "+hours+":"+minutes
    print(colored(ab1, random.choice(colors), bacg, atte)) ; speakText(ab1) ; sleep(2)

def trch(percent):
    brightness = int(percent)
    c = wmi.WMI(namespace="wmi")
    method = c.WmiMonitorBrightnessMethods()[0]
    method.WmiSetBrightness(brightness, 0)
    if(brightness == 100): 
        ab4 = "Maxed the brightness"
        print(colored(ab4, random.choice(colors), bacg, atte)) ; speakText(ab4)
    if(brightness == 0):
        ab5 = "Reduced the brightness"
        print(colored(ab5, random.choice(colors), bacg, atte)) ; speakText(ab5)    


def srhg():
    ab2 = "Tell me what you want to search or say exit to quit : "
    print(colored(ab2, random.choice(colors), bacg, atte)) ; speakText(ab2)
    search_string = alexa() ; sleep(1)
    if(search_string == None):
        srhg()
    elif(search_string == "exit"):
        print(colored("Quiting...", random.choice(colors), bacg, atte))    
    else:    
        search_string = str(search_string)
        url = "https://www.google.com.tr/search?q={}".format(search_string)
        webbrowser.open_new_tab(url)

def teljok():
    ac4 = (
        "Yesterday I saw a guy spill all his Scrabble letters on the road. I asked him, 'What’s the word on the street?'" ,
        "Hear about the new restaurant called Karma?" ,
        "A woman in labor suddenly shouted, 'Shouldn’t! Wouldn’t! Couldn’t! Didn’t! Can’t!'" ,
        "A bear walks into a bar and says, 'Give me a whiskey and … cola.'" ,
        "What do Alexander the Great and Winnie the Pooh have in common? Same middle name." ,
        "I was horrified when my wife told me that my six-year-old son wasn't actually mine. Apparently I need to pay more attention during school pick-up." ,
        "What is the opposite of a croissant? A happy uncle." ,
        "If April showers bring May flowers, what do May flowers bring? Pilgrims." ,
        "Which branch of the military accepts toddlers? The infantry." ,
        "Did you know you can actually listen to the blood in your veins? You just have to listen varicosely." ,
        "Though I enjoy the sport, I could never date a tennis player. Love means nothing to them." ,
        "I have a joke about time travel, but I'm not gonna share it. You guys didn't like it." ,
        "What's the opposite of irony? Wrinkly." ,
        "I was kidnapped by mimes once. They did unspeakable things to me." ,
        "Got a PS5 for my little brother. Best trade I've ever done!" ,
        "What do the movies Titanic and The Sixth Sense have in common? Icy dead people." ,
        "I finally decided to sell my vacuum cleaner. All it was doing was gathering dust!" ,
        "When you die, what part of the body dies last? The pupils…they dilate." ,
        "A friend of mine went bald years ago, but still carries around an old comb. He just can't part with it"
    )
    ac5 = random.choice(ac4)
    print(colored(ac5, random.choice(colors), bacg, atte)) ; speakText(ac5)

def whatname():
    print(colored(nameList[0], random.choice(colors), bacg, atte)) ; speakText("your name is "+nameList[0])

def ordfod():
    ab8 = "Coming soon..."
    print(colored(ab8, random.choice(colors), bacg, atte)) ; speakText(ab8) ; sleep(2)

def boktaxi():
    ab9 = "Coming soon..."
    print(colored(ab9, random.choice(colors), bacg, atte)) ; speakText(ab9) ; sleep(2)

def finsh():
    ac1 = "Closing..."
    print(colored(ac1, random.choice(colors), bacg, atte)) ; speakText(ac1)
    ac2 = "Thank you for using our app" 
    print(colored(ac2, random.choice(colors), bacg, atte)) ; speakText(ac2) ; sleep(2)
    print("---")

def app():
    print(colored("                               \n                          ", on_color = bacg))
    ab3 = ">> Set alarm \n>> On the torch \n>> Off the light \n>> Search on google \n>> Tell me a joke \n>> Order food \n>> Book a ride \n>> What is my name \n\nSay 'exit' for close the app" ; sleep(0.2)
    print(colored(ab3, random.choice(colors), bacg, atte))
    speech = alexa()
    if(speech == "set alarm"):
        sal()
        app()
    elif(speech == "on the torch"):
        trch(100) ; sleep(2)
        app()
    elif(speech == "search on google"):
        srhg() ; sleep(2)
        app()  
    elif(speech == "tell me a joke"):
        teljok() ; sleep(2)
        app()    
    elif(speech == "book a ride"):
        boktaxi()
        app()
    elif(speech == "order food"):
        ordfod()
        app()
    elif(speech == "off the light"):
        trch(0) ; sleep(2)
        app()
    elif(speech == "what is my name"):
        whatname()
        app()             
    elif(speech == "exit"):
        finsh()    
    else:
        ac9 = "Invalid option"
        print(colored(ac9, random.choice(colors), bacg, atte)) ; speakText(ac9)
        app()

app()
