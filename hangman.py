import random as r
words=["Pizza", "Spaghetti", "Tiger", "Giraffe","Octopus","Apple","Beach"
       ,"Clock","Dragon","Earth","Fruit","Guitar","Happy","Juice","Lemon"]

r_w=list((r.choice(words)).upper())
g=7
print("WELCOME TO HANGMAN".center(150))
print("YOUR WORD IS :")
g_w=[]
for i in r_w:
    g_w.append("_")

print(g_w)
print()
while True:
    print(f"GUESSES LEFT : {g}")
    p=input("Pick a letter:").upper()
    if p in "".join(r_w):
        for n,w in enumerate(r_w):
            if p==w:
                g_w[n]=p
            elif p!=w and  g_w[n]!="_":
                pass
            else:
                pass
    else:
        g=g-1
    print(g_w)
    if g==0:
        print("\nYOU LOST")
        print("\nTHANK YOU FOR PLAYING :)")
        break
    fw="".join(g_w)
    if "_" not in fw:
        print("\nYOU WON")
        print("\nTHANK YOU FOR PLAYING :)")
        break