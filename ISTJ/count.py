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


ISTJ = ['Arthur Wellington', 'George Washington', 'Dwight D. Eisenhower', 'Augustus', 'Warren Buffett', 'Jeff Bezos', 'Ingvar Kamprad', 'Stonewall Jackson', 'Thomas Hobbes', 'Sigmund Freud', 'Martin Heidegger', 'Frederick the Great', 'Richard Nixon', 'Angela Merkel', 'Joseph Ratzinger', 'Ayaan Hirsi Ali', 'Xenophon', 'Robert De Niro', 'Sean Connery', 'Christopher Lee', 'Elizabeth II', 'Natalie Portman', 'Rivers Cuomo', 'Jamie Hyneman', 'Nick Offerman', 'Danica McKellar']

if __name__=="__main__":
	os.system("touch outputadj.txt")
	fio = open("outputadj.txt","w")
	serial = 1
	fio.write("S.No    Name                         Category                    WordCount\n")                                                    
	for files in ISTJ:
		filea = files.replace(' ','_')
		i = filea + "_adj.txt"
		if i!='output.txt' and i!='temp.py' and i!='count.py' and i!='searchadj.py' and i!='outputadj.txt' and i!='countbio.py':
			out = main(i)
			outstring = str(serial) + "    " + i
			j = 30 - len(i)
			for u in range(j):
				outstring = outstring + ' '
			
			outstring = outstring + "ISTJ" + "                    " + str(out)+"\n"
			fio.write(outstring)
			serial = serial + 1
	fio.close()
			

