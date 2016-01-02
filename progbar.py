



def makeBar(prog, tot):
	perct = float(prog) / float(tot) * 100
	perct = str(perct) + '%'
	bar = '['
	for i in xrange(0, prog):
		bar += '-'
	bar += '>'
	for i in xrange(0, tot - prog):
		bar += ' '
	bar += '] ' + perct + '\n'
	return bar


def dance(nchanels = 10, nsteps = 14):
	
	import random, sys, time

	maxValue = 50
	CURSOR_UP_ONE = '\x1b[1A'
	ERASE_LINE = '\x1b[2K'

	dele = ''

	for i in xrange(0, nchanels + 1):
		dele += CURSOR_UP_ONE + ERASE_LINE

	for j in xrange(0, nsteps):
		
		sys.stdout.write('time = ' + str(j) + '\n' )

		for i in xrange(0, nchanels):
			value = int(random.random() * maxValue)
			sys.stdout.write( str(i) + ' ' + makeBar(value, maxValue) )

		time.sleep(0.1)
		

		if j < nsteps - 1:
			sys.stdout.write(dele)

dance()
