#클래스의 특수 메서드
class DeletableClass:
    def __del__(self):
         print("delete")

d = DeletableClass()
print(d)
del d
#print(d)

class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def __str__(self):
        return f'Person 설명, 이름은 {self.name} 키는 {self.height}'

    def __len__(self):
        return self.height

    def __getitem__(self, key):
         if key == 'name':
             return self.name
         elif key == 'age':
             return self.age
         return None

p = Person("예서", 17, 174)
print(p)
print(len(p))
print(p['age'])
print(p['unknown'])
print(p.name)