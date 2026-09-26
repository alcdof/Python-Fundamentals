vendas = int(input())
meta = 500

if vendas >= meta:
    print(f"Batemos a meta de vendas de cimento, vendemos {vendas} sacos.")
else:
    print(f"Infelizmente não batemos a meta de vendas de cimeto, vendemos {vendas} sacos. A meta era de {meta} sacos de cimento")