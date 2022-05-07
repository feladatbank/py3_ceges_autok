"""
nap,ora:perc,rendszam,személy azonosítója,km számláló ,ki/be hajtás 
1 08:45 CEG306 501 23989 0
1 09:04 CEG304 583 8477 0
1 11:37 CEG302 500 25385 0
1 12:02 CEG308 586 26496 0
"""

"""
                  Céges autók            (18 pont)
{{{{ Az osztály használata nem KÖTELEZŐ DE több pontot kaphat érte!!! }}}}
ÜGYELJEN arra hogy az autok.txt fálj beolvasásánál van fejléc!!!
nap,ora:perc,rendszam,személy azonosítója,km számláló ,ki/be hajtás

A parkolóból kihajtáskor 0,
A behajtáskor 1

1. A feladat megoldásához hozzon létre grafikus vagy konzolalkalmazást (projektet)
ceges_auto azonosítóval!

2. Hozzon létre egy osztályt (class), ami reprezentálja az adatok példányait (object isntance). Az osztály konstruktora (constructor) paraméterként kapjon meg egy beolvasott sort, és ebből határozza meg meg az adott attribútumokat (property). Az osztály használata nem KÖTELEZŐ DE több pontot kaphat érte!!! 

Olvassa be a autok.txt állományban található adatokat és tárolja el adatokat egy homogén listába, amely használatával a további feladatok megoldhatók! A terminálra való kiírás legyen a mintának megfelelő! 

3. Határozza meg és írja ki a képernyőre a minta szerint, hogy az állomány hány adatsort tartalmaz!

4. Kérjen be egy napot és írja kiaképernyőreaminta szerint,hogy mely autókat vitték ki (0) és hozták be (1) az adott napon!

5. Határozza meg a hogy mennyi a legnagyobb megtett távolság és rendelje hozzá annak az autónak a rendszámát.

Minta / Output: _______________________________________________________

3.feladat: 294 db.
4. Feladat
Kérek egy napot: 4
Forgalom a(z) 4. napon:
 12:50 CEG303 561 0
 19:17 CEG308 552 1
5. feladat: A legtöbb távot megtevő autó rendszáma: CEG300, 
                                  Amennyit megtett: 36060km

_______________________________________________________________________
"""
#1-2. feladat
class Ceges:
  def __init__(self,sor):
    nap,ora_perc,rendszam,szemelyi,km_szamlalo,ki_be = sor.strip().split(" ")
    self.nap         = int(nap)
    self.ora_perc    = ora_perc
    self.rendszam    = rendszam
    self.szemelyi    = int(szemelyi)
    self.km_szamlalo = int(km_szamlalo)
    self.ki_be       = int(ki_be)
with open("autok.txt","r",encoding="utf-8") as f:
  f.readline()
  lista = [Ceges(sor) for sor in f]
#3. feladat
print(f"3.feladat: {len(lista)} db.")

#4. feladat
print("4. Feladat")
bekeres = int(input("Kérek egy napot: "))

ki = [sor for sor in lista if sor.nap == bekeres]
print(f"Forgalom a(z) {bekeres}. napon:")
[print(f" {sor.ora_perc} {sor.rendszam} {sor.szemelyi} {sor.ki_be}") for sor in ki]



#5. feladat


nagy = 0
rendszam = ""
for sor in lista:
  if sor.km_szamlalo > nagy:
    nagy = sor.km_szamlalo
    rendszam = sor.rendszam
print(f"""5. feladat: A legtöbb távot megtevő autó rendszáma: {rendszam}, 
                                  Amennyit megtett: {nagy}km""")






























