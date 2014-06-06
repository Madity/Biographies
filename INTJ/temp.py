import os

INTJ = ['Isaac Newton', 'Karl Marx', 'Ayn Rand', 'Friedrich Nietzsche', 'Mark Zuckerberg', 'Elon Musk', 'Bobby Fischer', 'Nikola Tesla', 'Stephen Hawking', 'John Nash', 'John Maynard Keynes', 'Paul Krugman', 'John Adams', 'Isaac Asimov', 'Christopher Hitchens', 'H.L. Mencken', 'Martin Luther', 'G.W.F. Hegel', 'Heraclitus', 'Jean-Paul Sartre', 'James Cameron', 'Russell Crowe', 'Arnold Schwarzenegger', 'Jay-Z', 'Jodie Foster', 'Julia Stiles', 'Ashley Olsen', 'Roger Waters']


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
	for h in INTJ:
		main(h)
