REKURZIJA VAJE:

def vsota_stevk(n):
    if n <= 0:
        return 0
    else:
        return n % 10 + vsota_stevk(n // 10)

def vsota_vecjih_stevk(n, k=0):
    if n <= 0:
        return 0
    
    s = n % 10
    if s >= k:
        return s + vsota_vecjih_stevk(n // 10, k)
    else:
        return vsota_vecjih_stevk(n // 10, k)
    
def vsota_stevk_stevil_med(m, n):
    #Kdaj se ustavimo? 
    if m > n:
        return 0
    else:
        return vsota_stevk(m) + vsota_stevk_stevil_med(m + 1, n)
    
def najmanjse_stevilo_z_vsoto_stevk(n):
    # 1. Konec: če je n manjši od 10 (od 0 do 9), je odgovor kar n sam:
    if n < 10:
        return n
    
    # 2. Rekurzija: od n odštejemo 9, rešimo za ostanek, 
    # nato pa dobljeno število pomnožimo z 10 in na konec prilepimo 9:
    else:
        return 10 * najmanjse_stevilo_z_vsoto_stevk(n - 9) + 9
    
    
    def vsota_kvadratov_stevk(n):
        enica = n % 10
        desetica = n // 10 % 10
        stotica = n // 100
        return enica ** 2 + destica ** 2 + stotica ** 2
    
    def obrat(n):
        ah aokej stekam tole
        
    def dodaj_kontrolno_stevko(sklic):
    s1 = sklic % 10
    s2 = sklic // 10 % 10
    s3 = sklic // 100 % 10
    s4 = sklic // 1000 % 10
    s5 = sklic // 10000 % 10
    s6 = sklic // 100000 % 10
    s7 = sklic // 1000000 % 10
    s8 = sklic // 10000000 % 10
    s9 = sklic // 100000000 % 10
    s10 = sklic // 1000000000 % 10
    s11 = sklic // 10000000000 % 10
    s12 = sklic // 100000000000 % 10
    vsota = s1 * 2 + s2 * 3 + s3 * 4 + s4 * 5 + s5 * 6 + s6 * 7 + s7 * 8 + s8 * 9 + s9 * 10 + s10 * 11 + s11 * 12 + s12 * 13 
    ostanek = vsoto % 11
    kontrolna = 11 - ostanek 
    if kontrolna < 10:
        return kr moras sestet kontrolno z sklicem
    
def kolikokrat_se_pojavi_stevka(k, n):
    # 1. Konec:
    if n == 0:
        return 0
    
    # 2. Rekurzija:
    zadnja = n % 10
    if zadnja == k:
        return 1 + kolikokrat_se_pojavi_stevka(k, n // 10)
    else:
        return 0 + kolikokrat_se_pojavi_stevka(k, n // 10)
    
    ALI Z NIZEM:
    def kolikokrat_se_pojavi_stevka(k, n):
    return str(n).count(str(k))

def ali_ima_enkratne_stevke(n):
    if n < 10:
        return True
    if kolikokrat_se_pojavi_stevka(n % 10, n) > 1:
        return False
    return ali_ima_enkratne_stevke(n // 10 )

def naslednji_clen(n):
    if n % 2 == 0:
        return n // 2
    else:
        return n * 3 +1
    
def dolzina_zaporedja(n):
    if n == 1:
        return 1
    else:
        return 1 + dolzina_zaporedja(naslednji_clen(n))
    
def najvecji_clen(n):
    if n == 1:
        return 1
    elif n > najvecji_clen(naslednji_clen(n)):
        return n
    else:
        return najvecji_clen(naslednji_clen(n))
    
    if n == 1:
    return 1



Kaj naredi rekurzija?
Primerja trenutni člen ($n$) z največjim členom od vseh naslednjih:
else:
    najvecji_od_naslednjih = najvecji_clen(naslednji_clen(n))
    
    if n > najvecji_od_naslednjih:
        return n
    else:
        return najvecji_od_naslednjih



Točno to zgoraj pa krajše in lepše naredi vgrajena funkcija max(a, b):
def najvecji_clen(n):
    if n == 1:
        return 1
    else:
        return max(n, najvecji_clen(naslednji_clen(n)))
    


def najdaljse_zaporedje(m, n):
    if m == n:
        return dolzina_zaporedja(m)
    else:
        return max(jojjj teh tko ne razumem lih najboljse brez resitev)????????????
    
    
def binomski_izrek(n, k):
    return fakulteta(n) // (fakulteta(k) * fakulteta(n - k))

def stirling(n, k):
    tole si bom jutri malo bolj prebrala
    
    
    
    
    
    
    
    
    
    
    
    VAJE NIZI::::
def ima_samoglasnike(niz):
    samoglasnik = "aeiou"
    
    for crka in niz:
        if crka in samoglasniki:
            return True
    return False

def skoraj_enaka(niz1, niz2):
    if niz1.lower() == niz2.lower():
        return True
    else:
        return False
    
def zamenjaj(niz1, niz2):
    if len(niz1) == 0 or len(niz2) == 0:
        return niz1
    else:
        return niz1[:-1] + niz2[-1]
    
def zlij(niz1, niz2):
    rezultat = ""
    
    dolzina = min(len(niz1), len(niz2))
    for i in range(dolzina):
        rezultat += niz1[i] + niz2[i]
    
    rezultat += niz[dolzina:] + niz2[dolzina:]
    
    return rezultat

def prezrcali(niz):
    return niz[::-1]

def je_palindrom(niz):
    if niz == niz[::-1]:
        return True
    else:
        return False
    


def odstrani_samoglasnike(niz):
    samoglasniki = "aeiouAEIOU"
    
    # Dokler niz ni prazen IN je prva črka samoglasnik:
    while len(niz) > 0 and niz[0] in samoglasniki:
        # Odreži prvo črko stran (vzemi vse od mesta 1 naprej)
        niz = niz[1:]
        
    return niz

def odstrani_samoglasnike(niz):
    samoglasniki = "aeiouAEIOU"
    
    for i in range(len(niz)):
        # Če črka NI samoglasnik, smo našli začetek prave besede!
        if niz[i] not in samoglasniki:
            return niz[i:]  # Vrni vse od tega mesta i naprej
            
    # Če so bili ČISTO VSI znaki samoglasniki (npr. "aaaa"), vrnemo prazen niz:
    return ""

def odstrani_samoglasnike(niz):
    samoglasniki = "aeiouAEIOU"
    
    for i in range(len(niz)):
        if niz[i] not in samoglasniki:
            return niz[i:]
        
    return ""

def obrni_oklepaje(niz):
    nov_niz = ""                 # 1. Pripravimo prazen list
    
    for crka in niz:             # 2. Gremo po vsakem znaku
        if crka == "(":
            nov_niz += ")"       # Odpri postane zapri (prilepimo na list)
        elif crka == ")":
            nov_niz += "("       # Zapri postane odpri (prilepimo na list)
        else:
            nov_niz += crka      # Številke in računske znake pustimo pri miru
        
    return nov_niz               # 3. Na koncu vrnemo CELOTEN nov niz!








ZANKE
def vsota_prvih(n):
    vsota = 0
    
    if i in range(1, n+1):
        vsota += i
    return vsota

def vsota_prvih_kvadratov(n):
    vsota = 0
        
        if i in range(1, n+1):
            vsota += i ** 2
        return vsota
    
def vsota_stevk(n):
    vsota = 0
    for znak in str(n):
        vsota += int(znak)
    return vsota

def vsota_vecjih_stevk(n, k=0):
    vsota = 0
    for znak in str(n):
        stevka = int(znak)  # Spremenimo znak "5" v število 5
        if stevka > k:  # Če mora biti strogo večja (ali stevka >= k, če je večja ali enaka)
            vsota += stevka  # Prištejemo pravo število
    return vsota

def vsota_stevk_stevil_med(m, n):
    vsota = 0
    for i in range(m, n+1):
        vsota += vsota_stevk(i)
    return vsota

def pravilni_del_gesla(geslo, ugibanja):
    niz = ""
    
    for znak in geslo:
        if znak in ugibi:
            niz += znak
        else:
            niz += "_"
    return niz

def nepravilni_ugibi(geslo, ugibanja):
    niz = ""
    
    for znak in geslo:
        if znak not in geslo:
            niz += znak
    return niz

def celostevilski(niz):
    sprehod = 0
    
    for znak in niz:
        if znak == "+":
            sprehod += 1
        elif znak == "-":
            sprehod -= 1
    return sprehod

def ravninski(niz):
    x = 0
    y = 0
    
    for znak in niz:
        if znak == "S":
            y += 1
        elif korak == 'J':
            y -= 1
        elif korak == 'Z':
            x -= 1
        elif korak == 'V':
            x += 1
    return (x, y)

def hitri(tek):
    x = 0
    y = 0
    k = "123456789"
    


1. Različica: Vračanje celotne POTI (seznam vseh točk)
Naloga: Napiši funkcijo pot_sprehoda(niz), ki vrne seznam vseh točk, ki jih obiščemo.
def pot_sprehoda(niz):
    x = 0
    y = 0
    # Začnemo s seznamom, v katerem je že začetna točka (0, 0):
    obiskane_tocke = [(0, 0)]

    for znak in niz:
        if znak == "S":
            y += 1
        elif znak == "J":
            y -= 1
        elif znak == "V":
            x += 1
        elif znak == "Z":
            x -= 1

        # PO VSAKEM KORAKU: novo lokacijo (x, y) dodamo v seznam:
        obiskane_tocke.append((x, y))

    return obiskane_tocke


Razlaga: Za niz "SV" bo funkcija vrnila: [(0, 0), (0, 1), (1, 1)] (vse postaje na poti).


2. Različica: Razdalja od začetka do konca
Naloga: Napiši funkcijo razdalja(niz), ki izračuna, koliko korakov (zračna razdalja) smo oddaljeni od izhodišča $(0, 0)$.
def razdalja(niz):
    x = 0
    y = 0

    for znak in niz:
        if znak == "S":
            y += 1
        elif znak == "J":
            y -= 1
        elif znak == "V":
            x += 1
        elif znak == "Z":
            x -= 1

    # Na koncu izračunamo razdaljo s Pitagorovim izrekom: sqrt(x^2 + y^2)
    # V Pythonu koren naredimo s potenco ** 0.5:
    zracna_razdalja = (x**2 + y**2) ** 0.5
    return zracna_razdalja


3. Različica: Omejeno gibanje (stene / soba velikosti $0$ do $5$)
Naloga: Figurica se premika po sobi od $(0,0)$ do $(5,5)$. Če pride do stene, se ne more več premakniti v tisto smer (ostane na mestu).
def v_sobi(niz):
    x = 0
    y = 0

    for znak in niz:
        # Gremo gor samo, če smo še pod zgornjim robom (y < 5):
        if znak == "S" and y < 5:
            y += 1
        # Gremo dol samo, če smo nad spodnjim robom (y > 0):
        elif znak == "J" and y > 0:
            y -= 1
        # Gremo desno samo, če smo levo od desne stene (x < 5):
        elif znak == "V" and x < 5:
            x += 1
        # Gremo levo samo, če smo desno od leve stene (x > 0):
        elif znak == "Z" and x > 0:
            x -= 1

    return (x, y)


4. Različica: Vprašanje “Ali smo se vrnili na začetek?”
Naloga: Napiši funkcijo je_krog(niz), ki vrne True, če sprehod končamo točno tam, kjer smo začeli (v $(0, 0)$), sicer pa vrne False.
def je_krog(niz):
    x = 0
    y = 0

    for znak in niz:
        if znak == "S":
            y += 1
        elif znak == "J":
            y -= 1
        elif znak == "V":
            x += 1
        elif znak == "Z":
            x -= 1

    # Preverimo, ali sta obe koordinati spet enaki 0:
    if x == 0 and y == 0:
        return True
    else:
        return False
    

def naslednji_clen(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3*n + 1

def dolzina_zaporedja(n):
    dolzina = 1  # 1. Začnemo z 1 (začetni člen)

    while n != 1:  # 2. Dokler n ni prišel do 1:
        n = naslednji_clen(n)  # Izračunamo nov člen in posodobimo n
        dolzina += 1  # Povečamo dolžino za 1

    return dolzina  # 3. Ko je n prišel do 1, vrnemo dolžino




SEZNAMI IN NABORI:
def vecji_element(seznam, stevilo):
    for element in seznam:
        if element > stevilo
        return True
    return False

def prvi_najvecji(sez):
    for x in sez:
        if x > sez[0]:
            return False
    return True

def vsi_vecji(sez1, sez2):
    for a in sez1:
        for b in sez2:
            if a < b:
                return False
    return True

def porezani_podseznami(sez):
    nov = []
    # Zanka gre od 0 do len(sez), vključno z len(sez)
    for i in range(len(sez) + 1):
        nov.append(sez[i:])
    return nov

def najvecji_element(sez):
    if sez == []:
        return None
    najvecji_element = sez[0]
    for element in sez:
        if najvecji_element < element:
            najvecji_element = element
    return element #vedno izven zanke kr cene prvic ko najde tam element konca
    
    
def zdruzi_sezname(sez):
    seznam = [] 
        for s in sez: 
            seznam +=s 
        return seznam
 
   
   
def identicna(n):
    matrika = []
    
    for i in range(n):
        vrstica = []
        for j in range(n):
            if i == j:
                vrstica.append(1)
            else:
                vrstica.append(0)
        matrika.append(vrstica)
    return matrika


def sled_matrike(mat):
    vsota = 0
    for i in range(len(mat)):
        vsota += mat[i][i]
        return vsota

def pripravi_primer(sez1, sez2):
    seznam = []
    
    for i in range(len(sez1)):
        seznam.append((sez1[i], sez2[i]))
    return seznam


SLOVARJI IN MNOZICE:
    
def nakupovalni_seznam(sladkosnedi, gosti):
    rezultat = {}
    
    for gost in gostje:
        if gost in sladkosnedi:
            sladica = sladkosned[gost]
            
            if sladica in rezultat:
                rezultat[sladica] += 1
            else:
                rezultat[sladica] = 1
    return rezultat

def pomnozi(recept, faktor):
    nov_recept = {}
    
    for sestavine in recept:
        nov_recept[sestavine] = recept[sestavine] * faktor
    return nov_recept

def ali_imamo_sestavine(recept, shramba):

    for sestavina in recept:
        if sestavina not in shramba:
            return False 
        if shramba[sestavina] < recept[sestavina]:
            return False
    return True
          
def kaj_moramo_se_kupiti(recept, shramba):
    spisek = {}
    
    for sestavina in recept:
        if recept[sestavina] > shramba[sestavina]:
            spisek[sestavina] = recept[sestavina] - shramba[sestavina]
    return spisek

##tukaj manjka kaj ce u shrambi ni napisano!!!!

def sifriraj(nasa_sifra, beseda):
    rezultat = ""
    for crka in beseda:
        rezultat += nasa_sifra[crke]
    return rezultat

def slika(permutacija, x):
    return permutacija[x]

def narcisoidi(slovar):
    narcisi = set()
    for oseba in slovar:
        if oseba == slovar[oseba]:
            narcisi.add(oseba)
    return narcisi

class ImeRazreda:

    # 1. KORAK: ROJSTVO (Nastavi začetne lastnosti / predalčke)
    def __init__(self, lastnost1, lastnost2=privzeta_vrednost):
        self.lastnost1 = lastnost1
        self.lastnost2 = lastnost2

    # 2. KORAK: LEP IZPIS ZA ČLOVEKA (ko napišeš print(objekt))
    def __str__(self):
        return f"Opis objekta: {self.lastnost1}"

    # 3. KORAK: TEHNIČNI IZPIS ZA PYTHON
    def __repr__(self):
        return f"ImeRazreda({self.lastnost1}, {self.lastnost2})"

    # 4. KORAK: DEJANJA / METODE (Kaj ta objekt zna narediti?)
    def naredi_nekaj(self, sprememba):
        self.lastnost1 += sprememba
        return self.lastnost1
    
    
    DATOTEKEEE:
    1. Branje datotek (Recepti)
Pri branju datotek skoraj vedno uporabimo blok with open(...) as ..., saj ta poskrbi, da se datoteka po branju samodejno zapre.


Recept 1: Branje vrstico za vrstico (najpogostejši vzorec)
Uporabno, ko želimo predelati vsako vrstico posebej (npr. prešteti besede, poiskati določene podatke).
with open('datoteka.txt', encoding='UTF-8') as dat:
    for vrstica in dat:
        vrstica = vrstica.strip()  # .strip() odstrani odvečne presledke in znak za novo vrstico (\n)
        # tukaj obdelamo vrstico



Recept 2: Branje celotne vsebine naenkrat v en sam niz
Uporabno, ko je datoteka majhna ali želimo iskati vzorce po celotnem besedilu.
with open('datoteka.txt', encoding='UTF-8') as dat:
    vsebina = dat.read()



Recept 3: Branje vseh vrstic v seznam nizov
with open('datoteka.txt', encoding='UTF-8') as dat:
    vrstice = dat.readlines()  # vrne seznam, npr. ['prva\n', 'druga\n']




2. Pisanje v datoteke (Recepti)
Pri odpiranju za pisanje določimo način delovanja:


'w' (write): ustvari novo datoteko ali popolnoma prepiše obstoječo.


'a' (append): ohrani staro vsebino in doda novo na konec datoteke.


Recept 1: Pisanje z metodo .write()
Pozor: .write() ne doda nove vrstice samodejno, zato moramo sami dodati \n.
with open('izhod.txt', 'w', encoding='UTF-8') as dat:
    dat.write('Prva vrstica\n')
    dat.write('Druga vrstica\n')



Recept 2: Pisanje s funkcijo print(..., file=...)
print samodejno doda novo vrstico na koncu.
with open('izhod.txt', 'w', encoding='UTF-8') as dat:
    print('Prva vrstica', file=dat)
    print('Druga vrstica', file=dat)




3. Delo z mapami in potmi (os in os.path)
Knjižnica os omogoča premikanje po mapah in urejanje datotek, os.path pa manipulacijo z imeni poti.


Sestavljanje poti (zelo pomembno za združljivost med Windows in Linux):
import os
pot = os.path.join('mapa', 'podmapa', 'datoteka.txt')



Pregledovanje vsebine mape:
vse_datoteke = os.listdir('ime_mape')  # vrne seznam imen v mapi



Preverjanje obstoja in tipa:

os.path.exists(pot) $\rightarrow$ Ali datoteka/mapa sploh obstaja? (True/False)
os.path.isdir(pot) $\rightarrow$ Ali je to mapa? (True/False)
os.path.isfile(pot) $\rightarrow$ Ali je to datoteka? (True/False)



Razbijanje poti na dele:

os.path.splitext('pot/film.mp4') $\rightarrow$ ('pot/film', '.mp4') (loči ime in končnico)
os.path.split('pot/film.mp4') $\rightarrow$ ('pot', 'film.mp4') (loči mapo in ime datoteke)
os.path.basename('pot/film.mp4') $\rightarrow$ 'film.mp4'



Ustvarjanje in brisanje map/datotek:

os.makedirs('mapa1/mapa2', exist_ok=True) $\rightarrow$ ustvari mapo in vse vmesne podmape.
os.remove('datoteka.txt') $\rightarrow$ izbriše datoteko.
os.rmdir('prazna_mapa') $\rightarrow$ izbriše prazno mapo.




4. Delo z JSON datotekami (json)
JSON je standarden format za shranjevanje strukturiranih podatkov (seznamov, slovarjev, števil, nizov).


Razlika med funkcijami z s in brez s:

Brez s (load, dump): delata neposredno z datoteko (file object).
Z s (loads, dumps): delata z nizom (string).



Recept 1: Branje JSON datoteke v Python podatke
import json

with open('podatki.json', encoding='UTF-8') as dat:
    podatki = json.load(dat)  # podatki postanejo običajen Pythonov slovar ali seznam



Recept 2: Pisanje Python podatkov v JSON datoteko
import json

podatki = {'ime': 'Ana', 'ocene': [10, 9, 10]}

with open('podatki.json', 'w', encoding='UTF-8') as dat:
    json.dump(podatki, dat, ensure_ascii=False, indent=4)
    # ensure_ascii=False ohrani šumnike (č, š, ž)
    # indent=4 poskrbi za lep in berljiv izpis z zamiki




Pripravljen sem na vaše naloge! Prilepite jih, pa bova za vsako definirala natančen postopek in rešitev.  