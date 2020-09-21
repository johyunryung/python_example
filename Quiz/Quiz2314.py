def quiz_words():
    word = ['shell','ground zero','transform', 'overlook', 'terrify'] #영단어
    word_1 = ['포탄','핵폭탄이 떨어지는 지점','변환','간과하다','겁나게 하다'] #뜻

    score = 0  #점수
    i = 0 #차례대로 테스트하기

    while (i < len(word)):
        print(word[i]) #영단어
        answer = input(" >> 뜻 : ")
        
        ## 정답인 경우
        if answer == word_1[i]:
            print("정답입니다!")
            score += 1

        ## 오답인 경우
        else:
            print("오답, 정답은 "+ word_1[i])
            i += score #계속 돌아가는 단어에 점수를 부과
        i += 1 #다른 단어를 나오게 i에다가 1를 더해줌으로써 다른 단어 나옴

    ##테스트 종료
    print("당신의 점수는",(score*20),"점 입니다.") #한 문제당 20점

#출력
quiz_words()