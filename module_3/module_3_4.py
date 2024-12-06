
def single_root_words(root_word,*other_words):
    same_words = []
    up_root_word = root_word.upper()

    for word in other_words:
        up_word = word.upper()
        if up_root_word in up_word :
            same_words.append(word)
            continue
        elif up_word in up_root_word :
            same_words.append(word)
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)