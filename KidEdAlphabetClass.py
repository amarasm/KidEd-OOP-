import json
import random


class Alphabet:

    def __init__(self):
        self.category = {}
        self.loadFromJson()

    def loadFromJson(self):
        with open('Alphabet.json') as data_file:
            file = json.load(data_file)
        alphabetCateg = file["alphabet"]
        self.category = alphabetCateg

    def getAlphabet(self, count):
        alphabetList = []
        for keys in self.category.keys():
            alphabetList.append(keys)
        yourchoices = random.choices(alphabetList, k=count)
        for key in yourchoices:
            print("the lowercase is", key, "the uppercase is",
                  self.category[key]["upperCase"], ". For example:",
                  self.category[key]["example"])

    def getAlphabetCateg(self):
        print((", ").join(self.category.keys()))


def main():
    print("\nDear user welcome to this application. Here you can learn more about the alphabet.")

    while True:
        choice = input("\nDo you want to learn about animals right now or not? yes/no")

        if choice == "yes":
            alphabet = Alphabet()

            print("\nHere are the keys:")
            alphabet.getAlphabetCateg()

            number = 0
            while True:
                number = input("\nNumber of letters you want to learn today:")
                if number.isnumeric():
                    number = int(number)
                    if number < 27:
                        break
                    else:
                        print("\noops!You have to type a number from 1 to 26!Now try again!")
                else:
                    print("Please insert numbers only:)")

            alphabet.getAlphabet(number)

            break
        elif choice == "no":
            print("\nOkay but be sure to come back.")
            break
        else:
            print("\ntry again.")


main()

