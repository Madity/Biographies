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


ISFP = ['Jacqueline Kennedy Onassis', 'Ulysses S. Grant', 'Jonathan Ive', 'Joern Utzon', 'Thich Nhat Hanh', 'Nero', 'Leni Riefenstahl', 'Brad Pitt', 'Justin Timberlake', 'David Beckham', 'Ryan Gosling', 'Audrey Hepburn', 'Elizabeth Taylor', 'Nicole Kidman', 'Sofia Coppola', 'Michael Jackson', 'Prince', 'Bob Dylan', 'Paul McCartney', 'David Bowie', 'Lady Gaga', 'Eminem', 'Frank Ocean', 'Princess Diana', 'Marilyn Monroe', 'Britney Spears', 'Paris Hilton', 'Rihanna', 'Christina Aguilera', 'Monica Bellucci', 'Dita von Teese', 'Mick Jagger', 'Keith Richards', 'Jimi Hendrix', 'Andrew Bird', 'David Gilmour', 'Kate Bush', 'Trent Reznor', 'Skrillex', 'Drew Barrymore', 'Leona Lewis', 'John Travolta', 'Zac Efron', 'Liv Tyler', 'Pamela Anderson', 'Prince Harry', 'Prince Frederik', 'Enya']
if __name__=="__main__":
	os.system("touch outputadj.txt")
	fio = open("outputadj.txt","w")
	serial = 1
	fio.write("S.No    Name                         Category                    WordCount\n")                                                    
	for files in ISFP:
		filea = files.replace(' ','_')
		i = filea + "_adj.txt"
		if i!='output.txt' and i!='temp.py' and i!='count.py' and i!='searchadj.py' and i!='outputadj.txt' and i!='countbio.py':
			out = main(i)
			outstring = str(serial) + "    " + i
			j = 30 - len(i)
			for u in range(j):
				outstring = outstring + ' '
			
			outstring = outstring + "ISFP" + "                    " + str(out)+"\n"
			fio.write(outstring)
			serial = serial + 1
	fio.close()
			

