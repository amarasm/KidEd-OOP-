import json
import random


class Numbers:

    def __init__(self):
        self.category = {}
        self.loadFromJson()

    def loadFromJson(self):
        with open('Numbers.json') as data_file:
            file = json.load(data_file)
        numbersCateg = file["numbers"]
        self.category = numbersCateg

    def getNumbers(self, count):
        numberList = []
        for keys in self.category.keys():
            numberList.append(keys)
        yourchoices = random.choices(numberList, k=count)
        for key in yourchoices:
            print(key, " - ", self.category[key]["name"])

    def getNumbersCateg(self):
        print((", ").join(self.category.keys()))


def main():
    print("\nDear user welcome to this application. Here you can learn the numbers.")

    while True:
        choice = input("\nDo you want to learn about numbers right now or not? yes/no")

        if choice == "yes":
            numbers = Numbers()

            print("\nHere are the keys:")
            numbers.getNumbersCateg()

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


main()

