
class BAR():

	def __init__(self, 
				maxValue = 50, 
				nchannels = 10, 
				barProps = {'barStart' : '[', 
							'barEnd' : ']', 
							'barInter' : '-', 
							'barPoint' : '>'
							}
				):
		self.maxValue = maxValue
		self.CURSOR_UP_ONE = '\x1b[1A'
		self.ERASE_LINE = '\x1b[2K'
		self.nchannels = nchannels
		
		self.barStart = barProps['barStart']
		self.barEnd = barProps['barEnd']
		self.barInter = barProps['barInter']
		self.barPoint = barProps['barPoint']
		
		self.genDele()
		
	def genDele(self):
		dele = ''
		nheader_lines = 1
		for i in xrange(0, self.nchannels + nheader_lines):
			dele += self.CURSOR_UP_ONE + self.ERASE_LINE	
		self.dele = dele
		
	def makeBar(self, prog):
		perct = float(prog) / float(self.maxValue) * 100
		perct = str(perct) + '%'
		bar = self.barStart
		for i in xrange(0, prog):
			bar += self.barInter
		bar += self.barPoint
		for i in xrange(0, self.maxValue - prog):
			bar += ' '
		bar += self.barEnd + ' ' + perct
		
		return bar	
		
	def getChannelValue(self, ID):	
		import random
		return int(random.random() * 50 )
		
	def dance(self, tsleep = 0.1, nsteps = 14):	
		
		import random, sys, time

		for j in xrange(0, nsteps):	
			sys.stdout.write('time = ' + str(j+1) + '\n' )

			for channel in xrange(0, self.nchannels):
				value = self.getChannelValue(channel)
				sys.stdout.write( str(channel) + ' ' + self.makeBar(value) +'\n' )

			time.sleep(tsleep)
	

			if j < nsteps - 1:
				sys.stdout.write(self.dele)


appearance  = {'barStart' : '|', 
							'barEnd' : ']', 
							'barInter' : '*', 
							'barPoint' : '>'
							}
				
bar = BAR(barProps = appearance)
bar.dance()				