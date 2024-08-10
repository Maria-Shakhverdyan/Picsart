import json

def process_json(input_file, output_file, attribute, value):
    file = open(input_file, 'r')
    data = json.load(file)
    file.close()
    
    filtered_data = [entry for entry in data if entry.get(attribute) == value]
    
    file = open(output_file, 'w')
    json.dump(filtered_data, file)
    file.close()
    
    print(f"Filtered data has been written to {output_file}")
    
    
input_file = 'input_data.json'
output_file = 'output_data.json'
attribute = 'category'
value = 'literature'

process_json(input_file, output_file, attribute, value)