def bonus_salario(salario):
    if salario >= 0 and salario <= 400.00:
        salario = salario * 1.15
    elif salario >= 400.01 and salario <= 800.00:
        salario = salario * 1.12
    elif salario >= 800.01 and salario <= 1200.00:
        salario = salario * 1.10
    elif salario >= 1200.01 and salario <= 2000.00:
        salario = salario * 1.07
    elif salario >= 2000.00:
        salario = salario * 1.04

    return salario

salary1 = float(input())
salary = bonus_salario(salary1)

print(f"Novo salario: {salary:.2f}")
print(f"Reajuste ganho: {(salary - salary1):.2f}")
print(f"Em percentual: {(salary / salary1 - 1)* 100:.0f} %")