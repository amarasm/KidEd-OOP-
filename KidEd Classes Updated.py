import json
import random

class Game:
    def __init__(self):
        self.getFromJson()

    def getFromJson(self):
        with open('Categories.json') as data_file:
            file = json.load(data_file)
        categ = file["categories"]
        return categ

    def getCategories(self):
        json = self.getFromJson()
        print((", ").join(json.keys()))

class LinkedListforAnimals:

    def __init__(self):
        self.head = None

    def setHead(self, animalName, animalSound, animalKind):
        self.head = Animal(animalName, animalSound, animalKind)

    def appending(self, animalName, animalSound, animalKind):
        temp = self.head
        if temp is None:
            self.setHead(animalName, animalSound, animalKind)
        else:
            while temp.next is not None:
                temp = temp.next
            newAnimal = Animal(animalName, animalSound, animalKind)
            temp.next = newAnimal

    def displayData(self, key):
        printAnimal = self.head
        while printAnimal is not None:
            if printAnimal.name == key:
                print("Its name is", printAnimal.name, ", its sound is", printAnimal.sound,"and it's a type of", printAnimal.kind)
                break
            else:
                printAnimal = printAnimal.next


    def createCategory(self):
        names = []
        keys = self.head
        while keys is not None:
            names.append(keys.name)
            keys = keys.next
        return names

class Animals:

    def __init__(self):
        self.category = LinkedListforAnimals()
        self.loadFromJson()

    def loadFromJson(self):
        categ = Game()
        animals = categ.getFromJson()
        animalsCateg = animals["animals"]
        return animalsCateg


    def appendingNewAnimals(self):
        animalsCateg = self.loadFromJson()
        for key in animalsCateg:
            self.category.appending(animalsCateg[key]["name"], animalsCateg[key]["sound"], animalsCateg[key]["kind"])


    def getCategoryNames(self):
        temp = self.category
        print((", ").join(temp.createCategory()))

    def getAnimals(self, count):
        categ = self.category.createCategory()
        yourchoices = random.choices(categ, k=count)
        for key in yourchoices:
            self.category.displayData(key)



    @staticmethod
    def animal():

        print("\nDear user here you can learn more about animals.")

        while True:
            choice = input("\nDo you want to learn about animals right now or not? yes/no")

            if choice == "yes":
                animals = Animals()
                animals.appendingNewAnimals()

                print("Here are the keys:")
                animals.getCategoryNames()

                while True:
                    number = input("Number of animals you want to learn today:")
                    if number.isnumeric():
                        number = int(number)
                        if number < 26:
                            break
                        else:
                            print("oops!You have to type a number from 1 to 25!Now try again!")
                    else:
                        print("Please insert numbers only:)")

                animals.getAnimals(number)

                break
            elif choice == "no":
                print("\nOkay but be sure to come back.")
                break
            else:
                print("\ntry again.")

class Animal:
    def __init__(self, name, sound, kind):
        self.name = name
        self.sound = sound
        self.kind = kind
        self.next = None

class LinkedListforColors:
    def __init__(self):
        self.head = None

    def setHead(self, name, isprimarycolor):
        self.head = Color(name, isprimarycolor)

    def appending(self, name, isprimarycolor):
        temp = self.head
        if temp is None:
            self.setHead(name, isprimarycolor)
        else:
            while temp.next is not None:
                temp = temp.next
            newColor = Color(name, isprimarycolor)
            temp.next = newColor

    def displayData(self, key):
        printColor = self.head
        while printColor is not None:
            if printColor.name == key:
                print("\nThe color is", printColor.name)
                if printColor.isprimarycolor is True:
                    print("And it's a primary color")
                    break
                else:
                    print("And it's not a primary color")
                    break
            else:
                printColor = printColor.next

    def createCategory(self):
        names = []
        keys = self.head
        while keys is not None:
            names.append(keys.name)
            keys = keys.next
        return names

class Colors:

    def __init__(self):
        self.category = LinkedListforColors()
        self.loadFromJson()

    def loadFromJson(self):
        categ = Game()
        colors = categ.getFromJson()
        colorsCateg = colors["colors"]
        return colorsCateg

    def appendingNewColor(self):
        colorsCateg = self.loadFromJson()
        for key in colorsCateg:
            self.category.appending(colorsCateg[key]["name"], colorsCateg[key]["isPrimaryColor"])

    def getColorNames(self):
        temp = self.category
        print((", ").join(temp.createCategory()))

    def getColors(self, count):
        categ = self.category.createCategory()
        yourchoices = random.choices(categ, k=count)
        for key in yourchoices:
            self.category.displayData(key)

    @staticmethod
    def colors():

        print("\nDear user here you can learn more about colors.")

        while True:
            choice = input("\nDo you want to learn about colors right now or not? yes/no")

            if choice == "yes":
                colors = Colors()
                colors.appendingNewColor()

                print("\nHere are the keys:")
                colors.getColorNames()

                while True:
                    number = input("\nNumber of colors you want to learn today:")
                    if number.isnumeric():
                        number = int(number)
                        if number < 11:
                            break
                        else:
                            print("\noops!You have to type a number from 1 to 10!Now try again!")
                    else:
                        print("Please insert numbers only:)")

                colors.getColors(number)

                break
            elif choice == "no":
                print("\nOkay but be sure to come back.")
                break
            else:
                print("\ntry again.")

