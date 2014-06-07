import os


def main(e):
	fio = open(e,"r")
	lines = fio.readlines()  
	i =1
	for line in lines:
		if i is 1:
			i = i + 1
			print line
		else:
			txt = line.split('  ')
			num = txt[len(txt)-1]
			print int(num[:-1])
	fio.close()

if __name__=='__main__':
	main("outputadj.txt")
