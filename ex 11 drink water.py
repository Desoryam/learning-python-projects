# DRINK WATER REMINDER
import time 
from win10toast import ToastNotifier
import win32com.client


# speaker object
speaker = win32com.client.Dispatch("SAPI.SpVoice")


# create an object to ToastNotifier class
n = ToastNotifier()





print("WELCOME TO WATER REMINDER APP".center(150))
print()
inte=int(input("ENTER THE INTERVALS (in mins):"))


while True:
    ct= time.strftime("%H:%M")

    # MAKING SOUND
    speaker.Speak("TIME TO DRINK WATER")

    # SENDING NOTIFICATION
    n.show_toast("DRINK 250ml WATER RN!!", f"It's currently {ct}", duration = 10, 
icon_path =None)
    
    # making it repeat after the following interval
    time.sleep(60*inte)
