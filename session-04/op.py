'''
Created on Oct 3, 2013

@author: Khanh
'''
import operator

class Dummy:
    def __init__(self, value):
        self.value = value
    
    def echo(self, msg):
        print msg
        
    def __call__(self):
        return self.value
    
#     def __str__(self):
#         return 'This is a STRING from dummy'
#     
    def __repr__(self):
        return 'This is a REPR from dummy'
     
    def __add__(self, target):
        return self.value + target.value
a = Dummy(1)
b = Dummy(2)
# a.echo('ABC this is something')
# call = operator.methodcaller('echo','ABC this is something')
# call(a)

print a + b