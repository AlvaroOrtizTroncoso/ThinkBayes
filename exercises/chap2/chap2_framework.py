from thinkbayes import Pmf

class Cookie(Pmf):
	def __init__(self, hypos):
		Pmf.__init__(self)
		for hypo in hypos:
			self.Set(hypo, 1)
		self.Normalize()


	def Update(self, data):
		for hypo in self.Values():
			like = self.Likelihood(data,hypo)
			self.Mult(hypo, like)
		self.Normalize()
	
	mixes = { 'Bowl 1':dict(vanilla=0.75, chocolate=0.25), 'Bowl 2':dict(vanilla=0.5, chocolate=0.5), }
	def Likelihood(self, data, hypo):
		return self.mixes[hypo][data]
		
	
	def Print(self):
		for hypo, prob in pmf.Items():
			print(hypo, prob)

hypos = ['Bowl 1', 'Bowl 2']
pmf = Cookie(hypos)
pmf.Update('vanilla')
pmf.Print()	