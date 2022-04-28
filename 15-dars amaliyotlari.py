# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 13:09:40 2022

@author: User
"""
# lugat={"integer":"butun son",
#        "float":"o\'nlik son",
#        "for":"uchun",
#        "if":"agar",
#        "else":"unday bo'lmasa",
#        "print":"konsolga chiqarish",
#        "set":"elementlardan faqat bittsini chiqaradi",
#        "keys":"kalitlar",
#        "values":"qiyamtlar",
#        "dictionary":"lug'at"}
# for key,value in sorted(lugat.items()):
 #   print(f"{key.title()} - {value}")
davlat={"uzbekistan":"tashkent",
        "russia":"moscow",
        "india":"dekhli",
        "ukraina":"kiev",
        "BAA":"dubai",
        "katar":"doha",
        "egypt":"qohira"}
# print("dunyo davlatlari:")
# for key in sorted(davlat):
#     print(key.title())

# print("davlatlarning poytaxtlari:")
# for poytaxt in sorted(davlat.values()):
    # print(poytaxt.title())
# country=input("qaysi davlatni poytaxtini bilishni hohlaysiz?:")
# poytaxt=davlat.get(country)
# if poytaxt in davlat:
#     print(f"kechirasiz, bizda bunday davlat turi yo'q")
# else:
#  print(f"{country.upper()}ning poytaxti {poytaxt.title()} shahri")
 
taomlar={"osh":15000,
         "shashlik":10000,
         "sho'rva":8000,
         "mastava":12000,
         "do'lma":18000,
         "monti":6000,
         "somsa":5000,} 
print("qanday 3 xil taom buyurtma berasz?:")
buyurtmalar=[]
for n in range(3):
    buyurtmalar.append(input(f"{n+1}-taom:"))

for buyurtma in buyurtmalar:
   if  buyurtma in taomlar:
        print(f"{buyurtma.title()}={taomlar[buyurtma]} so'm")
   else:
        print(f"Kechirasiz, bizda {buyurtma} yo'q.")