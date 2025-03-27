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
""" class Calculator():
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
