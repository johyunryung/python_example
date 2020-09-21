#클래스 => 데이터 함수를 정의
#         수정하기가 용이
#접근 제어자 : public , private, protected
#멤버변수 : 속성; 데이터
#멤버함수 : 능력; 함수

class Car:
    count = 0
    def __init__(self, type, speed):
        self.type = type
        self.speed = speed
        Car.count += 1
        
    @classmethod
    def get_count(cls):
       return cls.count

    def move(self):
         print(self.type + "가" + str(self.speed) + " 속도로 움직입니다 !.")

    def speed_up(self, amount):
        self.speed += amount

    def speed_down(self, amount):
        self.speed -= amount



c = Car("스포츠카", 100) #객체 생성
print(Car.get_count())

d = Car("트럭", 50)
print(Car.get_count())

print(c)
print(type(c))

print(d)
print(type(d))

c.move()
c.speed_up(10)
c.move()
c.speed_down(20)
c.move()

#print(c.type)
#print(c.speed)

c.speed = 200
c.move()
