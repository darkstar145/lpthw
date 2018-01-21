ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop() # pop(more_stuff), or call pop on more_stuff
    print "Adding: ", next_one
    stuff.append(next_one) # append(stuff, next_one), or append next_one to stuff
    print "There are %d iterms now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] # whoa! fancy
print stuff.pop() # pop(stuff), or call pop on stuff
print ' '.join(stuff) # what? cool! # join(' ', stuff), or join stuff with spaces
print '#'.join(stuff[3:5]) # super stellar! # join('#', stuff[3:5]), or join items 3 and 4 of stuff with #