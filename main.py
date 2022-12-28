def factorial(n: int):
	if n == 0 or n == 1:
		return 1
	return n * factorial(n - 1)


# Делаем специальную синтаксическую ошибку
print("Hello world!
res = factorial(0)
assert(res == 1)
res = factorial(1)
assert(res == 1)
res = factorial(5)
assert(res == 120)
res = factorial(9)
assert(res == 362880)
print("Success!")

