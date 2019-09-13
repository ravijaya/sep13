from xml.etree.ElementTree import ElementTree, Element, SubElement
from json import load
from pprint import pprint as pp

content = load(open('group.json'))
# pp(content)

root_tag = Element('ssh-config')

for group_name, ssh_host_list in content.items():
    group_tag = SubElement(root_tag, 'group')
    group_tag.set('name', group_name)

    for ssh_host in ssh_host_list:
        ssh_tag = SubElement(group_tag, 'ssh')
        ssh_tag.set('host', ssh_host['host'])
        ssh_tag.set('port', str(ssh_host['port']))
        SubElement(ssh_tag, 'username').text = ssh_host['user']
        SubElement(ssh_tag, 'password').text = ssh_host['pwd']

ElementTree(root_tag).write('group.xml')
