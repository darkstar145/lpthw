class Parent(object):

    def override(self): # not override
        print "PARENT override()"

    def implicit(self): # not override
        print "PARENT implicit()"

    def altered(self): # not override
        print "PARENT altered()"

class Child(Parent):

    def override(self): # override
        print "CHILD override()"

    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered() # not override
        print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override() # override

dad.altered()
son.altered() # override