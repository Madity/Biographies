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


ENFJ = ['Martin Luther King, Jr.', 'Nelson Mandela', 'John Paul II', 'Johann von Goethe', 'Sheryl Sandberg', 'Pericles', 'Cicero', 'Erasmus of Rotterdam', 'Mikhail Gorbachev', 'Vaclav Havel', 'Joe Biden', 'Tony Blair', 'Matthieu Ricard', 'Daniel Goleman', 'Alfred Adler', 'Erich Fromm', 'Neil deGrasse Tyson', 'Michael Moore', 'Oprah Winfrey', 'Charlie Rose', 'Morgan Freeman', 'Bono', 'Reese Witherspoon', 'Kate Winslet', 'Helena Bonham Carter', 'Nigella Lawson', 'Jennifer Lawrence', 'Dakota Fanning', 'Emma Stone', 'AnnaSophia Robb', 'Zack de la Rocha', 'James Lipton', 'Dr. Drew']


if __name__=="__main__":
	os.system("touch outputadj.txt")
	fio = open("outputadj.txt","w")
	serial = 1
	fio.write("S.No    Name                         Category                    WordCount\n")                                                    
	for files in ENFJ:
		filea = files.replace(' ','_')
		i = filea + "_adj.txt"
		if i!='output.txt' and i!='temp.py' and i!='count.py' and i!='searchadj.py' and i!='outputadj.txt' and i!='countbio.py':
			out = main(i)
			outstring = str(serial) + "    " + i
			j = 30 - len(i)
			for u in range(j):
				outstring = outstring + ' '
			
			outstring = outstring + "ENFJ" + "                    " + str(out)+"\n"
			fio.write(outstring)
			serial = serial + 1
	fio.close()
			

