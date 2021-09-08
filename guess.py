import random 
start = input('請決定隨機數字範圍開始值： ')
end = input('請決定隨機數字範圍結束值: ')
start = int(start)
end = int(end)

r = random.randint(start, end)
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