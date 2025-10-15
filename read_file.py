import os #<-- use to join the path

#w - write mode
#a - append mode
#x - create new file
#r - read mode

# file_path= r"/Users/aziim/Desktop/AI:ML/Day8_exception/files"

file_path = os.getcwd()
filename = input("Enter file name to update file: ") #<-- create file
fullpath = os.path.join(file_path,filename)
if(os.path.exists(fullpath)):
    file = open(fullpath, 'r')
    content = file.read()
    print('File content as follows')
    print(content)
    file.close()
else:
    print(f"{filename} does not exists")