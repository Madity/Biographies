import os
import re
templist = ['ESTJ', 'ESFJ', 'ESTP', 'ESFP', 'INTP', 'INTJ', 'INFP', 'INFJ', 'ISTJ', 'ISFJ', 'ISTP', 'ISFP']
#ENFJ
def main(e):
	os.chdir('/home/Madity/IIITH/Biographies/'+e)
	os.system('touch trainadj.txt')
	fio = open('trainadj.csv','w')
	fio1 = open('train.txt','r')
	lines = fio1.readlines()
	for line in lines:
		spl = line.split(' ')
		t = 1
		while spl[t] == '' or spl[t] == '\t':
			t = t + 1
		a = spl[t]
		os.chdir('/home/Madity/IIITH/Biographies/'+e+'/Adjectiveslist/')
		temp = open(a,'r')
		templine = temp.readlines()
		for t in templine:
			a = a + ','+t[:-1]
		fio.write(a+'\n')
		temp.close()
	fio1.close()
	fio.close()


if __name__=='__main__':
	for i in templist:
		main('ENFJ')
	
