#07-dars LIST
#sana:30/03/2022
#muallif: Hikmatullo
 
mevalar = ['olma', "o'rik" , 'shaftoli' , "gilos"] #matnlar ro'yhati
narxlar = [20000,15000,3000,4000] #sonlar ro'yhati
aralash = ["bir","ikki",23,34] #sonlar va matnlar ro'yhati
ismlar = [] #bo'sh ro'yhat

#print(mevalar[0])
#print(mevalar[2])
#print(aralash[3])

#print(mevalar[-2])
#print(mevalar[-1])

#print(mevalar[2].upper())
#print(aralash[1].lower())
#print(mevalar[3].title())

#print(narxlar[0]+narxlar[3])

#Elementni o'zgartirish

mevalar[1]="anjir"
#print(mevalar)

#Append, elementni faqat oxiridan qo'shib keladi

mevalar.append("ananas")
mevalar.append("banan")
#print(mevalar)

#Insert, kiritgan joyga element qo'shadi

mevalar.insert(1,"kiwi")
#print(mevalar)
cars = []
cars.append ("spark")
cars.append ("nexia")
cars.append ("matiz")
#print(cars)

#delete qiish

del cars[0]
#print(cars)

cars.insert(0, "malibu")
#print(cars)

#Remove

cars.remove("matiz")
#print(cars)
 
#Remove ro'yhatdagi elementni faqat boshidagisini o'chiradi 

hayvonlar=["it", "sigir", "ot", "mushuk", "ot",]   
hayvonlar.remove("ot")
#print(hayvonlar)

#pop

bozorlik=["yog", "un","banan","go'sht","piyoz"]
#print(bozorlik)
mahsulot=bozorlik.pop(1)# ro'yhatdan un ni sug'urib olamiz
#print(mahsulot)
#print("men " + mahsulot + " sotib oldim")
#print("olinmagan mahsulotlar:", bozorlik)

#elementni raqamini qo'ymasak oxiridagini olib tashlaydi

mahsulot= bozorlik.pop()
#print(bozorlik)
#print(mahsulot)

narxlar.remove(3000)
#print(narxlar)
narxlar[0]= narxlar[0]+2000
#print(narxlar)

#Amaliyot

ismlar=["abror","bobur","jamoldin",]
#print("salom",ismlar[0], "bugun choyxonaga borasanmi?")
#print(ismlar[1],"ga ayt", ismlar[2], "meni uydan olib ketsin")
#print(ismlar[1]+ " biznkiga keldi")
#print(f"{ismlar[0]} va {ismlar[1]} ular kursdoshlar")

sonlar= [12,-22,2.3,34]
sonlar[0]=sonlar[0]+100
#print(sonlar)
del sonlar[2]
#print(sonlar)

t_shaxslar=["Amir Tumer", 'Imom Buxoriy hazrat']
z_shaxslar=["elon mask",'mark supergberk']
print(f"\nMen tarixiy shaxslardan {t_shaxslar.pop(1)} va zamonaviy shaxslardan,\n{z_shaxslar.pop(0)} bilan suhbat qilishni hohlayman. ")

friends = []
friends.append('bobur')
friends.append("olim")
friends.append('aziz')
friends.append("kamol")
#oxiriga odam qo'shdim friends.append("jamol")
friends.insert(0,"sardor")
friends.insert(2,'donyor')
#print(friends)

#yangi_mehmonlar = []
#yangi_mehmonlar=friends.pop(1)
#yangi_mehmonlar=friends.pop(2)
#print(yangi_mehmonlar)
#yangi_mehmonlar = []
#yangi_mehmonlar.append(friends.pop(2))
#yangi_mehmonlar.append(friends.pop(3))
#print("\nkelgan mehmonlar:", yangi_mehmonlar)


