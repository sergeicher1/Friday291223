tom = ("Tom", 23)
# print(tom)
bob = "bob", 25
# print(bob)
# print(bob[0])


def GetUser():
    name = "Tom"
    age = 22
    company = "Google"
    return name, age, company


#
# user = GetUser()
# print(type(user))
# print(user)

# for j in tom:
#     print(j)
#
# i = 0
# while i < len(bob):
#     print(bob[i])
#     i += 1

if "bob" in bob:
    print(True)