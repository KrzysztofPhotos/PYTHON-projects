def isprime(num):
    if num < 2:
        return False
    i = 2
    while i <= num:
        if num % i == 0:
            return False
        return True

file = open("punkty.txt",   'r')
Lines = file.readlines()

obieliczbypierwsze = 0
krawedz = 0
wewnatrz = 0
zewnatrz = 0

count = 0
for line in Lines:
    count += 1
    tablica = line.split(" ", 1)
    tablica[1] = tablica[1].replace('\n', '').replace('r', '')

    x = tablica[0]
    y = tablica[1]

    # 4.1
    if isprime(int(x)) and isprime(int(y)):
        obieliczbypierwsze += 1

    # 4.2


    # 4.4
    if int(x) == -5000 or int(x) == 5000 and -5000 <= int(y) <= 5000:
        krawedz += 1
    elif int(y) == -5000 or int(y) == 5000 and -5000 <= int(x) <= 5000:
        krawedz += 1
    elif 5000 > int(x) > -5000 and 5000 > int(y) > -5000:
        wewnatrz += 1
    else:
        zewnatrz += 1

print('obie liczby sa pierwsze: ' + str(obieliczbypierwsze))
print('na zewnatrz ' + str(zewnatrz))
print('wewnatrz: ' + str(wewnatrz))
print('krawedz: ' + str(krawedz))
