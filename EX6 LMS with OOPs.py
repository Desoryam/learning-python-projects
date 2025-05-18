# LIBRARY MANAGMENT SYSYTEM USING OOPS

class library:
  def __init__(self,B):
    self.booklist=B
    self.no=len(self.booklist)

  def check(self):
    print()
    if self.no==len(self.booklist):
      print("there are no errors in the system")
    else:
      print("there is an error in the ")

  def show(self):
    print()
    for a,i in enumerate(self.booklist,start=1):
      
      print(f"{a} ---- {i} ")
      
  def add(self):
    while True:
      print()
      ad=input("Enter the book name :")
      (self.booklist).append(ad)
      self.no+=1
      print("book added successfully ")
      ch=input("do you want to add more books(Y/N) :")
      if ch in "Nn":
        break
    
  def remove(self):
      while True:
        self.show()
        print()
        rm=int(input("Enter the book number to remove :"))
        (self.booklist).pop((rm-1))
        self.no-=1
        print("book removed successfully ")
        ch=input("do you want to remove more books(Y/N)")
        print()
        if ch in "Nn":
          break
    
l1=library([])
print(dir(library))
while True:
  print()
  print("1. Add book")
  print("2. Remove book")
  print("3. Show book")
  print("4. Check system")
  print("5. Exit")
  ch=int(input("Enter your choice :"))
  if ch==1:
    l1.add()
  elif ch==2:
    l1.remove()
  elif ch==3:
    l1.show()
  elif ch==4:
    l1.check()
  elif ch==5:
    break
  else:
    print("INVALID INPUT XXXXX****")