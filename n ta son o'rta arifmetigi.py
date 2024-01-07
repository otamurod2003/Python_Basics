soni = int(input("Nechta son kiritmoqchisiz:"))


sonlar = []

for son in range(soni):
    number = float(input(f"{son+1}-sonini kiriting:"))
    sonlar.append(number)
if soni > 0:
    orta_arifmetik = sum(sonlar)/son
    print("O'rta arifmetik qiymat: ",orta_arifmetik)
else:
    print('Sonlar mavjud emas')
