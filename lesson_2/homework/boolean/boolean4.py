#Uchta son qabul qiladigan va ularning barchasi har xil ekanligini tekshiradigan dastur yozing.

son1 = int(input("Birinchi raqamni kiriting: "))
son2 = int(input("Ikkinchi raqamni kiriting: "))
son3 = int(input("Uchinchi raqamni kiriting: "))

if son1 != son2 and son1 != son3 and son2 != son3:
    print("Kiritilgan raqamlar bir biriga teng emas.")
else:
    print("Kiritilgan raqamlardan ba'zilari bir biriga teng.")