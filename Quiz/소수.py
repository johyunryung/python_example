#def prime_number(number):
#    if number != 1: #number가 1이 아니면 ?
#        for i in range(2, number): #number % 2를 해야 하기 때문
#            if number % i == 0:
#                return False #소수가 아님
#    else: #만약 number이 1라면?
#        return False #1이 소수가 아님
#    return True #만약에 1도 아니고, 2로 나눠지지 않는다면 소수 판별


#num = input("숫자를 입력해주세요 : ")
#if prime_number(int(num)):
#    print("소수가 맞습니다 !3! ")
#else:
#    print("소수가 아닙니다 ㅜ3ㅜ")


def is_prime_number(number):
   #count = 0
   for i in range(2, number):
     if number % i == 0:
         #count += 1
          return "소수가 아닙니다."
   return "소수입니다."

   #if count == 0:
       #return  "소수입니다."
   #else:
       #return  "소수가 아닙니다."


print(is_prime_number(3))
print(is_prime_number(6))
print(is_prime_number(100000001))