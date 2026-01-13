#Foydalanuvchidan satr so'rang va barcha unli harflarni belgi bilan (masalan, `*`) almashtiring.

satr = input("So'zlarni kiriting: ")

for  almashtirish in "aeiouAEIOU":
    satr = satr.replace(almashtirish, "*")

print(satr)