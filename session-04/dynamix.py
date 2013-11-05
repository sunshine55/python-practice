'''
Created on Oct 3, 2013

@author: Khanh
'''
from inheritance import Animal

def fly(self):
    self.attitude = 10

def dive(self):
    self.depth = -40
    
Animal.fly = fly

if __name__=='__main__':
    bat = Animal()
    bat.fly()
    print 'Bat attitude: ', bat.attitude
    
    dolphin = Animal()
    Animal.dive = dive
    dolphin.dive()
    print 'Dolphin depth: ', dolphin.depth
    # BINDING IS STILL EFFECTIVE AFTER THE INSTANCE HAS BEEN CREATED
    
    bat.dive()
    print 'Bat depth: ', bat.depth