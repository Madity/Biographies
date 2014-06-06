import os

INFP = ['Jean-Jacques Rousseau', 'Soeren Kierkegaard', 'Albert Camus', 'George Orwell', 'J.R.R. Tolkien', 'C.S. Lewis', 'Virginia Woolf', 'John Kerry', 'Antoine de Saint-Exupery', 'A. A. Milne', 'Bill Watterson', 'J.K. Rowling', 'Franz Kafka', 'Edgar Allan Poe', 'John Milton', 'William Blake', 'Augustine', 'Vincent van Gogh', 'Hans Christian Andersen', 'William Shakespeare', 'Homer', 'John Lennon', 'Jim Morrison', 'Kurt Cobain', 'Ian Curtis', 'Tim Burton', 'Johnny Depp', 'Heath Ledger', 'Nicolas Cage', 'Florence Welch', 'Bjork', 'Tori Amos', 'Fiona Apple', 'Jarvis Cocker', 'Thom Yorke', 'Morrissey', 'David Simon', 'David Lynch', 'Terrence Malick', 'Andy Warhol', 'Teller', 'Louis C.K.', 'Jude Law', 'Andrew Garfield', 'Robert Pattinson', 'Mia Wasikowska', 'Chloe Sevigny', 'Mary-Kate Olsen', 'John Mayer']

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
	for h in INFP:
		main(h)