class Color:

    def __init__(self, name, isprimarycolor):
        self.name = name
        self.isprimarycolor = isprimarycolor
        self.next = None

class LinkedListforAlphabet:
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
        self.category = LinkedListforAlphabet()
        self.loadFromJson()

    def loadFromJson(self):
        categ = Game()
        alphabet = categ.getFromJson()
        alphabetCateg = alphabet["alphabet"]
        return alphabetCateg

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


    @staticmethod
    def alphabet():

        print("\nDear user here you can learn more about the alphabet.")

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

class Letter:
    def __init__(self, lowerCase, upperCase, example):
        self.lowerCase = lowerCase
        self.upperCase = upperCase
        self.example = example
        self.next = None

class LinkedListforNumbers:
    def __init__(self):
        self.head = None

    def setHead(self, key, name):
        self.head = Number(key, name)

    def appending(self, key, name):
        temp = self.head
        if temp is None:
            self.setHead(key, name)
        else:
            while temp.next is not None:
                temp = temp.next
            newNumber = Number(key, name)
            temp.next = newNumber

    def displayData(self, key):
        printNumber = self.head
        while printNumber is not None:
            if printNumber.name == key:
                print(printNumber.key, " - " , printNumber.name)
                break
            else:
                printNumber = printNumber.next


    def createCategory(self):
        names = []
        keys = self.head
        while keys is not None:
            names.append(keys.name)
            keys = keys.next
        return names

class Numbers:

    def __init__(self):
        self.category = LinkedListforNumbers()
        self.loadFromJson()

    def loadFromJson(self):
        categ = Game()
        numbers = categ.getFromJson()
        numbersCateg = numbers["numbers"]
        return numbersCateg


    def appendingNewNumbers(self):
        numbersCateg = self.loadFromJson()
        for key in numbersCateg:
            self.category.appending(numbersCateg[key]["key"], numbersCateg[key]["name"])

    def getNumberNames(self):
        temp = self.category
        print((", ").join(temp.createCategory()))

    def getNumbers(self, count):
        categ = self.category.createCategory()
        yourchoices = random.choices(categ, k=count)
        for key in yourchoices:
            self.category.displayData(key)

    @staticmethod
    def numbers():
        print("\nDear user here you can learn more about the numbers.")

        while True:
            choice = input("\nDo you want to learn about numbers right now or not? yes/no")

            if choice == "yes":
                numbers = Numbers()
                numbers.appendingNewNumbers()

                print("\nHere are the keys:")
                numbers.getNumberNames()


                while True:
                    number = input("\nThe numbers you want to learn today:")
                    if number.isnumeric():
                        number = int(number)
                        if number < 11:
                            break
                        else:
                            print("\noops!You have to type a number from 1 to 10!Now try again!")
                    else:
                        print("Please insert numbers only:)")

                numbers.getNumbers(number)

                break
            elif choice == "no":
                print("\nOkay but be sure to come back.")
                break
            else:
                print("\ntry again.")

class Number:
    def __init__(self, key, name):
        self.key = key
        self.name = name
        self.next = None

def main():
    print("\nDear user welcome to this application. Here you can learn the numbers, the alphabet, the colors and a lot about animals.")

    while True:
        start = input("\nDo you want to get started?")

        if start == "yes":

            game = Game()

            while True:
                print("\nHere are the keys:")
                game.getCategories()

                choice = input("Which one do you want to learn today?")

                if choice == "animals":
                    animal = Animals()
                    animal.animal()
                    break
                elif choice ==  "colors":
                    color = Colors()
                    color.colors()
                    break
                elif choice == "alphabet":
                    alphabet = Alphabet()
                    alphabet.alphabet()
                    break
                elif choice == "numbers":
                    number = Numbers()
                    number.numbers()
                    break
                else:
                    print("Dear user please take a look at the categories once more and try again!")
        elif start == "no":
            print("\nOh, Okay. Hope you change your mind.")
            break

        else:
            print("\nTry again")


main()