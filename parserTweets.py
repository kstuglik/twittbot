from bs4 import BeautifulSoup
import requests
import os

def getTweets(nick):
    link = "https://twitter.com/"+str(nick)+"?lang=pl"
    r  = requests.get(link)
    data = r.text
    soup = BeautifulSoup(data,'lxml')

    elems = soup.find_all(True, class_='TweetTextSize')

    print("\n")
    for elem in elems:
        print(elem.get_text())
    print("\n")

    i=0

    directory = "tweets"
    if not os.path.exists(directory):
        os.makedirs(directory)

    f   = open("tweets/p_"+str(nick)+".txt","w+")
    f2  = open("tweets/t_"+str(nick)+".txt","w+")

    for elem in elems:
        i+=1
        f.write("#"+str(i)+"\n"+elem.get_text()+"\n")
        f2.write(elem.get_text())
    f.close()
    f2.close()
    print("ZAPISANO W LOKALIZACJI: tweets/t_"+str(nick)+".txt\n")
