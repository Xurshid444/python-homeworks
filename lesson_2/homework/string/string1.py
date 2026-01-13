"""Foydalanuvchidan ism va tug'ilgan yilini so'raydigan 
   va ularga yoshini ayta oladigan dastur yarating.
"""

name = input("Ismingiz nima? ")
year = int(input("Tug'ilgan yilingiz: "))

year2 = 2026
c = year2 - year

print(f"Sizning ismingiz {name} va sizning yoshingiz taxminan {c} da.")
