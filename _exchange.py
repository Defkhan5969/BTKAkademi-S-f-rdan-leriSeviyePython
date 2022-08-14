import requests
import json

api_url="https://api.exchangeratesapi.io/latest?base="
bozulan_doviz=input("Bozulan döviz türü: ")
alınan_döviz=input("Alınan döviz türü: ")
miktar=int(input(f"Ne kadar {bozulan_doviz} bozdurmak istiyorsunuz?"))


result = requests.get(api_url+bozulan_doviz)

result = json.loads(result.text)

print("1 {0} = {1} {2}".format(bozulan_doviz,result["rates"][alınan_döviz],alınan_döviz))
print("{0} {1} = {3}".format(miktar,bozulan_doviz,miktar*result["rates"][alınan_döviz],alınan_döviz))