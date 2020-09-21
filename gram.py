#369게임
#1~99까지
#숫자에서 3 또는 6 또는 9 가 있으면 세자 -> count
#coutn == 0: 숫자출력하자
#count != 0: "짝" * count 출력하자
def count369(number): #number -> 369 count
#     count = 0
#     if number % 10 == 3 or number % 10 == 6 or number % 10 ==9:
#         count += 1
#     if number // 10 ==3 or number // 10 == 6 or number // 10 == 9:
#         count += 1
#     return count

    number_string = str(number)
    # count = 0
    # for n_string in number_string:
        # # if n_string == '3' or n_string == '6' or n_string == '9':
        # if n_string in "369":
        #     coutn += 1
    return number_string.count("3") + number_string.count('6') + number_string.count('9')


for number in range(1,99+1):
    count = count369(number)

    if count == 0:
        print(number)
    elif count != 0:
        print(number, "짝"*count)


for number in range(1, 99+1):
    if number % 5 ==0:
        print("뿌쓩!")
    else :
      number = count369(number)
      if count == 0:
          print(number)
      elif count != 0:
          print("짝"*count)

