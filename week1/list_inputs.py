import json
import yaml
import pprint


with open('yaml_output.yml', 'r') as f:
    output = yaml.load(f)
    pprint.pprint(output)
    f.close()

with open('json_output.json', 'r') as f:
    output = json.load(f)
    pprint.pprint(output)
    f.close()
