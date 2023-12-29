# dictionary = {key:value}
# users = {1: "Tom", 2: "Bob", 3: "Bill", "email": "bob@gmail.com"}
# objects = {}
# objects1 = dict()

# users_list = [["5555", "bob"], ["777", "tom"]]
# users_dict = dict(users_list)
# print(users_list)
# print(users_dict)
# print(users[1])
# print(users["email"])
# print(users.keys())
# print(users.values())
# key = "email"
# if key in users:
#     print("yes")
# users = {2: "Bob", 3: "Bill", "email": "bob@gmail.com"}
# # user = users.get("emails", "The post is not")
# # print(user)
# # get(key, default):
# # user2 = users.setdefault("email", "555")
# # print(user2)
# if 1 in users:
#     del users[1]
#
# print(users)
# users1 = {1: "Tom", 2: "Bob", 3: "Bill"}
# # users2 = {4: "Bom", 5: "Bob", 6: "Bill"}
# # users1.update(users2)
# users2 = users1
# # print(users1)
#
# users1[1] = "Sam"
# print(users2)
#
users = {
    "Tom": {
        "phone": "+971478745",
        "email": "tom12@gmail.com"
    },
    "Bob": {
        "phone": "+876390444",
        "email": "bob@gmail.com",
        "skype": "bob123"
    }
}
print(users["Bob"]["skype"])
print(users["Tom"].values())