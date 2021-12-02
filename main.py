####### FUNÇÃO 1 #######
def list_comprehension_exercise_1():
    output = [i for i in range(11)]
    
    return output
        

####### FUNÇÃO 2 #######
def list_comprehension_exercise_2():
    output = [i for i in range(22) if i%2 == 0 or i%3 == 0]

    return output


####### FUNÇÃO 3 #######
def list_comprehension_exercise_3():
    output = [i for i in range(-5, 32, 2) if not i%5 == 0]

    return output


####### FUNÇÃO 4 #######
def list_comprehension_exercise_4():
    output = [i*i for i in range(11)]

    return output



####### FUNÇÃO 5 #######
def list_comprehension_exercise_5(sentence):
    output = [letter for letter in sentence if letter.isupper()]

    return output



####### FUNÇÃO 6 #######
def list_comprehension_exercise_6(sentence):
    word_list = sentence.split(' ')
    output = [word for word in word_list if word[0].lower() == 'r' and len(word) >= 4]

    return output