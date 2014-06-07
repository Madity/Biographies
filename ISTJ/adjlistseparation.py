import os


def main(e):
	fio = open(e,"r")
	os.system("touch train.txt")	
	os.system("touch test.txt")
	fio1 = open("train.txt","w")
	fio2 = open("test.txt","w")
	lines = fio.readlines()
	con = {}
	sortlist = []
	count = 0
	for line in lines:
		count = count + 1
		content = line.split(' ')
		if int(content[len(content)-1][:-1]) in sortlist:
			con[int(content[len(content)-1][:-1])].append(line)
		else:	
			sortlist.append(int(content[len(content)-1][:-1]))
			con[int(content[len(content)-1][:-1])] = []
			con[int(content[len(content)-1][:-1])].append(line)
		

	sortlist.sort()
	le = len(sortlist)
	check = count/2
	print check
	t = le-1
	num = 1
	count1 = 0
	while t >= 0:
		temp = con[sortlist[t]]
		for i in temp:
			cont = str(num) + i[2:]
			if count1<check:
				fio1.write(cont)	
				count1 = count1 + 1
			else:
				fio2.write(cont)
			num = num + 1
		t = t - 1
	fio.close()
	fio1.close()
	fio2.close()

if __name__=='__main__':
	main("outputadj.txt")
		
