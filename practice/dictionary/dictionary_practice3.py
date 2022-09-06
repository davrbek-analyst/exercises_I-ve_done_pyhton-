# py_dictionary={
#     'int':'Butun sonnni ifodalovchi funksiya',
#     'foat':"O'nli sonni ifodslovchi funksiya",
#     'str':"Matinni ifodalovchi funksiya",
#     'input':'Foydalanuvchidan ma\'lumot so\'rovchi funksiya',
#     'tuple':"O'zgarmas ro'yxatni ifodalovchi funksiya",
#     'append':"Ro'yxatga element qo'shish uchun metod ",
#     'remove':"Ro'yxatdan element olib tashlash uchun metod",
#     'lsrtip':"Chap tomondagi bo'shliqni olib tashlaydigan metod",
#     'type':"O'zgaruvchining turini aniqlovchi funksiya",
#     'sort':"Ro'yxat elementlarini tartibga soluvchi metod"
#     }
# for k, v in sorted(py_dictionary.items()):
#     print(f"{k} - {v.title()}")








# davlatlar={
#     'aqsh':'washington d.c',
#     'italita':'rim',
#     'malayziya':'luala_lumpur',
#     "o'zbekiston":'toshkent',
#     'qirg\'iziston':'bishkek',
#     'qozog\'iston':'nursulton',
#     'rossiya':'moskva',
#     'singapur':'singapur',
#     'tojikiston':'dushanbe'
#     }
# print("Dunyo davlatlari:")
# for d in davlatlar.keys():
#     print(d.upper())
# print('\n Davlatlarning poytaxtlari:')
# for p in davlatlar.values():
#     print(p.title())

# d_nomi=input('Istalgan davlat nomini kiriting: ').lower()
# for d in davlatlar:
#     if d_nomi in d:
#       print(f"{d_nomi.upper()}ning poytxti {davlatlar[d_nomi].title()}")
# if d_nomi not in d:
#         print('Bizda bunday ma\'lumot yo\'q')

# poytaxt=davlatlar.get(d_nomi)
# if poytaxt==None:
#     print("Bizda bunday ma'lumot yo'q")
# else:
#     print(f"{d_nomi.upper()}ning poytaxti {poytaxt.title()}")









