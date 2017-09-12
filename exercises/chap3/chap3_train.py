from thinkbayes import Pmf
from thinkbayes import Suite
from thinkbayes import Percentile

class Train(Suite):
	
	def __init__(self, hypos):
		Pmf.__init__(self)
		for hypo in hypos:
			self.Set( hypo, 1.0/hypo)
		self.Normalize()
		
		
	def Likelihood(self, data, hypo):
		if hypo < data:
			return 0
		else:
			return 1.0/hypo


max = [500, 1000, 2000]
for m in max:
	hypos = range(1, m+1)
	suite = Train(hypos)
	for data in [60, 30, 90]: 
		suite.Update(data)

interval = Percentile(suite, 7.5), Percentile(suite, 92.5) 
print(interval)		
