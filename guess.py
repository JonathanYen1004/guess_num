import random
start = input('please choose random number start value: ')
end = input('please choose random number end value:  ')
start = int(start)
end = int(end)
r = random.randint(start, end)
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
