a = int(input("digite um numero entre 1 e 10: "))

while a < 1 or a > 10:
    a = int(input("isso não é um numero valido, digite outro numero: "))

print(f"o numero {a} é válido")
