from thinkbayes import Pmf

word_list=["bla","bla","boe","fasel"]
pmf = Pmf()
for word in word_list:
	pmf.Incr(word, 1)
pmf.Normalize()

print(pmf.Prob("bla"))
