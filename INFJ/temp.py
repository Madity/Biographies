import os

INFJ = ['Plato', 'Carl Gustav Jung', 'Niels Bohr', 'Mahatma Gandhi', 'Thomas Jefferson', 'Calvin Coolidge', 'Woodrow Wilson', 'Noam Chomsky', 'Simone de Beauvoir', 'Mary Wollstonecraft', 'Ludwig Wittgenstein', 'Sam Harris', 'Marcus Aurelius', 'Dante Alighieri', 'Fyodor Dostoevsky', 'Alexander Solzhenitsyn', 'Baruch Spinoza', 'Arthur Schopenhauer', 'Lars von Trier', 'David Fincher', 'Leonard Cohen', 'Marilyn Manson', 'Al Pacino', 'Daniel Day-Lewis', 'Edward Norton', 'Adrien Brody', 'Cate Blanchett', 'Michelle Pfeiffer', 'Rooney Mara', 'Carey Mulligan', 'Josh Radnor', 'Derren Brown', 'Mystery', 'Tilda Swinton', 'Sufjan Stevens', 'George Harrison']

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
	for h in INFJ:
		main(h)
