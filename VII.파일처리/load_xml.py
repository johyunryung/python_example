import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element,SubElement

file = open('movie.xml',encoding='utf-8')

data = file.read()

file.close()

tree = ET.ElementTree(ET.fromstring(data))
root = tree.getroot()
print(root.tag)
#print(root.text)
for child in root:
    print(f'tag : {child.tag}, text : {child.text}')

