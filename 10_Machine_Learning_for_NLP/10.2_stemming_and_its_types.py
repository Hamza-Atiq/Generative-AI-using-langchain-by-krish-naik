words : list[str] = ['eating' , 'eats' , 'eaten' , 'writing' , 'writes' , 'programming' , 
                     'programs' , 'history' , 'finally' , 'finalized' , 'congraltulations',
                     'sitting' , 'running' , 'walking' , 'jogging' , 'swimming' , 'playing' ,
                     'horse ridding' , 'fairly' , 'sportingly'] 

print(words)

##################

# for classification we mostly used stemming

# PorterStemmer

from nltk.stem import PorterStemmer

stemmer = PorterStemmer()        # Make an object
print('Port Stemmer : ')
for word in words:
    
    print(f'{word} --------- > {stemmer.stem(word)}')
    
print()
    
###########################

# RegexpStemmer class

from nltk.stem import RegexpStemmer

reg_stemmer = RegexpStemmer('ing$|s$|e$|able$' , min = 4)   # if $ in the last means remove from end

print('Regex Stemmer with $ in the last : ')

for word in words:
    
    print(f'{word} --------- > {reg_stemmer.stem(word)}')

print()

################################

reg_stemmer = RegexpStemmer('ing|s|e|able' , min = 4)   # if $ not in it , it will remove all  

print('Regex Stemmer without $ : ')

for word in words:
    
    print(f'{word} --------- > {reg_stemmer.stem(word)}')
    
print()
    
#################################

reg_stemmer = RegexpStemmer('$ing|$s|$e|$able' , min = 4)   # if $ in the last means remove from end

print('Regex Stemmer with $ in the start : ')

for word in words:
    
    print(f'{word} --------- > {reg_stemmer.stem(word)}')
    
print()

##############################

# SnowballStemmer

from nltk.stem import SnowballStemmer

snow_ball_stemmer = SnowballStemmer('english')

print('Snow Ball Stemmer : ')

for word in words:
    
    print(f'{word} --------- > {snow_ball_stemmer.stem(word)}')
    

