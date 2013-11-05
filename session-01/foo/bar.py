name = 'Tom'
age = 12

def report():
    print '%s is now %d years old' % (name, age)

def get_older():
    global age
    age += 1
    print '%s is now %d years old' % (name, age)
    
def describe_functions():
    def describe(func, desc):
        func.description = desc
    
    describe(report, 'A read-only function')
    describe(get_older, 'Changes the variable value')