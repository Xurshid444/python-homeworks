#Satr raqamlarni o'z ichiga olgan yoki yo'qligini tekshiradigan dastur yozing.

satr = input("Satrni kiriting: ")

if any(harf.isdigit() for harf in satr):
    print("Satr raqamlarni o'z ichiga oladi.")
else:
    print("Satr raqamlarni o'z ichiga olmaydi.")