import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")

na=[]

while True:
    print("WELCOME TO SHUTOUT GIVE")
    print("1. ENTER NAMES\n2. GIVE SHOUTOUT\n3. EXIT")

    print()
    ch=int(input("Enter your choice:"))
    if ch==1:
        while True:
            n=input("Enter the name:")
            na.append(n)
            c=input("Do you want to add more names??(Y/N)")
            if c in "Nn":
                break
    elif ch==2:
        if na == []:
            print("There are no names yet")
            break
        else:
            for name in na:
                speaker.Speak(f"SHOUTOUT TO {name}")
    else:
        print("thank you for using this :)")
        break