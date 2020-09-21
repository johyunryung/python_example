color = [255, 0, 127]
byte_list = bytes(color)


#try:
#    file = open('data.bin', 'wb')
#    file.write(byte_list)
#finally:
#    file.close()

with open('data.bin', 'wb') as file:
    file.write(byte_list)


