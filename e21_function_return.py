#!/bin/python

def add(a, b):
    print "Adding %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "Subtracting %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "Multiplying %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "Dividing %d / %d" % (a, b)
    return a / b

print "Let's do some math with just functions!"
age = add(3, 5)
height = subtract(10, 0)
weight = multiply(3, 1)
iq = divide(2, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway
print "Here is a puzzle"

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print "That becomes: %d, Can you do it by hand?" % what
