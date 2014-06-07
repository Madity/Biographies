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


ESFP = ['Bill Clinton', 'John F. Kennedy', 'Ronald Reagan', 'Peter the Great', 'Hugh Hefner', 'Richard Branson', 'Larry Ellison', 'Howard Schultz', 'Tony Robbins', 'Wayne Dyer', 'Deepak Chopra', 'Paulo Coelho', 'Horatio Nelson', 'Quentin Tarantino', 'Steven Spielberg', 'Mel Gibson', 'Beyonce', 'Denzel Washington', 'Will Smith', 'Jamie Oliver', 'Robbie Williams', 'Katy Perry', 'Nicki Minaj', 'Pink', 'Marina Diamandis', 'Leonardo DiCaprio', 'Justin Bieber', 'Harry Styles', 'Evan Rachel Wood', 'Miley Cyrus', 'Cameron Diaz', 'Ringo Starr', 'Dana White', 'Chloe Grace Moretz', 'Danielle de Niese']
if __name__=="__main__":
	os.system("touch outputadj.txt")
	fio = open("outputadj.txt","w")
	serial = 1
	fio.write("S.No    Name                         Category                    WordCount\n")                                                    
	for files in ESFP:
		filea = files.replace(' ','_')
		i = filea + "_adj.txt"
		if i!='output.txt' and i!='temp.py' and i!='count.py' and i!='searchadj.py' and i!='outputadj.txt' and i!='countbio.py':
			out = main(i)
			outstring = str(serial) + "    " + i
			j = 30 - len(i)
			for u in range(j):
				outstring = outstring + ' '
			
			outstring = outstring + "ESFP" + "                    " + str(out)+"\n"
			fio.write(outstring)
			serial = serial + 1
	fio.close()
			

