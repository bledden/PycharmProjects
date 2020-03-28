# Hi! This was made by Blake Ledden

# file = open('test.txt')
#
# file.close()


# Read the file and store all of the lines in the list
with open('test.txt', 'r') as reader:  # This line eliminates the need for file.close(); 'r' opens it in read mode
    content = reader.readlines()  # passes the list into object "content"
    reversed(content)  # Reverses the list, but we are only reading it
    with open('test.txt', 'w') as writer:  # Opens the file in write mode with 'w', this will change the file
        for line in reversed(content):  # This goes line by line, but in the reverse order presented by the object
            writer.write(line)  # This writes the lines
