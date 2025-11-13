import matplotlib.pyplot as plt
import numpy as np

# Configuração de fonte para melhor visualização
plt.rcParams['font.size'] = 10
plt.rcParams['figure.figsize'] = (12, 8)

# GRÁFICO DE COMPARAÇÃO B: Ranking de Benefícios Quantificados
fig, ax = plt.subplots()

beneficios = [
    'Aumento em Contratos Fechados/mês',
    'Redução em Tempo de Resposta',
    'Economia de Horas/semana',
    'Aumento em Leads Qualificados/mês',
    'Melhoria na Taxa de Conversão',
    'Redução em Custo por Lead',
    'Aumento em Receita Mensal'
]

valores = [18, 8.5, 25, 145, 57, 62, 12500]  # Valores em diferentes unidades
unidades = ['contratos', 'horas', 'horas', 'leads', '%', '%', 'R$']
cores = ['#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#DFE6E9', '#74B9FF', '#A29BFE']

# Criar barras horizontais
y_pos = np.arange(len(beneficios))
bars = ax.barh(y_pos, valores, color=cores, alpha=0.8, edgecolor='black', linewidth=0.7)

# Adicionar valores nas barras
for i, (bar, valor, unidade) in enumerate(zip(bars, valores, unidades)):
    width = bar.get_width()
    if unidade == 'R$':
        label = f'R$ {valor:,.0f}'
    elif unidade == '%':
        label = f'{valor:.0f}%'
    else:
        label = f'{valor:.0f} {unidade}'

    ax.text(width, bar.get_y() + bar.get_height()/2.,
            f'  {label}',
            ha='left', va='center', fontweight='bold', fontsize=10)

ax.set_yticks(y_pos)
ax.set_yticklabels(beneficios)
ax.invert_yaxis()  # Ranking do topo para baixo
ax.set_xlabel('Valor do Benefício (unidades variadas)', fontweight='bold', fontsize=11)
ax.set_title('GRÁFICO DE COMPARAÇÃO B\nRanking de Benefícios Quantificados da Automação IA',
             fontweight='bold', fontsize=13, pad=20)
ax.grid(axis='x', alpha=0.3, linestyle='--')

# Adicionar nota de rodapé
fig.text(0.5, 0.02, 'Fonte: Projeção baseada em implementação de automação comercial | Período: 12 meses após implementação\nUnidades: Contratos (unidades), Tempo (horas), Leads (quantidade), Conversão (%), Receita (R$)',
         ha='center', fontsize=8, style='italic', color='gray')

plt.tight_layout(rect=[0, 0.05, 1, 1])
plt.savefig('/home/user/Will/analise_ia_vendas/graficos/comparacao_b_beneficios.png',
            dpi=300, bbox_inches='tight')
print("✓ Gráfico de Comparação B gerado com sucesso!")
print("\nDados do Gráfico:")
print(f"Título: Ranking de Benefícios Quantificados da Automação IA")
print(f"Formato: Barras Horizontais (Ranking)")
print(f"Unidades: Variadas conforme métrica")
print("\nRanking de Benefícios:")
for i, (benef, val, uni) in enumerate(zip(beneficios, valores, unidades), 1):
    if uni == 'R$':
        print(f"{i}. {benef}: R$ {val:,.2f}")
    elif uni == '%':
        print(f"{i}. {benef}: {val:.0f}%")
    else:
        print(f"{i}. {benef}: {val:.0f} {uni}")
