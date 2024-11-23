# Read a whole file

with open(r'06_File_Handling\example.txt' , 'r') as file:
    
    content = file.read()
    print(content)
    
###########################
    
# Read a file line by line

with open(r'06_File_Handling\example.txt' , 'r') as file:
    
    for line in file:
        
        print(line)   # this add 1 blank line in the output
        
    # After the first loop, the file object (file) has been fully read,
    # and there’s no content left for the second loop.
    # To read the file again, you must reset the file pointer to the beginning 
    # using file.seek(0) before the second loop:
        
    file.seek(0)
        
    for line1 in file:
        
        print(line1.strip())  # this not add blank line in the output
        
#####################

# writing a file

with open(r'06_File_Handling\example.txt' , 'a') as file:
    
    file.write('I want to become Generative AI expert \n')
    file.write('My goal is to make a unicorn company\n')
    file.write('I live in Pakistan\n')
    
##########################

# overwriting a file

with open(r'06_File_Handling\example.txt' , 'w') as file:
    
    file.write('Assalmo Alikum \n')
    file.write('Welcome to pakistan \n')
    file.write('Pakistan is an atomic power\n')
    
############################

# writing a list of lines to a file

list = ['AI\n' , 'ML\n' , 'DL\n' , 'NLP\n' , 'Generative AI\n' , 'CV']

with open(r'06_File_Handling\example.txt' , 'a' ) as file:
    
    file.writelines(list)
    
with open(r'06_File_Handling\example.txt' , 'r') as file:
    
    read_data = file.read()
    
    print(read_data)

########################

# Binary files

# Writing to a binary files

data = b'\x00\x01\x02\x03\x04'

with open(r'06_File_Handling\binary_file.bin' , 'wb') as file:
    
    file.write(data)
    
# reading a binary file

with open(r'06_File_Handling\binary_file.bin' , 'rb') as file:
    
    content = file.read()
    
    print(content)
    
#####################

# copying a text file

with open(r'06_File_Handling\example.txt' , 'r') as file:
    
    content = file.read()
    
with open(r'06_File_Handling\destination.txt' , 'w') as destination_file:
    
    destination_file.write(content)
    
##################################

# Read a text file and count the number of lines , words and characters

# Procedure 1: Iterative Approach
with open(r'06_File_Handling\destination.txt', 'r') as file:
    lines = 0
    total_words = []
    characters = 0
    
    for line in file:
        words = line.split()
        total_words.extend(words)  # Add all words to the list
        characters += sum(len(word) for word in words)  # Count word characters only
        lines += 1
    
    print(f'Total number of lines in file: {lines}')
    print(f'Total words in file: {len(total_words)}')
    print(f'Total characters in file: {characters}')

# Procedure 2: Function Approach
def count_text_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        line_count = len(lines)
        word_count = sum(len(line.split()) for line in lines)
        char_count = sum(len(line.strip()) for line in lines)  # Excluding newlines
    return line_count, word_count, char_count

file_path = r'06_File_Handling\destination.txt'
lines, words, chars = count_text_file(file_path)
print(f'Lines: {lines}, Words: {words}, Characters: {chars}')

##############################

# Writing and then reading a file

with open(r'06_File_Handling\example.txt','w+') as file:
    
    file.write("Hello world\n")
    file.write("This is a new line \n")

    ## Move the file cursor to the beginning
    file.seek(0)

    ## Read the content of the file
    content=file.read()
    print(content)
