import matplotlib.pyplot as plt
import numpy as np

# Configuração de fonte para melhor visualização
plt.rcParams['font.size'] = 10
plt.rcParams['figure.figsize'] = (14, 9)

# GRÁFICO ATUAL X META: Gap Analysis
fig, ax = plt.subplots()

metricas = [
    'Contratos\nFechados/mês',
    'Leads\nQualificados/mês',
    'Taxa de\nConversão (%)',
    'Tempo de\nResposta (min)',
    'Follow-ups\nRealizados (%)',
    'Receita\nMensal (R$)',
    'Horas\nTrabalhadas/sem'
]

valores_atuais = [3, 25, 8, 240, 15, 4500, 50]
valores_meta = [21, 170, 65, 15, 92, 31500, 25]

x = np.arange(len(metricas))
width = 0.4

# Criar barras
bars_atuais = ax.bar(x - width/2, valores_atuais, width, label='Situação Atual',
                     color='#FF6B6B', alpha=0.8, edgecolor='black', linewidth=0.8)
bars_meta = ax.bar(x + width/2, valores_meta, width, label='Meta com Automação',
                   color='#4ECDC4', alpha=0.8, edgecolor='black', linewidth=0.8)

# Adicionar linhas horizontais de meta
for i, (atual, meta) in enumerate(zip(valores_atuais, valores_meta)):
    # Linha de meta
    ax.plot([i - 0.4, i + 0.4], [meta, meta], 'k--', linewidth=2, alpha=0.5)

    # Calcular gap
    gap = meta - atual
    gap_percent = (gap / meta) * 100

    # Adicionar seta de gap
    if gap > 0:
        ax.annotate('', xy=(i, meta), xytext=(i, atual),
                   arrowprops=dict(arrowstyle='<->', color='red', lw=2))

        # Adicionar texto do gap
        mid_point = (atual + meta) / 2
        if mid_point > max(valores_meta) * 0.7:
            ax.text(i + 0.5, mid_point, f'Gap:\n{gap_percent:.0f}%',
                   fontsize=8, ha='left', va='center',
                   bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.7))
        else:
            ax.text(i, mid_point, f'{gap_percent:.0f}%',
                   fontsize=8, ha='center', va='center',
                   bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.7))

# Adicionar valores nas barras
for bars in [bars_atuais, bars_meta]:
    for i, bar in enumerate(bars):
        height = bar.get_height()
        # Formatar valores especiais
        if i == 5:  # Receita
            label = f'R${height/1000:.1f}k'
        else:
            label = f'{height:.0f}'

        ax.text(bar.get_x() + bar.get_width()/2., height,
                label,
                ha='center', va='bottom', fontsize=8, fontweight='bold')

ax.set_xticks(x)
ax.set_xticklabels(metricas)
ax.set_ylabel('Valor da Métrica (unidades variadas)', fontweight='bold', fontsize=12)
ax.set_title('GRÁFICO ATUAL X META\nGap Analysis: Situação Atual vs Meta com Automação IA',
             fontweight='bold', fontsize=14, pad=20)
ax.legend(loc='upper left', fontsize=11)
ax.grid(axis='y', alpha=0.3, linestyle='--')

# Adicionar nota de rodapé
fig.text(0.5, 0.02, 'Fonte: Análise comparativa baseada em processo atual vs projetado | Período: Situação atual vs Meta 12 meses\nLinhas tracejadas horizontais = Valor da Meta | Setas vermelhas = Gap a ser fechado | Porcentagem = Gap em relação à meta',
         ha='center', fontsize=8, style='italic', color='gray', wrap=True)

plt.tight_layout(rect=[0, 0.05, 1, 1])
plt.savefig('/home/user/Will/analise_ia_vendas/graficos/atual_x_meta.png',
            dpi=300, bbox_inches='tight')
print("✓ Gráfico Atual x Meta gerado com sucesso!")
print("\nDados do Gráfico:")
print(f"Título: Gap Analysis - Situação Atual vs Meta com Automação IA")
print(f"Formato: Barras com Linhas de Meta")
print(f"Visualização: Gap analysis entre atual e meta")
print("\nComparação Atual vs Meta:")
for i, (metrica, atual, meta) in enumerate(zip(metricas, valores_atuais, valores_meta), 1):
    gap = meta - atual
    gap_percent = (gap / meta) * 100
    metrica_clean = metrica.replace('\n', ' ')

    if 'Receita' in metrica:
        print(f"{i}. {metrica_clean}")
        print(f"   Atual: R$ {atual:,.2f} | Meta: R$ {meta:,.2f} | Gap: {gap_percent:.0f}%")
    else:
        print(f"{i}. {metrica_clean}")
        print(f"   Atual: {atual} | Meta: {meta} | Gap: {gap_percent:.0f}%")
