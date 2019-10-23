import json
import random

class KidEd:
    def __init__(self):
        self.category = {}
        self.loadFromJson()

    def loadFromJson(self):
        with open('Categories.json') as data_file:
            file = json.load(data_file)
        categ = file["categories"]
        self.category = categ
        return categ

    def getCateg(self):
        category = self.category.keys()
        print((", ").join(category))

class Animals:
    def __init__(self):
        self.category = {}
        self.loadFromJson()

    def loadFromJson(self):
        json = KidEd()
        category = json.loadFromJson()
        categ = category["animals"]
        self.category = categ

    def getAnimals(self, count):
        animalList = []
        for keys in self.category.keys():
            animalList.append(keys)
        yourchoices = random.choices(animalList, k=count)
        for key in yourchoices:
            print("Its name is", key, ", its sound is", self.category[key]["sound"],
                  "and it's a type of", self.category[key]["kind"], ".")



    @staticmethod
    def animal():


        while True:
            choice = input("\nDo you want to learn about animals right now or not? yes/no")

            if choice == "yes":
                animals = Animals()

                number = 0
                while True:
                    number = input("\nNumber of animals you want to learn today:")
                    if number.isnumeric():
                        number = int(number)
                        if number < 26:
                            break
                        else:
                            print("\noops!You have to type a number from 1 to 25!Now try again!")
                    else:
                        print("Please insert numbers only:)")

                animals.getAnimals(number)

                break
            elif choice == "no":
                print("\nOkay but be sure to come back.")
                break
            else:
                print("\ntry again.")



class Colors:
    def __init__(self):
        self.category = {}
        self.loadFromJson()

    def loadFromJson(self):
        json = KidEd()
        category = json.loadFromJson()
        categ = category["colors"]
        self.category = categ

    def getColors(self, count):
        colorList = []
        for keys in self.category.keys():
            colorList.append(keys)
        yourchoices = random.choices(colorList, k=count)
        for key in yourchoices:
            print(key)



    @staticmethod
    def colors():

        while True:
            choice = input("\nDo you want to learn about colors right now or not? yes/no")

            if choice == "yes":
                colors = Colors()


                number = 0
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


class Alphabet:
    def __init__(self):
        self.category = {}
        self.loadFromJson()

    def loadFromJson(self):
        json = KidEd()
        category = json.loadFromJson()
        categ = category["animals"]
        self.category = categ

    def getAlphabet(self, count):
        alphabetList = []
        for keys in self.category.keys():
            alphabetList.append(keys)
        yourchoices = random.choices(alphabetList, k=count)
        for key in yourchoices:
            print("the lowercase is", key, "the uppercase is",
                  self.category[key]["upperCase"], ". For example:",
                  self.category[key]["example"])



    @staticmethod
    def alphabet():


        while True:
            choice = input("\nDo you want to learn about animals right now or not? yes/no")

            if choice == "yes":
                alphabet = Alphabet()



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


class Numbers:
    def __init__(self):
        self.category = {}
        self.loadFromJson()

    def loadFromJson(self):
        json = KidEd()
        category = json.loadFromJson()
        categ = category["animals"]
        self.category = categ

    def getNumbers(self, count):
        numberList = []
        for keys in self.category.keys():
            numberList.append(keys)
        yourchoices = random.choices(numberList, k=count)
        for key in yourchoices:
            print(key, " - ", self.category[key]["name"])



    @staticmethod
    def numbers():

        while True:
            choice = input("\nDo you want to learn about numbers right now or not? yes/no")

            if choice == "yes":
                numbers = Numbers()


                number = 0
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



def main():
    print("\nDear user welcome to this application. Here you can learn the numbers, the alphabet, the colors and a lot about animals.")

    while True:
        start = input("\nDo you want to get started?")

        if start == "yes":
            kidEd = KidEd()

            while True:
                print("\nHere are the keys:")
                print(kidEd.getCateg())
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