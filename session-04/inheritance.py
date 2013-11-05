'''
Created on Oct 2, 2013

@author: Khanh
'''
class Animal:
    s_static_animal='"s_static_animal" is accessible across all instances of Animal and all subclasses of Animal and instances thereof'
    def __init__(self):
        self.s_instance_animal='"s_instance_animal" is scoped inside the instances of Animal'
        self._weight = 0
    def eat(self):
        print '"Eat" is invoked using this class->"',self
    @property
    def color(self):
        return 'Blue'
    @property
    def weight(self):
        return self._weight
    @weight.setter
    def weight(self, value):
        if value >= 0:
            self._weight = value
        
    @staticmethod
    def info():
        return '"info" is a static method of Animal'
    @classmethod
    def inspect(cls):
        return '"inspect" is a class method of Animal:', cls
        
class Mammal(Animal):
    s_static_mammal='"s_static_mammal" is accessible across all instances of Mammal and all subclasses of Mammal and instances thereof'
    def __init__(self):
        Animal.__init__(self) # Invoke super() Pythonically
        self.s_instance_mammal='"s_instance_mammal" is scoped inside the instances of Mammal'
    def breastfeed(self):
        print '"breastfeed" is invoked using this class->"',self
    @property
    def weight(self):
        return '100 gram'    

if __name__=='__main__':
    print '- ALL ABOUT ANIMAL -'
    print '================================================'
    general_animal = Animal()
    print 'Accessing class Animal'
    print 'S_STATIC_ANIMAL = ', Animal.s_static_animal
    print 's_instance_animal = ', general_animal.s_instance_animal
    print 'instance.S_STATIC_ANIMAL = ', general_animal.s_static_animal
    print 'INFO(): ',Animal.info()
    print 'instance.INFO(): ',general_animal.info()
    print 'INSPECT(CLASS): ',Animal.inspect()
    print 'instance.INSPECT(CLASS): ',general_animal.inspect()
    
    print 'instance.color: ',general_animal.color
    print 'instance.weight: ',general_animal.weight
    general_animal.eat()
    
    print '\n- ALL ABOUT MAMMAL -'
    print '================================================'
    dog = Mammal()
    print 'Accessing class Mammal'
    print 'S_STATIC_ANIMAL = ', Mammal.s_static_animal
    print 's_instance_animal = ', dog.s_instance_animal
    print 'instance.S_STATIC_ANIMAL = ', dog.s_static_animal
    print 'INFO(): ',Mammal.info()
    print 'instance.INFO(): ',dog.info()
    print 'INSPECT(CLASS): ',Mammal.inspect()
    print 'instance.INSPECT(CLASS): ',dog.inspect()
    
    print 'instance.color: ',dog.color
    print 'instance.weight: ',dog.weight
    dog.eat()
    dog.breastfeed()