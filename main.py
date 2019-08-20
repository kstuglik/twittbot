from parserTweets import getTweets
from modules import *


def menu():
    clear()
    print("PROGRAM DO GENEROWANIA TWEETÓW (MARKOVCHAIN)\n")

    while True:
        print("=========================MENU========================")
        print("[1]  POBIERZ TWEETY WYBRANEJ OSOBY")
        print("[2]  UTWÓRZ SŁOWNIK")
        print("[3]  WYGENERUJ TEKST NA PODSTAWIE SŁOWNIKA")
        print("[4]  WYCZYSC EKRAN W OKNIE KONSOLI")
        print("[q]  ZAKOŃCZ DZIAŁANIE PROGRAMU")
        print("=====================================================")

        choice = input("[WYBIERAM OPCJE]\n>>  ")

        if choice == "1":
            clear()
            while True:
                print("[POBIERZ TWEETY WYBRANEJ OSOBY][WYBÓR KATERGORII]:")
                print("=====================================================")
                print("     [1] POLITYKA / morawieckim")
                print("     [2] AKTUALNOSCI / tvp_info")
                print("     [3] MUZYKA / Piotr_Rubik")
                print("     [4] INNE / WPROWADZ NICK")
                print("     [q] WYJDŻ")
                print("=====================================================")
                answer = input("[WYBIERAM OPCJE]\n>>  ")
                if answer == "1":
                    getTweets("morawieckim")
                elif answer == "2":
                    getTweets("tvp_info")
                elif answer == "3":
                    getTweets("Piotr_Rubik")
                elif answer == "4":

                    while True:
                        nick = input("WPROWADZ NICK LUB PRZERWIJ(q)\n>>  ")

                        if nick=="q":
                            print("PRZERWANO!")
                            break

                        link = "https://twitter.com/"+str(nick)+"?lang=pl"
                        ret =  requests.get(link)

                        if ret.status_code == 200:
                            break
                        else:
                            print ("URL NOT EXIST!")

                    getTweets(nick)
                elif answer == "q":
                    clear()
                    break
                else:
                    print("nieprawidłowy wybór")

        if choice == "2":
            clear()

            dictFile = input("WPROWADZ NAZWĘ PLIKU SŁOWNIKA Z *.json\n>>  ")
            if not os.path.exists(dictFile):
                file = open(dictFile,"w")
                json.dump({},file)
                file.close()
            file = open(dictFile,"r")

            dictionary = json.load(file)
            file.close()

            clear()

            while True:
                print("[UTWÓRZ SŁOWNIK]:\n")
                print("=====================================================")
                print("     [1] Z PLIKU TEKSTOWEGO")
                print("     [2] Z TEKSTU WPROWADZONEGO Z KLAWIATURY")
                print("     [q] WYJDŻ")
                print("=====================================================")
                answer = input("[WYBIERAM OPCJE]\n>>  ")
                clear()
                if answer == "1":

                    while True:
                        print("\n[PRZYKŁADOWA LOKALIZACJA PLIKU: tweets/t_nick.txt]\n")
                        inputFile = input("WPROWADZ LOKALIZACJE PLIKU, KTÓRY CHCESZ WCZYTAĆ LUB PRZERWIJ(q)\n>>  ")
                        if inputFile == "q":
                            clear()
                            break
                        elif not os.path.exists(inputFile):
                            print("NIE ODNALEZIONO!")
                        else:
                            break

                    if inputFile!="q":
                        f=open(inputFile, "r")
                        if f.mode == 'r':
                            # contents =f.read()
                            fileName =f.read()
                            print (fileName)

                            dictionary = learn(dictionary,fileName)
                            updateFile(dictFile,dictionary)
                    break
                elif answer == "2":
                    while True:
                        fileName = input("WPROWADZ TEKST\n>>  ")
                        if fileName == "":
                            break
                        dictionary = learn(dictionary,fileName)
                        updateFile(dictFile,dictionary)
                    break
                elif answer == "q":
                    clear()
                    break
                else:
                    print("nieprawidłowy wybór")
        if choice == "3":
            clear()
            print("[WYGENERUJ TEKST NA PODSTAWIE SŁOWNIKA]\n")
            while True:
                answer = input("WPROWADŹ NAZWĘ ISTNIEJĄCEGO SŁOWNIKA *.json LUB PRZERWIJ(q)\n>>  ")
                if answer == "q":
                    clear()
                    break
                elif not os.path.exists(answer):
                    print("NIE ODNALEZIONO!")
                else:
                    break

            if answer!="q":
                dictionary = loadDict(answer)

                length = input("OKREŚL LICZBĘ WYRAZÓW W WIADOMOŚCI\n>>  ")

                lastWord = ""
                result = ""

                for i in range(0,int(length)):
                    newWord = getNextWord(lastWord,dictionary)
                    result = result + " " + newWord
                    lastWord = newWord
                print("\n"+result+"\n")
        if choice == "4":
            clear()
        if choice == "q":
            break


if __name__ == '__main__':
    menu()
