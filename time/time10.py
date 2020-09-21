import time
import numpy as np

record = list()
for i in range(50):
    start = time.time()
    count = 0
    for i in range(1000000):
      current = i
      while current != 0:
        if current % 10 == 3 or current % 10 == 6 or current % 10 == 9:
        #if(current % 10) % 3 == 0 and (current % 10 ) != 0:
          count += 1
        current = current // 10
    end = time.time()
    record.append(end-start)

print("차이의 평균\t : ", np.mean(record))
print("차이의 표준편차\t : ", np.std(record))