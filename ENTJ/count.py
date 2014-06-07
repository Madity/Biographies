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


ENTJ = ['Napoleon Bonaparte', 'Julius Caesar', 'Margaret Thatcher', 'Aristotle', 'Alexander Hamilton', 'Garry Kasparov', 'Bill Gates', 'Carl Sagan', 'Karl Rove', 'Dick Cheney', 'Rahm Emanuel', 'Al Gore', 'Madeleine Albright', 'Nancy Pelosi', 'Aung San Suu Kyi', 'Peter Thiel', 'Rush Limbaugh', 'Jack Welch', 'David Letterman', 'George Clooney', 'Matt Damon', 'Penn Jillette', 'Charlize Theron', 'Katharine Hepburn', 'Tea Leoni', 'Adele', 'Cobie Smulders']

if __name__=="__main__":
	os.system("touch outputadj.txt")
	fio = open("outputadj.txt","w")
	serial = 1
	fio.write("S.No    Name                         Category                    WordCount\n")                                                    
	for files in ENTJ:
		filea = files.replace(' ','_')
		i = filea + "_adj.txt"
		if i!='output.txt' and i!='temp.py' and i!='count.py' and i!='searchadj.py' and i!='outputadj.txt' and i!='countbio.py':
			out = main(i)
			outstring = str(serial) + "    " + i
			j = 30 - len(i)
			for u in range(j):
				outstring = outstring + ' '
			
			outstring = outstring + "ENTJ" + "                    " + str(out)+"\n"
			fio.write(outstring)
			serial = serial + 1
	fio.close()
			

