# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 07:20:01 2022

@author: User
"""
talaba_0={'ism':'hikmatullo',
          'familya':'shavkatjonov',
          'yosh':24,
          'fakultet':'texnologik ta\'lim',
          'kurs':1
          }
#print(talaba_0)
# print(talaba_0.items())
# for kalit,qiymat in talaba_0.items():
#     print(f'Kalit:{kalit}')
#     print(f'Qiymat:{qiymat}')

telefonlar={'anvar':'iphone x',
            'bobur':'artel',
             'o\'zim':'red mi 9',
             'sen':'samsung s9',
             'ukam':'artel',
             'akam':'red mi 9'}
# for k,q in telefonlar.items():
#     print(f'{k.title()}ning telefoni {q}')
# #mahsulotlar={'anjir':25000,
#              'nok':15000,
#              'shaftoli':20000,
#              'olma':10000}
# print(mahsulotlar.keys())
# print(f'Do\'kondagi mahsulotlar:')
# # 1chi usul for mahsulot in mahsulotlar.keys():
# #     print(mahsulot.title())

# for mahsulot in mahsulotlar:
#     print(mahsulot.title())

# bozorlik=['anor','uzum','nok','olma']
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f'{mahsulot.title()} {mahsulotlar [mahsulot]} so\'m')
# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f'iltimos , do\'koningizga shu {buyum}ni ham olib kelsangiz')

#lug'at elementlarini tartib bilan chiqarish
# print("do'konimizdagi mahsulotlar:")
# for mahsulot in sorted(mahsulotlar):
#     print(mahsulot.title())
# print(mahsulotlar.keys())  

# .values()
#print(telefonlar.values())   
print('o\'rtoqlarim ushbu telefonlardan foydalanishadi:')
# for tel in telefonlar.values():
#     print(tel)

# set metodi
for tel in set(telefonlar.values()):
    print(tel)
toys={"car", "Bear", "car", "lamp", "ball", "lamp"} #takrorlangan elementlarni faqat bittasini chiqaradi
print(toys)