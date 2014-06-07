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

INFJ = ['Plato', 'Carl Gustav Jung', 'Niels Bohr', 'Mahatma Gandhi', 'Thomas Jefferson', 'Calvin Coolidge', 'Woodrow Wilson', 'Noam Chomsky', 'Simone de Beauvoir', 'Mary Wollstonecraft', 'Ludwig Wittgenstein', 'Sam Harris', 'Marcus Aurelius', 'Dante Alighieri', 'Fyodor Dostoevsky', 'Alexander Solzhenitsyn', 'Baruch Spinoza', 'Arthur Schopenhauer', 'Lars von Trier', 'David Fincher', 'Leonard Cohen', 'Marilyn Manson', 'Al Pacino', 'Daniel Day-Lewis', 'Edward Norton', 'Adrien Brody', 'Cate Blanchett', 'Michelle Pfeiffer', 'Rooney Mara', 'Carey Mulligan', 'Josh Radnor', 'Derren Brown', 'Mystery', 'Tilda Swinton', 'Sufjan Stevens', 'George Harrison']

if __name__=="__main__":
	os.system("touch outputadj.txt")
	fio = open("outputadj.txt","w")
	serial = 1
	fio.write("S.No    Name                         Category                    WordCount\n")                                                    
	for files in INFJ:
		filea = files.replace(' ','_')
		i = filea + "_adj.txt"
		if i!='output.txt' and i!='temp.py' and i!='count.py' and i!='searchadj.py' and i!='outputadj.txt' and i!='countbio.py':
			out = main(i)
			outstring = str(serial) + "    " + i
			j = 30 - len(i)
			for u in range(j):
				outstring = outstring + ' '
			
			outstring = outstring + "INFJ" + "                    " + str(out)+"\n"
			fio.write(outstring)
			serial = serial + 1
	fio.close()
			

