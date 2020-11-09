import sys

print(f'실행 파일명 : {sys.argv[0]} ')
for i in range(1, len(sys.argv)):
    print(f'옵션 {i} : {sys.argv[i]}')
sys.exit()
for i in range(1, 100):
    print('여기는 실행되지 않습니다.')