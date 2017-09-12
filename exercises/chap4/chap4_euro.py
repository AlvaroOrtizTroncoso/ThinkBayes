from thinkbayes import Suite

class Euro(Suite):
	def Likelihood(self, data, hypo):
		if data == 'H':
			return hypo/100.0
		else:
			return 1-hypo/100.0


suite = Euro( range(0,101) )
dataset = 'H' * 140 + 'T' * 110

for data in dataset:
	suite.Update(data)

print('MaximumLikelihood', suite.MaximumLikelihood())
print('CI', suite.CredibleInterval())