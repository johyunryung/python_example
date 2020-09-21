import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement

root = Element('movie')
title = SubElement(root ,'title')
title.text = '다만 악에서 구하소서'
genre = SubElement(root, 'genre')
genre.text = '스릴러'
rating = SubElement(root, 'rating')
rating.text = '5'

ET.ElementTree(root).write('movie.xml',encoding='utf8',xml_declaration=True)

