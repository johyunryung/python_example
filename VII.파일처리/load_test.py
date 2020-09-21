file = open('file.txt','r',encoding='utf-8')
data = file.read()
file.close()

print(data)