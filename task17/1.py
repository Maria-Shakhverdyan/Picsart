filename = 'append_mode.txt'

text_to_append = "Text appended to file.\n"

file = open(filename, 'a')
file.write(text_to_append)
file.close()

print(f"Text has been appended to {filename}.")