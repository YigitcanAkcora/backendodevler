bakiye = 0

while(True):
    secim = int(input('Bakiye sorgulama için 1, Para çekme için 2, Para Yatırma için 3, ATM den çıkmak için 4 yazın:  '))
    if secim == 1:
        print(f'Bakiyeniz = {bakiye}')
    elif secim == 2:
        cekim = int(input('Çekeceğiniz miktarı yazınız: '))
        if bakiye >= cekim:
            bakiye -= cekim
        else:
            print('Çekecek yeterli bakiyeniz yok')
    elif secim == 3:
        yatir = int(input('Yatıracağınız miktarı yazınız: '))
        bakiye += yatir
    elif secim == 4:
        break
    else:
        print('Hata alındı')