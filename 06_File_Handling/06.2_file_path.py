import os

# Creat a new directory

new_directory = 'package'
directory_path = '06_File_Handling/' + new_directory

if os.path.exists(directory_path):
    print(f'The directoy {new_directory} already exist')
    
else:
    
    os.mkdir(directory_path)

    print(f"Directory '{new_directory}' created")

# Listing files and directories

files = os.listdir('.')
print(files)

####################

# joining paths

dir_name = 'folder'
file_name = 'file.txt'

full_path = os.path.join(dir_name , file_name)

print(full_path)

# with current directory

dir_name = 'folder'
file_name = 'file.txt'

full_path = os.path.join(os.getcwd(),dir_name , file_name)

print(full_path)

##########################

# Checking if a Path is a File or Directory

path = '06_File_Handling/example.txt'

if os.path.isfile(path):
    
    print(f"The path '{path}' is a file.")
    
elif os.path.isdir(path):
    
    print(f"The path '{path}' is a directory.")
    
else:
    
    print(f"The path '{path}' is neither a file nor a directory.")
    
################

# Getting the absolute path

relative_path = 'example.txt'

absolute_path = os.path.abspath(relative_path)

print(absolute_path)