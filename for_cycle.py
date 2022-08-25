# # mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
# # for mehmon in mehmonlar:
# #     print('Salom',mehmon)

# mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
# for mehmon in mehmonlar:
#     print('Assalomu alaykum ',mehmon,', sizni tug\'ilgan kunga taklif qilamiz !')
# print('Hurmat bilan , Mirzaqisimovlar oilasi')
#   #print(f'Assalomu alakum {mehmon} , sizni 12-yanvar kungi nahorgi oshga taklif qilamiz')
    
# sonlar= list(range(1,11))
# for son in sonlar:
#     print(f"{son} ning kvadrati {son**2} ga teng")

# sonlar= list(range(11))
# sonlar_kvadrati= []
# for son in sonlar:
#     sonlar_kvadrati.append(son**2)
# print(sonlar)
# print(sonlar_kvadrati)

# dostlar=[]
# print("5 ta eng yaqin do'stingiz kim?")
# for n in range(5):
#     dostlar.append(input(f"{n+1}-do'stingizni kiriting: "))
# print(str(dostlar).title())

# mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
# for mehmon in mehmonlar:
#     print('Hayrli ting!',mehmon)
# print('Kod',len(mehmon),' marta takrorlandi')

# t_sonlar= list(range(11,101,2))
# for kub in t_sonlar:
#     print(kub**3)

# kinolar=[]
# print('5 ta sevimli kinoingizni kiriting')
# for k in range(5):
#     kinolar.append(input(f'{k+1}- kinoni kiriting: '))
# print(str(kinolar).title())   

odamlar=[]
s= input('Bugun nechta odam bilan uchrashdingiz?>>> ')
for n in range(int(s)):
    odamlar.append(input(f"{n+1}-suhbar qilgan odamingizni kiriting: "))
print(str(odamlar).title())    