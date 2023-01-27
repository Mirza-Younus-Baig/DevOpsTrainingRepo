import random
from Operations import *

a = random.randint(5, 10)
c = random.randint(5, 10)

# Multiplication of two random numbers
res1 = multiply(a, c)
print("Multiplication Output: ", res1)

print("Test Run for merge conflicts generations")

res3 = add(a,c)
print("Add Output: ", res3)

res5 = subtract(a,c)
print("Subtract Output: ", res5)

res4 = exponent(a,c)
print("Exponent Output: ", res4)


res2 = divide(a,c)
print("Divide Output: ", res2)

# # Create a list of random numbers of size res1
# res2 = [random.randint(1, 10) for i in range(res1)]

# res2 = random.sample(res2, res1-20)
# print(res2)

# print(Test)