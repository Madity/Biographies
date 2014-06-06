import os

ENFJ = ['Martin Luther King, Jr.', 'Nelson Mandela', 'John Paul II', 'Johann von Goethe', 'Sheryl Sandberg', 'Pericles', 'Cicero', 'Erasmus of Rotterdam', 'Mikhail Gorbachev', 'Vaclav Havel', 'Joe Biden', 'Tony Blair', 'Matthieu Ricard', 'Daniel Goleman', 'Alfred Adler', 'Erich Fromm', 'Neil deGrasse Tyson', 'Michael Moore', 'Oprah Winfrey', 'Charlie Rose', 'Morgan Freeman', 'Bono', 'Reese Witherspoon', 'Kate Winslet', 'Helena Bonham Carter', 'Nigella Lawson', 'Jennifer Lawrence', 'Dakota Fanning', 'Emma Stone', 'AnnaSophia Robb', 'Zack de la Rocha', 'James Lipton', 'Dr. Drew']
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
	for h in ENFJ:
		main(h)
