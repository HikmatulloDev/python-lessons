#05-dars string(matn)
# sana: 26/03/2022
# muallif: Hikmatullo

# string ustida matnlar

ism = "Muhammad"
#raxmatulprint("Mening ismim "+ism)
ism = "Ahad"
familya = "Qayum"
#print(ism + familya)
#print(ism + " " + familya)

# f- string

ism = "Ahad"
familya = "Qayum"
ism_sharif = f"{ism} {familya}"
#print(ism_sharif)

ism = "Hikmatullo"
familya = "Shavkatjonov"
#print(f"Assalamu alaykum mening ismim {ism} . {ism} {familya}!")

# maxsus belgilar
#print("hello\tworld!")
#print("hello\nworld!")

# string metodlar

ism = "Hikmatullo"
familya = "Shavkatjonov"
ism_sharif = f"{ism} {familya}"
ism_sharif = ism_sharif.upper()
#print(ism_sharif.upper())
#print(ism_sharif.lower())
#print(ism_sharif.title())
#print(ism_sharif.capitalize())
 
meva = "     olma    "
#print(meva)
#print("Men "  + meva.lstrip()+"yaxshi koraman")
#print("men "+ meva.rstrip()+ " yaxshi koraman")
#print("mn "+ meva.strip()+ " yaxshi koraman")

# input 

#ism = input("ismingiz nima?")
#print("assalamu alaykum"+ ism)
#ism = input("Ismingiz nima?\n>>>")
#print("Assalamu alaykum,"  + ism.title())
kocha="Bogbon"
mahalla="Yoshlik"
tuman="Asaka"
viloyat="Andijon"
#print(kocha+ " kochasi,",mahalla + " mahallasi,",tuman+ " tumani,",viloyat+ ' viloyati' )
#print("Iltimos quyidagi malumotlarni kiriting?")
kocha=input("kochangiz:")
mahalla=input("mahallangiz:")
tuman=input("tumaningiz:")
viloyat=input("viloyatingiz:")
manzil=f"{kocha}  kochasi,{mahalla} mahallasi,{tuman} tumani,{viloyat} viloyati"








