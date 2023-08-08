def find_words(input_text, file_path):
    with open(file_path, 'r') as f:
        words = f.read().splitlines()
    output_words = []
    for word in words:
        if input_text in word:
            output_words.append(word)
    return output_words

input_text = 'TUAL'
file_path = 'kbbi.txt'
output_words = find_words(input_text, file_path)
print(output_words)
