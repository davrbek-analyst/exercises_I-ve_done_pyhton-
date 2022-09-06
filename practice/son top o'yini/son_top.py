

import random as r

def son_top(x=10):
    """Foydalanuvchi dan o'ylangan sonni topishini so'rovchi funksiya"""
    print(f" 1 dan {x} gacha son o'yladim topa olasizmi?:",end='')
    t_s=r.randint(1, x)
    n=0
    while True:
        n+=1
        j=int(input(">>>"))
        if j<t_s :
            print(f'Xato, men o\'ylagan son bundan kattaroq.Yana harakat qiling:')
        elif j>t_s:
            print(f'Xato, men o\'ylagan son bundan kichikroq.Yana harakat qiling: ')
        else:
            break
    print(f"TOPDINGIZ ! {t_s} sonini o'ylagan edim. {n} ta taxmin bilan topdingiz.Tabriklayman!!")
    return n

def son_top_pc(x=10):
    """Foydalanuvchining o'ylagan sonini topadigan funksiya"""
    print(f"\n1 dan {x} gacha son o'ylang. Men topishga harakat qilaman.")
    input('Son o\'ylagan bo\'lsangiz istalgan tugmani bosing.')
    quyi=1
    yuqori=x
    n=0
    while True:
        n+=1
        i=r.randint(quyi,yuqori)
        j=input(f"Siz {i} sonini o'ylagansiz: to'g'ri(T),men o'ylagan son bundan kattaroq(+),yoki kichikroq(-)??: ")
        if j=='+':
            quyi=i+1
        elif j=="-":
            yuqori=i-1
        else:
           break
    print(f"Soningizni {n} ta taxmin bilan topdim!")
    return n

def start(x=10):
    yana=True
    while yana:
        natija_me=son_top(x)
        natija_pc=son_top_pc(x)
        if natija_me<natija_pc:
            print(f"\nTabriklayman {natija_me} ta taxmin bilan yutdingiz!!!")
        elif natija_me>natija_pc:
            print(f"\n{natija_pc} ta taxmin bilan yutdim!")
        else:
            print("\nO'yin durrang natija bilan yakunlandi.")
        yana=int(input("Yana o'ynashni xohlaysozmi: ha(1)/yo'q(0): "))
            
            
            
            
            
            
            
            
            