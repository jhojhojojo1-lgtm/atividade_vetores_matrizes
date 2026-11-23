#exercicio prova

cha= []
dia_s= ["Segunda-feira","Terça-feira","Quarta-feira","Quinta-feira","Sexta-feira"]
print('Controle de chamados do laboratório de informática')
for i in dia_s:
    while True:
        try:
            qtd=int(input(f'Digite a quantidade de chamados de {i}:'))
            if qtd<0:
                print('Erro!!! a quantidade não pode ser negativa. tente novamente')
            else:
                cha.append(qtd)
                break
        except ValueError:
            print('Erro!!! digite um número inteiro não negativo')
tlcha= sum(cha)
md_diaria= tlcha / len(cha)
M_quant= max(cha)
d_M_d= [dia_s[i] for i, qtd in enumerate(cha) if qtd == M_quant]
d_amd= [dia_s[i] for i, qtd in enumerate(cha) if qtd > md_diaria]
print("-"*40)
print("Relatório dos chamados")
print("-"*40)
print("\nRegistro diário")
for i in range (len(dia_s)):
    print(f"{dia_s[i]} chamados de {dia_s[i]}")
print(f"Total de chamados: {tlcha} ")
print(f"Média diário dos chamados: {md_diaria} ")
if len(d_M_d) ==1:
    print(f"Dia com maior demanda: {d_M_d[0]} ({M_quant} chamados)")
else:
    dias_str = ", ".join(d_M_d)
    print(f"Dias com maior demanda (empate): {dias_str} ({M_quant} chamados)")
if d_amd:
    print(f"Dias com chamados acima da média: {', '.join(d_amd)}")
else:
    print("Nenhum dia ficou acima da média.")
print("-" * 40)
