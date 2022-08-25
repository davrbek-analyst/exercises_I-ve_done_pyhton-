mahsulotlar= ['olma','ruchka','marker','pepsi','do\'ppi','guruch','sumka','futbolka','naushnik','telefon']
savat= []
print("Savatga kamida 5 ta mahsulot soning")
for n in range(5):
    savat.append(input(f"Savatga {n+1}-nahsulotni qo'shing: "))
    
for mahsulot in savat:
    if mahsulot.lower() in mahsulotlar:
        print(f"Do'konimizda {mahsulot} bor")
    else:
        print(f"Do'konimizda {mahsulot} yo'q")
        















