import math
from statistics import mean
import numpy as np
#1(10,15,30,45,60) değerlerine sahip bir dizi oluştur

dizi = np.array([10,15,30,45,60])


#5-15 sayıları arasındaki sayılarla numpy dizisi

dizi = np.arange(5,15)

#3 50-100 5'er artırımlı dizi
dizi = np.arange(50,100,5)



#4 10 elemenalı sıfır dizi

dizi = np.zeros(10)
#5 10 elemenalı bir dizi
dizi = np.ones(10)

#0-100 arasında eşit aralıklı 5 sayı

dizi = np.linspace(0,100,5)

# 10-30 arasında rastgele 5 sayı

dizi = np.random.randint(10,30,5)

#-1 1 arası 10 sayı
dizi = np.random.randn(10)

#3*5 boyutlarında 10-50 arası rastgele bir matris
dizi = np.random.randint(10,50,15)
matris = dizi.reshape(3,5)


#Matrisin satır ve sutün sayıları
rowTotal = matris.sum(axis=1)
colTotal = matris.sum(axis=0)

#Matris en büyük en küçük ortalama
result = matris.max()
result = matris.min()
result = matris.mean()


#Matris İndexleri
result = matris.argmax()
result = matris.argmin()

# Matrisin ilk 3 elemanını seç
dizi = np.arange(10,20)
result = dizi[0:3]

#Matrisin elemenlarını tersten yazdır
result = dizi[::-1]

#Matrisin ilk satırını seç

result = matris[0,:]

#Matrisin 2.satır 3.sutün elemanını seç

result = matris[1,2]

#Matrisin tüm satırlardaki ilk elemanı

result = matris[:,0]

#Matrisin her elemanının karesini al

dizi = matris**2

#Matrisin hangisi pozitif çift sayıdır

matris = np.random.randint(-50,50,15).reshape(3,5)
dizi = matris[matris >0]
dizi = dizi[dizi %2 == 0]

print(dizi)
print(matris)

