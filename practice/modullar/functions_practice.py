

def yil_top(ism,yosh):
    """Foydalanuvchi tug'ilgan yilini hisoblovchi funksiya"""
    print(f"{ism.title()} {2022-yosh} - yili tavallud topgan.")



def daraja_hisobla(son):
    """Sonlling kvadrati va kubini hisoblaydigan funksiya"""
    print(f"{son} ning kubi: {son**3}\n"
          f"{son} ning kvadrati: {son**2}")




def son_aniqla(son):
    """Sonning juft yoki toqligini aniqlaydigan funksiya"""
    if son%2==0:
        print(f"{son} juft son")
    else:
        print(f"{son} toq son")


def katta_top(son1, son2):
    """Ikki sondan kattasini aniqlaydi"""
    if son1>son2:
        print(son1)
    elif son1<son2:
        print(son2)
    else:
        print('Sonlar teng')
   



def daraja_oshir(x,y):
    """x ning darajasi y bo'lgan ifodani hisoblaydi"""
    print(f"{x} ning {y}-darajasi: {x**y}")




def bolinish_alomatlari(son):
    """Sonning 2 dan 10 gacha sonlarga qoldiqsiz bo'linishini tekshiradi"""
    a=list(range(2,11))
    for n in a:
        if son%n==0:
            print(f"{son} {n}ga qoldiqsiz bo'linadi")

 