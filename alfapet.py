tiedosto = open('kotus_sanat.txt', 'r', encoding='latin-1')
sanat = [rivi.rstrip() for rivi in tiedosto.readlines()]

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
