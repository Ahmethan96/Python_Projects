name1 = input("what is your name? \n")
name2 = input("what is their name? \n")

x = name1.lower()
y = name2.lower()

first = "true"
second = "love"

true = 0
love = 0

ibo = [s for s in first if x.count(s) > 0]
print(ibo)

for i in first:
    # print(i)
    true += x.count(i)
    true += y.count(i)

for j in second:
    # print(j)
    love += x.count(j)
    love += y.count(j)

print(true)
print(love)

print("your score love in {}{}".format(true,love))

z = str(true)
d = str(love)
w = z + d
print(type(w))
print(w)
c = int(w)

if c < 10 and c > 90:
    print("your score is {}, you go together like coke and mentos.".format(c))
elif c >= 40 and c <= 50:
    print("your score is {}, you are alright together.".format(c))
else:
    print("your score is {}".format(c))



func2 = lambda x: x + 5
