class Hayvan():
    def __init__(self, tür, ayak_sayisi):
        self.tür = tür
        self.ayak_sayisi = ayak_sayisi
    
    def __str__(self):
        return f'Hayvanin türü: {self.tür}, hayvanin ayak sayisi: {self.ayak_sayisi}.'
    
class Kopek(Hayvan):
    def __init__(self, tür, ayak_sayisi, kopek_cinsi):
        super().__init__(tür, ayak_sayisi)
        self.kopek_cinsi = kopek_cinsi
    
    def havla(self):
        print(f'{self.kopek_cinsi}: Hav!')

    def __str__(self):
        return f'Köpek cinsi: {self.kopek_cinsi}.'


kopek1 = Kopek('Köpek', 4, 'Golden Retriever')
kopek2 = Kopek('Köpek', 4, 'Labrador')

print(kopek1)
print(kopek2)

kopek1.havla()
kopek2.havla()

print('*' * 30)

class Kedi(Hayvan):
    def __init__(self, tür, ayak_sayisi, kedi_cinsi):
        super().__init__(tür, ayak_sayisi)
        self.kedi_cinsi = kedi_cinsi
    

    def miyavla(self):
        print(f'{self.kedi_cinsi}: Miyav!')
    
    def __str__(self):
        return f'Kedi cinsi: {self.kedi_cinsi}'

kedi1 = Kedi('Kedi', 4, 'Ankara kedisi')
kedi2 = Kedi('Kedi', 4 ,'Van kedisi')

print(kedi1)
print(kedi2)

kedi1.miyavla()
kedi2.miyavla()

print('*' * 30)

class Kus(Hayvan):
    def __init__(self, tür, ayak_sayisi, kus_cinsi):
        super().__init__(tür, ayak_sayisi)
        self.kus_cinsi = kus_cinsi
    
    def ucmak(self):
        print(f'{self.kus_cinsi}, uçtu gitti.')

    def __str__(self):
        return f'Kuş cinsi: {self.kus_cinsi}'

kus1 = Kus('Kuş', 2, 'Papağan')
kus2 = Kus('Kuş', 2, 'Serçe')

print(kus1)
print(kus2)

kus1.ucmak()
kus2.ucmak()