#Foydalanuvchi nomi va parolni qabul qiladigan va 
#ikkalasi ham bo'sh emasligini tekshiradigan dastur yozing.

user = input("Foydalanuvchi nomini kiriting: ")
parol = input("Parolni kiriting: ")

if user != "" and parol != "":
    print("Foydalanuvchi nomi va parol qabul qilindi.")
else:
    print("Foydalanuvchi nomi yoki parol bo'sh.")