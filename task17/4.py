filename = 'peterrabbit.txt'

words_to_count = ["example", "all", "word", "up", "did", "him"]

word_counts = {word: 0 for word in words_to_count}

file = open(filename, 'r')

content = file.read().lower()

file.close()

for word in words_to_count:
    word_counts[word] = content.split().count(word)

for word, count in word_counts.items():
    print(f"The word '{word}' appears {count} times in the file.")
