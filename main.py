from funcs import factorial


res = factorial(0)
assert(res == 1)
res = factorial(1)
assert(res == 1)
res = factorial(5)
assert(res == 120)
res = factorial(9)
assert(res == 362880)
print("Success!")

