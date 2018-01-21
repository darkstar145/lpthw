def write_num(n, x):
	i = 0
	numbers = []
	for i in range(0, n, x):
		print "At the top is %d" % i
		
		numbers.append(i)
		
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
		
	print "The numbers: "
	for num in numbers:
		print num

write_num(10, 2)