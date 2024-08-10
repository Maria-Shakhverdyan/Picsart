def file_data(input_file, output_file):
    word_count = 0
    char_count = 0
    line_count = 0

    file = open(input_file, 'r')

    for line in file:
        line_count += 1

        strip_line = line.strip()

        words = strip_line.split()
        word_count += len(words)

        char_count += len(strip_line)
    
    file.close()
    
    info = (
        f"Count of lines: {line_count}\n"
        f"count of words: {word_count}\n"
        f"count of characters: {char_count}\n"
    )
    
    file = open(output_file, 'w')
    file.write(info)
    file.close()
    
    print(f"The info has been written to {output_file}")

input_file = "test.txt"
output_file = "result.txt"
file_data(input_file, output_file)
