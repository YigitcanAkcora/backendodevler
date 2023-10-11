 # Tas, kagit, makas

import random






userScore = 0
botScore= 0

while(True):
    print(f'Kullanıcı skoru = {userScore}')
    print(f'Botun skoru = {botScore}')
    kullanici = input('Taş, kağit ya da makas ? ')
    bot = random.choice(('tas', 'kagit', 'makas'))
    print(f'Botun secimi = {bot}')
    if kullanici == 'makas' and bot == 'makas':
        print('berabere')

    elif kullanici == 'kagit' and bot == 'kagit':
        print('berabere')

    elif kullanici == 'tas' and bot == 'tas':
        print('berabere')

    elif kullanici == 'makas' and bot == 'kagit':
        print('kullanici kazandi')
        userScore += 1

    elif kullanici == 'kagit' and bot == 'tas':
        print('kullanici kazandi')
        userScore += 1

    elif kullanici == 'tas' and bot == 'makas':
        print('kullanicim kazandi')
        userScore += 1

    elif bot == 'tas' and kullanici == 'makas':
        print('bot kazandi')
        botScore += 1

    elif bot == 'makas' and kullanici == 'kagit':
        print('bot kazandi')
        botScore += 1

    elif bot == 'kagit' and kullanici == 'tas':
        print('bot kazandi')
        botScore += 1

    else:
        print('yanliş değer girdiniz')
    if userScore >= 3:
        print('Maçı kullanıcı kazandı.')
        break
    elif botScore >= 3:
        print('Maçı bot kazandı.')
        break