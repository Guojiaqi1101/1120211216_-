num=int(input("输入一个五位整数："))
single=num%10
thousand=num//1000%10
print("%d的个位数是%d："%(num,single))
print("%d的千位数是%d："%(num,thousand))