import matplotlib.pyplot as plt 
from collections import OrderedDict
from operator import itemgetter


def hash(string):
	s = 0
	for i, char in enumerate(string):
		x = ord(char)
		x << 32
		y = 11
		s += (x + 11**i)
	return s % 33091

def hash2(string):
	s = 0
	for i, char in enumerate(string):
		x = ord(char)
		x << 7
		y = 5
		s += (5**x)
	return s % 33091

def count_collisions(d):
	count = 0
	for k,v in d.items():
		if v > 2:
			count += 1
	return float(count / 25144)

def print_collisions(d):
	count = 0
	for k,v in d.items():
		if v > 2:
			print(k,v)

def insert(word, table):
	h = hash2(word)
	if not table[h]:
		table[h] = word
	else:
		offset = hash(word)
		if not table[((h + offset) % 33091) + 1]:
			table[((h + offset) % 33091) + 1] = word
		else:
			print("collision!")




if __name__ == '__main__':

	with open('dictionary.txt', 'r') as f:
	words = [x for x in f.read().split('\n') if x != '']
	

	data = [hash2(string) for string in words]



	unique_elements = set(data)

	d = {}
	for element in unique_elements:
		d[element] = data.count(element)

	print_collisions(d)
	print(count_collisions(d))
	plt.hist(data, bins=10)
	plt.show()