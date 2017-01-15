import json
import yaml


sample_list = ['first string', 'second string']
sample_list.append({'ip_addr': '10.10.10.101', 'attribs': range(8)})

with open('yaml_output.yml', 'w') as f:
    f.write(yaml.dump(sample_list))
    f.close()

with open('json_output.json', 'w') as f:
    f.write(json.dumps(sample_list))
    f.close()
