# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narh':narhi}
#     return avto

# print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
# avtolar=[] # salondagi avtolar uchun bo'sh ro'yxat
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting")
#     kompaniya=input("Ishlab chiqaruvchi: ")
#     model=input("Modeli: ")
#     rangi=input("Rangi: ")
#     korobka=input("Korobka: ")
#     yili=input("Ishlab chiqarilgan yili: ")
#     narhi=input("Narhi: ")
    
#     #Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida 
#     #lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
#     avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
    
#     # Yana avto qo'shish-qo'shmaslikni so'raymiz
#     javob = input("Yana avto qo'shasizmi? (yes/no): ")
#     if javob=='no':
#         break
# print('Salonimizdagi avtolar:')
# for avto in avtolar:
#     print(f"{avto['rang'].title()} {avto['model'].title()},"
#           f"{avto['korobka']} korobka. Narhi:{avto['narh']}")

#Amaliyot 1 and 2

# def shaxs_info(ism, familiya, t_yil, t_joy, e_manzil=None, tel_raqam=None ):
#     """Shaxslar haqidagi ma'lumotlarni lug'at shaklida qaytaruvchi funksiya"""
#     info={
#         'ism':ism,
#         'familiya':familiya,
#         't_yil':t_yil,
#         't_joy':t_joy,
#         'e_manzil':e_manzil,
#         'tel_raqam':tel_raqam}
#     return info

# print("Mijozlar haqidagi ma'lumotlarni yaratamiz")
# mijozlar=[]
# while True:
#     ism=input("Ism: ")
#     familiya=input('Familiya: ')
#     t_yil=int(input("Tug'ilgan yil: "))
#     t_joy=input("Tug'ilgan joy: ")
#     email=input("Elektron manzil(xohlamasangiz 'Enter' ni bosing): ")
#     tel_raqam=input("Telefon raqam(xohlamasangiz 'Enter' ni bosing): ")
#     mijozlar.append(shaxs_info(ism, familiya, t_yil, t_joy,email,tel_raqam))
#     javob=input('Yana ma\'lumot berasizmi(yes/no): ')
#     if javob=='no':
#         break
# for mijoz in mijozlar:
#     if mijoz['e_manzil']:
#         print(f"\n{mijoz['ism'].title()} {mijoz['familiya'].title()} haqidagi ma'lumotlar:\n"
#               f"\nTug'ilgan yili: {mijoz['t_yil']}\n"
#               f"Tug'ilgan joyi: {mijoz['t_joy'].title()}\n"
#               f"Elektron manzili: {mijoz['e_manzil']}")
#     elif mijoz['tel_raqam']:
#         print(f"\n{mijoz['ism'].title()} {mijoz['familiya'].title()} haqidagi ma'lumotlar:\n"
#               f"\nTug'ilgan yili: {mijoz['t_yil']}\n"
#               f"Tug'ilgan joyi: {mijoz['t_joy'].title()}\n"
#               f"Telefon raqami: {mijoz['e_manzil']}")
#     elif  mijoz['e_manzil'] and mijoz['tel_raqam']:
#         print(f"\n{mijoz['ism'].title()} {mijoz['familiya'].title()} haqidagi ma'lumotlar:\n"
#               f"\nTug'ilgan yili: {mijoz['t_yil']}\n"
#               f"Tug'ilgan joyi: {mijoz['t_joy'].title()}\n"
#               f"Elektron manzili: {mijoz['e_manzil']}\n"
#               f"Telefon raqami: {mijoz['e_manzil']}\n")
#     else:
#         print(f"\n{mijoz['ism'].title()} {mijoz['familiya'].title()} haqidagi ma'lumotlar:\n"
#               f"\nTug'ilgan yili: {mijoz['t_yil']}\n"
#               f"Tug'ilgan joyi: {mijoz['t_joy'].title()}")
             

#Amaliyot 3

# def max_top(son1, son2, son3):
#     """3 sondan eng kattasini topuvchi funksiya"""
#     a=max(son1, son2, son3)
#     return a

# katta=max_top(112, 12.36, 45.33)
# print(katta)

#Amaliyot 4

# def aylana(radius):
#     """Aylana radiusi orqali perimerti,yuzi va diametrini lug'at qiladi"""
#     diametr=2*radius
#     perimetr=2*3.14*radius
#     yuza=3.14*(radius**2)
    
#     olchamlar={
#         'radius':radius,
#         'diametr':diametr,
#         "perimetr":perimetr,
#         'yuza':yuza}
#     return olchamlar


#Amaliyot 5
#1-usul

# def tub_son(min,max):
#     tub_sonlar=[]
#     for n in range(min,max+1):
#         if n>1:
#             for i in range(2,n):
#                 if n%i==0:
#                     break
#             else:
#                   tub_sonlar.append(n)
#     return tub_sonlar
# tub=tub_son(17, 99)   
# print(tub)             
    
#2-usul

# def tub_son(min,max):
#     tub_sonlar=[]
#     for n in range(min,max+1):
#         tub=True
#         if n>1:
#             for i in range(2,n):
#                 if n%i==0:
#                     tub=False
            
#         if tub:
#          tub_sonlar.append(n)
#     return tub_sonlar 
# tsonlar=tub_son(17, 99)    
# print(tsonlar)



#Amaliyot 6
# 1-usul

# def fibona_son(son):
#     fibonachilar=[1,1]
#     n=0
#     while n<son:
#         fibonachilar.append(fibonachilar[-1]+fibonachilar[-2])
#         n+=1
#     return fibonachilar
# f=fibona_son(15)
# print(f)

#2-usul

# def fibona_son(son):
#     fibonachilar=[1,1]
#     for i in range(2,son+1):
#         fibonachilar.append(fibonachilar[-1]+fibonachilar[-2])
#     return fibonachilar
# f=fibona_son(15)
# print(f)

