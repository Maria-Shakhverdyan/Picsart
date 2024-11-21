import yaml
import json

'''Problem: Convert a complex YAML structure into JSON format.
The YAML data will contain nested lists and dictionaries. After converting, save it as data.json.
Be sure to validate that the JSON structure retains all information.
'''

try:
    with open('config.yaml', 'r') as file:
        data = yaml.safe_load(file)

    with open('new.json', 'w') as file:
        json.dump(data, file, indent=2)
        print("Data loaded to new.json successfuly.")
        
except Exception as e:
    print(f"Error: {e}")