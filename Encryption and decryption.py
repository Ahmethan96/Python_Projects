
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

lis = []
lis2 = []
lis3 = []


# print(f"this is original {lis}")
def encrypt(text, shift):
    for j in range(len(alphabet)):
        lis.append(alphabet[j])
    for i in range(shift):
        lis.append(lis.pop(0))
    # print(f"this is shifted  {lis}")

    for k in text:
        # print(k, end="")
        if k in alphabet:
            lis2.append(alphabet.index(k))
    # print(lis2)

    for g in lis2:
        f = lis[g]
        print(f"{f}", end="")


def decrypt(text, shift):
    for j in range(len(alphabet)):
        lis.append(alphabet[j])
    # print(alphabet)
    # print(lis)
    for i in range(shift):
        lis.append(lis.pop(0))

    for k in text:
        if k in lis:
            lis3.append(lis.index(k))
    print(lis3)
    print(lis)

    for b in lis3:
        x = alphabet[b]
        print(f"{x}", end="")


if direction == "encrypt":
    encrypt(text, shift)
elif direction == "decrypt":
    decrypt(text, shift)

#######################################################

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

alphabet_2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text,shift):
    # text = input("Type your message:\n").lower()
    ibo = []
    for j in range(len(text)):
        index = alphabet.index(text[j])
        ibo.append(index)
    print(ibo)

    for i in range(shift):
        num = 0
        x = alphabet.pop(num)
        alphabet.append(x)
    new = []
    for k in range(len(ibo)):
        g = alphabet[ibo[k]]
        new.append(g)
    print("".join(new))

print(encrypt(text, shift))

##############################################################

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
    ciper_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        ciper_text += new_letter
    print(ciper_text)

print(encrypt(text, shift))


##############################################################


ask = input("type your massage: ")
shift = int(input("how many shifts? "))
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
mylist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in range(shift):
    i = 0
    s = mylist.pop(i)
    mylist.append(s)

print(alphabet)
print(mylist)
index = []
for j in ask:
    if j in alphabet:
        d = alphabet.index(j)
        index.append(d)
print(index)

massage = []
for c in (index):
    massage.append(mylist[c])
    "".join(massage)

print("your encrypted massage is {}".format("".join(massage)))

