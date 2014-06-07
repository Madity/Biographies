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


ISTP = ['Miyamoto Musashi', 'Erwin Rommel', 'Steve Jobs', 'Jack Dorsey', 'Diogenes the Dog', 'Dalai Lama XIV', 'Ron Paul', 'Donald Rumsfeld', 'Miles Davis', 'Frank Zappa', 'Stanley Kubrick', 'Clint Eastwood', 'Daniel Craig', 'Harrison Ford', 'Tom Cruise', 'Christian Bale', 'Scarlett Johansson', 'Ellen Page', 'Kristen Stewart', 'Demi Moore', 'Snoop Dogg', 'Phil Ivey', 'David Blaine', 'Steven Wright', 'Woody Allen', 'Ashton Kutcher', 'Bruce Lee', 'Jenna Jameson', 'Rodney Mullen', 'Simon Cowell']
if __name__=="__main__":
	os.system("touch outputadj.txt")
	fio = open("outputadj.txt","w")
	serial = 1
	fio.write("S.No    Name                         Category                    WordCount\n")                                                    
	for files in ISTP:
		filea = files.replace(' ','_')
		i = filea + "_adj.txt"
		if i!='output.txt' and i!='temp.py' and i!='count.py' and i!='searchadj.py' and i!='outputadj.txt' and i!='countbio.py':
			out = main(i)
			outstring = str(serial) + "    " + i
			j = 30 - len(i)
			for u in range(j):
				outstring = outstring + ' '
			
			outstring = outstring + "ISTP" + "                    " + str(out)+"\n"
			fio.write(outstring)
			serial = serial + 1
	fio.close()
			

