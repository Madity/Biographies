import os

INTP = ['Abraham Lincoln', 'Albert Einstein', 'Charles Darwin', 'Immanuel Kant', 'Hannah Arendt', 'Marie Curie', 'Richard Dawkins', 'John Locke', 'James Madison', 'Adam Smith', 'Friedrich A. Hayek', 'Milton Friedman', 'Thomas Aquinas', 'Rene Descartes', 'Parmenides', 'Thucydides', 'Jimmy Wales', 'Paul Allen', 'Larry Page', 'Sergey Brin', 'Jane Austen', 'Alan Greenspan', 'David Cronenberg', 'Jesse Eisenberg', 'Charlotte Gainsbourg', 'Sigourney Weaver', 'Tina Fey', 'Asia Carrera', 'Ben Stein', 'Andreas Scholl', 'Glenn Gould', 'Richard Ayoade', 'Randall Munroe']

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
	os.system("mv -f "+filename+ " " + e + ".txt")
	

if __name__=="__main__":
	for h in INTP:
		main(h)
