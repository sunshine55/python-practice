short_list = ['a','b','c']
long_list = [1,2,3,4,5,6,7,8,9,0]

print '### LIST LENGTH ###'
print 'Short: %i' % len(short_list)
print 'Long: %i' % len(long_list)

print '### LIST CONCAT ###'
big_list = short_list + long_list
print 'BIG: ', big_list

print '### LIST REPETITION ###'
rep_list = short_list * 10
print 'Repeated: ', big_list

print '### LIST INDEXING and SLICING ###'
list_0_4 = long_list[0:4]
list_5_7 = long_list[5:7]
list_even = long_list[::2]
print 'List 0 to 4: ', list_0_4
print 'List 5 to 7: ', list_5_7
print 'List even items: ', list_even

print '### LIST SORT ###'
# sort
sorted_list = sorted(long_list)
print sorted_list

# in-place sort
long_list.sort()
print long_list