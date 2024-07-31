import enchant
import time
# Create a dictionary object for English (US)
d = enchant.Dict('en_US')

version = str(1)

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

text_input = input(str('\n' + 'Enter text for decryption:' + ' \n'))
punctuation = ['!', '?', '.', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '#', '/', ':', ';',
                    '<', '=', '>', '"', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


def decryptor(word):
    word_split = []
    pop_list = []
    l = 1
    original = ''
    for x in word: #
        if x in nums: # instantly returns if number
            return word
        word_split.append(x) # converts all strings to lowercase
    for x in range(len(word_split)):
        if word_split[x] in punctuation: # filters and removes punctuation
            pop_list.append(x)
        word_split[x] = word_split[x].lower()
    if pop_list:
        for x in pop_list:
            word_split.pop(x)
            print('Filtering punctuation!')

    for y in range(2):
        word_split.pop()
    if word_split[len(word_split)-1] == 'y': # considers the word originally as a vowel
        print('Processing vowel word!')
        word_split.pop()
        word = "".join(word_split)
        print(word_split)
        print(word + ' is a real word.')
        return word
    else:
        while True:
            if l == 4:
                print('Word failed to decrypt')
                return('error')
            rearLetters = len(word_split) - l
            cutSplit = word_split[:rearLetters]
            moveLetters = word_split[rearLetters:]
            print('Processing consonant word!')
            print(word_split)
            print(cutSplit)
            print(moveLetters)
            extended_list = moveLetters + cutSplit
            fullWord = "".join(extended_list)
            print(fullWord )
            if d.check(fullWord):
                print(fullWord, 'is a real word.' + '\n')
                return fullWord
            else:
                print(fullWord, "is not a real word." + '\n')
                l += 1










def sentence(text_input):
    final_sentence = []
    sentence_initial = text_input.split()

    for x in sentence_initial:
        final_sentence.append(decryptor(x))

    joined_sentence = " ".join(final_sentence)
    return joined_sentence

def loopStart(text_input):
    print('\n' + '\n' + '\n' + '\n' + 'Decrypted Result:' + '\n' + sentence(text_input) + '\n' + '\n')
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


