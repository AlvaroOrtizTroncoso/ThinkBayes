from thinkbayes import Suite

class Bowl(Suite):
	mixes = { 'Bowl 1':dict(vanilla=0.75, chocolate=0.25), 'Bowl 2':dict(vanilla=0.5, chocolate=0.5), }
	def Likelihood(self, data, hypo):
		return self.mixes[hypo][data]


hypos = ['Bowl 1', 'Bowl 2']
suite = Bowl(hypos)
suite.Update('vanilla')
suite.Print()	