#mazoxisttt

def process_json(input_file, output_file, attribute, value):
    try:
        file = open(input_file, 'r')
        content = file.read()
        file.close()

        data = []
        content = content.strip()[1:-1].split('}, {')
        for entry in content:
            entry_dict = {}
            entry = entry.strip('{} ')
            items = entry.split(', ')
            for item in items:
                key, val = item.split(': ')
                key = key.strip('\'"')
                val = val.strip('\'"')
                val = int(val) if val.isdigit() else val
                entry_dict[key] = val
            data.append(entry_dict)

        filtered_data = []
        for entry in data:
            if entry.get(attribute) == value:
                filtered_data.append(entry)

        json_string = '['
        for entry in filtered_data:
            json_string += '{'
            for key, val in entry.items():
                if isinstance(val, str):
                    json_string += f'"{key}": "{val}", '
                else:
                    json_string += f'"{key}": {val}, '
            json_string = json_string.rstrip(', ') + '}, '
        json_string = json_string.rstrip(', ') + ']'

        file = open(output_file, 'w')
        file.write(json_string)
        file.close()

        print(f"Filtered data has been written to {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

input_file = 'input_data.json'
output_file = 'output_data.json'
attribute = 'category'
value = 'electronics'

process_json(input_file, output_file, attribute, value)
