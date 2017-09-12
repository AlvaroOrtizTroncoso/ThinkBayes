from thinkbayes import Beta

beta = Beta()
beta.Update((140, 110))
print('Mean', beta.Mean())
print('CI', beta.MakePmf().CredibleInterval())