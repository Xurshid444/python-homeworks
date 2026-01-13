#Sonni qabul qiladigan va u 3 ga ham, 5 ga ham bo'linishini tekshiradigan dastur yarating.

son = int(input("Raqam kiriting: "))

if son % 3 == 0 and son % 5 == 0:
    print("Kiritilgan son 3 ga ham 5 ga ham bo'linadi.")
elif son % 3 == 0 and son % 5 != 0:
    print("Kiritilgan son 3 ga bo'linadi lekin 5 ga bo'linmaydi")
elif son % 3 != 0 and son % 5 == 0:
    print("Kiritilgan son 3 ga bo'linmaydi lekin 5 ga bo'linadi")
else:
    print("Kiritilgan son 3 ga ham 5 ga ham bo'linmaydi")