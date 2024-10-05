'''Semantic Similarity

Author: Michael Guerzhoy. 
Modified by: Vhea He
UTORid: hevhea
Student Number: 1009525202
'''

import math


def norm(vec):
    '''Return the norm of a vector stored as a dictionary, as 
    described in the handout for Project 3.
    '''
    
    sum_of_squares = 0.0  
    for x in vec:
        sum_of_squares += vec[x] * vec[x]
    
    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
    #computes dot product numerator
    dot_sum = 0 
    for word, count in vec1.items():
        if (word in vec1) and (word in vec2):
            dot_sum += vec1[word]*vec2[word]
    
    #computes magnitude product
    mag_sum_1 = 0
    for word, count in vec1.items():
        mag_sum_1 += count**2

    mag_sum_2 = 0
    for word, count in vec2.items():
        mag_sum_2 += count**2
    
    return dot_sum/(mag_sum_2 * mag_sum_1)**0.5

def build_semantic_descriptors(sentences):
    main_dic = {}
    for sen in sentences:
        counted_words = {}
        for word in sen:
            if word in counted_words:
                continue
            if main_dic.get(word) == None:
                main_dic[word] = {}
                counted_words[word] = 1
            for w in sen:
                if w != word:
                    if w in main_dic[word]:
                        main_dic[word][w] += 1
                    else:
                        main_dic[word][w] = 1
    return main_dic

    #dic or setS

#HELPER FUNCTION
# splits a sentence into a list of words
def split_sentence(sentence):
    res = sentence.split()
    return res

def build_semantic_descriptors_from_files(filenames):
    sentences = []
    for i in range (len(filenames)):
        file = open(filenames[i], "r", encoding="latin1").read()
        #make everything lowercase
        file = file.lower()

        #get rid of mid sentence punctuations and special characters
        file = file.replace(",", "")
        file = file.replace("-", "")
        file = file.replace("--", "")
        file = file.replace(":", "")
        file = file.replace(";", "")
        file = file.replace("'", "")
        file = file.replace("_", "")
        file = file.replace("\"", "")
        file = file.replace("\n", " ")
        file = file.replace("\t", " ")
        file = file.replace("(", " ")
        file = file.replace(")", " ")
        file = file.replace("â\x80\x9c", "")
        file = file.replace("â\x80\x94", " ")
        file = file.replace("â\x80\x99", "")
        file = file.replace("â\x80\x9d", "")
        file = file.replace("â\x80\x98", "")
        file = file.replace("  ", " ")
        file = file.replace("   ", " ")

        #replace all sentence ending punctuation with periods
        file = file.replace("!", ".")
        file = file.replace("?", ".")
        file = file.split(".")

        for sen in file:
            sentences.append(split_sentence(sen))

    dic = build_semantic_descriptors(sentences)

    return dic 

def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    cur_max_score = -1
    cur_best_word = None
    for option in choices:
        if option in semantic_descriptors and word in semantic_descriptors:
            vec1 = semantic_descriptors[option]
            vec2 = semantic_descriptors[word]
            sim_score = similarity_fn(vec1, vec2)
            if sim_score > cur_max_score:
                cur_max_score = sim_score
                cur_best_word = option
        else:
            sim_score = -1
    return cur_best_word

#HELPER FUNCTION
# return number of matching elements in two lists
def how_many_correct(guesses, answers):
    num_correct = 0
    for i in range(len(guesses)):
        if guesses[i] == answers[i]:
            num_correct += 1
    return num_correct

def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    txt = open(filename, "r", encoding="latin1").read()
    txt = txt.split("\n")
    questions = []
    answers = []
    guesses = []
    for sen in txt:
        sen = sen.split(" ")
        q = sen[0]
        a = sen[1]
        choices = sen[2:]
        questions.append([q, choices])
        answers.append(a)
    for q in questions:
        guess = most_similar_word(q[0], q[1], semantic_descriptors, similarity_fn)
        guesses.append(guess)
    res = (how_many_correct(guesses, answers)/len(answers))*100
    return res
