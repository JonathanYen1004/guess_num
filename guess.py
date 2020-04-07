import random
r = random.randint(1, 100)
while True:
	num = input('guess: ')
	num = int(num)
	if num == r:
		print('correct')
		break
	elif num < r:
		print('bigger')
	elif num > r:
		print('smaller')
