'''
Created on Oct 3, 2013

@author: Khanh
'''
from sys import getrefcount as refcount
import weakref
import gc

class Dummy:
    pass

class VirtualList:
    def __init__(self):
        self.w1=None
        self.w2=None
        self.w3=None
    def set_all(self,*args):
        self.w1 = weakref.ref(args[0])
        self.w2 = weakref.ref(args[1])
        self.w3 = weakref.ref(args[2])
        
        
    def get_all(self):
        # print 'id: ', id(a), '=> ', refcount(a)
        
        print self.w1()
        print self.w2()
        print self.w3()

a = Dummy()
b = Dummy()
c = Dummy()

#wr = weakref.ref(a)
#print wr
vlist = VirtualList()
vlist.set_all(a,b,c)

print 'id: ', id(a), '=> ', refcount(a)
print 'id: ', id(b), '=> ', refcount(b)
# print gc.get_referents(a, b)
# print gc.get_referrers(a)
print '================================='
del b, c
vlist.get_all()