import json
import random

class LinkedList:
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
        self.category = LinkedList()
        self.loadFromJson()

    def loadFromJson(self):
        with open('Colors.json') as data_file:
            file = json.load(data_file)
        colorsCateg = file["colors"]
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

class Color:

    def __init__(self, name, isprimarycolor):
        self.name = name
        self.isprimarycolor = isprimarycolor
        self.next = None

def main():
    print("\nDear user welcome to this application. Here you can learn more about colors.")

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


main()

