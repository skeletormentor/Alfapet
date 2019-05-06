import pandas as pd

sanat = pd.read_csv('kotus_sanat.txt', header=None, squeeze=True, engine='python')

kirjainpisteet = {}
def pisteytys(kirjaimet, pisteet):
    uusidict = dict(zip(list(kirjaimet), [pisteet]*len(kirjaimet)))
    kirjainpisteet.update(uusidict)

pisteytys('aitensklo', 1)
pisteytys('mpruvä', 2)
pisteytys('hjy', 3)
pisteytys('ödg', 4)
pisteytys('bf', 6)
pisteytys('c', 8)
pisteytys('qwxzå', 0)