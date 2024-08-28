def tam(x, y):
    hasil1 = x + y
    return hasil1

def kur(x, y):
    hasil2 = x - y
    return hasil2

def kal(x, y):
    hasil3 = x * y
    return hasil3

def bag(x, y):
    hasil4 = x / y
    if y == 0:
        return "pembagian nol!."
    else:
        return hasil4

print("Operasi: \n1. pertamban \n2. pengurangan \n3. perkalian \n4. pembagian")

choice = input("pilihan (+/-/*/:): ")

x = float(input("angka pertama: "))
y = float(input("angka kedua: "))

if choice == '+':
    print(f"hasil pertamban: {tam(x, y)}")
elif choice == '-':
    print(f"hasil pengurangan: {kur(x, y)}")
elif choice == '*':
    print(f"hasil perkalian: {kal(x, y)}")
elif choice == ':':
    print(f"hasil pembagian: {bag(x, y)}")
else:
    print("tidak valid")

