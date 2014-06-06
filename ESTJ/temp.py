import os

ESTJ = ['Bernard Montgomery', 'Henry Ford', 'Hillary Clinton', 'Condoleezza Rice', 'Dr. Phil', 'Amy Chua', 'Martha Stewart', 'Michelle Obama', 'Ann Coulter', 'Michelle Malkin',  'Alan Dershowitz', 'Paul of Tarsus', 'Muhammad', 'Billy Graham', 'Jerry Falwell', 'Sonia Sotomayor', 'Tom Clancy', 'Uma Thurman', 'Lucy Liu', 'Emma Watson', 'Courteney Cox', 'Alec Baldwin', 'Kelsey Grammer', 'Roger Ebert', 'Judge Judy', 'Nancy Grace', 'Laura Schlessinger', 'Ivanka Trump']


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
	for h in ESTJ:
		main(h)
