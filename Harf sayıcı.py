cumle = input("Lütfen cümleyi yazınız: ")
harf = input("Hangi harfi saymak istiyorsunuz? ")
sayac = 0

for x in cumle:
    if x == harf:
        sayac += 1

print(sayac)