#result = {"A": 0, "B": 0, "AB": 0, "O": 0}
#students = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
#for s in students:
#    result[s] += 1
#print("{'A형': %d, 'O형': %d, 'B형': %d, 'AB형': %d}" % (result["A"], result["O"], result["B"], result["AB"]))

## 값에 대해 알고 있을때
blood_type = {'A': 0, 'B': 0, 'O': 0, 'AB': 0}
반3 = ['O','B','B','O','AB','A','B','A','AB','B']
for 학생 in 반3:
     blood_type[학생] = blood_type[학생] + 1
print(blood_type)

##값에 대해 모르고 있을때
반3 = ['O','B','B','O','AB','A','B','A','AB','B']
혈액형 = {}
for 학생 in 반3:
  try :
      혈액형[학생] += 1
  except:
     혈액형[학생] = 1
print(혈액형)

## 이름 성만 출력하기
names = ['유병석','유재석','황광희']
count_last_name = {}
for name in names:
  name = name[0]
  try :
      count_last_name[name] += 1
  except:
     count_last_name[name] = 1
print(count_last_name)
