#for loop
edgerrunnerVernacular = ["gonk", "choom", "preem", "nova", "shimra"]

for word in edgerrunnerVernacular:
    print (word "is something only edgerunners say, bud")

#forjava
#for (var i = 0; i < 5; i++) {
#    console.log(i);
#}

#while loop: repeats code block every time the condition is true

#challenges
#Loop through characters in a string:
name = "QueenieVonCurvacious"

nameLength = 0
for letter in name:
    print(letter)
    nameLength += 1

print (f"Name is {nameLength} letters long.")

#Use break/continue:
planets = ["tatooine", "Yavin IV", "Alderaan"]
rebelBase = "Alderaan"
target = "none"

for thisPlanet in planets:
    print (f"Scanning {thisPlanet}")
    if thisPlanet == rebelBase:
        target = thisPlanet
        break
    print(f"Rebel base found! Firing lasers at {target}!" )

wordList = ["toast", "boast", "jam" "do", "a", "amtidestabilishmentarianism"]
wordLengthLimit = 4
for thisWord in wordList:
    if len(thisWord) <= wordLengthLimit:
        shortWords += 1
    continue
    longWords += 1
    print (f"Long word detected: {thisWord}")
print (f"found {longWords} long words")


#Use range:
tickets = 6
for nowServing in range(tickets):
        print(f"Now serving ticket #{nowServing + 1}")

#Use else after for loop:
listOfPeople = ["Big Boss", "Solid Snake", "Revolver Ocelot", "Liquid Snake"]

for checkIdentity in listOfPeople:
    print(f"Checking identity. Subject found: {checkIdentity}")
if "Snake" in checkIdentity:
    print ("SNAAAAAAAAAKE!")
    break
else:
    print("All clear! No snake here.")

#Nested loops:

listofCars = ["Viper", "Miata", "Veloster"]
listOfParts = ["Engine", "Exhaust", "Headlight Fluid"]

for thisCar in listofCars:
    for thisPart in listOfParts:
        print(f"Wow, check out the {thisPart} on that {thisCar}!")

#pass
for i in range (3):
    pass

#Define a Function: use "snake_case" when naming a function in Python.
def add_two_numbers(num1 = 1, num2 = 3):
    result = num1 + num2
    return result

myResult = add_two_numbers(1)
myResult = add_two_numbers(1)
print(myResult)

#Invoking functions: check slides for example
#add_two_numbers(2, 2)

start = 10
income = 2
myTotal = add_two_numbers(start, income)

print(f"My totoal is {myTotal}")



def say_hello():
    print("Hello")
say_hello()



#classes and objects: Object Oriented Programming(OOP) check slides for example breakdown

class Car:
    def __init__(self, make, model, year, owner):
        self.make = make
        self.model = model
        self.year = year
        self.owner = owner
    def identify(self):
        print(f"I am a {self.year} {self.make} {self.model}, owned by {self.owner}")
    def drive(self):
        print("Vroom!")

myCorolla = Car("Toyota", "Corolla", 2023, "Rin")

myCorolla.identify()


#4 pillars of OOP:
    #Encapsulation: Vending Machine Demo file



    #Polymorphism:


    #Inheritance:


    #Abstraction:


#Errors: Syntax, Logical, Runtime, etc. Be specific when addressing error types.

    #Exceptions: ValueError if a prompt requires numerical integer response, and users might spell out number values, instead.

prompt = f"How many fish?\n(int)"
response = input(prompt)

print (f"You said {response} fish. ")

try:
    for _ in range(int(response)):
        print("<><")
except ValueError:
    print("Response must be a numerical integer. Try again, please!")



#Can use .casefold() instead of strip().lower().

