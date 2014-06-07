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


ISFJ = ['David Petraeus', 'George Marshall', 'Robert E. Lee', 'George A. Custer', 'Jimmy Carter', 'George H.W. Bush', 'Mitt Romney', 'Rosa Parks', 'Mother Teresa', 'Christopher Walken', 'Anthony Hopkins', 'Naomi Watts', 'Halle Berry', 'Dr. Dre', '50 Cent', 'Kanye West', 'Kim Kardashian', 'Tiger Woods', 'Lance Reddick', 'Kirsten Dunst', 'Jessica Simpson', 'Bruce Willis', 'Prince Charles', 'Kate Middleton', 'Princess Mary', 'Katie Holmes']

if __name__=="__main__":
	os.system("touch outputadj.txt")
	fio = open("outputadj.txt","w")
	serial = 1
	fio.write("S.No    Name                         Category                    WordCount\n")                                                    
	for files in ISFJ:
		filea = files.replace(' ','_')
		i = filea + "_adj.txt"
		if i!='output.txt' and i!='temp.py' and i!='count.py' and i!='searchadj.py' and i!='outputadj.txt' and i!='countbio.py':
			out = main(i)
			outstring = str(serial) + "    " + i
			j = 30 - len(i)
			for u in range(j):
				outstring = outstring + ' '
			
			outstring = outstring + "ISFJ" + "                    " + str(out)+"\n"
			fio.write(outstring)
			serial = serial + 1
	fio.close()
			

