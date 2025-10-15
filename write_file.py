import os #<-- use to join the path

#w - write mode
#a - append mode
#x - create new file
#r - read mode

# file_path= r"/Users/aziim/Desktop/AI:ML/Day8_exception/files"

# file_path = "/Users/aziim/Desktop/AI:ML/Day8_filehandling/files"
file_path = os.getcwd()
filename = input("Enter file name to create file: ") #<-- create file
fullpath = os.path.join(file_path,filename)
file = open(fullpath, 'w')
content = input("Enter text to write in file: ")
file.write(content)
print(f'File {filename} create at {fullpath} and content saved in file')
file.close()