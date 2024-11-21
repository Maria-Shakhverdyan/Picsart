import yaml

'''Problem: You have been given a YAML file named config.yaml with configuration settings for a server and logging.
Your task is to load the data, change the server’s port number from 8080 to 9090, and save the modified data back to the YAML file.
'''

try:
    with open('config.yaml', 'r') as file:
        data = yaml.safe_load(file)
        if data is None:
            data = {}
        print("The loaded data:")
        print(data)
    
    if 'server' not in data:
        data['server'] = {}
    data['server']['port'] = 9090
    print("Updated data:")
    print(data)

    with open('config.yaml', 'w') as file:
        yaml.safe_dump(data, file)
        print("Data loaded to config.yaml successfuly.")
        
except Exception as e:
    print(f"Error: {e}")