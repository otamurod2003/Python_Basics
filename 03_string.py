#String malumot turi bilan ishlaymiz

#Muallif: Otamurod Pirnapasov
#Dastur yaratilgan sana: 12.08.2023

#string malumot turidan faqat matnlar bilan ishlashimiz mumkin. U o'zida barcha unikodlarini qamrab oladi.
#O'zgaruvchi nomi lotin harflardan tashkil topadi. Ammo uning qiymati istalgan alifbodan bo'lishi mumkin
ism = "Otamurod"
familiya = 'Пирнапасов'

#string ustida amallar
print(ism + " " + familiya)  #matnlarni bir biriga qo'shish
print("uning ismi" ,ism)

#f-string:  matn ichida o'zgaruvchilardan foydalanish
ism_familiya = f"{ism} {familiya}"
print(ism_familiya)

ismFamiliya = f"Salom mening ismim {ism}. Familiyam {familiya}"

print("Hello world")
print("Hello \tWorld") # \t matn ichida bitta "tab" qo'shib beradi
print('Hello \n world') # \n belgisidan keyinga barcha so'zlar boshqa qatordan chiqariladi


#STRING metodlar: upper(), lower() and etc.

name = "sadulla"
name = name.upper() # bu metod string tarkibidagi elementlarini barchasini katta harflarga o'girib beradi
print(name)

surname = "abdullayev"
surname = surname.lower() #ushbu metod string tarkibidagi elementlarini kichik harflarga o'girib beradi

ism_sharif = "abdulla oripov" # etibor bering! barcha belgilarimiz kichik harflardan iborat
ism_sharif = ism_sharif.title() # ushbu metoda matn ichidagi har bir so'zning bosh harfini kattasiga o'girib beradi
print(ism_sharif)

print(ism_sharif.capitalize())  #captilize() metodi kiritilan matnning faqat birinchi elementini katta harfga o'girib beradi

# STRIP metodlar  lstrip(), rstrip(), strip() ushbu metodlar berilgan matn ichidagi so'zlar orasidagi bo'sh joylarini o'chirish uchun xizmat qiladi
book_title = "      Adam Freeman        "  #korib turibsizki berilgan matn orasida bo'sh joylar katta
print("Asl matn: " + book_title)
print("lstrip metodi natijasi: " + book_title.lstrip() + " mana shunaqa")
print("rstrip metodi natijasi: " + book_title.rstrip() + " mana shunaqa")
print("strip metodi natijasi: " + book_title.strip()+ " mana shunaqa")