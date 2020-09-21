# position = {'Le' : 2 , 'R' : 1 , 'C' : 2, 'S': 1, 'Lr' : 1}
# names = {'이소영', '강소휘', '문지윤', '한수지', '김유리', '이현', '김해빈'}
# for volleyBall in names:
#   volleyBall =  volleyBall[0]
#   try :
#       volleyBall[position] += 1
#   except:
#       volleyBall[position]= 1
#
# print(volleyBall)


def volley_ball(name1, name2, name3, name4, name5, name6,name7):
    team = {'L1': name1, 'L2': name2, 'R':name3, 'C1':name4 , 'C2':name5, 'S':name6, 'Li':name7 }
    for key in team:
        print(f'{key} {team[key]}')

if __name__ == '__main__':
      volley_ball('이소영', '강소휘', '문지윤', '한수지', '김유리', '이현', '김해빈')
      volley_ball('효정', '미미', '유아', '지호', '승희', '빈이', '아린')






