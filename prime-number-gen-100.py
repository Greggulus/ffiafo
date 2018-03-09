# Print Primesnumbers up to 'n'
def prime(n):
	for y in range(2, n):
		for x in range(2, y):
			if y % x == 0:
				break
		else:
			print(y, end=' ')

prime(100)
