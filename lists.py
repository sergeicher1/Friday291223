# create list

# numbers = [1, 2, 3, 4, 5]
# strs = ["Tom", "Bob"]
#
# # constructor
# number1 = [] # one way
# numbers2 = list() # other way


# objects = [1, 2.6, "hello", True]
# print(objects)

# create list with the same values
# numbers = [5] * 6
# print(numbers)

# names = ["Tom"]*6
# print(names)


# words = ["one", "two", "three"]
# print(words[0])
# print(words[1])
# print(words[2])

# words[0] = "Zero"
# print(words[0])
# one = words[0]
# one_value1 = words[0]
# two_value1 = words[0]

# print(one)
# mishtane1, mishtane2, three = words
# print(mishtane1)
# print(mishtane2)

# words = ["one", "two", "three"]
# # for word in words:
# #     print(word)
#
# i = 0
# while i < len(words):
#     print(words[i])
#     i += 1

# words = ["one", "two", "three"]
# words2 = ["one", "two", "three"]
# if words == words2:
#     print("The lists are equal")
# else:
#     print("The lists aren't equal")


# list[:end]
# list[start:end]
# list[start:end:step]

# print(words[::])
# words.reverse()
# words_rev = words[::-1]
# print(words)
# print(words_rev)
# words2 = reversed(words)
# print(words2)

# print(sorted(words))

# words = ["one", "two", "three", "four", "five", "six"]
# words.append("seven")
# print(words)
# words.insert(1,"one and a half")
# print(words)
# words.extend(["zero", "ten",10])
# print(words)

# index_of_four = words.index("four")
# print(words.index("four"))
# print(words[3])

# if "four" in words:
#     print("yes")
#     words.remove("four")
# print(words)
words = ["one", "two", "three", "four", "five", "six"]
# del words[3]
# print(words)

words.clear()

print(words)