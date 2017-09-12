from thinkbayes import Suite

class Dice(Suite):
	def Likelihood(self, data, hypo):
		if hypo < data: 
			return 0
		else:
			return 1.0/hypo

dice = Dice([4,6,8,12,20])
dice.Update(6)
for roll in [6, 8, 7, 7, 5, 4]:
	dice.Update(roll)
	
dice.Print()	