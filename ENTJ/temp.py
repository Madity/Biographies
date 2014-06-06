import os

ENTJ = ['Napoleon Bonaparte', 'Julius Caesar', 'Margaret Thatcher', 'Aristotle', 'Alexander Hamilton', 'Garry Kasparov', 'Bill Gates', 'Carl Sagan', 'Karl Rove', 'Dick Cheney', 'Rahm Emanuel', 'Al Gore', 'Madeleine Albright', 'Nancy Pelosi', 'Aung San Suu Kyi', 'Peter Thiel', 'Rush Limbaugh', 'Jack Welch', 'David Letterman', 'George Clooney', 'Matt Damon', 'Penn Jillette', 'Charlize Theron', 'Katharine Hepburn', 'Tea Leoni', 'Adele', 'Cobie Smulders']

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
	for h in ENTJ:
		main(h)
