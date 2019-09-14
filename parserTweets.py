from bs4 import BeautifulSoup
from pathlib import Path
import requests
import os

def processTweets(data,lokalizacja):
    keyWordClass = 'TweetTextSize'

    while True:
        print("PARSOWANIE TEKSTU ODBYWA SIE DLA ZNACZNIKOW Z ATRYBUTEM CLASS = 'TweetTextSize'\nCZY ZACHOWAĆ USTAWIENIA? [t/n]")
        odpowiedz = input(">>   ").lower()
        if(odpowiedz=="t"):
            break
        elif(odpowiedz=="n"):
            keyWordClass=input("WPROWADZ INNĄ WARTOŚĆ DLA ATRYBUTU: CLASS\n>>   ")
            break

    soup = BeautifulSoup(data, 'lxml')
    elems = soup.find_all(True, class_=keyWordClass)

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

        new_words = elem.get_text().split(" ")

        for word in new_words:
            if word.find(".com") != -1 or word.find("pic.") != -1 or word.find("http") != -1 or word.find("#") != -1:
                print("usuwam: "+word)
                new_words.remove(word)

        f2.writelines(' '.join(new_words))

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
