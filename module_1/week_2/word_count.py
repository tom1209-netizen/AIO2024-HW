def count_word(file_path):
    file_content = open(file_path, 'r').read()

    counter = {}
    words = [word.lower() for word in file_content.split()]

    for word in words:
        counter[word] = words.count(word)

    return counter


file_path = 'content/P1_data.txt'
result = count_word(file_path)
assert result['who'] == 3
print(result['man'])
