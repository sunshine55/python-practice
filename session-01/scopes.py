x = 1
print 'Module scope: %s' % x

def cook():
    print 'Cook scope: %s' % x
    
cook()

def serve():
    # Comment the below and uncomment next segment to generate Error
    x = 2
    print 'Serve scope: %s' % x
    """ Uncomment the following to generate UnboundLocalError
    print 'Serve scope: %s' % x
    x = 2
    """
    
serve()
print 'Module scope: %s' % x

def clean():
    from sys import argv
    print 'Clean scope: ', argv
    
clean();
# argv is imported into the scope of function clean()
# so it is not accessible in module scope
# print 'Module scope: ', argv