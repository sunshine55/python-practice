'''
Created on Oct 2, 2013

@author: Khanh
'''

class Service(object):
    '''
    classdocs: We document the class here
    '''

    def __init__(self, param_1, param_2):
        '''
        Constructor: We need two parameters 
        '''
        
if __name__=='__main__':
    print 'Using "Service docstring"', Service.__doc__
    print 'And Service.__init__ doc string', Service.__init__.__doc__
    help(Service.__init__)