import enchant
import time
from files.vars import *
from files.ascii import *
# Create a dictionary object for English (US)
d = enchant.Dict('en_US')

print(ascii_kermitine_portrait)
print(ascii_kermitine)

print('Decrypter V' + version)
print('Powered by PyEnchant')

text_input = input(str('\n' + 'Enter text for decryption:' + ' \n'))


def decrypter(word):
    word_split = []
    punc_list = []
    pop_list = []
    fail_count = 1
    joined_word = ''.join(word)
    end_consonants = 1
    time.sleep(gap_time)

    for x in word:  # splits word into list containing all characters
        if x in nums:   # instantly returns if it's a number
            return word
        word_split.append(x)

    # renders all characters lowercase----------------------------------------------------------------------------------
    for x in range(len(word_split)):
        word_split[x] = word_split[x].lower()
    # ------------------------------------------------------------------------------------------------------------------

    # Punctuation extraction and purging----------------------------------------------------------------------------
    for x in range(len(word_split)):
        if word_split[x] in end_punc:
            print('Punctuation detected, sorting')
            punc_list.append(word_split[x])
            pop_list.append(x)
        elif word_split[x] in else_punc:
            print('Purging unneeded punctuation')
            pop_list.append(x)
    if pop_list:
        for x in sorted(pop_list, reverse=True):
            word_split.pop(x)
    # ------------------------------------------------------------------------------------------------------------------

    for y in range(2):  # remove final 'ay' from word
        word_split.pop()
    if word_split[len(word_split)-1] == 'y':    # the word is a vowel according to pig latin rules
        print('Processing', joined_word + '_' + str(fail_count))
        word_split.pop()
        word = "".join(word_split)
        print(word_split)
        print("'" + word + "'" + ' is a recognized word.' + '\n')
        if punc_list:   # reassembles punctuation, and returns word
            word_split = word_split + punc_list
            word = "".join(word_split)
        return word
    else:
        while True:
            if end_consonants == 5:
                print("'" + joined_word + "'" ' failed to decrypt' + '\n')
                return '|decryption_failure|'
            rear_letters = len(word_split) - end_consonants
            cut_split = word_split[:rear_letters]
            move_letters = word_split[rear_letters:]
            print('Processing', joined_word + '_' + str(fail_count))
            print(word_split)
            print(move_letters)
            print(cut_split)
            extended_list = move_letters + cut_split
            full_word = "".join(extended_list)
            print(full_word)
            if d.check(full_word):
                print("'" + full_word + "'" + ' is a recognized word.' + '\n')
                if punc_list:   # reassembles punctuation, and returns word
                    extended_list = extended_list + punc_list
                    full_word = "".join(extended_list)
                return full_word
            else:
                print("'" + full_word + "'" ' is not a recognized word.' + '\n')
                end_consonants += 1
                fail_count += 1


def sentence(text_input):   # separates sentence into words and runs each through decrypter()
    global final_sentence
    final_sentence = []
    sentence_initial = text_input.split()

    final_sentence = [decrypter(x) for x in sentence_initial]

    # Capitalization sequence
    final_sentence[0] = final_sentence[0].capitalize()  # Capitalizes very first character of first word
    for z in range(1, len(final_sentence)):
        for currentChar in final_sentence[z-1]:
            if currentChar in full_stop_punc:  # if a full-stop punctuation is detected, capitalize the next word
                final_sentence[z] = final_sentence[z].capitalize()
    # -----------------------


    joined_sentence = " ".join(final_sentence)
    return joined_sentence


def loopStart(text_input):
    print('\n' + '\n' + '\n' + '\n' + 'Decrypted Result:' + '\n' + sentence(text_input) + '\n' + '\n')
    for x in final_sentence:
        if x in ['decryption_failure', 'Decryption_failure']:
            print('Errors detected. Check log for anything verification could have missed.' + '\n')
            break
    input_code = input(str('\n' + 'Enter t to translate another sentence. Enter any other key to exit.' + '\n'))
    return input_code


# Continuous code loop

exit_code = str(loopStart(text_input))

while True:
    if exit_code in ['t', 'T']:
        text_input = input(str('\n' + 'Enter text for decryption:' + ' \n'))
        exit_code = loopStart(text_input)
    else:
        print('Program Terminating...')
        time.sleep(1.5)
        break

# ------------------------


