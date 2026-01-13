"""Satr bitta so'z bilan boshlanishi va boshqasi bilan tugashini tekshiradigan dastur yozing.
    Misol:
    - Kirish: "Python qiziqarli!"
    - Bilan boshlanadi: "Python"
    - Bilan tugaydi: "qiziqarli!" """

satr = input("Satrni kiriting: ")
boshlanish = input("Quyidagi so'z bilan boshlanadi: ")
tugash = input("Quyidagi so'z bilan tugaydi: ")

if satr.startswith(boshlanish) and satr.endswith(tugash):
    print("Satr boshlanish so'zi va tugash so'zi to'g'ri.")
elif satr.startswith(boshlanish):
    print("Satr boshlanish so'zi to'g'ri lekin tugash so'zi noto'g'ri.")
elif satr.endswith(tugash):
    print("Satr tugash so'zi to'g'ri lekin boshlanish so'zi noto'g'ri")
else:
    print("Satr boshlanish so'zi va tugash so'zi noto'g'ri")
