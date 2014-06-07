import os


def main(e):
	os.system("touch adj_list.txt")
	fio = open("adj_list_backup.txt", "r")
	fio1 = open("adj_list.txt", "a")
	a = fio.readlines()
	for i in a:
		k = i.split(' ')
		fio1.write(k[0]+"\n")
	fio.close()
	fio1.close()


if __name__=="__main__":
	main("adj_list_backup.txt")
	print "Completed"
