from bs4 import BeautifulSoup
from pathlib import Path
import requests
import os

def processTweets(data,lokalizacja):
    soup = BeautifulSoup(data, 'lxml')
    elems = soup.find_all(True, class_='TweetTextSize')

    print("\n")
    for elem in elems:
        print(elem.get_text())
    print("\n")

    i=0

    directory = "tweets"
    if not os.path.exists(directory):
        os.makedirs(directory)

    f   = open(lokalizacja+"P.txt","w+")
    f2  = open(lokalizacja+"T.txt","w+")

    for elem in elems:
        i+=1
        f.write("#"+str(i)+"\n"+elem.get_text()+"\n")
        f2.write(elem.get_text())
    f.close()
    f2.close()
    print("ZAPISANO "+str(i)+" TWEETOW:\n"+lokalizacja+"P.txt\n"+lokalizacja+"T.txt\n")

def getTweetsFromTwitter(nick):
    lokalizacja = "tweets/"+str(nick)
    link = "https://twitter.com/"+str(nick)+"?lang=pl"
    r  = requests.get(link)
    data = r.text
    processTweets(data,lokalizacja)

def getTweetsFromFile(pathToFile):
    fileName = Path(pathToFile).stem
    lokalizacja = "tweets/"+fileName
    data = open(pathToFile)
    processTweets(data,lokalizacja)
