import spell





def removeErab(input_word):
    temp = input_word
    removables = ("َ", "ِ", "ُ" )#fathe, kasre, zamme    
    for rem in removables:
        temp = temp.replace(rem, "")
    
    return temp

def correct(input_word):
    return spell.correction(input_word)


input_word = "هجامنش"
input_word = removeErab(input_word)
print(correct(input_word))


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
    return corrected_word
        


result = text_to_word_list(read_from_file("to_be_corrected"))
#print (result)

