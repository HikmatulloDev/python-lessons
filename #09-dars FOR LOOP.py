# 09-dars  :FOR LOOP
# Sana:05/04/2022
#muallif: Hikmatullo

mehmonlar = ['vali','aziz','ali',"bobir","jasur"]
#print("salom",mehmonlar[0])
#print("salom", mehmonlar[3])
#for mehmon in mehmonlar:
    #print("salom",mehmon)
    #print('xayr',mehmon))
    #print(f"hurmatli {mehmon} szni 12 dekabr kuni nahorga oshga taklif qilamiz")
    #print("hurmat bilan palonchiyevlar oilasi\n")
#sonlar = list(range(1,11))   
#print(sonlar)
#for son in sonlar:
 #print(f"{son} ning kvadrati {son**2} ga teng")    
#sonlar = list(range(11))   #1dan 10 gacha sonlar royhati
#sonlar_kvadrati = []        #bosh royhat yasaymiz
#for son in sonlar: # sonlardagi har bir son uchun
    #sonlar_kvadrati.append(son**2)
#print(sonlar)
#print(sonlar_kvadrati)


#dostlar = []
#print("5 ta eng yaqin dostingiz kim ?")
#for n in range(5):
    #dostlar.append(input(f"{n+1}-dostingizni ismini kiriting:"))
    #print(dostlar)

# AMALIYOTLAR
#ismlar = ["ali",'usmon',"umar",'zubayr',"ikrom"]
#for op in ismlar:
# print(f"assalamu alaykum, {op} . sahifamizga xush kelibsz")    
#print(f"kod {len(ismlar)} marta takrorlandi")
    
#toq_sonlar = list(range(11,100,2))
#for son in toq_sonlar:
 #   print(son**3)
#kino = []
#print("5 ta eng sevimlik kinoyingiz qaysi?")
#for cinema in range(5):
    #kino.append(input(f"{cinema+1}-kinoyingiz:")) 
    #print(kino)
n_people = int(input("bugun necha kishi  bilan korishdingiz?>>>"))
ismlar = []
for n in range(n_people):
       ismlar.append(input(f"{n+1}-odamingiz kim edi?"))
print(ismlar)