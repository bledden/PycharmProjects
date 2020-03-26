# Hello! This was made by Blake Ledden

values = [1, 2.69, "Blake", 4, 5]  # This is a list/array

# print(values[0])
# print(values[:0])
# print(values[:4])
# print(values[0:])
# print(values[4:])
# print(values[0:1])
# print(values[0:2])
# print(values[0:4])
# print(values[0::1])
# print(values[0::2])
# print(values[0::4])
# print(values[0::])
# print(values[::4])

print(values[3])
print(values[-1])
print(values[1:3])
values.insert(3, "shetty")
print(values)
# values.insert("blake") <-- This will not work because you MUST designate where you are inserting an obj in an array
values.append("blake")  # This works because .append places the object at the end of the array
(print(values))
values[2] = 'BOOBS'  # This is how we can replace a value; also you can do single quotes for strings as well
print(values)
del values[0]  # This deletes values at a designated location
print(values)
#_____________________________________________________________________________________________________________________

val = (1, 2, "buhlakay", 0.5)  # This is a tuple (round brackets)

print(val[2])
# val[0] = "new"  <-- This does not work because you cannot modify a tuple in Python
#______________________________________________________________________________________________________________________

dic = {"a": 0, 2: "abcd", "c": "hello world!", 4: 4}  # This is a dictionary with a key: value format

print(dic[2])
print(dic["a"])
print(dic["c"])

dict = {}
print(dict)
# Below is how to pass values to a dictionary
dict["firstname"] = "Blake"
print(dict["firstname"])
dict["lastname"] = "Ledden"
print(dict["lastname"])
print(dict)
