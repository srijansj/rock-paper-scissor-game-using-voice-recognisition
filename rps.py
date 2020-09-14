import pyaudio
import speech_recognition as sr
import smtplib
import pyttsx3
import datetime
import random
engine=pyttsx3.init('sapi5')


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wish():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning! Welcome to rock paper scissor")
    elif hour>=12 and hour<18:
        speak("Good AfterNoon! Welcome to rock paper scissor")
    else:
        speak("Good Evening! Welcome to rock paper scissor")
    speak("Let's Start the Game")

def t():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        speak("Your Turn")
        #r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        q=r.recognize_google(audio, language='en-in')
        print(f"You Choose: {q}")
    except Exception as e:
        print("Say that again please....")
        return None
    return q
wish()
speak("Please Enter your name")
name=input()
#e=t()
#speak("You Choose")
#speak(e)
#computer=('rock','paper','scissors')
#computer=random.choice(computer)
#print(f"Computer Choose {computer}")
#speak("computer choose:")
#speak(computer)
lives = 2
score = 0
draw = 0
cscore=0
while lives>0:
    e=t()
    if e==None:
        continue
    
    speak("You Choose")
    speak(e)
    computer=('rock','paper','scissors')
    computer=random.choice(computer)
    print(f"Computer Choose {computer}")
    speak("computer choose:")
    speak(computer)
    if e.lower() == "rock" and computer == "paper":
        speak("oh no You Loose")
        speak(f"your Score is {score} ")
        cscore+=1
        lives-=1
    if e.lower() == "rock" and computer == "scissors":
        score+=1
        lives-=1
        speak("Congratulations You win")
        speak(f"your score {score}")
    if e.lower() == "paper" and computer == "rock":
        score+=1
        lives-=1
        speak("Congratulations You win")
        speak(f"your score {score}")
    if e.lower() == "paper" and computer == "scissors":
        speak("oh no You Loose")
        speak(f"your Score is {score} ")
        cscore+=1
        lives-=1

    if e.lower() == "scissors" and computer == "paper":
        score+=1
        lives-=1
        speak("Congratulations You win")
        speak(f"your score {score}")
    if e.lower() == "scissors" and computer == "rock":
        speak("oh no You Loose")
        speak(f"your Score is {score} ")
        lives-=1
        cscore+=1


    if e.lower() == "rock" and computer == "rock":
        speak("Both choose rock game draw")
        speak(f"your score {score}")
        lives-=1

    if e.lower() == "paper" and computer == "paper":
        speak("Both choose paper game draw")
        speak(f"your score {score}")
        lives-=1
    if e.lower() == "scissors" and computer == "scissors":
        speak("Both choose scissors game draw")
        speak(f"your score {score}")
        lives-=1

                        
speak("Game Complete")
if score>cscore:
    speak("you win the game")
elif score<cscore:
    speak("You loose the game")
else:
    speak("game is draw")
speak(f"Thank you for playing {name}")
