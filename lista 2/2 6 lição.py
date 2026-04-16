valor_hora = float(input("Quanto você ganha por hora? "))
horas = float(input("Horas trabalhadas no mês: "))

salario_bruto = valor_hora * horas

ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05

descontos = ir + inss + sindicato
salario_liquido = salario_bruto - descontos

print("Salário Bruto: R$", salario_bruto)
print("IR (11%): R$", ir)
print("INSS (8%): R$", inss)
print("Sindicato (5%): R$", sindicato)
print("Salário Líquido: R$", salario_liquido)
