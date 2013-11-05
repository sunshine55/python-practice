class Boo:
    _count = 0
    
    def __init__(self, name):
        self._name = name
        Boo._count += 1
    
    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self, name):
        self._name = name
        
    @classmethod    
    def instance_count(cls):
        return cls._count
        
    @staticmethod
    def generate_lastname():
        return 'Johns'