from foo import dummy_var
import foo.bar as foo_bar

print 'Module scope: from package foo: dummy_var = %s' % dummy_var
print 'Module scope: from module foo.bar: name = %s, age = %d' % (foo_bar.name, foo_bar.age)