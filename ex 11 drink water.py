# DRINK WATER REMINDER
import time 
import asyncio as ac
from win10toast import ToastNotifier
import win32com.client


# speaker object
speaker = win32com.client.Dispatch("SAPI.SpVoice")


# create an object to ToastNotifier class
n = ToastNotifier()

async def noti():
    n.show_toast("DRINK 250ml WATER RN!!", f"It's currently {ct}", duration = 10, 
icon_path =None)
    return 0
   
async def sound():
    speaker.Speak("TIME TO DRINK WATER")
    return 1

async def main():
    t2=ac.create_task(sound())
    r2=await t2
    t1=ac.create_task(noti())
    r1= await t1
    
    print(r2,r1)





print("WELCOME TO WATER REMINDER APP".center(150))
print()
inte=eval(input("ENTER THE INTERVALS (in mins):"))


while True:
    ct= time.strftime("%H:%M")

    ac.run(main())
    # making it repeat after the following interval
    time.sleep(60*inte)
