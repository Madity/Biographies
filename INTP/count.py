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


INTP = ['Abraham Lincoln', 'Albert Einstein', 'Charles Darwin', 'Immanuel Kant', 'Hannah Arendt', 'Marie Curie', 'Richard Dawkins', 'John Locke', 'James Madison', 'Adam Smith', 'Friedrich A. Hayek', 'Milton Friedman', 'Thomas Aquinas', 'Rene Descartes', 'Parmenides', 'Thucydides', 'Jimmy Wales', 'Paul Allen', 'Larry Page', 'Sergey Brin', 'Jane Austen', 'Alan Greenspan', 'David Cronenberg', 'Jesse Eisenberg', 'Charlotte Gainsbourg', 'Sigourney Weaver', 'Tina Fey', 'Asia Carrera', 'Ben Stein', 'Andreas Scholl', 'Glenn Gould', 'Richard Ayoade', 'Randall Munroe']

if __name__=="__main__":
	os.system("touch outputadj.txt")
	fio = open("outputadj.txt","w")
	serial = 1
	fio.write("S.No    Name                         Category                    WordCount\n")                                                    
	for files in INTP:
		filea = files.replace(' ','_')
		i = filea + "_adj.txt"
		if i!='output.txt' and i!='temp.py' and i!='count.py' and i!='searchadj.py' and i!='outputadj.txt' and i!='countbio.py':
			out = main(i)
			outstring = str(serial) + "    " + i
			j = 30 - len(i)
			for u in range(j):
				outstring = outstring + ' '
			
			outstring = outstring + "INTP" + "                    " + str(out)+"\n"
			fio.write(outstring)
			serial = serial + 1
	fio.close()
			

