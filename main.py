from parserTweets import *
from modules import *


def menu():
    clear()
    print("PROGRAM DO GENEROWANIA TWEETÓW (MARKOVCHAIN)\n")

    while True:
        print("=========================MENU========================")
        print("[1]  POBIERZ TEKST Z TWEETOW/HTML")
        print("[2]  UTWÓRZ SŁOWNIK")
        print("[3]  WYGENERUJ TEKST ZE SŁOWNIKA")
        print("[4]  WYCZYSC EKRAN")
        print("[q]  ZAKOŃCZ")
        print("=====================================================")

        choice = input("[WYBIERAM OPCJE]\n>>  ")

        if choice == "1":
            clear()
            while True:
                print("[POBIERZ TEKST Z TWEETOW/HTML][WYBIERZ ŹRÓDŁO]:")
                print("=====================================================")
                print("     [1] TWITTER [nick]")
                print("     [2] PLIK TXT/HTML [CLASS='']")
                print("     [q] WYJDŻ")
                print("=====================================================")
                answer = input("[WYBIERAM OPCJE]\n>>  ")

                if answer == "1":
                    clear()
                    while True:
                        print("[POBIERZ TEKST Z TWEETOW/HTML][WYBIERZ KATERGORIE]:")
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
        if choice == "2":
            clear()
            dictFile = input("WPROWADZ NAZWĘ SŁOWNIKA:\n>>  ").lower()

            if ".json" not in dictFile:
              dictFile += ".json"

            if not os.path.exists("dicts"):
                os.makedirs("dicts")

            ff = "dicts//"+dictFile

            if not os.path.exists(ff):
              file = open(ff,"w+")
              json.dump({},file)
              file.close()

            file = open(ff,"r")

            dictionary = json.load(file)
            file.close()

            # clear()

            while True:
              print("[UTWÓRZ SŁOWNIK]:\n")
              print("=====================================================")
              print("     [1] Z PLIKU TEKSTOWEGO")
              print("     [2] Z KLAWIATURY")
              print("     [q] WYJDŻ")
              print("=====================================================")
              answer = input("[WYBIERAM OPCJE]\n>>  ")
              clear()
              if answer == "1":

                  while True:
                      print("[PRZYKŁADOWA LOKALIZACJA: tweets/nazwa_kontaT.txt]")
                      inputFile = input("WPROWADZ LOKALIZACJE PLIKU TEKSTOWEGO LUB PRZERWIJ(q)\n>>  ")
                      if inputFile == "q":
                          clear()
                          break
                      elif not os.path.exists(inputFile):
                          print("--- NIE ODNALEZIONO! ---")
                      else:
                          break

                  if inputFile!="q":
                      f=open(inputFile, "r")
                      if f.mode == 'r':
                          # contents =f.read()
                          fileName =f.read()
                          print("--- OK - WCZYTANO ZAWARTOŚĆ PLIIKU ---")

                          dictionary = learn(dictionary,fileName)
                          #poprawić sposob budowania slownika
                          updateFile(ff,dictionary)
                  break
              elif answer == "2":
                  while True:
                      fileName = input("WPROWADZ TEKST\n>>  ")
                      if fileName == "":
                          break
                      dictionary = learn(dictionary,fileName)
                      updateFile(ff,dictionary)
                  break
              elif answer == "q":
                  clear()
                  break
              else:
                  print("--- NIEPRAWIDŁOWY WYBÓR ---")
        if choice == "3":
            clear()
            print("[WYGENERUJ TEKST NA PODSTAWIE SŁOWNIKA]")
            print("[PRZYKŁADOWA LOKALIZACJA: dicts/nazwa_słownika.json]")
            while True:
                answer = input("\nWPROWADZ ŚCIEŻKĘ DLA PLIKU SŁOWNIKA LUB PRZERWIJ(q)\n>>  ")
                if answer == "q":
                    clear()
                    break
                elif not os.path.exists(answer):
                    print("--- NIE ODNALEZIONO! ---")
                else:
                    break

            if answer!="q":
                dictionary = loadDict(answer)

                while True:
                    length = input("OKREŚL LICZBĘ WYRAZÓW DLA WYGENEROWANEJ WIADOMOŚCI LUB PRZERWIJ(q)\n>>  ")

                    if length == "q":
                        break

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
