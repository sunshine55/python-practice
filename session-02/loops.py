# FOR .. IN ..:
my_scores = [10,30,40]
for score in my_scores:
	print 'Score: ', score
else:
	print 'Loop is done'

# FOR(i=0;i<5;i++)
for i in range(5):
	print i

# WHILE
count=10
while count>0:
	print 'Count: ',count
	count -= 1
else:
	print 'Final count: ',count

#DO-WHILE
count=1
while True:
	print count
	count += 1
	if count==5: break
