import os
import sys

extra = {}
extra1 = {}
s = 'Id,Agreeableness'
num = 1
num1 = 1
fio1 = open('Agreeableness.csv','w')
fio2 = open('Agreeablenesslist.txt','w')
def main():
	global s
	global fio1
	fio = open('Adjective_list.csv','r')
	lines = fio.readlines()
	t = 1
	for line in lines:
		if t == 1:
			t = t + 1
			pass
		else:	
			temp = line.split(',') 
			extra[temp[0].upper()] = temp[1]
	fio.close()
	for i in extra.keys():
		s = s + ',' + i
	fio1.write(s+'\n')
#	print extra

def saving(e):
	global fio1
	global fio2
	global extra 
	global extra1
	global num
	global num1
	os.chdir('/home/Madity/IIITH/Biographies/'+e)
	fio = open('trainadj.csv','r')
	lines = fio.readlines()
	for line in lines:
		for i in extra.keys():
			extra1[i] = '0'
		temp = line.split(',')
		t = 1
		if e == 'INTP' or e == 'INTJ' or e == 'ISTJ' or e == 'ISTP' or e == 'ENTP' or e == 'ENTJ' or e == 'ESTJ' or e == 'ESTP':
			st = str(num1)+','+ '0'
		else:
			st = str(num1) + ',' +'1'
		num1 = num1 + 1
		for i in temp:
			if t == 1:
				fio2.write(str(num) + '    '+ i + '    ' + e +'\n')
				t = t + 1
				num = num + 1
				pass
			else:
				try:
					if i[-1] == '\n':
						extra1[i[:-1].upper()] = extra[i[:-1].upper()]
					else:
						extra1[i.upper()] = extra[i.upper()]
				except Exception,f:
					print e
					print f
		for i in extra1.keys():
			st = st + ',' + extra1[i]
		fio1.write(st+'\n')
			

templist = ['ENTP', 'ENTJ', 'ENFP', 'ENFJ', 'ESTJ', 'ESFJ', 'ESTP', 'ESFP', 'INTP', 'INTJ', 'INFP', 'INFJ', 'ISTJ', 'ISFJ', 'ISTP', 'ISFP']
if __name__=='__main__':
	main()
	for i in templist:
		saving(i)
	fio1.close()
	fio2.close()
