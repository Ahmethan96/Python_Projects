# file = open("ibrahim.txt")
# contents = file.read()
# print(contents)

# with open("ibrahim.txt") as file:
#     contents = file.read()
#     print(contents)
#
# with open("ibrahim.txt", mode= "w") as file:
#     file.write("Merhaba, ben ibrahim")


with open("ibrahim.txt", mode= "a") as file:
    file.write("\n Hi, this is ibrahim")
