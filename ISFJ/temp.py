import os

ISFJ = ['David Petraeus', 'George Marshall', 'Robert E. Lee', 'George A. Custer', 'Jimmy Carter', 'George H.W. Bush', 'Mitt Romney', 'Rosa Parks', 'Mother Teresa', 'Christopher Walken', 'Anthony Hopkins', 'Naomi Watts', 'Halle Berry', 'Dr. Dre', '50 Cent', 'Kanye West', 'Kim Kardashian', 'Tiger Woods', 'Lance Reddick', 'Kirsten Dunst', 'Jessica Simpson', 'Bruce Willis', 'Prince Charles', 'Kate Middleton', 'Princess Mary', 'Katie Holmes']

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
	for h in ISFJ:
		main(h)
