
import json
import random

class BST:
    def __init__(self):
        self.root = None

    def addNode(self, node):
        if self.root is None:
            self.root = node
        else:
            self.__addNode(node, self.root)

    def __addNode(self, node, root):
        if root.left is None and root.key > node.key:
            root.left = node
        elif root.right is None and root.key < node.key:
            root.right = node
        elif root.left.key < node.key:
            self.__addNode(root.left, node)
        elif root.right.key > node.key:
            self.__addNode(root.right, node)
        else:
            print('Same value')



class NumberBST:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class LinkedList:
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
                print(printNumber.key, " - ", printNumber.name)
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


    def getKeyForBst(self, key):
        while key is not None:
            return key.key




class Numbers:

    def __init__(self):
        self.category = LinkedList()
        self.loadFromJson()

    def loadFromJson(self):
        with open('Numbers.json') as data_file:
            file = json.load(data_file)
        numbersCateg = file["numbers"]
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

    def addNodeToBST(self):
        while self.category.head is not None:
            numbersCateg = self.category.getKeyForBst(self.category.head)
            bst = BST()
            while numbersCateg is not None:
                temp = NumberBST(numbersCateg)
                bst.addNode(temp)

                numbersCateg = self.category.getKeyForBst(self.category.head.next)




class Number:
    def __init__(self, key, name):
        self.key = key
        self.name = name
        self.next = None


def main():
    print("\nDear user welcome to this application. Here you can learn the numbers.")

    while True:
        choice = input("\nDo you want to learn about numbers right now or not? yes/no")

        if choice == "yes":
            numbers = Numbers()

            numbers.appendingNewNumbers()
            numbers.addNodeToBST()


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

main()

