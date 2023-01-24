import random
from Operations import *

a = random.randint(5, 10)
b = random.randint(5, 10)

# Multiplication of two random numbers
res1 = multiply(a, b)
print("Multiplication Output: ", res1)

res2 = divide(a,b)
print("Divide Output: ", res2)




# # Create a list of random numbers of size res1
# res2 = [random.randint(1, 10) for i in range(res1)]

# res2 = random.sample(res2, res1-20)
# print(res2)

# print(res2[0:10])