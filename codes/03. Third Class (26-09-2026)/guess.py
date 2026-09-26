secret_number = -105

print(
"""
+===================================+
| Bem vindo ao meu jogo, trouxa!    |
| Insira um número inteiro          |
| e adivinhar o número que tenho    |
| escolhidos para você.             |
| Então, qual é o número secreto?   |
+===================================+
""")

num = None
while(num != secret_number):
    num = int(input())
    if num == secret_number:
        print("Você ganhou!")