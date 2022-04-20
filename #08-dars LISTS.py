#08-DARS LISTS
# SANA: 02/04/2022
# MUALLIF:HIKMATULLO

#RO'YHATNI KESISH 

#TARTIBLASH 
#cars.sort() # bu alifbo tartibida tartiblash
# cars.sort(reverse = True) teskari tartibda tartiblash

#SORTED()
# print(sorted(cars)) asl royhatda tegmasdan tartiblash
#print(sorted(cars,reverse = True)) asl royhatga tegmasdan teskari tartibda tartiblash

#ROYHATNI ORTIDAN BOSHLAB CHIQARISH
# cars.reverse() royhatni oxiridan boshiga ozgartirish

#ROYHAT UZUNLIGI
#len(cars)

#RANGE()
#sonlar= list(range(0,10))
# print(sonlar)

#RANGE VA QADAM
#toq_sonlar = list(range(1,20,2)) 1dan 20gacha 2qadam tashlab chiqardi
#juft_sonlar = list(range(2,20,2)) 2dan 20gacha 2 qadam tashlandi

#MIN(), MAX(),SUM()
#narhlar = [2200, 1300, 3400, 5600, 4500]
#arzon = min(narhlar)
#qimmat = max(narhlar)
#jami = sum(narhlar)
#print("eng arzon narx", arzon, "eng qimmat narx", qimmat, "jami narx esa", jami)

#ROYHATNI KESISH
cars = ["bmw","tesla","chevrolet", "opel", 'honda','hyundai','ravon']
#print(cars[2:5])# 2chi elematdan boshlab 4gacha
#print(cars[:4])# 0 dan boshlab uchgacha
#print(cars[2:])# 2dan boshlab oxirigacha
my_cars = cars
#print(my_cars.remove("tesla"))
#print(cars.append('tesla'))
#print(cars)

#RO'YHATDAN NUSXA OLISH
my_cars = cars[:]
#print(my_cars.remove("tesla"))
#print(my_cars)
#print(cars)
my_cars[0]="lacetti"

#TUPLE
toys = ("horse",'snake','cow','lizard',"bear",'rabbit',"wolf")
#print(toys[-2])
#toys[0]="car"
#toys.append("car")
#toys.remove("bear")
#print(type(toys))
toys = list(toys)
#print(type(toys))
toys.append("teddy")
#print(toys)
toys = tuple(toys)
#print(type(toys))

#amaliyot
#davlat= ['aqsh','uzbekistan','senegal','polsha']

