class Animal(object):
    def __init__(self):
        self.kind='Animal'
        self.weight=1
    def eat(self):
        print '%s is eating' % self.kind
        self.weight+=1

        
class Plant(object):
    def __init__(self):
        self.kind='Plant'
        self.weight=100
    def eat(self):
        print '%s is sucking' % self.kind
        self.weight+=10

        
class Organism(Animal, Plant):
    def __init__(self):
        Animal.__init__(self)
        Plant.__init__(self)
    def eat(self):
        print 'Organism is doing several things...'
        # super(Organism, self).eat()
        Plant.eat(self)
        Animal.eat(self)
        
if __name__ == '__main__':
    a = Organism()
    a.eat()
    print a.weight
    
    help(a)