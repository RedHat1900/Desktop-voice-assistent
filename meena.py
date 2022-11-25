import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib 

engine = pyttsx3.init('sapi5')
voice= engine.getProperty('voice')
print(voice[0])
engine.setProperty('voice', voice[0])







def speak(audio):
    engine.say(audio) 
    engine.runAndWait() #Without this command, speech will not be audible to us.
     
     
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
        speak(" I am EDITH sir, Please tell me how can i help you")
   

    elif  hour>=12 and hour<18:
     speak("Good Afternoon!")
    speak(" I am EDITH sir, Please tell me how can i help you")
     
def takeCommand():
    #It takes microphone input from the user and returns string output

      r = sr.Recognizer()
      with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

      try:
    
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.


      except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
      return query

def sendEmail(to, content):    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('godlanas4@gmail.com', 'samar@1234') 
    server.sendmail('godlanas4@gmail.com', to, content)
    server.close() 

if __name__=="__main__" :
          speak("Hello Sir, i was made by TEAM Hex")
          wishme()

#while True:    
if 1:
         query = takeCommand().lower()
         if 'wikipedia' in query:
          speak('Serching wikipedia...')
          query = query.replace("wikipedia", "")
          result = wikipedia.summary(query, sentences=2)
          speak("According to wikipedia")
          print(result)
          speak(result)

         elif 'open youtube' in query:
             webbrowser.open("youtube.com") 
         elif 'open google' in query:
             webbrowser.open("google.com")
         elif 'open stackoverflow' in query:
             webbrowser.open("stackoverflow.com")
         elif 'open whatsapp' in query:
             webbrowser.open("whatsapp.com")
         elif 'open spotify' in query:
             webbrowser.open("spotify.com")
         elif 'open gmail' in query:
             webbrowser.open("gmail.com")

         elif 'the time' in query:
             strTime = datetime.datetime.now().strftime("%H:%M:%S")
             speak(f"sir, the time is{strTime}")

        
         elif 'open vs code' in query:
             codepath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
             os.startfile(codepath)
             
         elif 'email to adnan'in query:                                                                                                                                                                                                                                                                                                                                                                                                     
             try:
                 speak("What should I say?")
                 content = takeCommand()
                 to = "godlanas4@gmail.com"
                 sendEmail(to, content)
                 speak("Email has been sent!")
             except Exception as e: 
                 print(e)
                 speak("sorry sir i am not able to send the mail to adnan because of server issue sir ")
 
             
            
             
             
             


       
          

    
 