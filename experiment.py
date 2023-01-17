import random

class ChestOpener:

    def __init__(self,crateSize):
        self.crateSize = crateSize

    def doYourThing(self):

        numOfTries = 0
        currentNumber = 0
        while currentNumber != self.crateSize:
            if random.randint(0,self.crateSize) > currentNumber:
                currentNumber = currentNumber + 1
            numOfTries = numOfTries + 1
        self.numOfTries = numOfTries

def main():
    number = 10000
    result = 0
    co = ChestOpener(1000)
    while number > 0:
        co.doYourThing()
        print(co.numOfTries)
        result = result + (co.numOfTries/float(10000))
        print(result)
        number = number - 1
    print(result)


if __name__ == "__main__":
    main()