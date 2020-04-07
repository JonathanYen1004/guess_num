import random
r = random.randint(1, 100)
count = 0
while True:
	count += 1 #count = count + 1
	num = input('guess: ')
	num = int(num)
	if num == r:
		print('correct')
		print('you guess ', count, ' times')
		break
	elif num < r:
		print('bigger')
	elif num > r:
		print('smaller')
	print('you guess ', count, ' times')
