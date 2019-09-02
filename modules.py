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

def loadDict(dictFile):
    if not os.path.exists(dictFile):
        file = open(dictFile,"w")
        json.dump({},file)
        file.close()
    file = open(dictFile,"r")
    dictionary = json.load(file)
    file.close()
    return dictionary

def learn(dict,inp):
    tokens = inp.split(" ")
    for i in range(0,len(tokens)-1):
        currWord = tokens[i]
        nextWord = tokens[i+1]
        if currWord not in dict:
            dict[currWord] = {nextWord:1}
        else:
            # exist in dict
            allNextWords = dict[currWord]

            if nextWord not in allNextWords:
                #add new state
                dict[currWord][nextWord] = 1
            else:
                dict[currWord][nextWord] = dict[currWord][nextWord]+1
    return dict

def updateFile(fileName, dictionary):
    file = open(fileName,"w")
    json.dump(dictionary,file)
    file.close()
    print("--- OK - ZAPISANO ZAWARTOŚĆ SŁOWNIKA: "+fileName+" ---")

def getNextWord(lastWord,dictionary):
    if lastWord not in dictionary:
        #wez nowe
        newWord = randomWord(dictionary)
        return newWord
    else:
        candidates = dictionary[lastWord]
        candidatesNormalized = []

        for word in candidates:
            freq = candidates[word]
            for i in range(0,freq):
                candidatesNormalized.append(word)
        rnd = random.randint(0,len(candidatesNormalized)-1)
        return candidatesNormalized[rnd]

def randomWord(dict):
    randNum = random.randint(0,len(dict)-1)
    newWord = list(dict.keys())[randNum]
    return newWord
