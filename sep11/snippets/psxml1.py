import xml.etree.ElementTree as et

doc = et.parse('group.xml')
print(doc)
print()
print(doc.getroot())
print()
print(doc.getroot().tag)
print()
print(doc.getroot().attrib)