# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 14:36:35 2022

@author: user
"""
# ism=input("Ismingiz nima?")
# print('Assalomu alaykum, '+ism)
# ism=input("Ismingiz nima?\n>>>")
# print('Assalomu alaykum '+ism.title()+'!')
# kocha='Bog\'bon'
# mahalla='Sog\'bon'
# tuman='Bodomzor'
# viloyat='Samarqand'
# print(kocha+' ko\'chasi,'+mahalla+' mahallasi,'+tuman+' tumani,'+viloyat+' viloyati')
salom='Assalomu alaykum ! Iltimos quyidagi anketani to\'ldiring '
kocha=input('Assalomu alaykum ! Iltimos quyidagi anketani to\'ldiring 👇\n \nKo\'changiz nomini kiriting\n>>>')
mahalla=input('Mahallangiz nomini kiriting\n>>>')
tuman= input('Tumaningiz nomini kiriting\n>>>')
viloyat=input('Viloyatingiz nomini kiriting\n>>>')
# print('Assalomu alaykum ! Iltimos quyidagi anketani to\'ldiring 👇\n>>>')
# manzil=kocha.title()+' '+mahalla.title()+' '+tuman.title()+' '+ viloyat.title()
manzil=f'{kocha.title()}  {mahalla.title()}  {tuman.title()} {viloyat.title()}'
print('Yashash joyingiz haqida malumot:\n \n'+manzil)






