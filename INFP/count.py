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


INFP = ['Jean-Jacques Rousseau', 'Soeren Kierkegaard', 'Albert Camus', 'George Orwell', 'J.R.R. Tolkien', 'C.S. Lewis', 'Virginia Woolf', 'John Kerry', 'Antoine de Saint-Exupery', 'A. A. Milne', 'Bill Watterson', 'J.K. Rowling', 'Franz Kafka', 'Edgar Allan Poe', 'John Milton', 'William Blake', 'Augustine', 'Vincent van Gogh', 'Hans Christian Andersen', 'William Shakespeare', 'Homer', 'John Lennon', 'Jim Morrison', 'Kurt Cobain', 'Ian Curtis', 'Tim Burton', 'Johnny Depp', 'Heath Ledger', 'Nicolas Cage', 'Florence Welch', 'Bjork', 'Tori Amos', 'Fiona Apple', 'Jarvis Cocker', 'Thom Yorke', 'Morrissey', 'David Simon', 'David Lynch', 'Terrence Malick', 'Andy Warhol', 'Teller', 'Louis C.K.', 'Jude Law', 'Andrew Garfield', 'Robert Pattinson', 'Mia Wasikowska', 'Chloe Sevigny', 'Mary-Kate Olsen', 'John Mayer']
if __name__=="__main__":
	os.system("touch outputadj.txt")
	fio = open("outputadj.txt","w")
	serial = 1
	fio.write("S.No    Name                         Category                    WordCount\n")                                                    
	for files in INFP:
		filea = files.replace(' ','_')
		i = filea + "_adj.txt"
		if i!='output.txt' and i!='temp.py' and i!='count.py' and i!='searchadj.py' and i!='outputadj.txt' and i!='countbio.py':
			out = main(i)
			outstring = str(serial) + "    " + i
			j = 30 - len(i)
			for u in range(j):
				outstring = outstring + ' '
			
			outstring = outstring + "INFP" + "                    " + str(out)+"\n"
			fio.write(outstring)
			serial = serial + 1
	fio.close()
			

