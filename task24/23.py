def word_count(text):
    return len(text.split())

def char_count(text):
    return len(text)

def find_word(text, word):
    positions = []
    start = 0
    while True:
        start = text.find(word, start)
        if start == -1:
            break
        positions.append(start)
        start += len(word)
    return positions

def replace_word(text, old_word, new_word):
    return text.replace(old_word, new_word)

text_operations = {
    'word_count': word_count,
    'char_count': char_count,
    'find_word': find_word,
    'replace_word': replace_word
}

def process_text(text, operation, **kwargs):
    if operation not in text_operations:
        raise ValueError("Unknown operation")
    
    func = text_operations[operation]
    return func(text, **kwargs)

text = "hello world, my name is Maria"

try:
    print("Word count:", process_text(text, 'word_count'))
    print("Character count:", process_text(text, 'char_count'))
    print("Find 'Maria':", process_text(text, 'find_word', word='Maria'))
    print("Replace 'Maria' with 'John':", process_text(text, 'replace_word', old_word='Maria', new_word='John'))
except ValueError as e:
    print(e)
