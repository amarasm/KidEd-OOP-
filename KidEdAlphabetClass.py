import json
import random


class LinkedList:
    def __init__(self):
        self.head = None

    def setHead(self, lowerCase, upperCase, example):
        self.head = Letter(lowerCase, upperCase, example)

    def appending(self, lowerCase, upperCase, example):
        temp = self.head
        if temp is None:
            self.setHead( lowerCase, upperCase, example)
        else:
            while temp.next is not None:
                temp = temp.next
            newLetter = Letter(lowerCase, upperCase, example)
            temp.next = newLetter

    def displayData(self, key):
        printLetter = self.head
        while printLetter is not None:
            if printLetter.lowerCase == key:
                print("The lowercase is", printLetter.lowerCase, ", the uppercase is", printLetter.upperCase,". For example:", printLetter.example)
                break
            else:
                printLetter = printLetter.next

    def createCategory(self):
        names = []
        keys = self.head
        while keys is not None:
            names.append(keys.lowerCase)
            keys = keys.next
        return names

class Alphabet:

    def __init__(self):
        self.category = LinkedList()
        self.loadFromJson()

    def loadFromJson(self):
        with open('Alphabet.json') as data_file:
            file = json.load(data_file)
        alphabetCateg = file["alphabet"]
        return alphabetCateg
        # for key in alphabetCateg:
        #     letter = Letter(key, alphabetCateg[key]["upperCase"], alphabetCateg[key]["example"])
        #     self.category[key] = letter

    def appendingNewLetter(self):
        alphabetCateg = self.loadFromJson()
        for key in alphabetCateg:
            self.category.appending(alphabetCateg[key]["lowerCase"], alphabetCateg[key]["upperCase"], alphabetCateg[key]["example"])


    def getLetterName(self):
        temp = self.category
        print((", ").join(temp.createCategory()))

    def getAlphabet(self, count):
        categ = self.category.createCategory()
        yourchoices = random.choices(categ, k=count)
        for key in yourchoices:
            self.category.displayData(key)





class Letter:
    def __init__(self, lowerCase, upperCase, example):
        self.lowerCase = lowerCase
        self.upperCase = upperCase
        self.example = example
        self.next = None


def main():
    print("\nDear user welcome to this application. Here you can learn more about the alphabet.")

    while True:
        choice = input("\nDo you want to learn about animals right now or not? yes/no")

        if choice == "yes":
            alphabet = Alphabet()

            alphabet.appendingNewLetter()

            print("\nHere are the keys:")
            alphabet.getLetterName()



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

