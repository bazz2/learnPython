#!/bin/python

def print_list(max_num, increment):
    i = 0
    numbers = []

    print "max: %d; increment: %d" % (max_num, increment)
    while i < max_num:
        print "At the top i is %d" % i
        numbers.append(i)

        i += increment
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "
    for num in numbers:
        print num

    print numbers
    
print_list(10, 2)
