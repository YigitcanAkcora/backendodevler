# sayilar = [1,2,3,4,20]

# print(max(sayilar))

# quiz notları kullanıcıdan input ile alalım
# for ile max kullanmadan max bulma

notlar = input('Notlar: ').split()

i = 0
while i < len(notlar):
    notlar[i] = int(notlar[i])
    i += 1

max_deger = 0

skor = 0
while skor < len(notlar):
    if notlar[skor] > max_deger:
        max_deger = notlar[skor]
    skor += 1


print(max_deger)





""" quiz_notlari = []  

for i in range(4):
    score = float(input(f"{i+1}. quiz notunu girin: ")) 
    quiz_notlari.append(score)  

maksimum_not = quiz_notlari[0]  

for score in quiz_notlari:
    if score > maksimum_not:
        maksimum_not = score            
        

print(f"En yüksek quiz notu: {maksimum_not}") """