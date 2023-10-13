x = 0
while x <= 10:
    print(x)
    x += 1


# 1'den 101'e kadar bütün sayıların toplamını

toplam = 0

y = 0
while y <= 100:

    toplam += y
    y += 1

print(toplam) # 5050

# Kullanıcadan 0 - 1000 çift sayıların toplamı

cift_toplam = 0

kullanici_deger = int(input('0 - 1000: '))

z = 0

while z <= kullanici_deger + 1:
    if z % 2 == 0:
        cift_toplam += z
    z += 1

print(cift_toplam)

# fizzbuzz

i = 0

while i <= 100:
    if i % 3 == 0 and i % 5 == 0:
        print('fizzbuz')
    elif i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('buzz')
    else:
        print(i)
    i += 1


