# shaxs0={
#         'ism':'abu abdulloh muhammad',
#         'yil':'810',
#         'joy':'buxoro',
#         'asar':['Al-jome as-sahih', 'Al-adab al-mufrad', 'At-tarix al kabir'],
#         'y_yosh':'60 yil',
#         }
# shaxs1={
#         'ism':'abdulla qodiriy',
#         'yil':'1894',
#         'joy':'toshkent',
#         'asar':['O\'tkan kunlar', 'Mehrobdan chayon', 'Obid ketom'],
#         'y_yosh':'44 yil',
#         }
# shaxs2={
#         'ism':'erkin vohidov',
#         'yil':'1936',
#         'asar':['Tong nafasi', 'Qo\'shiqlarim sizga', 'O\'zbegim'],
#         'joy':'farg\'ona',
#         'y_yosh':'80 yil',
#         }
# shaxs3={
#         'ism':'alisher navoiy',
#         'yil':'1441',
#         'joy':'xirot',
#         'asar':['Xamsa', 'Lison ut-Tayr', 'Mahbub Al-Qulub'],
#         'y_yosh':'60 yil',
#         }
# shaxslar=[shaxs0, shaxs1, shaxs2, shaxs3]

# for shaxs in shaxslar:
#         print(f"{shaxs['ism'].title()} "
#               f"{shaxs['yil']} {shaxs['joy'].title()}da tavallud topgan. {shaxs['y_yosh']} umir ko'rgan.")
        
# for shaxs in shaxslar:
#     print(f"\n{shaxs['ism'].title()} ning mashxur asarlari:")
#     for asar in shaxs['asar']:
#         print(asar)









# odamlar={
#     'ali':['Terminator','Rambo','Titanic'],
#     'vali':['Tenet','Inception','Interstellar'],
#     'hasan':['Abdullajon','Bomba','Shaytanat'],
#     'husan':['Mahallada duv-duv gap','John Wick']
#     }


# for ism,kinolar in odamlar.items():
#     print(f"\n{ism.title()}ning sevimli kinolari:")
#     for kino in kinolar : 
#         print(kino)







# davlatlar={
#     'o\'zbekiston':{'hududi':448978,
#                     'aholisi':33000000,
#                     'pul':'so\'m',
#                     'poytaxt':'Toshkent'},
#     'rossiya':{'hududi':17098246,
#                'aholisi':144000000,
#                'pul':'rubl',
#                'poytaxt':'Moskva'},
#     'aqsh':{'hududi':9631418,
#                'aholisi':327000000,
#                'pul':'dollar',
#                'poytaxt':'Washington'},
#     'malayziya':{'hududi':329750,
#                'aholisi':25000000,
#                'pul':'rinngit',
#                'poytaxt':'Kuala-Lumpur'}
#     }

# for davlat,info in davlatlar.items():
#         hudud=info['hududi']
#         aholi=info['aholisi']
#         pul=info['pul']
#         poytaxt=info['poytaxt']

# country=input('Davlat nomini kiriting: ').lower()

# if country in davlatlar:
#     info=davlatlar[country]
#     print(f"\n{country.title()}ning poytaxti: {info['poytaxt']}"
#                   f"\nHududi: {info['hududi']}"
#                   f"\nAholisi: {info['aholisi']}"
#                   f"\nPul birligi: {info['pul']}"
#                   )
# else:
#       print('Bizda bu davlat haqida ma\'lumot yo\'q')
    