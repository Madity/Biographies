import os

ISFP = ['Jacqueline Kennedy Onassis', 'Ulysses S. Grant', 'Jonathan Ive', 'Joern Utzon', 'Thich Nhat Hanh', 'Nero', 'Leni Riefenstahl', 'Brad Pitt', 'Justin Timberlake', 'David Beckham', 'Ryan Gosling', 'Audrey Hepburn', 'Elizabeth Taylor', 'Nicole Kidman', 'Sofia Coppola', 'Michael Jackson', 'Prince', 'Bob Dylan', 'Paul McCartney', 'David Bowie', 'Lady Gaga', 'Eminem', 'Frank Ocean', 'Princess Diana', 'Marilyn Monroe', 'Britney Spears', 'Paris Hilton', 'Rihanna', 'Christina Aguilera', 'Monica Bellucci', 'Dita von Teese', 'Mick Jagger', 'Keith Richards', 'Jimi Hendrix', 'Andrew Bird', 'David Gilmour', 'Kate Bush', 'Trent Reznor', 'Skrillex', 'Drew Barrymore', 'Leona Lewis', 'John Travolta', 'Zac Efron', 'Liv Tyler', 'Pamela Anderson', 'Prince Harry', 'Prince Frederik', 'Enya']

def main(e):
	e = e.replace(' ','_')
	filename = e+"1.txt"
	os.system("touch "+filename)
	fio = open(e+".txt","r")
	fio1 = open(filename,"w")
	lines = fio.readlines()
	for line in lines:
		if line[0] == '^':
			pass
		elif line[0] == '#' or line[0] == '}':
			pass
		else:
			fio1.write(line)
	#	print line
	#	print "<<<<<<<<<>>>>>>>>>>>>>>>"
	fio.close()
	fio1.close()
	os.system("rm -rf "+e+".txt")
	os.system("mv "+filename+ " " + e + ".txt")
	

if __name__=="__main__":
	for h in ISFP:
		main(h)
