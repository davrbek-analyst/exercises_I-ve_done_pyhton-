# Amaliyot 1
# 1-usul

# qiymat=""
# while qiymat !='stop':
#     qiymat= input('Yoqtirgan kitoblaringizni kiriting: ')
#     print(qiymat)
# print("Ma'lumot uchun rahmat!")

# 2-usul

# while True:
#     qiymat= input('Yoqtirgan kitoblaringizni kiriting: ')
#     if qiymat=='stop':
#         break
#     else:
#         print(qiymat)
# print("Ma'lumot uchun rahmat!")

# Amaliyot 2
#1-usul(break)

# print("Chipta narxlarini bilish dasturi(to'xtatish uchun 'exit' yoki 'quit' deb yozing)")
# while True:
#     qiymat=input('Yoshingizni kiriting: ')
#     if qiymat != 'exit'  or qiymat != 'quit':    
#         break
#         yosh=int(qiymat)
#     if yosh<7:
#         narh=2000
#     elif 7<=yosh<18:
#         narh=3000
#     elif 18<=yosh<65:
#         narh=10000
#     elif yosh>=65:
#         narh=0
#     print(f"Yoshingiz {yosh} daligi uchun chipta narhi {narh} so'm")        
# print('Dastur tamom')

#2-usul(ishora)

# print("Chipta narxlarini bilish dasturi(to'xtatish uchun 'exit' yoki 'quit' deb yozing)")
# ishora=True
# while ishora:
#     qiymat=input('Yoshingizni kiriting: ')
#     if qiymat == 'exit'  or qiymat == 'quit':    
#         ishora=False
#     else:    
#         yosh=int(qiymat)
#         if yosh<7:
#             narh=2000
#         elif 7<=yosh<18:
#             narh=3000
#         elif 18<=yosh<65:
#             narh=10000
#         elif yosh>=65:
#             narh=0
#         print(f"Yoshingiz {yosh} daligi uchun chipta narhi {narh} so'm")        
# print('Dastur tamom')

# 3-usul(shart bilan)

# print("Chipta narxlarini bilish dasturi(to'xtatish uchun 'exit' yoki 'quit' deb yozing)")
# qiymat=''
# while qiymat != 'exit'  and qiymat != 'quit':
#     qiymat=input('Yoshingizni kiriting: ')
#     if qiymat != 'exit'  and qiymat != 'quit':   
#         yosh=int(qiymat)
#         if yosh<7:
#             narh=2000
#         elif 7<=yosh<18:
#             narh=3000
#         elif 18<=yosh<65:
#             narh=10000
#         elif yosh>=65:
#             narh=0
#         print(f"Yoshingiz {yosh} daligi uchun chipta narhi {narh} so'm")        
# print('Dastur tamom')


#Amaliyot 3

# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat=='exit':
#         break
#     elif float(qiymat)<0:
#         continue
#     else:
#         ildiz = float(qiymat)**0.5 
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")






