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


INTJ = ['Isaac Newton', 'Karl Marx', 'Ayn Rand', 'Friedrich Nietzsche', 'Mark Zuckerberg', 'Elon Musk', 'Bobby Fischer', 'Nikola Tesla', 'Stephen Hawking', 'John Nash', 'John Maynard Keynes', 'Paul Krugman', 'John Adams', 'Isaac Asimov', 'Christopher Hitchens', 'H.L. Mencken', 'Martin Luther', 'G.W.F. Hegel', 'Heraclitus', 'Jean-Paul Sartre', 'James Cameron', 'Russell Crowe', 'Arnold Schwarzenegger', 'Jay-Z', 'Jodie Foster', 'Julia Stiles', 'Ashley Olsen', 'Roger Waters']
if __name__=="__main__":
	os.system("touch outputadj.txt")
	fio = open("outputadj.txt","w")
	serial = 1
	fio.write("S.No    Name                         Category                    WordCount\n")                                                    
	for files in INTJ:
		filea = files.replace(' ','_')
		i = filea + "_adj.txt"
		if i!='output.txt' and i!='temp.py' and i!='count.py' and i!='searchadj.py' and i!='outputadj.txt' and i!='countbio.py':
			out = main(i)
			outstring = str(serial) + "    " + i
			j = 30 - len(i)
			for u in range(j):
				outstring = outstring + ' '
			
			outstring = outstring + "INTJ" + "                    " + str(out)+"\n"
			fio.write(outstring)
			serial = serial + 1
	fio.close()
			

