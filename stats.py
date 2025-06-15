def num_words(file_contents):
    numwords = file_contents.split()
    number = len(numwords)
    return number
def get_character_count(file_contents):
    letterdict = {}
    lowerchar = file_contents.lower()
    # Count the occurrences of each letter in the text
    for i in lowerchar:
        if i in letterdict:
            letterdict[i] += 1
        else:
            letterdict[i] = 1
    return letterdict
def convert_to_list(letterdict): 
    new_dict = {}
    new_list = []
    for i in letterdict:
        new_dict = {"char":i,"num":letterdict[i]}
        new_list.append(new_dict)
    return new_list
def sort_on(new_list):
    return new_list["num"]
