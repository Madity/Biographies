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


ESTJ = ['Bernard Montgomery', 'Henry Ford', 'Hillary Clinton', 'Condoleezza Rice', 'Dr. Phil', 'Amy Chua', 'Martha Stewart', 'Michelle Obama', 'Ann Coulter', 'Michelle Malkin', "Bill O'Reilly", 'Alan Dershowitz', 'Paul of Tarsus', 'Muhammad', 'Billy Graham', 'Jerry Falwell', 'Sonia Sotomayor', 'Tom Clancy', 'Uma Thurman', 'Lucy Liu', 'Emma Watson', 'Courteney Cox', 'Alec Baldwin', 'Kelsey Grammer', 'Roger Ebert', 'Judge Judy', 'Nancy Grace', 'Laura Schlessinger', 'Ivanka Trump']

if __name__=="__main__":
	os.system("touch outputadj.txt")
	fio = open("outputadj.txt","w")
	serial = 1
	fio.write("S.No    Name                         Category                    WordCount\n")                                                    
	for files in ESTJ:
		filea = files.replace(' ','_')
		i = filea + "_adj.txt"
		if i!='output.txt' and i!='temp.py' and i!='count.py' and i!='searchadj.py' and i!='outputadj.txt' and i!='countbio.py':
			out = main(i)
			outstring = str(serial) + "    " + i
			j = 30 - len(i)
			for u in range(j):
				outstring = outstring + ' '
			
			outstring = outstring + "ESTJ" + "                    " + str(out)+"\n"
			fio.write(outstring)
			serial = serial + 1
	fio.close()
			

