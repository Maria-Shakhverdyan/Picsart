def read_file_lines(file_path):
    try:
        file = open(file_path, 'r')
        for line in file:
            yield line
    except FileNotFoundError:
        print("The file was not found")
    finally:
        file.close()

file_path = 'file.txt'
for line in read_file_lines(file_path):
    print(line,end='')
