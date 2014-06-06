import os

ENFP = ['Hunter S. Thompson', 'Mark Twain', 'Oscar Wilde', 'Aldous Huxley', 'Umberto Eco', 'Salman Rushdie', 'Julian Assange', 'Ralph Nader', 'Anne Frank', 'Arianna Huffington', 'Walt Disney', 'Kurt Vonnegut', 'Osho', 'Naomi Klein', 'Michio Kaku', 'Brian Cox', 'Joseph Campbell', 'Alan Watts', 'Jacques Derrida', 'Anais Nin', 'Ellen DeGeneres', 'Katie Couric', 'Rachel Maddow', 'Keira Knightley', 'Orson Welles', 'George Carlin', 'Oliver Stone', 'Jack White', 'Robin Williams', 'Jerry Seinfeld', 'Gwen Stefani', 'Jennifer Aniston', 'Sandra Bullock', 'Jenna Elfman', 'Alicia Silverstone', 'Sarah Michelle Gellar', 'Daniel Radcliffe', 'James Mercer', 'Carly Rae Jepsen', 'Philippe Jaroussky', 'Sharon Stone']

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
	for h in ENFP:
		main(h)
