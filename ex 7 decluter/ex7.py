
#python file declutor
import os

e=[".",".png",".jpeg",".txt",".docx",".csv",".mp3",".mp4"]
n=0
def declu(ext,l):
    global n
    if l==ext:
    
        os.rename(f"{fol}/{file}",f"{fol}/{n}{l}")
        n+=1

while True:
    print("welcome to FILE DECLUTER".center(150))
    fol=input("Enter the name or path of the folder:".capitalize())

    if  os.path.exists(fol):
        folder=os.listdir(fol)
        print("1. png\n2. jpeg\n3. text\n4. docx\n5. CSV\n6. MP3\n7. MP4")
        print("0. EXIT")
        ch=int(input("Enter your choice:"))
        if ch==1:
            for file in folder:
                tup=os.path.splitext(file)
                ex=tup[1]
                na=tup[0]

                declu(e[1],ex)
            print("CHANGE HAS TAKKEN PLACE SUCCESFULLY")
        elif ch==2:
            for file in folder:
                tup=os.path.splitext(file)
                ex=tup[1]
                na=tup[0]
                declu(e[2],ex)
            print("CHANGE HAS TAKKEN PLACE SUCCESFULLY")
        elif ch==3:
            for file in folder:
                tup=os.path.splitext(file)
                ex=tup[1]
                na=tup[0]
                declu(e[3],ex)
            print("CHANGE HAS TAKKEN PLACE SUCCESFULLY")
        elif ch==4:
            for file in folder:
                tup=os.path.splitext(file)
                ex=tup[1]
                na=tup[0]
            
                declu(e[4],ex)
            print("CHANGE HAS TAKKEN PLACE SUCCESFULLY")
        elif ch==5:
            for file in folder:
                tup=os.path.splitext(file)
                ex=tup[1]
                na=tup[0]
                declu(e[5],ex)
            print("CHANGE HAS TAKKEN PLACE SUCCESFULLY")
        elif ch==6:
            for file in folder:
                tup=os.path.splitext(file)
                ex=tup[1]
                na=tup[0]
                declu(e[1],ex)
            print("CHANGE HAS TAKKEN PLACE SUCCESFULLY")
        elif ch==7:
            for file in folder:
                tup=os.path.splitext(file)
                ex=tup[1]
                na=tup[0]
                declu(e[7],ex)
            print("CHANGE HAS TAKKEN PLACE SUCCESFULLY")
        elif ch==0:
            print("thank you for using this")
            break
        else:
            print("INVALID CHOICE")

        


    else:
        print("folder does not exist")
        break