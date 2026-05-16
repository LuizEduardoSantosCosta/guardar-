a = int(input("qual seu primeiro numero: "))
b = int(input("qual seu segundo numero: "))
num1 = a
num2 = b
i = 2
l = 1
while a > 0 and b > 0:
    print('-'*25)
    print(f"conta {l} = {a}")
    print('-'*25)
    print(f"conta {i} = {b}")
    a = a % b
    if a == 0:
        mdc = b  
        break
    b = b % a
    if b == 0:
        mdc = a
        break
    i = i + 2
    l = l + 2
print('='*35)
print(f"O MDC entre {num1} e {num2} é: {mdc}")
print('='*35)
