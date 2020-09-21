from sys import *
def exit():
    print('my exit()')

while True:
    print('종료하러면 exit를 입력하세요 : ')
    user_input = input('>')
    if user_input == 'exit':
        exit()