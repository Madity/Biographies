import os

def main(e):
	fio = open(e,"r")
	a = fio.readlines()
	b = []
	for i in a:
		b.append(i[:-1])

	print b
	print "==="
	print len(b)


if __name__=='__main__':
	main("adj_list.txt")
