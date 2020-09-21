import pickle

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
       return f'name : {self.name}, age: {self.age}'

p = Person('김범수', 12)

with open('person_data.bin','wb') as file:
   pickle.dump(p, file)