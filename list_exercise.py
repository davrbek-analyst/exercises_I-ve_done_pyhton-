# ismlar=  ['Nuriddin', 'Bunyodbek', 'Jahongir','Muhammadyaxyo']
# print("Salom ",ismlar[1],', bugun choyxona bormi?')
# print(ismlar[-1], ', choyxonaga boramizmi?')
# sonlar= [5, 29, -12, 3.54, -6.5]
# print(sonlar[-1]*56)
# print(sonlar[2]+sonlar[0])
# print(sonlar[3]**2)
# sonlar.append(88)
# sonlar.append(-63.3)
# print(sonlar)
# sonlar.insert(1, 6)
# print(sonlar)

# t_shaxslar= ['Alisher Navoiy','Fitrat', 'Cho\'lpon', 'Mahmudiy']
# z_shaxslar= ['Bill Geyts', 'Habib', 'Stiv Jobs','Robib Sharma']
# print('Men tarixiy shaxslardan ',t_shaxslar[2], ' bilan\nzamonaviy shaxslardann esa ',z_shaxslar[-1],' bilan suhbatlashishni hoxlardim')
# print('Men tarixiy shaxslardan ',t_shaxslar.pop(2), ' bilan\nzamonaviy shaxslardann esa ',z_shaxslar.pop(-1),' bilan suhbatlashishni hoxlardim')

friends= ['Orifjon','Asadbek Abdujalilov', 'Asadbek Inomov','Mizakammol','Sardorbek']
friends.remove('Sardorbek')
friends.remove('Asadbek Abdujalilov')
print(friends)

friends.insert(0, 'Afzalbek')
friends.insert(1, 'Farrux')
friends.append('Javohir')
mehmonlar= []
m1 = friends.pop(0)
m2 = friends.pop(2)
m3 = friends.pop(-1)
mehmonlar.append(m1)
mehmonlar.append(m2)
mehmonlar.append(m3)
print('Taklif qilingan mehmonlardan  ', mehmonlar,' kelishadi ekan')