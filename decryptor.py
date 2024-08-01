import enchant
import time
# Create a dictionary object for English (US)
d = enchant.Dict('en_US')

version = str('1.4.2')

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
    pop_list = []
    puncList = []
    failcount = 1
    joined_word = ''.join(word)
    l = 1
    original = ''
    for x in word: #
        if x in nums: # instantly returns if number
            return word
        word_split.append(x)
    for x in range(len(word_split)):
        word_split[x] = word_split[x].lower() # converts all strings to lowercase
    for x in range(len(word_split)):
        if word_split[x] in punctuation:
            print('Punctuation detected, sorting')
            puncList.append(word_split[x])
            word_split.pop(x)


    for y in range(2):
        word_split.pop()
    if word_split[len(word_split)-1] == 'y': # considers the word originally as a vowel
        print('Processing', joined_word + '_' + str(failcount))
        word_split.pop()
        word = "".join(word_split)
        print(word_split)
        print("'" + word + "'" + ' is a recognized word.' + '\n')
        if puncList:
            word_split = word_split + puncList
            word = "".join(word_split)
        return word
    else:
        while True:
            if l == 5:
                print("'" + joined_word + "'" ' failed to decrypt' + '\n')
                return('error')
            rearLetters = len(word_split) - l
            cutSplit = word_split[:rearLetters]
            moveLetters = word_split[rearLetters:]
            print('Processing', joined_word + '_' + str(failcount))
            print(word_split)
            print(moveLetters)
            print(cutSplit)
            extended_list = moveLetters + cutSplit
            fullWord = "".join(extended_list)
            print(fullWord)
            if d.check(fullWord):
                print("'" + fullWord + "'" + ' is a recognized word.' + '\n')
                if puncList:
                    print('Punctuation detected, sorting')
                    extended_list = extended_list + puncList
                    fullWord = "".join(extended_list)
                return fullWord
            else:
                print("'" + fullWord + "'" ' is not a recognized word.' + '\n')
                l += 1
                failcount += 1










def sentence(text_input):
    global final_sentence
    final_sentence = []
    sentence_initial = text_input.split()

    for x in sentence_initial:
        final_sentence.append(decryptor(x))
        time.sleep(0.05)
    print(final_sentence[0])

    # Capitalization sequence
    final_sentence[0] = final_sentence[0].capitalize()  # Capitalizes very first character of first word
    for z in range(1, len(final_sentence)):
        for currentChar in final_sentence[z-1]: # cycles through every character of every word
            if currentChar in full_stop_punc:  # if a full-stop punctuation is detected, capitalize the next word
                final_sentence[z] = final_sentence[z].capitalize()
                pass
    # -----------------------


    joined_sentence = " ".join(final_sentence)
    return joined_sentence

def loopStart(text_input):
    print('\n' + '\n' + '\n' + '\n' + 'Decrypted Result:' + '\n' + sentence(text_input) + '\n' + '\n')
    for x in final_sentence:
        if x == 'error':
            print('Errors detected. Check log for anything verification could have missed.' + '\n')
            break
    exitCode = input(str('\n' + 'Enter t to translate another sentence. Enter any other key to exit.' + '\n'))
    return exitCode






exitCode1 = str(loopStart(text_input))


while True:
    if exitCode1 in ['t', 'T']:
        text_input = input(str('\n' + 'Enter text for decryption:' + ' \n'))
        exitCode1 = loopStart(text_input)
    elif exitCode1 is None:
        print('Program Terminating...')
        time.sleep(1.5)
        break
    else:
        print('Program Terminating...')
        time.sleep(1.5)
        break


