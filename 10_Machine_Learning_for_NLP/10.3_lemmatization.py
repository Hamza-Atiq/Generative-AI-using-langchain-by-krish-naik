import nltk
nltk.download('wordnet')

words : list[str] = ['eating' , 'eats' , 'eaten' , 'writing' , 'writes' , 'programming' , 
                     'programs' , 'history' , 'finally' , 'finalized' , 'congraltulations',
                     'sitting' , 'running' , 'walking' , 'jogging' , 'swimming' , 'playing' ,
                     'horse ridding' , 'fairly' , 'sportingly'] 

print(words)

##################################

# Lemmatizer used for chatbots , text summarization

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print('Word Net Lemmatizer with pos tag \'n\' : ')

"""
Post tag in lammatizer 

Noun - n
Verb - v
Adjective - a
adverb - r

"""

for word in words:
    
    print(f'{word} --------- > {lemmatizer.lemmatize(word , pos = 'n')}')
    
print()

####################################

print('Word Net Lemmatizer with pos tag \'a\' : ')

for word in words:
    
    print(f'{word} --------- > {lemmatizer.lemmatize(word , pos = 'a')}')
    
print()

#####################################

print('Word Net Lemmatizer with pos tag \'v\' : ')

for word in words:
    
    print(f'{word} --------- > {lemmatizer.lemmatize(word , pos = 'v')}')
    
print()

##################################

print('Word Net Lemmatizer with pos tag \'r\' : ')

for word in words:
    
    print(f'{word} --------- > {lemmatizer.lemmatize(word , pos = 'r')}')
    
print()

