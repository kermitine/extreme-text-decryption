import enchant

# Create a dictionary object for English (US)
d = enchant.Dict('en_US')

version = str(0.3)
print('Decryptor V' + version)

text_input = input(str('\n' + 'Enter text for decryption:' + ' \n'))



def decryptor(word):
    word_split = []
    l = 1
    original = ''
    # piss is isspay
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
            if l == 4:
                print('Error, no word detected.')
                break
            rearLetters = len(word_split) - l
            cutSplit = word_split[:rearLetters]
            moveLetters = word_split[rearLetters:]
            print(cutSplit)
            print(moveLetters)
            extended_list = moveLetters + cutSplit
            print(extended_list)
            fullWord = "".join(extended_list)
            print(fullWord)
            if d.check(fullWord):
                print(fullWord, 'is a real word.')
                return fullWord
            else:
                print(f"'{fullWord}' is not a real word.")
                l += 1










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