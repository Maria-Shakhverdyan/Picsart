def read(file_name):
    try:
        file = open(file_name, 'r')
        content = file.read()
        file.close()
        return content
    except FileNotFoundError:
        return (f"The file {file_name} not found")
    except IOError:
        return (f"Error while reading the file {file_name}")

def write(file_name, content):
    try:
        file = open(file_name, 'w')
        file.write(content)
        file.close()
        return ("Content written to file")
    except IOError as e:
        return f"Error writing to file '{file_name}': {e}"

def append(file_name, content):
    try:
        file = open(file_name, 'a')
        file.write(content)
        file.close()
        return ("Content appended to file")
    except IOError as e:
        return f"Error writing to file '{file_name}': {e}"


def delete(file_name):
    try:
        file = open(file_name, 'r')
        file.close()
        file = open(file_name, 'w')
        file.close()
        return ("The file was deleted")
    except FileNotFoundError:
        return (f"The file {file_name} not found")
    except IOError:
        return (f"Error while reading the file {file_name}")

file_opers = {
    'read' : read,
    'write' : write,
    'append' : append,
    'delete' : delete
}

def file_manager(file_name, operation, content=None):
    if operation not in file_opers:
        return ("Unsupported operation")
    if operation in ['write', 'append'] and content is None:
        return ("Not such content to write or append")
    
    try:
        file_func = file_opers[operation]
        if operation in ['write', 'append']:
            return file_func(file_name, content)
        if operation in ['read', 'delete']:
            return file_func(file_name)
        
    except Exception as e:
        print(e)

    
file_name = 'test.txt'

try:
    print(file_manager(file_name, 'write', 'hello world'))
    print("Read file: ", file_manager(file_name, 'read'))
    print(file_manager(file_name, 'append', '\nhow are you'))
    print("Read file after append: ", file_manager(file_name, 'read'))
    print(file_manager(file_name, 'delete'))
except ValueError as e:
    print(e)