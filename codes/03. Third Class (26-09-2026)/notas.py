nota = float(input())

if nota >= 7.0:
    print("Você está aprovado por média")
    if nota > 9.0:
        print("Parabéns!")
    print("Boas férias")
elif nota >= 4.0 and nota < 7.0:
    print("Você pode fazer a Substitutiva")
    print("Venha na Próxima Semana")
else: 
    print("Você está reprovado!")
    print("A gente se vê no próximo semestre")