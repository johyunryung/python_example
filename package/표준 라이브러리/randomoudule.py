import random

print(f'0 <= r < 1 사이의 랜덤 실수: {random.random()}')
print(f'0~9까지 랜덤 정수: {int(random.random() * 10)}')
print(f'0~10까지 랜덤 정수: {int(random.random() * 10)+1}')
print(f'0~2까지 랜덤 정수: {int(random.random() * 10)%3}')

print(f'시작 <= r < 끝 랜덤 실수: {random.uniform(2.5 , 10.0)}')

print(f'0~9까지 랜덤 정수: {random.randrange(9+1)}')
print(f'0~10까지 랜덤 정수: {random.randrange(1, 10+1)}')

print(f'0~10까지 랜덤 정수: {random.randint(1, 10)}')
print(f'0~2까지 랜덤 정수: {random.randrange(0,2)}')

season = ['봄', '여름', '가을', '겨울']
print(f'season 중 랜덤한 하나 요소 :{random.choice(season)}')

foods = ['핫도그','토스트','비빔면']
print(f'오늘 뭐 먹을래? {random.choice(foods)}')

반3 = list(range(1, 17+1))
반3.remove(4)
print(반3)
random.shuffle(반3)
print(반3)

print(random.sample(반3, 3))

