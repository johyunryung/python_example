import pickle

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
       return f'name : {self.name}, age: {self.age}'

with open('person_data.bin','rb') as file:
    person = pickle.load(file)

print(person)