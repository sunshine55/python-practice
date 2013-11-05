# -*- coding: utf-8 -*-

a = set(['java','c#','php'])
b = set(['php','python','ruby'])
z = set(['php', 'c#'])

print 'Union – Merge two sets'
print a.union(b) # OR a | b

print 'Subtraction – Remove members from a set'
print a - b
print b - a

print 'Intersection – Take the common members from two sets'
print a.intersection(b)

print 'Exclusion – Take the disjoint members in two sets'
print a.symmetric_difference(b) # a^b
print b^a

print 'Test for superset/subset'
print 'a contains z? ',a.issuperset(z)
print 'z belongs to a? ', z.issubset(a)