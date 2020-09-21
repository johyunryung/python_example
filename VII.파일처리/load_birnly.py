import array

with open('data.bin','rb') as file:
    data = array.array('B') #byte 단위의 공간을 생성
    data.fromfile(file, 3)

for item in data:
    print(bin(item))

