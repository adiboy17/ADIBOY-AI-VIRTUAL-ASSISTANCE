import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import wolframalpha
import webbrowser as wb
import os
import pyfiglet
import smtplib
import requests,_json
from selenium import webdriver

from pprint import pprint
from selenium import webdriver

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    speak("Welcome back sir")
    hour = int(datetime.datetime.now().hour)
    print(hour)
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    print(Time)
    print(date)
    print(month)
    print(year)
    ascii_banner = pyfiglet.figlet_format("         ADIBOY")
    print(ascii_banner)
    print("[     YOUR VIRTUAL ASSISTANT HOW MAY I HELP YOU !!  ]")
    speak("I AM ADIBOY")
    speak(" YOUR VIRTUAL ASSISTANT HOW MAY I HELP YOU")
    speak("the current Time is")
    speak(Time)
    speak("the current Date is")
    speak(date)
    speak(month)
    speak(year)
    if hour >= 6 and hour < 12:
        speak("Good Morning adiboy!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon adiboy!")

    elif hour >= 18 and hour < 24:
        speak("Good Evening adiboy")

    else:
        speak("Good Night adiboy")

    speak("adiboy at your Service. Please tell me how can I help You ")


# wishMe()
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"adiboy Said:{query}\n")

    except Exception as e:
        print(e)
        print("Say that again Please...")
        speak("Say that again Please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('govindsingh277@gmail.com', 'Password')
    server.sendmail('govindsingh277@gmail.com', to, content)
    server.close()


def lighton():
    driver = webdriver.Chrome('C:\\Users\Pinki\Downloads\edgedriver_win64\msedgedriver.exe')  # add the location of the chrome Drivers
    driver.get("https://Add here.000webhostapp.com/main.html")  # Add the webhost name
    elem1 = driver.find_element_by_id("S1off")
    elem1.click()


def lightoff():
    driver = webdriver.Chrome('C:/Users/HACKER47/Downloads/chromedriver.exe')
    driver.get("https://Add here.000webhostapp.com/main.html")  # Add the webhost name
    elem1 = driver.find_element_by_id("S1on")
    elem1.click()



if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'internet' in query:
            speak("what should i search?")
            chrome_path = 'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe %s'  # Add the Location of the chrome browser

            r = sr.Recognizer()

            with sr.Microphone() as source:
                print('say something!')
                audio = r.listen(source)
                print("done")
            try:
                text = r.recognize_google(audio)
                print('google think you said:\n' + text + '.com')
                wb.get(chrome_path).open(text + '.com')
            except Exception as e:
                print(e)

        elif 'how is the weather' and 'weather' in query:
            api_key = "a164dad277139aad3353c00e8c424106"
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            #city_name = input("Kanpur, IN : ")
            url = base_url + "appid=" + api_key + "&q=" + "Kanpur, IN"  # Open api link here

            res = requests.get(url)

            data = res.json()

            weather = data['weather'][0]['main']
            temp = data['main']['temp']
            wind_speed = data['wind']['speed']

            latitude = data['coord']['lat']
            longitude = data['coord']['lon']

            description = data['weather'][0]['description']
            speak('Temperature : {} degree celcius'.format(temp))
            print('Wind Speed : {} m/s'.format(wind_speed))
            print('Latitude : {}'.format(latitude))
            print('Longitude : {}'.format(longitude))
            print('Description : {}'.format(description))
            print('weather is: {} '.format(weather))
            speak('weather is : {} '.format(weather))


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'the date' in query:
            year = int(datetime.datetime.now().year)
            month = int(datetime.datetime.now().month)
            date = int(datetime.datetime.now().day)
            speak("the current Date is")
            speak(date)
            speak(month)
            speak(year)


        elif 'email to akashdeep' and 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "akashdeepg196@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend . I am not able to send this email")

        elif 'media' in query:
            codePath = "C:\Program Files (x86)\Windows Media Player\wmplayer.exe"  # ADD THE PATH OF THE PROGRAM HERE
            os.system("wmplayer")


        elif 'explorer' in query:
            os.system('explorer C://{}'.format(query.replace('Open', '')))


        elif 'turn on lights' in query:
            speak("OK,sir turning on the Lights")
            lighton()
            speak("Lights are on")

        elif 'turn off lights' in query:
            speak("OK,sir turning off the Lights")
            lightoff()
            speak("Lights are off")

        elif 'search' in query:
            speak("ok")
            url = "https: // www.google.co. in /" + "add"


        elif 'google' in query:
            try:
                from googlesearch import search
            except ImportError:
                print("No module named 'google' found")

                # to search
            query = "www.google.com"

            for j in search(query, tld="co.in", num=10, stop=10, pause=2):
                print(j)

        elif 'calculator' in query:
            os.system("calc")

        elif 'atom' in query:
            os.system("atom")

        elif 'notepad' in query:
            os.system("notepad")

        elif 'command' in query:
            os.system("control")

        elif 'control' in query:
            os.system("calc")

        elif 'bluetooth' in query:
            os.system("fsquirt")

        elif 'manifyer' in query:
            os.system("magnify")

        elif 'task' in query:
            os.system("launchtm")

        elif 'paint' in query:
            os.system("mspaint")

        elif 'account' in query:
            os.system("netplwiz")

        elif 'keyboard' in query:
            os.system("osk")

        elif 'performance' in query:
            os.system("perfmon")

        elif 'step' in query:
            os.system("psr")

        elif 'snipping' in query:
            os.system("snippingtool")

        elif 'volume' in query:
            os.system("sndvol")

        elif 'window' in query:
            os.system("winver")

        elif 'wordpad' in query:
            os.system("write")

        elif 'python' in query:
            os.system("py")

        elif 'explorer' in query:
            os.system("snippingtool")

        elif 'vlc' in query:
            os.system("vlc")

        elif 'browser' in query:
            os.system("msedge")

        elif 'calculator' in query:
            speak("are you sure sir")
            os.system("calc")
            speak("Thanku")

        elif "made" in query:
            speak("Govind Singh is my creater")

        elif "who are you" in query:
            speak("I am virtual assistant created by govind singh ")


        elif "bye bye" in query:
            speak("ok sir shutting down the system")
            quit()


