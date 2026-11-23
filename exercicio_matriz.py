#exercicio prova 2

pr= ["Camisetas", "Canecas", "Bonés"]
peri= ["Dia 1 - Manhã", "Dia 1 - Tarde", "Dia 2 - Manhã", "Dia 2 - Tarde"]
mv= []
print("--- Controle de Vendas da Feira Tecnológica ---")
for i in range(len(pr)):
    linha_pr = []
    print(f"\n[Produto: {pr[i]}]")
    for j in range(len(peri)):
        while True:
            try:
                qtd = int(input(f"  Digite a quantidade vendida no período '{peri[j]}': "))
                if qtd < 0:
                    print("  Erro: A quantidade não pode ser negativa. Tente novamente.")
                else:
                    linha_pr.append(qtd)
                    break
            except ValueError:
                print("  Erro: Digite um número inteiro válido.")
    mv.append(linha_pr)
tpr= [sum(linha) for linha in mv]
tperi= []
for j in range(len(peri)):
    sm_colu= sum(mv[i][j] for i in range(len(pr)))
    tperi.append(sm_colu)
total= sum(tpr)
maior_venda_prod= max(tpr)
melhores_pr= [pr[i] for i, t in enumerate(tperi) if t == maior_venda_prod]
maior_mov_per= max(tperi)
melhores_peri= [peri[j] for j, t in enumerate(tperi) if t == maior_mov_per]
print("\n" + "-"*50)
print("             RELATÓRIO FINAL DA FEIRA             ")
print("-"*50)
print("\n--- Matriz de Vendas (Produto x Período) ---")
cabecalho= f"{'Produto':<12}" + "".join([f"{p[:10]:<14}" for p in peri]) + f"{'Total':<10}"
print(cabecalho)
print("-" * len(cabecalho))
for i in range(len(pr)):
    linha_str = f"{pr[i]:<12}"
    for j in range(len(peri)):
        linha_str += f"{mv[i][j]:<14}"
    linha_str += f"{tpr[i]:<10}"
    print(linha_str)
totais_str= f"{'Total/Per':<12}"
for t in tperi:
    totais_str += f"{t:<14}"
totais_str += f"{total:<10}"
print("-" * len(cabecalho))
print(totais_str)
print("\n--- Estatísticas e Destaques ---")
print(f"Total geral de itens vendidos: {total} unidades")
if len(melhores_pr) == 1:
    print(f"Produto destaque em vendas: {melhores_pr[0]} ({maior_venda_prod} unidades)")
else:
    print(f"Produtos destaque (empate): {', '.join(melhores_pr)} ({maior_venda_prod} unidades)")
if len(melhores_peri) == 1:
    print(f"Período de maior movimento: {melhores_peri[0]} ({maior_mov_per} unidades)")
else:
    print(f"Períodos de maior movimento (empate): {', '.join(melhores_peri)} ({maior_mov_per} unidades)")
print("-"*50)
