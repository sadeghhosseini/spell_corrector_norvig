import spell





def remove_erab(input_word):
    temp = input_word
    removables = ("َ", "ِ", "ُ" )#fathe, kasre, zamme    
    for rem in removables:
        temp = temp.replace(rem, "")
    return temp

def remove_erab_from_word_list(input_word_list):
    result_word_list = []
    temp_word = ''
    removables = ("َ", "ِ", "ُ" )#fathe, kasre, zamme  
    for word in input_word_list:
        temp_word = word  
        for rem in removables:
            temp_word = temp_word.replace(rem, "")
        result_word_list.append(temp_word)   
    return result_word_list

def correct(input_word):
    return spell.correction(input_word)





def read_from_file(path):
    fo = open(path, "r", encoding="utf8")
    result = fo.read()
    fo.close()
    return result

def text_to_word_list(big_text):
    '''gets big text returns list of all word in that text, 
    the first word will be the first owrd in the list and the second word, 
    the second in the list and so on'''
    result_list = big_text.split()
    return result_list

def correct_list(word_list):
    '''gets the list that contains words as it's elements, and class correct function on each of them'''
    corrected_word_list = []
    for word in word_list:
        corrected_word = correct(word)
        corrected_word_list.append(corrected_word)
    return corrected_word_list
        

# def correct_word_list(word_list):
#     result_str = ''
#     for word in word_list:
#         temp_word = correct(word)
#         result_str += temp_word
#     return result_str    

#How to use:

#1. Reading string from file
result = correct_list(remove_erab_from_word_list(text_to_word_list(read_from_file("to_be_corrected"))))
print(result)
#2 entering word in program
input_word = "هجامنش"
input_word = remove_erab(input_word)
print(correct(input_word))

