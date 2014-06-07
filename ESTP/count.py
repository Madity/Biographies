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


ESTP = ['Alexander the Great', 'Winston Churchill', 'Theodore Roosevelt', 'George S. Patton', 'Andrew Jackson', 'Franklin D. Roosevelt', 'Malcolm X', 'Douglas MacArthur', 'Donald Trump', 'Peter Schiff', 'James Randi', 'Ernest Hemingway', 'Epicurus', 'Stephen R. Covey', 'Dale Carnegie', 'L. Ron Hubbard', 'George W. Bush', 'Lyndon B. Johnson', 'David Cameron', 'Glenn Beck', 'Marquis de Sade', 'Bret Easton Ellis', 'Alfred Hitchcock', 'Angelina Jolie', 'Meryl Streep', 'Madonna', 'Jack Nicholson', 'Kevin Spacey', 'Ben Affleck', 'Ryan Seacrest', 'Mila Kunis', 'Amy Winehouse', 'Milla Jovovich', 'Anna Wintour', 'Judi Dench', 'Helen Mirren', 'Glenn Close', 'Camilla Parker Bowles', 'Taylor Swift', 'Sasha Grey', 'Traci Lords', 'James Deen', 'Robin Thicke', 'Megan Fox']
if __name__=="__main__":
	os.system("touch outputadj.txt")
	fio = open("outputadj.txt","w")
	serial = 1
	fio.write("S.No    Name                         Category                    WordCount\n")                                                    
	for files in ESTP:
		filea = files.replace(' ','_')
		i = filea + "_adj.txt"
		if i!='output.txt' and i!='temp.py' and i!='count.py' and i!='searchadj.py' and i!='outputadj.txt' and i!='countbio.py':
			out = main(i)
			outstring = str(serial) + "    " + i
			j = 30 - len(i)
			for u in range(j):
				outstring = outstring + ' '
			
			outstring = outstring + "ESTP" + "                    " + str(out)+"\n"
			fio.write(outstring)
			serial = serial + 1
	fio.close()
			

