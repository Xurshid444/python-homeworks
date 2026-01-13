"""Berilgan satr `palindrom` yoki emasligini tekshiradigan Python dasturini yozing.
> Palindrom Satr nima? Agar satrning teskarisi asl satr bilan bir xil bo'lsa, 
bunday satr palindrom deyiladi. Misol: "madam", "racecar", "12321"."""

satr = input("Satrni kiriting: ")

satr_palindrom = satr.replace(" ", "").lower()

# Palindrom tekshiruvi
if satr_palindrom == satr_palindrom[::-1]:
    print("Satr palindrom.")
else:
    print("Satr palindrom emas.")
