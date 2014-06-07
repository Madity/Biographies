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


ESFJ = ['Harry S. Truman', 'Gerald Ford', 'Colin Powell', 'Desmond Tutu', 'Andrew Carnegie', 'Sam Walton', 'Andy Rooney', 'Francis', 'Sarah Palin', 'Rick Santorum', 'John Boehner', 'Larry King', 'Regis Philbin', 'Barbara Walters', 'Chris Wallace', 'Alyson Hannigan', 'Jason Segel', 'Anne Hathaway', 'Penelope Cruz', 'Selena Gomez', 'Jessica Alba', 'Jennifer Garner', 'Sarah Jessica Parker', 'Whitney Houston', 'Mariah Carey', 'Alicia Keys', 'Shania Twain', 'Prince William', 'Lesley Stahl', 'Elton John', 'Randy Jackson', 'Hugh Jackman', 'Jamie Bell', 'Vin Diesel', 'Woody Harrelson', 'Tyra Banks', 'Jenny McCarthy', 'Laura Harring', 'Victoria Beckham', 'Adam Young', 'Vanessa Hudgens']

if __name__=="__main__":
	os.system("touch outputadj.txt")
	fio = open("outputadj.txt","w")
	serial = 1
	fio.write("S.No    Name                         Category                    WordCount\n")                                                    
	for files in ESFJ:
		filea = files.replace(' ','_')
		i = filea + "_adj.txt"
		if i!='output.txt' and i!='temp.py' and i!='count.py' and i!='searchadj.py' and i!='outputadj.txt' and i!='countbio.py':
			out = main(i)
			outstring = str(serial) + "    " + i
			j = 30 - len(i)
			for u in range(j):
				outstring = outstring + ' '
			
			outstring = outstring + "ESFJ" + "                    " + str(out)+"\n"
			fio.write(outstring)
			serial = serial + 1
	fio.close()
			

