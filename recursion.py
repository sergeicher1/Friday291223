# def function():
#     function()
#

def FactorialRecursion(n):
    result = 0
    print("The n: ", n)
    if n == 1:
        return n

    else:
        result = result * n
        print(result)
        return n * FactorialRecursion(n - 1)



FactorialRecursion(10)
