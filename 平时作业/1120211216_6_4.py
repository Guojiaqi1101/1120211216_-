water=float(input("输入一年用水量（立方米）："))
if water>0 and water<=220:
	price=water*3.45
	print("总水费为{:.2f}元".format(price))
elif water>220 and water<=300:
	price=water*4.83
	print("总水费为{:.2f}元".format(price))
else:
	price=water*5.83
	print("总水费为{:.2f}元".format(price))