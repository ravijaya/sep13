from json import load
from pprint import pprint as pp

content = load(open('users.json'))

for name, value in content.items():
    if type(value) is list:
        print(name, ':')

        for user in value:
            if user['id'] == 7:
                for user_param_name, user_param_value in user.items():
                    print("\t", user_param_name, ':', user_param_value)
                print()
    else:
        print(name, ':', value)
