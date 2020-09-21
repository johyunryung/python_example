# 숫자를 각 자릿수 값으로 분해하여 리스트로 리턴

def num_to_list(number):  # 함수정의 (num)
    num = (list)((str)(number))  #num을 문자열로 반환한 걸 리스트로 생성
    numrear = list() # num을 받을 numrear를 리스트로 생성
    for j in range(len(str(number))): #num의 문자열의 길이까지 for문을 돌림
        numrear.append((int)(num[j])* 10 ** (len(str(number)) - j - 1))
        #num은 지금 문자열이기 때문에 형변환을 해줘야 함
        #num[j] = 앞에 숫자들을 100, 10, 1을 곱해서 리스트에 추가함
        #10 ** 은 10의 진수
        #문자열의 길이인 num을 리스트에 추가한 j를 빼고 난 후 다시 1을 빼서 다른 자리를 채우고 난 후 마지막에 1의 자리인 정수num을 추가함
    return numrear #구한 값을 리턴 해줌


li1 = num_to_list(54321)  # 54321에 함수적용
print(li1)  # [50000, 4000, 300, 20, 1]
print(sum(li1))
# print(sum(num_to_list(54321)))


