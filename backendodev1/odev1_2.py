kilo = int(input('Kilonuzu giriniz:(kg) '))
boy = float(input('Boyunuzu giriniz:(m) '))

print(f'{kilo}kg')
print(f'{boy}m')

endeks = kilo / (boy * boy)

print(f'Beden kitle endeksiniz = {endeks}')

if endeks < 18.5:
    print('Düşük Kilolu')
elif endeks >= 18.5 and endeks <= 24.99:
    print('Normal Kilo')
elif endeks > 24.99 and endeks <= 29.99:
    print('Fazla Kilolu')
elif endeks > 29.99:
    print('Obez')
else:
    print('Hata alındı')
