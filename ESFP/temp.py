import os

ESFP = ['Bill Clinton', 'John F. Kennedy', 'Ronald Reagan', 'Peter the Great', 'Hugh Hefner', 'Richard Branson', 'Larry Ellison', 'Howard Schultz', 'Tony Robbins', 'Wayne Dyer', 'Deepak Chopra', 'Paulo Coelho', 'Horatio Nelson', 'Quentin Tarantino', 'Steven Spielberg', 'Mel Gibson', 'Beyonce', 'Denzel Washington', 'Will Smith', 'Jamie Oliver', 'Robbie Williams', 'Katy Perry', 'Nicki Minaj', 'Pink', 'Marina Diamandis', 'Leonardo DiCaprio', 'Justin Bieber', 'Harry Styles', 'Evan Rachel Wood', 'Miley Cyrus', 'Cameron Diaz', 'Ringo Starr', 'Dana White', 'Chloe Grace Moretz', 'Danielle de Niese']


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
	for h in ESFP:
		main(h)
