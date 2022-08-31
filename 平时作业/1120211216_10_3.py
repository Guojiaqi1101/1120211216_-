path1="score.txt"
f1=open(path1,"r",encoding='utf-8')
num=0
table={}
#sum_class1_grade2
nopass_grade2=0
nopass_grade3=0
for line1 in f1.readlines():
	newline1=line1.rstrip()
	newwords1=newline1.split(" ")
	table[num]=newwords1
	num+=1
len=len(table)
i=1
while i<len:
	score=table[i]
	if int(score[2])<60 | int(score[1])<60:
		if int(score[3])==2:
			nopass_grade2 +=1
		else:
			nopass_grade3 +=1
	i=i+1
print("2年级不及格人数：{}".format(nopass_grade2))
print("3年级不及格人数：{}".format(nopass_grade3))