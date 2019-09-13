from json import load
import yaml


def json2yaml(json_file, yaml_file):
    json_content = load(open(json_file))
    yaml.dump(json_content, open(yaml_file, 'w'))


json2yaml('tmp.json', 'tmp.yaml')

"""http://collabedit.com/vqkeg"""
