from os import system, name
from time import sleep
import sys
import os.path
import json
import random
import requests

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def learn2(chain, filePath,order_m=1):
    tokens = [] 
    fileHandler = open(filePath,"r")
    for line in fileHandler:  
        line = line.replace('\r', ' ').replace('\n', ' ').replace(',', '').replace('!', '').replace('"','').replace('.', '')

        new_words = line.split()

        for word in new_words:
            new_words = [word.lower() for word in new_words if word not in ['', ' ']]
        tokens = tokens + new_words

    print('Rozmiar korpusu to: {0} tokeny.'.format(len(tokens))) 
    
#    tokens = fileHandler.split(" ")
    
    if order_m == 1:
        for i in range(0,len(tokens)-1):
            currWord = tokens[i]
            nextWord = tokens[i+1]

            if currWord not in chain:
                chain[currWord] = {nextWord:1}
            else:
                # exist in chain
                allNextWords = chain[currWord]

                if nextWord not in allNextWords:
                    #add new state
                    chain[currWord][nextWord] = 1
                else:
                    chain[currWord][nextWord] = chain[currWord][nextWord]+1
    elif order_m>1 and order_m <5:
        for i, keyV in enumerate(tokens):  
            if len(tokens) > i + order_m:

                keys = list()

                for ii in range(1,order_m):
                    keys.append(tokens[i+ii])

                word = tokens[i + order_m]

                if (keyV, *keys) not in chain:
                    chain[(keyV, *keys)] = [word]
                else:
                    chain[(keyV, *keys)].append(word)
    else:
        exit()
        
    print('\nŁańcuch Markova składa się z: {0} par słów.\n'.format(len(chain)))
    return tokens,chain


def markov_tweet(chain, words,order_m,length):  
    print(chain)
    r = random.randint(0, len(words) - order_m)
#    key = ('porozumienie', 'na','rzecz')

    if order_m==2:
        key = (words[r], words[r + 1])
        tweet = key[0] + ' ' + key[1]
    if order_m==3:
        key = (words[r], words[r + 1],words[r + 2])
        tweet = key[0] + ' ' + key[1] + ' ' + key[2]
    if order_m==4:
        key = (words[r], words[r + 1],words[r + 2],words[r + 3])
        tweet = key[0] + ' ' + key[1] + ' ' + key[2]+ ' ' + key[3]
    else:
        exit()
            
    i=0
            
    while i<length:
        w = random.choice(chain[key])
        if (len(tweet) + len(w)) >= 200 and len(w)<4:
            w = ""
        tweet += ' ' + w

        if order_m==2:
            key = (key[1],w)
        if order_m==3:
            key = (key[1],key[2], w)
        if order_m==4:
            key = (key[1],key[2],key[3], w)
        else:
            exit()
        i+=1
    print(tweet + '\n')
