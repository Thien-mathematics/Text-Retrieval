import re

def Lowercasing(string):
    return string.lower()

def Punctuations_removal(string):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for x in string.lower(): 
        if x in punctuations: 
            string = string.replace(x, "") 
    return string

def URL_removal(string):
    return re.sub(r"http\S+", "", string)

def html_tags_removal(string):
    return re.sub(r'<[^>]+>', '', string)

def frequent_words_removal(string):
    frequent_words = ['a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'was', 'were', 'will', 'with']
    for x in string.split(): 
        if x in frequent_words: 
            string = string.replace(x, "") 
    return string

def tokenize(string):
    return string.split()

def create_dictionary(string):
    dictionary = {}
    for x in string:
        if x in dictionary:
            dictionary[x] += 1
        else:
            dictionary[x] = 1
    return dictionary

def One_hot_encoding(dictionary, string):
    one_hot_encoding = []
    for x in dictionary:
        if x in string:
            one_hot_encoding.append(1)
        else:
            one_hot_encoding.append(0)
    return one_hot_encoding


