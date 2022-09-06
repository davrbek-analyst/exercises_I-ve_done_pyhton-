# def  bahola(ismlar):
#     baholar={}
#     while ismlar:
#         ism=ismlar.pop()
#         baho=input(f"Talaba {ism.title()} ning bahosini kiriting: ")
#         baholar[ism]=int(baho)
#     return baholar
# talabalar=['ali', 'vali','hasan','bobur','javohir']
# baholar=bahola(talabalar[:])
# print(baholar)

# Amaliyot 1
#1-usul

# def katta_harf(sozlar):
#     katta_harflar=[]
#     while sozlar:
#         katta_harflar.append((sozlar.pop()).title())
#     return katta_harflar

# viloyatlar=['andijon','namangan',"farg'ona",'toshkent']
# k_viloyatlar=katta_harf(viloyatlar[:])
# print(k_viloyatlar)

# 2-usul

# def katta_harf(sozlar):
#     n=0
#     while n<len(sozlar):
#         sozlar[n]=sozlar[n].title()
#         n+=1
#     return sozlar    

# viloyatlar=['andijon','namangan',"farg'ona",'toshkent']
# k_viloyatlar=katta_harf(viloyatlar[:])
# print(k_viloyatlar)

# 3-usul

# def katta_harf(sozlar):
#     for i in range(len(sozlar)):
#         sozlar[i]=sozlar[i].title()
#     return sozlar

# viloyatlar=['andijon','namangan',"farg'ona",'toshkent']
# k_viloyatlar=katta_harf(viloyatlar[:])
# print(k_viloyatlar)

# Amaliyot 2
#1-usul

# def  bahola(ismlar):
#     baholar={}
#     for i in range(len(ismlar)):
#         ism=ismlar[i]
#         baho=input(f"Talaba {ism.title()} ning bahosini kiriting: ")
#         baholar[ism]=int(baho)
#     return baholar

# talabalar=['ali', 'vali','hasan','bobur','javohir']
# baholar=bahola(talabalar[:])
# print(baholar)

#2-usul

# def  bahola(ismlar):
#     baholar={}
#     for ism in ismlar:
#         baho=input(f"Talaba {ism.title()} ning bahosini kiriting: ")
#         baholar[ism]=int(baho)
#     return baholar

# talabalar=['ali', 'vali','hasan','bobur','javohir']
# baholar=bahola(talabalar[:])
# print(baholar)










