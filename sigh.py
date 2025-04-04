""" You will be creating an application that has two modes

Teacher Mode

In teacher mode you will be asking the user to input a word/phrase and the
answer as a key:value pair. These pairs will be written to a json file called
FlashCards.json

Student Mode
In student mode you will present the student with the
phrases/words/images and the user will type the answer in the terminal.
Keep a tally of correct answers and provide a score. Give students bonus
points for “Streaks” """
"""class Calculator():
    def add(x,y):
        print(x+y)
        return x + y
    def add_many(list):
        print(sum(list))
        return sum(list)
    def subtract(list):
        return list

Calculator.add(9,12) """
""" class Merchant:
    def __init__(self, name, products):
        self.name = name
        self.products = products
    def sell(self, item):
        self.products.remove(item)
        print(self.products)
Joanna = Merchant("Joanna", ['Chicken', 'Pork', 'Beef'])
print(Joanna.sell('Pork'))
Alvin = Merchant('Alvin', ['Human', "Alvin's Servitude", 'Break', 'Organs'])
print(Alvin.sell('Human')) """
import json 

class TeacherMode:
    def __init__(self, filename = "FlashCards.json"):
        self.flashcards = {}
        self.filename = filename
    def save(self):
        with open("FlashCards.json", "w") as file:
            json.dump(self.flashcards, file, indent=4)

    def add(self):
        while True:
            word = input("put in a phrase, or stop by typing stop")
            if word == "stop":
                break
            ans = input(f"put an answer for {word}")
            self.flashcards[word] = ans
            self.save()
""" flashcard = open("./FlashCards.json", encoding="utf8")
data = json.load(flashcard) """
class StudentMode:
    def __init__(self, learn):
        self.learn = learn
    def learning(self):
        for key, value in self.learn.Flashcards.json.items

while True:
    lols = input("Type 1 for Teacher Mode or 2 for Student Mode, or 3 to stop")
    if lols == "1":
        plus = TeacherMode()
        plus.add()
        break
    elif lols == "2":
        break
    elif lols == "3":
        break
    else:
       print("U must choose 1, 2, or 3 pls")
