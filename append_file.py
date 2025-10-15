import os #<-- use to join the path

# file_path= r"/Users/aziim/Desktop/AI:ML/Day8_exception/files"
#w - write mode
#a - append mode
#x - create new file
#r - read mode


#----------------------if the file doesnot exist in directory, print not exist-------------- 

# file_path = os.getcwd()
# filename = input("Enter file name to update file: ") #<-- create file
# fullpath = os.path.join(file_path,filename)
# if(os.path.exists(fullpath)):
#     file = open(fullpath, 'a')
#     content = input("Enter text to append in file: ")
#     file.write(content)
#     print(f'File {filename} updated')
#     file.close()
# else:
#     print(f"{filename} does not exists")


#------------------------if the file doesnot exist in directory, create new file--------------
file_path = os.getcwd()
filename = input("Enter file name to update file: ") #<-- create file
fullpath = os.path.join(file_path,filename)

file = open(fullpath, 'a')
content = input("Enter text to append in file: ")
file.write(content)
print(f'File {filename} updated')
file.close()

