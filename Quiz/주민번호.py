def social_security_number(number):
    areanum = int(number[8] + number[9])
    if areanum == 0:
        print("%s: 서울" % number)
    elif areanum == 1:
        print("%s: 경기도" % number)
    elif areanum == 2:
        print("%s: 인천" % number)
    elif areanum == 3:
        print("%s: 충청북도" % number)
    elif areanum == 4:
        print("%s: 전라북도" % number)
    elif areanum == 5:
        print("%s: 경상도" % number)
    elif areanum == 6:
        print("%s: 부산" % number)
    elif areanum == 7:
        print("%s: 강원도" % number)
    elif areanum == 8:
        print("%s: 충청남도" % number)
    elif areanum == 9:
        print("%s: 전라남도" % number)
    elif areanum == 10:
        print("%s: 제주도" % number)
s = social_security_number('030713-4101111')







