filename = 'exclusive_mode.txt'

text_to_write = "This is the new text that will be written to the file.\n"

try:
    file = open(filename, 'x')
    file.write(text_to_write)
    file.close()
    print(f"Text has been written to {filename}.")
except FileExistsError:
    print(f"The file {filename} already exists.")
