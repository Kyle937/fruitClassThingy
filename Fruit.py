# imports
import requests
import json

# Class
class Fruit:
    # API
    def __init__(self,name,calories,sugar,family):
        self.__name = name
        self.__family = family
        self.__sugar = sugar
        self.__calories = calories
        
    def getName(self):
        return self.__name
        
    def getCalories(self):
        return self.__calories
        
    def getSugar(self):
        return self.__sugar
        
    def getFamily(self):
        return self.__family
    
    def __str__(self):
        return f"{self.__name}: \n Family: {self.__family} \nCalories: {self.__calories} \n Sugar: {self.__sugar}"

# get data func
def getFruitInfo(fruit):

    endpoint = f"https://www.fruityvice.com/api/fruit/{fruit}"

    response = requests.get(endpoint)

    fruitData = response.json()

    return fruitData

# list
fruits = []

# welcome
print("welcome to the fruit tracker thingy!")

# loop
gameRunning = True
while gameRunning:

    # ask for fruit
    print("what fruit would you like to see?")
    userChoice = input("> ").strip().lower()

    # new object
    fruitJson = getFruitInfo(userChoice)

    # putting everything into an object
    newFruit = Fruit(fruitJson["name"], fruitJson["nutritions"]["calories"], fruitJson["nutritions"]["sugar"], fruitJson["family"])
    
    # add to list
    fruits.append(newFruit)

    # another
    print("want to add another? (y/n)")
    confirm = input("> ")
    if confirm == "y":
        gameRunning = True
    if confirm == "n":
        gameRunning = False

    

# display total Calories
total = 0
for item in fruits:
    total += item.getCalories()
print(f"total calories: {total}")
