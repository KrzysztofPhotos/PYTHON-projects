lines = []
with open("instrukcje.txt", encoding='UTF-8') as f:
    for line in f:
        lines.append(line.strip())

moj_napis = []
for i in lines:
    z = i.split()
    if z[0] == "DOPISZ":
        moj_napis.append(str(z[1]))
    elif z[0] == "USUN":
        moj_napis.pop()
    elif z[0] == "ZMIEN":
        moj_napis.pop()
        moj_napis.append(str(z[1]))
    elif z[0] == "PRZESUN":
        zmienna = 0
        while moj_napis[zmienna] != z[1]:
            zmienna += 1
        if ord(z[1])+1 > 90:
            nowa_liczba = chr(ord(z[1]) + 1 - 26)
        else:
            nowa_liczba = chr(ord(z[1])+1)
        moj_napis[zmienna] = nowa_liczba

wynik_koncowy = ""
for i in moj_napis:
    wynik_koncowy += i

dlugosc = len(wynik_koncowy)

#4.2
licznik = 1
save = 0
przewaga = ""
sam_poczatek_lista = []
for i in lines:
    rozdzielone = i.split()
    sam_poczatek_lista.append(rozdzielone[0])

for i in range(len(sam_poczatek_lista)-1):
    if sam_poczatek_lista[i] == sam_poczatek_lista[i+1]:
        # dwa takie same obok siebie
        licznik += 1
        if licznik > save:
            przewaga = sam_poczatek_lista[i]
            save = licznik
    else:
        # dwa różne obok siebie zatem zeruj
        licznik = 1

tablica = []
for i in lines:
    rozdzielone = i.split()
    if rozdzielone[0] == "DOPISZ":
        tablica.append(rozdzielone[1])

tablica.sort()
top_count = 0
top = ''
for i in range(26):
    alfabet = chr(int(i+65))
    if tablica.count(alfabet) > top_count:
        top = alfabet
        top_count = tablica.count(alfabet)

s = open('wynik4.txt', 'w')
s.write("4.1 " + str(dlugosc))
s.write("\n4.2 " + str(przewaga) + " " + str(save))
s.write("\n4.3 " + str(top) + " " + str(top_count))
s.write("\n4.4 " + str(wynik_koncowy))