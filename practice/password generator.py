from random import choice as c
from random import randint as rn

x="QWERTYUIOPASDFGHJKLZXCVBNNM=-0987654321~!@#$%&*\"\"qwertyuiopasdfghjklzxcvbnm"
y="QWERTYUIOPASDFGHJKLZXCVBNNMqwertyuiopasdfghjklzxcvbnm"
k="QWERTYUIOPASDFGHJKLZXCVBNNM=-~!@#$%&*\"\"qwertyuiopasdfghjklzxcvbnm"
z="QWERTYUIOPASDFGHJKLZXCVBNNM0987654321qwertyuiopasdfghjklzxcvbnm"

def k_pas_gen(l):
    for i in range(rn(8,l)):
        pas=c(k)
        print(pas,end="")

def x_pas_gen(l):

    for i in range(rn(8,l)):
        pas=c(x)
        print(pas,end="")

def y_pas_gen(l):

    for i in range(rn(8,l)):
        pas=c(y)
        print(pas,end="")

def z_pas_gen(l):

    for i in range(rn(8,l)):
        pas=c(z)
        print(pas,end="")

while True:

    a=int(input("How many password do you want to generate: "))
    le=int(input("enter maximum length of password (more than 8):"))
    sp=input("Do you want to include special characters? (Y/N):")
    no=input("Do you want to include numbers? (Y/N):")
    if le>=8:
        if sp in "Yy" and no in "Yy":
            for o in range(a):
                x_pas_gen(le)
                print()
        elif sp in "Nn" and no in "Nn":
            for o in range(a):
                y_pas_gen(le)
                print()
    
        elif sp in "Yy" and no in "nN":

            for o in range(a):
                k_pas_gen(le)
                print()
        elif sp in "Nn" and no in "Yy":
            for o in range(a):
                z_pas_gen(le)
                print()
        else:
            print("invalid input")
            print()
        ch=input("Do you want to generate more? (Y/N):")
        if ch in "Nn":
            print("thank you for using this....")
            break
    else:
        print("length should be more than 8")
