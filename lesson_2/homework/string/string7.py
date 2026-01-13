"""Foydalanuvchidan gap va almashtiriladigan so'zni kiritishni so'rang. 
O'sha so'zni foydalanuvchi bergan boshqa so'z bilan almashtiring.
Misol:
   - Kirish gap: "Men olma yaxshi ko'raman."
   - Almashtirish: "olma"
   - Bilan: "apelsin"
   - Chiqish: "Men apelsin yaxshi ko'raman."""

satr1 = input("Birinchi satrni kiriting: ")
satr2 = input("Almashtiriladigan so'zni kiriting: ")
satr3 = satr1.replace(satr2, input("Yangi so'zni kiriting: "))

print(f"{satr3}")
