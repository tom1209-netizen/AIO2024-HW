word = "hello"


def character_count(word):
    character_statistic = {}
    chars = list(word)

    for char in list(word):
        character_statistic[char] = chars.count(char)

    return character_statistic


assert character_count("Baby") == {'B': 1, 'a': 1, 'b': 1, 'y': 1}
print(character_count('smiles'))
