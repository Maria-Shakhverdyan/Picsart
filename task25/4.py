import time

def retry(retry_count):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempt = 0
            
            while attempt < retry_count:
                try:
                    func(*args, **kwargs)
                except Exception as e:
                    attempt += 1
                    print(f"The attempt {attempt} failed: {e}")
                    time.sleep(2)
            raise Exception(f"Function failed after {retry_count} retries")
        return wrapper
    return decorator

@retry(retry_count = 3)
def read_file(path):
    print(f"Trying to read {path}...")
    file = open(path, 'r')
    data = file.read()
    file.close()

    return data

try:
    content = read_file('test.txt')
    print("File content:", content)
except Exception as e:
    print(e)
