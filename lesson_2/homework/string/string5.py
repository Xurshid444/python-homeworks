#Berilgan satrdagi unli va undosh harflar sonini hisoblaydigan dastur yozing.

satr = input("Satrni kiriting: ").lower()

print("Unli harflar:", sum(c in "aeiou" for c in satr))
print("Undosh harflar:", sum(c in "bcdfghjklmnpqrstvwxyz" for c in satr))


