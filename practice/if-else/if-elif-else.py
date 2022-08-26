# yosh=int(input('Yoshingiz nechida? '))
# if yosh<=4:
#     narh=0
# elif yosh<=12:
#     narh=10000
# elif yosh<=18:
#     narh=15000
# elif yosh<=25:
#     narh=20000
# else:
#     narh=25000
# print('Siz kirish uchun ',narh,' so\'m to\'lashungiz kerak')

# kun=input("Bugun nima kun?>>>")
# if kun.lower()=='shanba' or kun.lower()=='yakshanba':
#     print("Bugun dam olish kuni")
# else:
#     print("Bugun ish kuni")

# kun=input("Bugun kun nima?>>>")
# harorat=float(input('Havo harorati nechi gradus?>>> '))
# if (kun.lower()=='yakshanba' or kun.lower()=='shanba') and harorat>=30:
#     print("Cho'milgani ketdik")
# elif (kun.lower()=='yakshanba' or kun.lower()=='shanba') and harorat<30:
#     print('Uyda dam olamiz')

# narh= 15000
# choy= True
# salat=True

# if choy and salat:
#     narh=narh+10000
# elif choy or salat:
#     narh=narh+5000
# print(f"Jami {narh} so'm")

# narh = 15000 # mijoz 15 so'mga ovqat oldi
# choy = True
# salat = False
# non = True
# kompot = True
# assorti = False

# if choy:
#     print('Mijoz choy oldi')
#     narh=narh+3000
# if salat:
#     print('Mijoz salat oldi')
#     narh=narh+5000
# if non:
#     print('Mijoz non oldi')
#     narh=narh+2000
# if kompot:
#     print('Minoz kopot oldi')
#     narh=narh+5000
# if assorti:
#     print('Mijoz assorti oldi')
#     narh=narh+15000

# print(f"Jami {narh} so'm")

# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# ovqat= input('Nima ovqat yeysiz?>>>')
# if ovqat.lower() in menu:
#     print('Buyutna qabul qilindi')
# else:
#     print(f"Uzur bizda {ovqat} yo'q")

menu = ['osh','qazonkabob','shashlik','norin','somsa'] 
buyurtmalar=['osh','somsa','manti','shashlik']

for taom in buyurtmalar:
    if taom in menu:
        print(f"{taom.title()} menuda bor")
    else:
        print(f"Kechirasiz {taom.title()} menuda yo'q")




