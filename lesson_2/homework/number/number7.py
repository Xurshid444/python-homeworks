"""Sonni qabul qiladigan va uning juft son
   yoki juft son emasligini tekshiradigan dastur yarating.
"""

a = int(input("Sonni kiriting = "))

if a % 2 == 0:
    print(f"{a} - bu juft son.")
else:
    print(f"{a} - bu juft son emas.")
