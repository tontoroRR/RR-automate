import yaml
import json

with open("modules/resources/units_common.yml", "r") as file:
    data = yaml.safe_load(file)

print(json.dumps(data, indent=2))
