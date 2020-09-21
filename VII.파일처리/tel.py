phonebook = open('pb.txt','w',encoding='utf-8')

phonebook.write('나현아 :\t010-3065-0535\n')
phonebook.write('박서빈 :\t010-3344-3661\n')

phonebook.close()

data =[]

rb = open('pb.txt','r',encoding='utf-8')

data = rb.readlines()

#while True:
#   line = rb.readline()
#   if not line: # if line == None:
#       break
#   line = line.replace('\n','')
#   data.append(line)

rb.close()

for d in data:
    person = d.split('\t')
    person[0] = person[0].replace(' : ', '')
    print(person[0])
    person[1] = person[1].replace('\n','')
    print(person[1])