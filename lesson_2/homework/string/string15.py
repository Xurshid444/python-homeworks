"""Foydalanuvchidan gap so'rang va har bir so'zning birinchi harflaridan akronim yarating.
    Misol:
    - Kirish: "Jahon Sog'liqni Saqlash Tashkiloti"
    - Chiqish: "JSST" """

satr = input("Gapni kiriting: ")

akronim = "".join(suz[0].upper() for suz in satr.split())

print("Akronim:", akronim)
