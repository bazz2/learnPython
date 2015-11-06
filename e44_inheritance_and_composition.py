#!/bin/python

""" implicit inheritance """
class Parent(object):
    def implicit(self):
        print "Parent implicit()"
class Child(Parent):
    pass
dad = Parent()
son = Child()
dad.implicit()
son.implicit()


""" override inheritance """
class Parent_ii(object):
    def override(self):
        print "Parent override()"
class Child_ii(Parent_ii):
    def override(self):
        print "Child override()"
dad = Parent_ii()
son = Child_ii()
dad.override()
son.override()

""" alter inheritance """
class Parent_iii(object):
    def altered(self):
        print "Parent altered()"
class Child_iii(Parent_iii):
    def altered(self):
        print "Child, before parent altered()"
        super(Child_iii, self).altered()
        print "Chile, after parent altered()"
dad = Parent_iii()
son = Child_iii()
dad.altered()
son.altered()
