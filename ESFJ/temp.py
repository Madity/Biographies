import os


ESFJ = ['Harry S. Truman', 'Gerald Ford', 'Colin Powell', 'Desmond Tutu', 'Andrew Carnegie', 'Sam Walton', 'Andy Rooney', 'Francis', 'Sarah Palin', 'Rick Santorum', 'John Boehner', 'Larry King', 'Regis Philbin', 'Barbara Walters', 'Chris Wallace', 'Alyson Hannigan', 'Jason Segel', 'Anne Hathaway', 'Penelope Cruz', 'Selena Gomez', 'Jessica Alba', 'Jennifer Garner', 'Sarah Jessica Parker', 'Whitney Houston', 'Mariah Carey', 'Alicia Keys', 'Shania Twain', 'Prince William', 'Lesley Stahl', 'Elton John', 'Randy Jackson', 'Hugh Jackman', 'Jamie Bell', 'Vin Diesel', 'Woody Harrelson', 'Tyra Banks', 'Jenny McCarthy', 'Laura Harring', 'Victoria Beckham', 'Adam Young', 'Vanessa Hudgens']


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
	for h in ESFJ:
		main(h)
