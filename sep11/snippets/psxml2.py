import xml.etree.ElementTree as et

doc = et.parse('group.xml')

for group_tag in doc.getiterator('group'):  # select tag by tag-name
    print(group_tag.get('name'))
    print(group_tag.attrib)
    # print(dir(group_tag))
    # print(list(group_tag))
    # break
    for ssh_tag in [group_tag[0]]:
        print('host :', ssh_tag.get('host'))
        print('port  :', ssh_tag.get('port'))

        for user_info in ssh_tag:
            print(user_info.tag, ':', user_info.text)
        print()

    print()
