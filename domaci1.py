'''
Domaci 1 Django

'''
from bs4 import BeautifulSoup
import requests

page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
soup = BeautifulSoup(page.content, 'html.parser')

f = open("./primjer.html","w")
f.write(soup.prettify())
f.close()

class Knjiga:
    '''
    Klasa Knjiga

    '''
    def __init__(self, naslov, zanr, autor, cijena=0):
        self.naslov = naslov
        self.zanr = zanr
        self.autor = autor
        self.__cijena = cijena

    def get_naslov(self):
        '''
        getter naslova
        '''
        return self.naslov

    def get_cijena(self, kolicina):
        '''
        getter cijene u zavisnosti od kolicine
        '''
        return self.__cijena*kolicina
    def set_cijena(self, popust):
        '''
        setter cijene
        '''
        self.__cijena = self.__cijena - self.__cijena*popust/100
class Poezija(Knjiga):
    '''
    Klasa Poezija nasljedjuje klasu Knjiga
    '''
    #pylint: disable=too-many-arguments
    def __init__(self, naslov, zanr, autor, cijena, br_pjesama):
        super().__init__(naslov, zanr, autor, cijena)
        self.br_pjesama = br_pjesama

knjiga1 = Knjiga("Nepodnosljiva lakoca postojanja", "Filozofska fikcija", "Milan Kundera", 10)
knjiga2 = Knjiga("Proces", "Filozofska fikcija", "Franc Kafka")
print(knjiga1.get_naslov())
print(knjiga1.get_cijena(5))
print(knjiga2.get_cijena(1))
knjiga1.set_cijena(20)
print(knjiga1.get_cijena(1))
zbirka = Poezija("Lirika Itake", "Lirska poezija", "Milos Crnjanski", 5, 48)
print(zbirka.get_naslov())




knjige=[]
update_knjige=[]
taster=input("Da li želite da unesete nove knjige? Pritisnite 1 ako da, 0 ako ne. \n")
while taster=='1':
    nova_knjiga=input("Unesite knjigu, i to naziv, zanr, autora, cijenu\n ")
    update_knjige.append(nova_knjiga)
    taster=input("Da li želite da unesete još knjiga? Pritisnite 1 ako da, 0 ako ne. \n")
    if taster=='0':
        break

f = open("./knjige.txt","a")
for linija in update_knjige:
    f.write("\n")
    f.write(linija)
f.close()


f = open("./knjige.txt")
for line in f:
    line1 = line.split('\n')
    knjige.append(line1[0].split(", "))
f.close()
print(knjige)

knjige_klase = []
for i in knjige:
    knjige_klase.append(Knjiga(*i))

print(knjige_klase[1].get_cijena(1))
