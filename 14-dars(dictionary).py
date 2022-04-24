# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 10:36:29 2022

@author: User
"""
car_0={'model':'opel',"rang":"oq"}
#print(car_0['model'])
#print(car_0['rang'])

en_uz={'apple':'olma',"key":'kalit',"apricot":"shaftoli"}
#print(en_uz["apple"])

mevalar = {"olma":10000,"kon":8000,'gilos':15000}
#print(f"olma narhi {mevalar ['olma'] }so'm")

#lug'atlarda istalgan ma'lumot turlarini saqlash mumkin
talaba_0={"ism":"Shavkatjonov Hikmatullo","yosh":"24","yil":"1998"}
#print(f"{talaba_0['ism'].title()},\
# {talaba_0['yosh']} yoshda,\
#{talaba_0['yil']}da tug'ilgan.")

# yangi kalit so'z va qiymat qo'shish
talaba_0['kurs']=1
talaba_0["yo'nalish"]="texnologik ta'lim"
talaba_0['ism']='Abdulloh'

#bo'sh ro'yhat
# talaba_1={}   
#print(talaba_1)
#print(f"{talaba_1['ism'].title()},\
#{talaba_1 ['kurs']} - kurs,\
#talaba_1['yosh']} yoshda")

#qiymatni yangilash
#talaba_1['kurs']=4
#print(f"Talaba {talaba_1['ism'].title()},\
#{talaba_1['kurs']} -kursda o'qiydi,\
#{talaba_1['yosh']} yoshda")


# kalit so'z-qiymat ni o'chirib tashlash
talaba_0={"ism":'shavkatjonov hikmatulloh',"yosh":24,"yil":1998}
del talaba_0['yosh']
#print(talaba_0)
# print(en_uz)

#lug'atlarni bir nechta qatorda yozish
telefonlar={'ali':'redmi 8',
            'vali':'iphone 11 pro',
            'kozim':'nokia 1200',
            'bobur':'maxi'}

# get metodi
phone=telefonlar['ali']
# print(f'alining telefoni {phone} telefoni')
phone = telefonlar.get('ali')
# print(phone)
phone=telefonlar.get("hasan",'bunday ism mavjud emas')
# print(phone)
phone=telefonlar.get('hasan')
print(phone)




            

