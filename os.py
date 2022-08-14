import os
import datetime
result=dir(os)
result=os.name

#Dizin Değitirme
# os.chdir('C:\\')
# os.chdir('..')
#Klasör oluşturma
# os.mkdir("Newdirector")
# os.makedirs("newdirectory/yeniklasör")
# os.rename("newdirectory", "yeniklasör")
# os.rmdir("newdirector")
# os.removedirs("yeniklasör/yeniklasör")
#listeleme

# result = os.listdir()
# result=os.listdir("C:\\")

# for dosya in os.listdir():
#     if dosya.endswith('.py'):
#         print(dosya)


#Etkin dizi öğrenme
# result=os.getcwd()


# result = os.stat("os.py")
# result = result.st_size/1024
# result = datetime.datetime.fromtimestamp(result.st_ctime)
# result = datetime.datetime.fromtimestamp(result.st_mtime)


# os.system("notepad.exe")


#PATH

result = os.path.abspath("os.py")
result = os.path.dirname("D:/Dosya/Kodlar/Python/os.py")
result = os.path.dirname(os.path.abspath("os.py"))
result = os.path.exists("D:\Dosya\Kodlar\Python\os1.py")
result = os.path.isdir("D:\Dosya\Kodlar\Python\os.py")
result = os.path.isfile("os.py")
result = os.path.join("C:\\","deneme","deneme1")
result = os.path.split("C:\\deneme")
result = os.path.splitext("os.py")
result = result[1]
print(result)