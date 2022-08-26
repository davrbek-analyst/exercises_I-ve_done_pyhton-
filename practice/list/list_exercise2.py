# cars = ['bmw','mercedens benz','audi','volvo','tesla']
# cars.sort()
# print(cars)
# cars.sort(reverse=True)
# print(cars)

# mehmonlar= ['Odil','Hamid','Temur','Avazbek','Farruh','Shamsiddin']
# print('sorted() qaytargan natija: ',sorted(mehmonlar))
# print('Asl ro\'yxat o\'zgarmadi: ',mehmonlar)
# print(sorted(mehmonlar, reverse=True))

# ages = [12, 98, 34, 65, 76, 11,]
# ages.sort()
# print(ages)
# print(sorted(ages,reverse=True))

# fruits= ['pear','banana','apple','watermelon','lemon']
# fruits.reverse()
# print(fruits)

# fruits= ['pear','banana','apple','watermelon','lemon']
# print('Number of fruits in the baket is: ',len(fruits))

# sonlar=list(range(0,10))
# print(sonlar)

# juft_sonlar= list(range(0,20,2))
# toq_sonlar= list(range(1,20,2))
# print('Jusft sonlar: ',juft_sonlar)
# print('Toq sonlar: ',toq_sonlar)

# narxlar= [12000, 22500, 23456, 9800, 5600, 9934, 32874]
# arzon= min(narxlar)
# qimmat= max(narxlar)
# jami= sum(narxlar)
# print('Eng arzon narh: ',arzon,' . Eng qimmat narh: ',qimmat,'. Jami narxlar yig\'indisi: ',jami)

# cars = ['bmw','mercedens benz','audi','volvo','tesla']
# my_cars = cars[0:3]
# print(my_cars)
# print(cars[:4])
# print(cars[2:])

# sonlar= [1, 8, 12, 66, 25, 44]
# sonlar2= sonlar[:]
# sonlar2.append(-5)
# print('Birinchi sonlar ro\'yxati: ',sonlar)
# print('Ikkinchi sonlar ro\'yxati: ',sonlar2)

toys = ('bus','car','bear','dino','snake','lizard')
# print(toys[0])
# print(toys[-1])
# print(toys[2:5])

toys=list(toys)
toys.append('gun')
toys.remove('car')
#print(toys)
toys.insert(1, 'joja')
print(toys)