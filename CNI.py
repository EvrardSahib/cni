class Cni:
    print("une CNI viens d'etre créé")
    def __init__(self, noms, prenoms, date_de_naissance, numero_de_la_CNI, nationalite, taille, date_de_delivrance, date_expiration):
        self.noms=noms
        self.prenoms=prenoms
        self.date_de_naissance=date_de_naissance
        self.numero_de_la_CNI=numero_de_la_CNI
        self.nationalite=nationalite
        self.taille=taille
        self.date_de_delivrance=date_de_delivrance
        self.date_expiration=date_expiration


    def setnoms(self,noms,date_de_naissance,numero_de_la_CNI):
        self.noms=noms
brice=Cni('brice', 'olinga',12/34/2022,56678,'camerounais',12,11,34)
print(brice.noms,brice.prenoms,brice.date_de_naissance,brice.numero_de_la_CNI)

