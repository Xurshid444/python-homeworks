#Sonning musbat va juft son ekanligini tekshiradigan dastur yozing.

son = int(input("Raqam kiriting: "))

if son > 0:
    if son % 2 == 0:
        print("Kiritilgan son musbat va juft.")
    else:
        print("Kiritilgan son musbat, lekin toq son.")
else:
    print("Kiritilgan son musbat emas.")
