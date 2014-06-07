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


ENTP = ['Socrates', 'Leonardo da Vinci', 'Benjamin Franklin', 'Richard Feynman', 'Voltaire', 'Catherine the Great', 'Niccolo Machiavelli', 'David Hume', 'Steve Wozniak', 'Werner Heisenberg', 'Karl Popper', 'Bertrand Russell', 'John Stuart Mill', 'Edmund Burke', 'Newt Gingrich', 'Barack Obama', 'Murray Rothbard', 'Henry Kissinger', 'Jon Stewart', 'Stephen Colbert', 'Bill Maher', 'Sacha Baron Cohen', 'Terry Gilliam', 'John Cleese', 'Robert Downey Jr.', 'Rowan Atkinson', 'Federico Fellini', 'Karl Lagerfeld', 'Stephen Fry', 'Bill Hicks', 'Neil Patrick Harris', 'David Hyde Pierce', 'Matthew Perry', 'Megan Mullally', 'Gillian Anderson', 'Elizabeth Olsen', 'Salma Hayek', 'Rose McGowan', 'Adam Savage', 'Jeremy Clarkson', 'Hugh Grant', 'Celine Dion', 'Siouxsie Sioux', 'Kevin Barnes', 'Cedric Bixler-Zavala', 'Diablo Cody', 'Maddox', 'Matthew Inman']


if __name__=="__main__":
	os.system("touch outputadj.txt")
	fio = open("outputadj.txt","a")
	serial = 1
	fio.write("S.No    Name                         Category                    WordCount\n")                                                    
	for files in ENTP:
		filea = files.replace(' ','_')
		i = filea + "_adj.txt"
		if i!='output.txt' and i!='temp.py' and i!='count.py' and i!='searchadj.py' and i!='outputall.txt':
			out = main(i)
			outstring = str(serial) + "    " + i
			j = 30 - len(i)
			for u in range(j):
				outstring = outstring + ' '
			
			outstring = outstring + "ENTP" + "                    " + str(out)+"\n"
			fio.write(outstring)
			serial = serial + 1
	fio.close()
			

