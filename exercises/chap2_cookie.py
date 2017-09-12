from thinkbayes import Pmf

pmf = Pmf() 
# set prior probability
pmf.Set('Bowl 1', 0.5) 
pmf.Set('Bowl 2', 0.5)
# update with new data
pmf.Mult('Bowl 1', 0.75) 
pmf.Mult('Bowl 2', 0.5)
# renormalize, as hypotheses are mutually exclusive
pmf.Normalize()
# posterior probabilities
print (pmf.Prob('Bowl 1'))
print (pmf.Prob('Bowl 2'))
