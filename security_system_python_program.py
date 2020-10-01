# pip install pyttsx3
import pyttsx3
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Here i create a function for the program to speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# this is a function to wish the user
def wish_user():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak('Good Morning')
    elif hour >= 12 and hour <= 18:
        speak('Good Afternoon')
    else:
        speak('Good evening')

wish_user()

speak("Enter your name")
name = input("Enter your name: ")
print(f"Hi {name}, hope you are doing fine :)")
speak(f"Hi {name}, hope you are doing fine :)")


secret_answer = "I love my family".lower()
while True:
    output = input("Enter the password: ")
    if output == secret_answer:
            print("The password you entered is correct")
            speak("The password you entered is correct")
            break

    else:
        speak('Sorry password is wrong')

        # this is the code to capture the image (photo)
        from cv2 import *

        cam = VideoCapture(0)
        s, img = cam.read()
        if s:
            namedWindow("Eric Codes cam-test")
            imshow("Eric Codes cam-test", img)
            waitKey(0)
            destroyWindow("cam-test")
            imwrite("test.jpg", img)
        cv2.destroyAllWindows()

        # generating the otp
        import random
        otp = random.randint(1000, 9999)

        # for sending the message via SMS
        # also you have to install twilio - pip install twilio , and go to its official website to get your account number, etc.
        def sms_otp():
            from twilio.rest import Client

            account_sid = ' # your account '
            auth_token = ' # your auth token'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                from_= '# your twilio account number',
                body=f'Hello Sir, A person named {name} is in your car at {datetime.datetime.now()}, your otp - {otp}',
                to='# your phone number',

            )

            print(message.sid)
        sms_otp()

        print(otp)
        enter_otp = input("The password you entered is wrong, now you have to enter the otp: ")

        if enter_otp == str(otp):
           print('The otp you entered is correct')
           break

        else:
            print('Sorry, The otp you entered is wrong ')
            sms_otp()
