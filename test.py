import os
import re

def main():
	fio = open('Adjective_list.csv','r')
	lines = fio.readlines()
	for line in lines:
		s = line.split(',')
		print s
		print '====='


if __name__=='__main__':
	main()
