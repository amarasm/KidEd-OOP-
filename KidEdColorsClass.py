import json
import random


class Colors:

    def __init__(self):
        self.category = {}
        self.loadFromJson()

    def loadFromJson(self):
        with open('Colors.json') as data_file:
            file = json.load(data_file)
        colorsCateg = file["colors"]
        self.category = colorsCateg

    def getColors(self, count):
        colorList = []
        for keys in self.category.keys():
            colorList.append(keys)
        yourchoices = random.choices(colorList, k=count)
        for key in yourchoices:
            print(key)

    def getColorsCateg(self):
        print((", ").join(self.category.keys()))


def main():
    print("\nDear user welcome to this application. Here you can learn more about colors.")

    while True:
        choice = input("\nDo you want to learn about colors right now or not? yes/no")

        if choice == "yes":
            colors = Colors()

            print("\nHere are the keys:")
            colors.getColorsCateg()

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


main()

