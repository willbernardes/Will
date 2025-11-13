import matplotlib.pyplot as plt
import numpy as np

# Configuração de fonte para melhor visualização
plt.rcParams['font.size'] = 10
plt.rcParams['figure.figsize'] = (14, 8)

# GRÁFICO DE TENDÊNCIA: Evolução de Contratos Fechados ao Longo do Tempo
fig, ax = plt.subplots()

meses = ['Mês 1\n(Atual)', 'Mês 2', 'Mês 3', 'Mês 4', 'Mês 5', 'Mês 6',
         'Mês 7', 'Mês 8', 'Mês 9', 'Mês 10', 'Mês 11', 'Mês 12']

# Contratos fechados ao longo do tempo (evolução com automação)
contratos = [3, 5, 8, 12, 15, 18, 21, 23, 25, 26, 27, 28]

# Linha de tendência (regressão linear simples)
x_vals = np.arange(len(contratos))
z = np.polyfit(x_vals, contratos, 1)
p = np.poly1d(z)
tendencia = p(x_vals)

# Plotar linha principal
line = ax.plot(meses, contratos, marker='o', linewidth=3, markersize=10,
               color='#4ECDC4', label='Contratos Fechados', markerfacecolor='#FF6B6B',
               markeredgecolor='#4ECDC4', markeredgewidth=2)

# Plotar linha de tendência
ax.plot(meses, tendencia, linestyle='--', linewidth=2, color='#95A5A6',
        label='Linha de Tendência', alpha=0.7)

# Destacar pontos importantes
pontos_destaque = [0, 5, 11]  # Mês 1, Mês 6, Mês 12
labels_destaque = ['Início\nSem Automação', 'Implementação\nCompleta', 'Meta\nAlcançada']

for idx, label in zip(pontos_destaque, labels_destaque):
    ax.annotate(label,
                xy=(idx, contratos[idx]),
                xytext=(0, 25),
                textcoords='offset points',
                ha='center',
                fontsize=9,
                fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.7),
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0',
                               color='red', lw=2))

# Adicionar valores em cada ponto
for i, (mes, valor) in enumerate(zip(meses, contratos)):
    ax.text(i, valor + 1, f'{valor}',
            ha='center', va='bottom', fontsize=9, fontweight='bold')

ax.set_xlabel('Período de Análise (12 meses)', fontweight='bold', fontsize=12)
ax.set_ylabel('Número de Contratos Fechados', fontweight='bold', fontsize=12)
ax.set_title('GRÁFICO DE TENDÊNCIA\nEvolução de Contratos Fechados com Implementação da Automação IA',
             fontweight='bold', fontsize=14, pad=20)
ax.legend(loc='upper left', fontsize=11)
ax.grid(True, alpha=0.3, linestyle='--')
ax.set_ylim(0, 35)

# Adicionar área sombreada para destacar fase de crescimento
ax.axvspan(0, 2, alpha=0.1, color='red', label='Fase Manual')
ax.axvspan(2, 6, alpha=0.1, color='orange', label='Fase Transição')
ax.axvspan(6, 11, alpha=0.1, color='green', label='Fase Automação Completa')

# Adicionar nota de rodapé
fig.text(0.5, 0.02, 'Fonte: Projeção baseada em curva de adoção de automação comercial | Período: Jan-Dez 2025\nImplementação gradual: Meses 1-3 (Manual), Meses 4-6 (Transição), Meses 7-12 (Automação Completa)',
         ha='center', fontsize=8, style='italic', color='gray')

plt.tight_layout(rect=[0, 0.05, 1, 1])
plt.savefig('/home/user/Will/analise_ia_vendas/graficos/tendencia_evolucao.png',
            dpi=300, bbox_inches='tight')
print("✓ Gráfico de Tendência gerado com sucesso!")
print("\nDados do Gráfico:")
print(f"Título: Evolução de Contratos Fechados com Implementação da Automação IA")
print(f"Eixo Y: Número de Contratos Fechados")
print(f"Eixo X: Período de 12 meses")
print(f"Período: Janeiro a Dezembro 2025")
print("\nEvolução Mensal:")
for mes, valor in zip(meses, contratos):
    print(f"  {mes.replace(chr(10), ' ')}: {valor} contratos")
print(f"\nCrescimento Total: {contratos[0]} → {contratos[-1]} contratos (+{((contratos[-1]/contratos[0])-1)*100:.0f}%)")
