def yil_top(ism,yosh):
    """Foydalanuvchi tug'ilgan yilini hisoblovchi funksiya"""
    print(f"{ism.title()} {2022-yosh} - yili tavallud topgan.")

yil_top('davrbek', 20)

# Amaliyot 2

def daraja_hisobla(son):
    """Sonlling kvadrati va kubini hisoblaydigan funksiya"""
    print(f"{son} ning kubi: {son**3}\n"
          f"{son} ning kvadrati: {son**2}")

daraja_hisobla(25)

# Amaliyot 3

def son_aniqla(son):
    """Sonning juft yoki toqligini aniqlaydigan funksiya"""
    if son%2==0:
        print(f"{son} juft son")
    else:
        print(f"{son} toq son")
son_aniqla(115)        

# Amaliyot 4

def katta_top(son1, son2):
    """Ikki sondan kattasini aniqlaydi"""
    if son1>son2:
        print(son1)
    elif son1<son2:
        print(son2)
    else:
        print('Sonlar teng')
katta_top(17/25,18/26)    

# Amaliyot 5

def daraja_oshir(x,y):
    """x ning darajasi y bo'lgan ifodani hisoblaydi"""
    print(f"{x} ning {y}-darajasi: {x**y}")

daraja_oshir(4, 5)    

# Amaliyot 6

def daraja_oshir(x,y=2):
    """x ning kvadratini hisoblaydi"""
    print(f"{x} ning 2-darajasi: {x**2}")

daraja_oshir(5)

# Amaliyot 7

# 1-usul
def bolinish_alomatlari(son):
    """Sonning 2 dan 10 gacha sonlarga qoldiqsiz bo'linishini tekshiradi"""
    a=list(range(2,11))
    for n in a:
        if son%n==0:
            print(f"{son} {n}ga qoldiqsiz bo'linadi")
bolinish_alomatlari(112)            

  # 2-usuul
# def bolinish_alomatlari(son):
#     """Sonning 2 dan 10 gacha sonlarga qoldiqsiz bo'linishini tekshiradi"""
#     a=2
#     while a<=10 :
#         if son%a==0:
#           print(f"{son} {a}ga qoldiqsiz bo'linadi")
#         a+=1

# bolinish_alomatlari(112)


