a=float(input('qual o preço do produto: '))
b=float(input('porcentagem do desconto: '))
d=a*(b/100)
c=a-d
print(f'o valor do produto R${a} com o desconto de {b}% é de R${c} com o desocnto total de R${d}')
