import enchant
import time
# Create a dictionary object for English (US)
d = enchant.Dict('en_US')

version = str('1.4.4')

print('''                                                                                                       
                                                    ###%%%#*                                           
                                                  #%%%%%%%%%%*                                         
                                               +%%%%%%%%%%%%%%%#=                                      
                                            =#%%%%%%%%%%%%%%%%%%%%*                                    
                                          *%%%%%%%%%%%%%%%%%%%%%%@%%*                                  
                                      =*#%%%%%%%%%%%%%%%%%%%%%@@%%@@%#                                 
                                    *%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@%                                
      -----                       #%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@+                              
    -=++*#+=-                  +#@@@@@@@@@@@@@@@@@@%%%%%@@@@@@@@@@@@@@@@@*                             
    -+#+:=#*=-               *%@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%@%%@@@@@@@@@@*                            
    -=*#=:-##+-            *@@@@@@@@@%%%%%%%%%%%@@@@@@@@@@%%%%%@@@@@@@@@@@@#                           
      =*#=:-*#+-          @@@@@@@@%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@%                          
       =*#+::*#+-        #@@@@@@@%%%#####%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@%*                        
        =*#+::*#+-      *@@@@@@@%%#########%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@%+                       
         -+#+::+#*=     %@@@@@@%%##*****#####%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@+                      
          -+#*::+#*=   #@@@@@@@%#******#####%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@%                      
           -+#*-:=#*= +%@@@@@@@%#*****######%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@+                      
            -+#*-:=#*=#@@@@@@@@@##**######%%%%%%%%%@@@@%%%%%%@@@@@@@@@@@@@@@@@@@+                      
             -=##-:-###%@@@@@@@%#@@@%%%%@@@@@@%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@*                     
              -=*#=:-###%@@@@@@%#**####%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@%-                    
               -=*#=:-###%@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@#                    
                -=*#+::*##%@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@*                   
                  =##+::*##%@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@%-                  
                   ###*::+###@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@%                  
                  +@%##*::+###@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@*                 
                  =@@%##*-:=###@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@%+                
                  *@@@%###-:=###%@@@@@@@@%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@#                
                  %@@@@%###-:-###%@@@@@@@@%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@%                
                  %@@@@@%###=:-###%@@@@@@@@@@@@%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#               
                  @@@@@@@%###=:-###%@@@@@@@@@@@@%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-              
                  %@@@@@@@@###+::*##%@@@@@@@@@@%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#              
                  %@@@@@@@@@###+::*##%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*             
                  *@@@@@@@@@@%##*::+###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=            
                  +@@@@@@@@@@@%##*::+###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%*             
                  =@@@@@@@@@@@@%###-:=###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%              
                   #@@@@@@@@@@@@%###-.=###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*             
                   #@@@@@@@@@@@@@%###=-+*#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#             
                    ##@@@@@@@@@@@@@##*%#**@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#            
                        +@@@@@@@@@@@%%#%*##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#            
                       *@@@@@@@@@@@@@@@%%@*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#           


                                                                                                       ''')

print(''' __                             .__   __   .__                 
|  | __  ____  _______   _____  |__|_/  |_ |__|  ____    ____  
|  |/ /_/ __ \ \_  __ \ /     \ |  |\   __\|  | /    \ _/ __ \ 
|    < \  ___/  |  | \/|  Y Y  \|  | |  |  |  ||   |  \\  ___/ 
|__|_ \ \___  > |__|   |__|_|  /|__| |__|  |__||___|  / \___  >
     \/     \/               \/                     \/      \/ ''')


print('Decryptor V' + version)
print('Powered by PyEnchant')

text_input = input(str('\n' + 'Enter text for decryption:' + ' \n'))
punctuation = ['!', '?', '.', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '#', '/', ':', ';',
                    '<', '=', '>', '"', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
full_stop_punc = punctuation[:3]
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


def decryptor(word):
    word_split = []
    punc_list = []
    fail_count = 1
    joined_word = ''.join(word)
    end_consonants = 1
    for x in word:
        if x in nums:   # instantly returns if number
            return word
        word_split.append(x)

    # Lowercase sequence
    for x in range(len(word_split)):
        word_split[x] = word_split[x].lower()
    # ------------------

    # Punctuation extraction
    for x in range(len(word_split)):
        if word_split[x] in punctuation:
            print('Punctuation detected, sorting')
            punc_list.append(word_split[x])
            word_split.pop(x)
    # -------------------

    for y in range(2):
        word_split.pop()
    if word_split[len(word_split)-1] == 'y':    # considers the word as a vowel
        print('Processing', joined_word + '_' + str(fail_count))
        word_split.pop()
        word = "".join(word_split)
        print(word_split)
        print("'" + word + "'" + ' is a recognized word.' + '\n')
        if punc_list:
            word_split = word_split + punc_list
            word = "".join(word_split)
        return word
    else:
        while True:
            if end_consonants == 5:
                print("'" + joined_word + "'" ' failed to decrypt' + '\n')
                return 'error'
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
                if punc_list:
                    print('Punctuation detected, sorting')
                    extended_list = extended_list + punc_list
                    full_word = "".join(extended_list)
                return full_word
            else:
                print("'" + full_word + "'" ' is not a recognized word.' + '\n')
                end_consonants += 1
                fail_count += 1










def sentence(text_input):
    global final_sentence
    final_sentence = []
    sentence_initial = text_input.split()

    for x in sentence_initial:
        final_sentence.append(decryptor(x))
        time.sleep(0.05)

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
        if x == 'error':
            print('Errors detected. Check log for anything verification could have missed.' + '\n')
            break
    input_code = input(str('\n' + 'Enter t to translate another sentence. Enter any other key to exit.' + '\n'))
    return input_code


# Continuous code loop
exit_code = str(loopStart(text_input))  # calls loopStart() which calls all other functions. loopstart() returns input_code

while True:
    if exit_code in ['t', 'T']:
        text_input = input(str('\n' + 'Enter text for decryption:' + ' \n'))
        exit_code = loopStart(text_input)
    else:
        print('Program Terminating...')
        time.sleep(1.5)
        break

# ------------------------


