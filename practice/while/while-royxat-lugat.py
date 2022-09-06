# While and list

# ismlar = []

# print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
# n=1 # ismlarni sanash uchun o'zgaruvchi
# savol = f"{n}-do'stingiz ismini kiriting:"
# while True:
#     savol = f"{n}-do'stingiz ismini kiriting:"
#     ism = input(savol)
#     ismlar.append(ism)
#     javob = input("Yana ism qo'shasizmi? (ha/yo'q)")
#     if javob =='ha':
#         n+=1
#     else:
#         break
# print('Do\'stlaringiz ro\'yxati:')
# for ism in ismlar:
#     print(ism.title())

#While and dictionary

# print("Do'stlaringiz qanday telefon ishlatishlarini aniqlaymiz")
# friends={}
# n=1
# while True:
#     ism=input(f"{n}-do'stingizni ismini kiriting: ")
#     tel=input(f"{ism.title()} ning telefoni modelini kiriting: ")
#     friends[ism]=tel.title()

#     javob=input("Yana do'stlaringiz haqida ma'lumot ulashasizmi? (ha/yo'q): ")
#     if javob == 'ha':
#         n+=1
#     else:
#         break
# print("\nDo'stlaringizning telefonlari markalari:\n")
# for ism,tel in friends.items():
#     print(f"{ism.title()} {tel} markali telefon ishlatadi.")


# Deltening elements of lists

# mevalar=['olma', 'behi', 'anor', 'shaftoli', 'olma','hurmo','olma','behi']
# meva='behi'
# while meva in mevalar:
#     mevalar.remove(meva)
# print(mevalar)

# Taking elements from one list into another list with while operator

# print('Ob-havo ma\'lumotlarini taxlil qilamiz')
# kunlar=['Dushanba', 'Deshanba','Chorshanba','Payshanba','Juma','Shanba','Yakshanba']
# kunlar.reverse()
# analiz={}
# while kunlar:
#     kun=kunlar.pop()
#     harorat=input(kun +' kungi harorat darajasini kiriting: ')
#     analiz[kun]=float(harorat)
# print('Haftalik ob-havo ma\'lumotlari:')
# for kun,harorat in analiz.items():
#     print(f"\n{kun} kuni havo harorti: {harorat}℃")






#Amaliyot 1

# taomlar=[]
# n=1
# while True:
#     taomlar.append(input(f'Nima buyurasiz?\n{n}-buyurtma: '))
#     javob=input("Yana buyurtma qilasizmi? (ha/yo'q): ")
#     if javob=='ha':
#         n+=1
#     else:
#         break
# print('\nBuyurtma qilingan taomlar to\'yxati:')
# for taom in taomlar:
#     print(taom.capitalize())  

#Amaliyot 2

# e_bozor={}
    
# print("\nIltimos, do'konda qolgan 3 ta mahsulot nomi va narhlarini yozib bering!")
# n=0
# while n<3:
#     n+=1
#     tovar=input('Mahsulot nomi: ')
#     narh=input('Narhi: ')
#     e_bozor[tovar]=float(narh)
# print()
# for tovar, narh in e_bozor.items():
#     print(f"{tovar.title()} ning narhi {narh} so'm")
  
#Amaliyot 3

# bozor={
#        'un':120000,
#        'guruch':20000,
#        "yog\'":70000
#        }
# mahsulot=['un','shakar','guruch']

# while mahsulot:
#     tovar=mahsulot.pop()    
#     if tovar in bozor:
#             narh=bozor[tovar]
#             print(f"{tovar.title()} narhi {narh} so'm")
#     else:
#             print('Bizda bu mahsulot yo\'q')
    
    
