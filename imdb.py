from operator import index
import pandas as pd

df = pd.read_csv("imdb.csv")
result = df
result = df.columns
result = df.info

#İlk 5 kaydı göster
result = df.head(10)
#Son 5 ve 10 kayıt
result = df.tail()
result = df.tail(10)
#Sadece Movie title ve ilk 5 kayıt
result = df["Movie_Title"]
result = df["Movie_Title"].head()
result = df["Movie_Title"].tail()

#Sadece Movie_Title ve Rating ilk ve son 7 kayıt al

result = df[["Movie_Title","Rating"]].head(7)
result = df[["Movie_Title","Rating"]].tail(7)

#Sadece Movie_Title ve Rating içeren ikinci 5 kaydı al

result = df.loc[5:][["Movie_Title","Rating"]].head()
#Sadece Movie_Title ve Rating kolonunu içieren ve imdb puanı 8.0 üstünden olan kayıtlardan ilk 50 tanesi

result = df[df["Rating"] >9.0][["Movie_Title","Rating"]].head(50)


#Yayın tarıhi 2014 ile 2015 araından olan filmlerin isimlerini getiriniz.
result = df[(df["YR_Released"]>=2014) & (df["YR_Released"]<=2015)][["Movie_Title","YR_Released"]].head(50)
#Değerlendirme Sayısı (Num_Reviews) 100.000 'dan büyük ya da imdb puanı 8 ile 9 arası olan filmleri listele

result =df[(df["Num_Reviews"] >= 100000) | ((df["Rating"]>=8) & (df["Rating"] <= 9))][["Movie_Title","Rating","Num_Reviews"]]


print(result)

