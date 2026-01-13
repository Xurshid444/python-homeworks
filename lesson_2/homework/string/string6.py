#Bir satr boshqa satrni o'z ichiga olganligini tekshiradigan Python dasturini yozing.

satr1 = input("Birinchi satrni kiriting: ")
satr2 = input("Ikkinchi satrni kiriting: ")

# Tekshiruv
if satr2 in satr1:
    print("Birinchi satr ikkinchi satrni o'z ichiga oladi.")
elif satr1 in satr2:
    print("Ikkinchi satr birinchi satrni o'z ichiga oladi.")
else:
    print("Bu satrlar bir birini o'z ichiga olmaydi.")