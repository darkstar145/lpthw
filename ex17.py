from sys import argv
from os.path import exists

script, from_file, to_file = argv

with open(from_file) as f:
	in_data = f.read()
with open(to_file, 'w') as t:
	t.write(in_data)