import requests
import json


while True:
  print("WELCOME TO THE NEWS APP".center(10))
  print()
  type=input("Enter the topic of your interest\nOR ENTER q to quit:")
  print()
  if type!="q":
    url=f"https://newsapi.org/v2/everything?q={type}&from=2025-04-03&sortBy=publishedAt&apiKey=3d559f9483cc428eb4b0ebf33d524e1c"
    r=requests.get(url)
    news=json.loads(r.text)
    for art in news["articles"]:
      sor=art["source"]["name"]
      print(f"From {sor}")
      print()
      print(art["title"])
      print()
      print(art["description"])
      print()
      print("For more information vsit:")
      print(art["url"])
      print("----------------------------------------------")
    # print(news)

  else:
    print("THANK YOU FOR USING THIS APP")
    break


