mahsulotlar= ['olma','ruchka','marker','pepsi','do\'ppi','guruch','sumka','futbolka','naushnik','telefon']
savat= []
bor_mahsulotlar=[]
mavjud_emas=[]
print("Savatga kamida 5 ta mahsulot soning")
for n in range(5):
    savat.append(input(f"Savatga {n+1}-nahsulotni qo'shing: "))

for mahsulot in savat:
    if mahsulot.lower() in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)
if  len(mavjud_emas)==0: #yoki if mavjud_emas:
        print('Siz so\'ragan barcha mahsulotlar do\'konimizda bor')
else:
        print(f"Quyidagi mahsulotlar mavjud emas:")
        for yoq in mavjud_emas:
            print(yoq)
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    