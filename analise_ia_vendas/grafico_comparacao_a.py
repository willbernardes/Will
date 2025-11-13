import matplotlib.pyplot as plt
import numpy as np

# Configuração de fonte para melhor visualização
plt.rcParams['font.size'] = 10
plt.rcParams['figure.figsize'] = (12, 7)

# GRÁFICO DE COMPARAÇÃO A: Eficiência do Processo com/sem Automação
fig, ax = plt.subplots()

categorias = ['Taxa de\nResposta', 'Follow-up\nRealizado', 'Leads\nProspectados/dia',
              'Tempo de\nQualificação', 'Taxa de\nConversão']
sem_automacao = [25, 15, 10, 85, 8]  # Valores em %
com_automacao = [78, 92, 95, 18, 65]  # Valores em %

x = np.arange(len(categorias))
width = 0.35

bars1 = ax.bar(x - width/2, sem_automacao, width, label='Sem Automação',
               color='#FF6B6B', alpha=0.8)
bars2 = ax.bar(x + width/2, com_automacao, width, label='Com Automação IA',
               color='#4ECDC4', alpha=0.8)

# Adicionar valores nas barras
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.0f}%',
                ha='center', va='bottom', fontweight='bold', fontsize=9)

ax.set_xlabel('Parâmetros de Comparação', fontweight='bold', fontsize=11)
ax.set_ylabel('Eficiência (%)', fontweight='bold', fontsize=11)
ax.set_title('GRÁFICO DE COMPARAÇÃO A\nEficiência do Processo: Atual vs Com Automação IA',
             fontweight='bold', fontsize=13, pad=20)
ax.set_xticks(x)
ax.set_xticklabels(categorias)
ax.legend(loc='upper left', fontsize=10)
ax.grid(axis='y', alpha=0.3, linestyle='--')
ax.set_ylim(0, 110)

# Adicionar nota de rodapé
fig.text(0.5, 0.02, 'Fonte: Análise baseada em benchmarks de automação comercial B2B | Período: Projeção 12 meses (2025)\nMétodo: Comparação de performance entre processo manual vs automatizado',
         ha='center', fontsize=8, style='italic', color='gray')

plt.tight_layout(rect=[0, 0.05, 1, 1])
plt.savefig('/home/user/Will/analise_ia_vendas/graficos/comparacao_a_eficiencia.png',
            dpi=300, bbox_inches='tight')
print("✓ Gráfico de Comparação A gerado com sucesso!")
print("\nDados do Gráfico:")
print(f"Título: Eficiência do Processo: Atual vs Com Automação IA")
print(f"Eixo Y: Eficiência (%)")
print(f"Eixo X: Parâmetros de Comparação")
print("\nValores Sem Automação:")
for cat, val in zip(categorias, sem_automacao):
    print(f"  {cat.replace(chr(10), ' ')}: {val}%")
print("\nValores Com Automação IA:")
for cat, val in zip(categorias, com_automacao):
    print(f"  {cat.replace(chr(10), ' ')}: {val}%")
