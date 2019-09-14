#Modul rozszerza "MAIN" o możliwość tworzenia łąncuhców Markoba rzędu: 2, 3 i 4

from parserTweets import *
from modules2 import *
import random

def menu():
    clear()
    print("PROGRAM DO GENEROWANIA TWEETÓW (MARKOVCHAIN)\n")

    while True:
        print("=========================MENU========================")
        print("[1]  PRZYGOTUJ TEKST")
        print("[2]  WYGENERUJ TEKST")
        print("[q]  ZAKOŃCZ")
        print("=====================================================")

        choice = input("[WYBIERAM OPCJE]\n>>  ")

        if choice == "1":
            clear()
            while True:
                print("[PRZYGOTUJ TEKST][WYBIERZ ŹRÓDŁO]:")
                print("=====================================================")
                print("     [1] TWITTER [nick]")
                print("     [2] PLIK TXT/HTML [CLASS='']")
                print("     [q] WYJDŻ")
                print("=====================================================")
                answer = input("[WYBIERAM OPCJE]\n>>  ")

                if answer == "1":
                    clear()
                    while True:
                        print("[PRZYGOTUJ TEKST][WYBIERZ KATERGORIE]:")
                        print("=====================================================")
                        print("     [1] POLITYKA / morawieckim")
                        print("     [2] AKTUALNOSCI / tvp_info")
                        print("     [3] MUZYKA / Piotr_Rubik")
                        print("     [4] INNE / WPROWADZ NICK")
                        print("     [q] WYJDŻ")
                        print("=====================================================")
                        nextAnswer = input("[WYBIERAM OPCJE]\n>>  ")
                        if nextAnswer == "1":
                            getTweetsFromTwitter("morawieckim")
                        elif nextAnswer == "2":
                            getTweetsFromTwitter("tvp_info")
                        elif nextAnswer == "3":
                            getTweetsFromTwitter("Piotr_Rubik")
                        elif nextAnswer == "4":
                            while True:
                                nick = input("WPROWADZ NICK LUB PRZERWIJ(q)\n>>  ")

                                if nick=="q":
                                    print("--- PRZERWANO! ---")
                                    break

                                link = "https://twitter.com/"+str(nick)+"?lang=pl"
                                ret =  requests.get(link)

                                if ret.status_code == 200:
                                    break
                                else:
                                    print ("--- URL NOT EXIST! ---")
                            getTweetsFromTwitter(nick)
                        elif nextAnswer == "q":
                            clear()
                            break
                        else:
                            print("--- NIEPRAWIDŁOWY WYBÓR ---")

                elif answer == "2":
                    clear()
                    while True:
                        print("[POBIERZ TEKST Z TWEETOW][PLIK TXT/HTML]:")
                        while True:
                            pathToFile = input("WPROWADZ ŚCIEŻKĘ DO PLIKU:\n>>  ")
                            if pathToFile == "q":
                                break
                            elif not os.path.exists(pathToFile):
                                print("--- PODANA ŚCIEŻKA NIE ISTNIEJE! ---")
                            else:
                                clear()
                                print("--- OK - POLECENIE W TRAKCIE PRZETWARZANIA ---")
                                getTweetsFromFile(pathToFile)
                                break
                        break
                    break
                elif answer == "q":
                    clear()
                    break
                else:
                    print("--- NIEPRAWIDŁOWY WYBÓR ---")
        else:
            clear()
            break



def prepareCorpus(filePath,order_m):
    text = open(filePath,"r")
    words = []
    for line in text:
        line = line.replace('\r', ' ').replace('\n', ' ').replace(',', '').replace('!', '').replace('"','').replace('.', '')

        new_words = line.split()

        for word in new_words:
            new_words = [word.lower() for word in new_words if word not in ['', ' ']]
        words = words + new_words

    print('Corpus size: {0} words.'.format(len(words)))

    chain = {}
    n_words = len(words)
    for i, keyV in enumerate(words):
        if n_words > i + order_m:

            keys = list()

            for ii in range(1,order_m):
                keys.append(words[i+ii])

            word = words[i + order_m]

            if (keyV, *keys) not in chain:
                chain[(keyV, *keys)] = [word]
            else:
                chain[(keyV, *keys)].append(word)

    print('\nChain size: {0} distinct word pairs.\n'.format(len(chain)))

    #    print(chain)
    return chain,words

def markov_tweet2(chain, words,r):
    order_m =2
    # r = random.randint(0, len(words) - order_m)

    key = (words[r], words[r + 1])
    tweet = key[0] + ' ' + key[1]

    while len(tweet) < 250:
        w = random.choice(chain[key])
        tweet += ' ' + w
        key = (key[1],w)
    print(tweet + '\n')

def markov_tweet3(chain, words,r):
    order_m = 3

    r = random.randint(0, len(words) - order_m)

    key = (words[r], words[r + 1],words[r + 2])
    tweet = key[0] + ' ' + key[1] + ' ' + key[2]

    while len(tweet) < 250:
        w = random.choice(chain[key])
        tweet += ' ' + w
        key = (key[1],key[2], w)
    print(tweet + '\n')

def markov_tweet4(chain, words,r):
    order_m = 4

    key = (words[r], words[r + 1],words[r + 2],words[r + 3])
    tweet = key[0] + ' ' + key[1] + ' ' + key[2]+ ' ' + key[3]

    while len(tweet) < 250:
        w = random.choice(chain[key])
        tweet += ' ' + w
        key = (key[1],key[2],key[3], w)
    print(tweet + '\n')

if __name__ == '__main__':
    menu()
    filePath = input("podaj sciezke do pliku tekstowego [np.: tweets/tvp_infoT.txt]:\n>>    ")
#Przypadek 1
    for i in [2,3,4]:
        chain = {}
        words = []

        order_m = i

        chain,words = prepareCorpus(filePath,order_m)

        for ii in [1,2,3,4,5]:
            rr  = random.randint(0, len(words) - order_m)
            print("--- MARKOV CHAIN ORDER = "+str(order_m)+", rr = "+str(rr))

            if order_m == 2:
                markov_tweet2(chain, words,rr)
            if order_m == 3:
                markov_tweet3(chain, words,rr)
            if order_m == 4:
                markov_tweet4(chain, words,rr)



#Przypadek 2
#    for i in [2,3,4]:
#        chain = {}
#        words = []
#
#        order_m = i
#        rr = 88
#
#        print("--- MARKOV CHAIN ORDER = "+str(order_m)+", rr = "+str(rr))
#        chain,words = prepareCorpus("tweets/morawieckimT.txt",order_m)
#
#        for i in range(5):
#            if order_m == 2:
#                markov_tweet2(chain, words,rr)
#            if order_m == 3:
#                markov_tweet3(chain, words,rr)
#            if order_m == 4:
#                markov_tweet4(chain, words,rr)

#https://medium.com/@jdwittenauer/markov-chains-from-scratch-33340ba6535b
