import os

ISTJ = ['Arthur Wellington', 'George Washington', 'Dwight D. Eisenhower', 'Augustus', 'Warren Buffett', 'Jeff Bezos', 'Ingvar Kamprad', 'Stonewall Jackson', 'Thomas Hobbes', 'Sigmund Freud', 'Martin Heidegger', 'Frederick the Great', 'Richard Nixon', 'Angela Merkel', 'Joseph Ratzinger', 'Ayaan Hirsi Ali', 'Xenophon', 'Robert De Niro', 'Sean Connery', 'Christopher Lee', 'Elizabeth II', 'Natalie Portman', 'Rivers Cuomo', 'Jamie Hyneman', 'Nick Offerman', 'Danica McKellar']

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
	for h in ISTJ:
		main(h)
