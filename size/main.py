import os

def get_size(dir):
    total=0
    for path,name,files in os.walk(dir):
        for f in files:
            total += os.path.getsize(os.path.join(path,f))
    return total

while True:
    print("WELCOME TO SIZE ANALYZER".center(125))
    print("press q to quit")
    dir=input("write the folder name:")

    if dir!="q":
        try:
            size= get_size(dir)
            print(f"the size of {dir} is {size * 10**-6} MB")
        except:
            print("SOMETHING WENT WRONG :(")
    else:
        print("THANK YOU USING THIS :)")
        break
