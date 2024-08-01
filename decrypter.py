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


def consonant_processing(char_list, joined_word, punc_list, end_consonants):
    rear_letters = []
    cut_split = []
    move_letters = []
    extended_list = []
    full_word = ''
    while True:
        try:
            if end_consonants == 5:
                print("'" + joined_word + "'" ' failed to decrypt' + '\n')
                return '|decryption_failure|'
            rear_letters = len(char_list) - end_consonants
            cut_split = char_list[:rear_letters]
            move_letters = char_list[rear_letters:]
            print('Processing', joined_word + '_' + str(end_consonants))
            print(char_list)
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
        except:
            print('An error occured. Are you sure you entered ciphertext?')


def vowel_processing(char_list, joined_word, end_consonants, punc_list):
    vowel_state = False
    word = ''
    try:
        if char_list[len(char_list)-1] == 'y':    # the word is a vowel according to pig latin rules
            print('Processing', joined_word + '_' + str(end_consonants))
            char_list.pop()
            word = "".join(char_list)
            print(char_list)
            print("'" + word + "'" + ' is a recognized word.' + '\n')
            vowel_state = True
            if punc_list:   # reassembles punctuation, and returns word
                char_list = char_list + punc_list
                word = "".join(char_list)
        return word, vowel_state
    except:
        print('An error occured. Are you sure you entered ciphertext?')
        vowel_state = False


def casing_filter(char_list):
    for x in range(len(char_list)):
        char_list[x] = char_list[x].lower()
    return char_list


def punctuation_filter(char_list):
    punc_list = []  # resets for each word
    pop_list = []   # resets for each word
    for x in range(len(char_list)):
        if char_list[x] in end_punc:
            print('Punctuation detected, sorting')
            punc_list.append(char_list[x])
            pop_list.append(x)
        elif char_list[x] in else_punc:
            print('Purging unneeded punctuation')
            pop_list.append(x)
    if pop_list:
        for x in sorted(pop_list, reverse=True):
            char_list.pop(x)
    return char_list, punc_list


def capitalization_processing(final_sentence, full_stop_punc, sentence):
    final_sentence[0] = final_sentence[0].capitalize()  # Capitalizes very first character of first word
    if sentence == True:
        for z in range(1, len(final_sentence)):
            for currentChar in final_sentence[z-1]:
                if currentChar in full_stop_punc:  # if a full-stop punctuation is detected, capitalize the next word
                    final_sentence[z] = final_sentence[z].capitalize()
            return final_sentence
    else:
        return final_sentence
    
    
def decrypter(word):
    # variable initialization
    word_split = []
    end_consonants = 1
    joined_word = ''.join(word)
    
    # delay between each word process
    time.sleep(gap_time)

    for x in word:  # splits word into list containing each individual character
        if x in nums:   
            return word
        word_split.append(x)

    word_split = casing_filter(word_split)  # renders entire string lowercase
    word_split, punc_list = punctuation_filter(word_split) # Punctuation extraction and filtering

    for y in range(2):  # remove final 'ay' from word
        word_split.pop()
    
    full_word, vowel_state = vowel_processing(word_split, joined_word, end_consonants, punc_list)

    if vowel_state == True:
        return full_word
    else:
        full_word = consonant_processing(word_split, joined_word, punc_list, end_consonants)
        return full_word
            

def sentence(text_input):   # separates sentence into words and runs each through decrypter()
    global final_sentence
    final_sentence = []
    sentence = False
    sentence_initial = text_input.split()
    for x in sentence_initial:
        final_sentence.append(decrypter(x))
    
    if len(final_sentence) >= 2:
        sentence = True

    final_sentence = capitalization_processing(final_sentence, full_stop_punc, sentence)


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


