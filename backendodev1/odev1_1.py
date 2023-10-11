import random
secenek = random.choice(('tas', 'kagit', 'makas'))
print(f'Bilgisayarın seçimi: {secenek}')

userChoice = int(input('Taş için 1, Kağıt için 2, Makas için 3 yazınız: '))

if userChoice == 1:
    userChoice = 'tas'
elif userChoice == 2:
    userChoice = 'kagit'
elif userChoice == 3:
    userChoice = 'makas'
else:
    print('Lütfen geçerli bir değer giriniz')

print(f'Kullanıcının seçimi: {userChoice}')


if userChoice == secenek:
    print('Berabere')
elif userChoice == 'tas' and secenek == 'makas':
    print('Kazandınız.')
elif userChoice == 'tas' and secenek == 'kagit':
    print('Kaybettiniz')
elif userChoice == 'makas' and secenek == 'kagit':
    print('Kazandınız.')
elif userChoice == 'makas' and secenek == 'tas':
    print('Kaybettiniz.')
elif userChoice == 'kagit' and secenek == 'tas':
    print('Kazandınız.')
elif userChoice == 'kagit' and secenek == 'makas':
    print('Kaybettiniz.')
else:
    print('Hata alındı.')