mod_x = 0

class Moo:
    # This mod_x does not overshadow module's mod_x
    # Must be referenced to as Moo.mod_x
    mod_x = 100
    
    def __init__(self):
        global mod_x
        mod_x += 1
        Moo.mod_x += 100
        # Instance variables
        self.name = 'Tom'
        self.age = 20
        
    def get_older(self):
        self.age += 1
        self.report()
        
    def report(self):
        print '%s is not %d' % (self.name, self.age)
        
class PaPaClass:
    class KidClass:
        pass
    pass