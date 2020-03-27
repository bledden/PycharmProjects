# Hi! This was made by Blake Ledden

file = open('test.txt')  # Use single quotations when designating file path; this file is in the same directory
# print(file.read())  # Reads all of the contents of the file
# print(file.read())  # Placing numbers inside the parentheses has it read n number of characters

# print(file.readline())  # Reads first line
# print(file.readline())  # Reads second line
# print(file.readline())  # Reads third line

line = file.readline()
while line != "":
    


file.close()  # Always close your files
