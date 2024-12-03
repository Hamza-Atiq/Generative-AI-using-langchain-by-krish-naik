import nltk
nltk.download('punkt')

# First define a corpus

corpus : str = """
Assalmo Alikum.
Welcome to NLP tutorials.
Please do watch the entire course ! to become expert in NLP.
"""

print(corpus , '\n')

##########################################

# Tokenization

# corpus --> sentence

# used Sentence tokenizer

from nltk.tokenize import sent_tokenize

documents : list = sent_tokenize(corpus)

print(documents , '\n')
print(type(documents) , '\n')

for sentence in documents:
    
    print(sentence)
    
####################################

# corpus --> words

# used Word tokenizer

from nltk.tokenize import word_tokenize

words : list = word_tokenize(corpus)

print('\n' , words , '\n')

for word in words:
    
    print(word)
    
print()
    
############################

# senetence --> words

# used Word tokenizer

for sentence in documents:
    
    print(word_tokenize(sentence))
    
##############################

# used wordpunct tokenizer which tokenize the ' also

from nltk.tokenize import wordpunct_tokenize

print('\n' , wordpunct_tokenize(corpus) , '\n')

############################

# used Treebankword tokenizer and its tokenize method it not seperate . in the tokenization 

from nltk.tokenize import TreebankWordTokenizer

tokenizer = TreebankWordTokenizer()

print(tokenizer.tokenize(corpus) , '\n')

print(dir(nltk) , '\n')

print(dir(nltk).index('TreebankWordTokenizer') , '\n')

print(dir(sent_tokenize) , '\n')

print(dir(TreebankWordTokenizer) , '\n')

