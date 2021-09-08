import random 

r = random.randint(1, 100)
while True:
	num = input('請猜數字： ') # input 都會把所有野存成字串
	num = int(num) # casting
	if num == r:
		print('終於猜對了！')
		break
	elif num > r:
		print('太大拉')
	elif num < r:
		print('太細拉')