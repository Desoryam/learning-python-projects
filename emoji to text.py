import demoji 
 
while True:
    print("WELCOME TO EMOJI TRANSLATOR".center(150))
    text=input("ENTER YOUR TEXT OR EMOJIES:")
    demoji.findall(text)
    ch=input("Do you wnat to do more(y/n):")
    if ch in "Nn":
        print("thank you for using :) ")
        break