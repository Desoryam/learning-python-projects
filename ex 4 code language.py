import random as r

x="abcdefghijklmnopqrstuvwxyzAABCDEFGHIJKLMNOPQRSTUVWXYZ"
def code(k):
  if len(k)>=3:
    a=list(k)
    o=a.pop(0)
    a.append(o)

    a=''.join(a)
    return (r.choice(x)+r.choice(x)+r.choice(x)+a+r.choice(x)+r.choice(x)+r.choice(x))
  else:
    return (i[::-1])

def decode(k):
    if len(k)>3:
      a=list(k)
      del a[:3]
      a.pop()
      a.pop()
      a.pop()
      o=a.pop()
      a.insert(0,o)
      a="".join(a)
      return a
    else:
      return (k[::-1])

while True:
  print("\n\n1.Code message \n2.Decode message \n3.Exit")
  ch=int(input("Enter your choice: "))
 
  
  if ch==1:
    u=input("enter your message:")
    s=u.split()
    for i in s:
      print(code(i),end=" ")
  elif ch==2:
    u=input("enter your message:")
    s=u.split()
    for i in s:
      print(decode(i),end=" ")
  elif ch==3:
    print("closing program bye")
    break
  else:
    print("Invalid choice")
    
