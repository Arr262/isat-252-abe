#this is the multiplicaiton file in python
def multiply(a, b):
....if a < 0: return -multiply(-a, b)
....if a == 0: return 0
....return b + multiply(a - 1, b)
print(multiply(3, 1)) # ===> 3
print(multiply(3, -1)) # ===> -3
print(multiply(-3, 1)) # ===> -3
print(multiply(-3, -1)) # ===> 3