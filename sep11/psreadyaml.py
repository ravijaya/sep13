# import yaml
# from pprint import  pprint as pp
#
# data_set = yaml.safe_load(open('tmp.yaml'))
# pp(data_set)

"""
<directories>
    <directory name='/tmp'>
      <file size="124" mtime="12 Mon Sep 19">file_name</file>
      <dir size="124" mtime="12 Mon Sep 19">dir_name</dir>
    </directory>
</directories>
"""
"http://collabedit.com/vqkeg"
from xml.etree.ElementTree import Element, SubElement, ElementTree

root_tag = Element('directories')
directory_tag = SubElement(root_tag, 'directory')
directory_tag.set('name', '/tmp')
file_tag = SubElement(directory_tag, 'file')
file_tag.text = 'ansible' # adding text node to the tag
file_tag.attrib = dict(size="124", mtime="12 Mon Sep 19")

ElementTree(root_tag).write('tmp.xml')



