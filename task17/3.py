filename = 'specific_position.txt'

initial_text = "This is the initial text in the file.\n"

text_to_write = "This text is written at a specific position.\n"

write_position = 10

try:
    file = open(filename, 'r+')
    
except FileNotFoundError:
    file = open(filename, 'w')
    file.write(initial_text)
    file.close()
    file = open(filename, 'r+')

content = file.read()

new_content = content[:write_position] + text_to_write + content[write_position:]

file.seek(0)

file.write(new_content)

file.close()

print(f"Text has been written to {filename} at position {write_position}.")
