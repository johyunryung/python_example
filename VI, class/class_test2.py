#클래스 상속
class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age

    def eat(self, food):
        print(self.name + "가" + food + "를 먹습니다")

    def __str__(self):
        return self.name + "는 " + str(self.age) + "살 입니다"


class Employee(Person):
    def __init__(self, name, age, salary):
       super().__init__(name, age)
       self.salary = salary

    def work(self):
        print("열심히 일을 합니다.")

    def get_salary(self):
        print("급료를 받습니다.")
        return self.salary

e = Employee("영희", 19, 100)
print(e)

e.eat('삼겹살 두루치기')
e.work()
r = e.get_salary()
print(f'급료는 {r}만원 입니다')