from sys import exit #import sys

while True:
    print('종료할려면 exit를 입력하세요 : ')
    user_input = input(">")
    if user_input == 'exit':
        exit()  #sys.exit