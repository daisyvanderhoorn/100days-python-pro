"""Data types"""

integer = 1234
string = "1234"
float = 0.15
boolean = True

# print(type(integer))
# print(type(string))
# print(type(float))
# print(type(boolean))


"""Type casting"""
print("123" + "456")
# Outputs: 123456

addend = "23"
# <- converts string to integer ->
int(addend)

print(int(addend) + int(addend))


"""String conversion"""
name_of_user = input("Enter your name: ")
length_of_name = len(name_of_user)

print("Number of letters in your name: " + str(length_of_name))
