import os
def main(s):
	fio = open(s,"r")
	lines = fio.readlines()
	number = 0
	for line in lines:
		if line[0] == '=':
			pass
		else:
			line = line.split(' ')
			number = number + len(line)
	return number

if __name__=="__main__":
	os.system("touch output.txt")
	fio = open("output.txt","a")
	serial = 179
	for subdirs, dirs, files in os.walk('.'):
		for i in files:
			if i!='output.txt' and i!='temp.py' and i!='count.py':
				out = main(i)
				outstring = str(serial) + "    " + i
				j = 30 - len(i)
				for u in range(j):
					outstring = outstring + ' '
				
				outstring = outstring + "ESFJ" + "                    " + str(out)+"\n"
				fio.write(outstring)
				serial = serial + 1

		fio.close()
			

