from yaml import dump
from json import load

"""pip install pyyaml"""


yaml_content = dump(load(open('group.json')))
print(yaml_content)