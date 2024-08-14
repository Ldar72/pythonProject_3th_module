def single_root_words(root_word, *other_words):
    root_word_lower = root_word.lower()
    same_words = []
    for word in other_words:
        if root_word_lower in word.lower() or word.lower() in root_word_lower:
            same_words.append(word)
    return same_words


result1 = single_root_words('брат', 'братство', 'братский', 'сестра', 'Братск')
result2 = single_root_words('body', 'anybody', 'BodyCam', 'Disable', 'somebody')
result3 = single_root_words('berries', 'Cranberries', 'Wildberries', 'pomegranate')

print(result1)
print(result2)
print(result3)
