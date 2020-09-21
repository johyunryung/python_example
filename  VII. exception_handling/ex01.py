#print(10/0) => 에러남
#print(4 + spam * 3)
#print('2' + 2) TypeError: can only concatenate str (not "int") to str

list0 = [1,2,3]
try:
    print(list0[0])
    print(list0[1])
    print(list0[2])
    print(list0[3]) #IndexError: list index out of range
    print(list0[2])
except IndexError as e:
    print(e)
except: 
    print("에러 발생")    
else:
    print("에러 안 발생")
finally:
    print("무조껀 실행")