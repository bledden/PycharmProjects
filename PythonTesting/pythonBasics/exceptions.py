# Hi! This was made by Blake Ledden

itemsInCart = 0
# 2 items will be added to the cart



if itemsInCart != 2:
    # raise Exception("Product Count Does Not Match")
    pass

assert(itemsInCart == 0)

# try , except (which is basically catch)

try:
    with open('test.txt', 'r') as reader:  # changing this file name is an example of try-except blocks
        print(reader.read())

except Exception as e:  # Printing the exception as e prints the error Python through instead of a custom error message
    print(e)

finally:  # Only use after try and except mechanism; gets executed no matter what at the end of the try-except block
    print("Cleaning up the records")
