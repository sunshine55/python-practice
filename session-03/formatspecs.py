print '### NUMBERS ###'

i_int = 200
f_float = 3.14159
i_bigint = 3000000000

print 'Decimal: %d' % f_float
print 'Integer:  %i' % i_int
print 'Octal: %o' % i_int
print 'Hex: %x' % i_int
print 'Floating-point exponent: %e' % i_bigint

print '### NUMBERS w/ ALIGNMENT###'

print '%10s %40d' % ('Decimal:',f_float)
print '%10s %40i' % ('Integer:',i_int)
print '%10s %40o' % ('Octal:',i_int)
print '%10s %40x' % ('Hex:',i_int)
print 'Floating-point exponent: %40.2e' % i_bigint

print '### CHARACTERS and STRINGS ###'

s_name = 'Tom'
c_char = 'c'

print 'String: %s' % s_name
print 'Character: %c' % c_char

print '### BINARY ###'

print 'Binary: {0:b}'.format(i_int)