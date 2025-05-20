# SIMPLE CALCULATOR

while True:
    print("CALCULATOR".center(150))
    a=int(input("ENTER YOUR FIRST No. :"))
    b=int(input("ENTER YOUR SECOND No. :"))
    print("1. ADD/n2. SUBTRACT/n3. MULTIPLY/n4. DIVIDE/n5. EXIT")
    c=int(input("ENTER YOUR CHOICE (y/n):"))
    if c==1:
        print("ADDITION IS :",a+b)
    elif c==2:
        print("SUBTRACTION IS :",a-b)
    elif c==3:
        print("MULTIPLICATION IS :",a*b)
    elif c==4:
        print("DIVISION IS :",a/b)
    elif c==5:
        print("THANK YOU FOR USING CALCULATOR :)")
        break
    else:
        print("INVALID CHOICE")
    
