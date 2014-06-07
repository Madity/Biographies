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


ENFP = ['Hunter S. Thompson', 'Mark Twain', 'Oscar Wilde', 'Aldous Huxley', 'Umberto Eco', 'Salman Rushdie', 'Julian Assange', 'Ralph Nader', 'Anne Frank', 'Arianna Huffington', 'Walt Disney', 'Kurt Vonnegut', 'Osho', 'Naomi Klein', 'Michio Kaku', 'Brian Cox', 'Joseph Campbell', 'Alan Watts', 'Jacques Derrida', 'Anais Nin', 'Ellen DeGeneres', 'Katie Couric', 'Rachel Maddow', 'Keira Knightley', 'Orson Welles', 'George Carlin', 'Oliver Stone', 'Jack White', 'Robin Williams', 'Jerry Seinfeld', 'Gwen Stefani', 'Jennifer Aniston', 'Sandra Bullock', 'Jenna Elfman', 'Alicia Silverstone', 'Sarah Michelle Gellar', 'Daniel Radcliffe', 'James Mercer', 'Carly Rae Jepsen', 'Philippe Jaroussky', 'Sharon Stone']


if __name__=="__main__":
	os.system("touch outputadj.txt")
	fio = open("outputadj.txt","w")
	serial = 1
	fio.write("S.No    Name                         Category                    WordCount\n")                                                    
	for files in ENFP:
		filea = files.replace(' ','_')
		i = filea + "_adj.txt"
		if i!='output.txt' and i!='temp.py' and i!='count.py' and i!='searchadj.py' and i!='outputadj.txt' and i!='countbio.py':
			out = main(i)
			outstring = str(serial) + "    " + i
			j = 30 - len(i)
			for u in range(j):
				outstring = outstring + ' '
			
			outstring = outstring + "ENFP" + "                    " + str(out)+"\n"
			fio.write(outstring)
			serial = serial + 1
	fio.close()
			

