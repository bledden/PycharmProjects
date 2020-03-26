# Hi! This was made by Blake Ledden

# if loops

greeting = "Morning"
a = 1

if greeting == "Morning":
    print("Condition Matches for \"Morning\"!")
    print("Second Line")
elif greeting == "Good":
    print("Condition Matches for \"Good\"!")
elif greeting == "Good Morning":
    print("Condition Matches for \"Good Morning\"!")
else:
    print("Conditions do not match :(")

if a > 2:
    print("YOLOSWAG420")
else:
    print("LOSER")
#______________________________________________________________________________________________________________________
print()
# for loops

obj = [2, 3, 5, 7, 9]

for i in obj:
    # print(i) <-- This prints all in list
    print(i*2)

print()
summation1 = 0  # Basically using the sum as a counter or holder of the value we want
summation2 = 0
for j in range(0, 6):
    summation1 = summation1 + j
    summation2 += j  # This does the same as above, but cleaner
    # print(j) <-- This prints the whole list line by line, can be mutable

print()
print(summation1)  # print outside of the for loops
print(summation2)
print("***************")

for k in range(1, 10, 3):  # The third column tells the computer what iteration to go with
    print(k)

print("******** skipping first index *********")

for m in range(10):  # By default, python takes this value as the maximum, starts at 0 and ends with value-1
    print(m)

#______________________________________________________________________________________________________________________

