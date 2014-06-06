import os

ISTP = ['Miyamoto Musashi', 'Erwin Rommel', 'Steve Jobs', 'Jack Dorsey', 'Diogenes the Dog', 'Dalai Lama XIV', 'Ron Paul', 'Donald Rumsfeld', 'Miles Davis', 'Frank Zappa', 'Stanley Kubrick', 'Clint Eastwood', 'Daniel Craig', 'Harrison Ford', 'Tom Cruise', 'Christian Bale', 'Scarlett Johansson', 'Ellen Page', 'Kristen Stewart', 'Demi Moore', 'Snoop Dogg', 'Phil Ivey', 'David Blaine', 'Steven Wright', 'Woody Allen', 'Ashton Kutcher', 'Bruce Lee', 'Jenna Jameson', 'Rodney Mullen', 'Simon Cowell']

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
	for h in ISTP:
		main(h)
