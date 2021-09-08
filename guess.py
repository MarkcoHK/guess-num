import random 

r = random.randint(1, 100)
count = 0 
while True:
	count += 1 # count = count + 1 
	num = input('請猜數字： ') # input 都會把所有野存成字串
	num = int(num) # casting
	if num == r:
		print('終於猜對了！')
		print('這是你猜既第', count, '次')
		break
	elif num > r:
		print('太大拉')
	elif num < r:
		print('太細拉')
	print('這是你猜既第', count, '次')