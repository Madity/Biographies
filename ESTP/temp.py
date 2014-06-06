import os

ESTP = ['Alexander the Great', 'Winston Churchill', 'Theodore Roosevelt', 'George S. Patton', 'Andrew Jackson', 'Franklin D. Roosevelt', 'Malcolm X', 'Douglas MacArthur', 'Donald Trump', 'Peter Schiff', 'James Randi', 'Ernest Hemingway', 'Epicurus', 'Stephen R. Covey', 'Dale Carnegie', 'L. Ron Hubbard', 'George W. Bush', 'Lyndon B. Johnson', 'David Cameron', 'Glenn Beck', 'Marquis de Sade', 'Bret Easton Ellis', 'Alfred Hitchcock', 'Angelina Jolie', 'Meryl Streep', 'Madonna', 'Jack Nicholson', 'Kevin Spacey', 'Ben Affleck', 'Ryan Seacrest', 'Mila Kunis', 'Amy Winehouse', 'Milla Jovovich', 'Anna Wintour', 'Judi Dench', 'Helen Mirren', 'Glenn Close', 'Camilla Parker Bowles', 'Taylor Swift', 'Sasha Grey', 'Traci Lords', 'James Deen', 'Robin Thicke', 'Megan Fox']

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
	for h in ESTP:
		main(h)
