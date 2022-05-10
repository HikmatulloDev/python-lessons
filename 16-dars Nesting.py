# -*- coding: utf-8 -*-



 #lugatlar ro\'yhati

# car0={"model":'lacetti',
#       'rang':'qora',
#       'yil':'2020',
#       'narh':'11000',
#       'km':'80000',
#       'korobka':'mexanika'}

# car1={"model":"spark",
#       "yil":"2022",
#       "rang":"oq",
#       "narh":"8000",
#       "km":"50000",
#       "korobka":"avtomat"}

# car2={"model":"matiz",
#       "yil":"2015",
#       "rang":"qizil",
#       "narh":"5600",
#       "km":"15000",
#       "korobka":"mexanika"}
# cars=[car0,car1,car2]
# for car in cars:
#     print(f"{car['model'].title()},\n"
#       f"{car['yil']}-yil, {car['narh']}$, {car['rang']} rang,"
#       f"{car['km']}km yurgan,\n"
#       f"{car['korobka']}\n")

# print(f"{cars[2]['model'].title()}  "
#       f"{cars[2]['narh']}")
# teslas=[]
# for t in range(10):
#     new_car={'model':'tesla',
#          'km':0,
#          'narh':'None',
#          "rang":"None",
#          "yil":"2022",
#          "korobka":"avtomat"}
#     teslas.append(new_car)
# for tesla in teslas[:3]:
#    tesla['rang']='qora'    
# #for tesla in teslas:
# #    print(tesla)
# for tesla in teslas[3:6]:
#   tesla['rang']='qizil'
# for tesla in teslas[6:]:
#     tesla['rang']='oq'
#     tesla['korobka']='mexanika'
# #for tesla in teslas:
# # print(tesla)  
# for tesla in teslas:
#     if tesla ['korobka']=='avtomat':
#         tesla['narh']=45000 
#     else:
#         tesla['narh']=40000
# for tesla in teslas:
#         print(tesla)
# dasturchilar={'bobur':['python','c++'],
#               'nodir':['php','c#'],
#               'ali':['sql','java'],
#               'vali':['go','kotlin'],
#               }
# for ism,tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
#     for til in tillar:
#        # print(til.upper())
#        print(f'{til.upper()} ',end='')

hamkasblar={
     'Hikmatullo':{'familya':'shavkatjonov',
               'yil':1998,
               'malumot':'oliy',
              "tillar":['python','java']},
    'ukam':{'familya':'shavkatjonov',
            "yil":2000,
            "malumot":"o'rta",
            "tillar":["html","css"]},
    }
for ism,info in hamkasblar.items():
    print(f"\n{ism.title()} {info['familya'].title()} "
          f'{info["yil"]}-yilda tug\'ilgan.\n'
          f'Ma\'lumoti:{info["malumot"]}.\n'
          "Quyidagi dasturlash tillarini biladi:"
          )
    for til in info["tillar"]:
        print(til.upper())