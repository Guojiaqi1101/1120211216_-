path1="score.txt"
f1=open(path1,"r",encoding='utf-8')
num=0
table={}
#sum_class1_grade2
sum_grade2=0
sum_grade3=0
count_grade2=0
count_grade3=0
for line1 in f1.readlines():
	newline1=line1.rstrip()
	newwords1=newline1.split(" ")
	table[num]=newwords1
	num+=1
len=len(table)
i=1
while i<len:
	score=table[i]
	if int(score[3])==2:
		sum_grade2=sum_grade2+int(score[1])+int(score[2])
		count_grade2=count_grade2+1
	else:
		sum_grade3=sum_grade3+int(score[1])+int(score[2])
		count_grade3=count_grade3+1
	i=i+1
aver_grade2=sum_grade2/count_grade2
aver_grade3=sum_grade3/count_grade3
print("2年级的平均分：{:.2f}".format(aver_grade2))
print("3年级的平均分：{:.2f}".format(aver_grade3))