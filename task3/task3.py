import sys
import json


def value_inserter(d_list, id_, value):
    for el in d_list:
        if el['id'] == id_:
            el['value'] = value
            break
        else:
            if 'values' in el.keys():
                value_inserter(el['values'], id_, value)


with open(sys.argv[1], 'r') as f1:
    tests = json.load(f1)

with open(sys.argv[2], 'r') as f2:
    values = json.load(f2)

for i in values['values']:
    value_inserter(tests['tests'], i['id'], i['value'])

with open('report.json', 'w') as f3:
    json.dump(tests, f3, indent=2)
