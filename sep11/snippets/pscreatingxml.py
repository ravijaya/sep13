"""write xml"""


from xml.etree.ElementTree import ElementTree, Element, SubElement


root_tag = Element('ssh-config')
ssh_tag = SubElement(root_tag, 'ssh')
ssh_tag.set('host', 'localhost')
ssh_tag.set('port', '22')
SubElement(ssh_tag, 'username').text='training'
SubElement(ssh_tag, 'password').text='training'

ElementTree(root_tag).write('hosts.xml')
