


class BAR():
	def __init__(self, minValue = 0, maxValue = 1):
		self.minValue = minValue
		self.maxValue = maxValue
		self.nbars = 50
		self.dBar = (float(self.maxValue) - float(self.minValue) ) / float(self.nbars)
		self.prog = 0
		

	def getNbars(self, value):
		print value, self.dBar
		return int(value * self.dBar)

	def makeBar(self, currentValue):

		currentNbars = self.getNbars(currentValue)
		
		bar = '['
		for i in xrange(0, currentNbars):
			bar += '-'
		bar += '>'
		for i in xrange(0, self.nbars - currentNbars):
			bar += ' '
		bar += ']'
		self.barStr = bar

	def getBar(self):

		self.makeBar(self.prog)
		self.prog += 1
		return self.barStr
		
bar = BAR(maxValue = 5)

#for i in xrange(0, bar.maxValue):
#	print bar.getBar()
 	
def makeBar(prog, tot):
	perct = float(prog) / float(tot) * 100
	perct = str(perct) + '%'
	bar = '['
	for i in xrange(0, prog):
		bar += '-'
	bar += '>'
	for i in xrange(0, tot - prog):
		bar += ' '
	bar += '] ' + perct
	return bar

def getChannelValue(channelID):
	import random
	return int(random.random() * 50 )

def dance(nchanels = 10, nsteps = 14, tsleep = 0.1):
	
	import random, sys, time

	maxValue = 50
	CURSOR_UP_ONE = '\x1b[1A'
	ERASE_LINE = '\x1b[2K'

	dele = ''
	nheader_lines = 1
	for i in xrange(0, nchanels + nheader_lines):
		dele += CURSOR_UP_ONE + ERASE_LINE

	for j in xrange(0, nsteps):
		
		sys.stdout.write('time = ' + str(j+1) + '\n' )

		for channel in xrange(0, nchanels):
			value = getChannelValue(channel)
			sys.stdout.write( str(channel) + ' ' + makeBar(value, maxValue) +'\n' )

		time.sleep(tsleep)
		

		if j < nsteps - 1:
			sys.stdout.write(dele)

dance(nchanels = 10, nsteps = 14, tsleep = 0.1)
