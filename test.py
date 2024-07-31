import enchant

# Create a dictionary object for English (US)
d = enchant.Dict('en_US')

text_input = input(str('\n' + 'Enter text for decryption:' + ' \n'))



def decryptor(word):
    word_split = []
    # ayrikyay
    for x in word:
        word_split.append(x)
    for y in range(2):
        word_split.pop()
    if word_split[len(word_split)-1] == 'y': # considers the word originally as a vowel
        word_split.pop()
        word = "".join(word_split)
        return word
    else:
        while True:
            last_element = word_split.pop()
            word_split.insert(0, last_element)
            word = "".join(word_split)
            if d.check(word):
                return word
            else:
                print('not a real word!')
                break
    return word_split
def sentence(text_input):
    final_sentence = []
    sentence_initial = text_input.split()

    for x in sentence_initial:
        final_sentence.append(decryptor(x))
    print(final_sentence)



sentence(text_input)

'''if d.check(word):
    print(f"'{word}' is a real word.")
else:
    print(f"'{word}' is not a real word.")'''