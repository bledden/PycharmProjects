# Hi! This was made by Blake Ledden

# while loops

it = 10
# print(it)
print("**********************")
while it >= 1:
    if it == 9:
        print("Yo!")
        it -= 1  # Decrementing this here is what will keep it moving after the continue command, but also replace 9 with "Yo!"
        continue
    if it == 3:
        print("Yay")
        break
    print(it)
    it -= 1
print("This ish is finish")
