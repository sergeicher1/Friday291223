# string = "hello"
# number = int(string)
# print(number)

# string = input("Enter number: ")
# number = int(string)
# print(number)


# try:
#     instructions
# except:
#     instructions

# try:
#     string = input("Enter number: ")
#     result = int(string) + 5
#     print("The result: ", result)
# except ValueError as error_info:
#     print("The error is: ", error_info)
#
#
# finally:
#     print("The finally works anyway")


try:
    number1 = int(input("Enter number: "))
    number2 = int(input("Enter number: "))
    if number2 == 0:
        raise Exception("Second num should be more than 0")

except ValueError:
    print("The numbers incorrect")
    
except Exception as e:
    print("The error: ", e)
