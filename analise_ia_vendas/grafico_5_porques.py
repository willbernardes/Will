import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

# Configuração de fonte para melhor visualização
plt.rcParams['font.size'] = 10
plt.rcParams['figure.figsize'] = (14, 10)

# DIAGRAMA DOS 5 PORQUÊS: Análise de Causa Raiz
fig, ax = plt.subplots()

# Definir os 5 níveis de "Por quê?"
niveis = [
    {
        'titulo': 'PROBLEMA',
        'texto': 'Por que as vendas de energia por\nassinatura não estão escalando?',
        'y': 9,
        'cor': '#FF6B6B'
    },
    {
        'titulo': 'POR QUÊ? #1',
        'texto': 'Porque não consigo gerar leads\nqualificados de forma consistente',
        'y': 7,
        'cor': '#FFA07A'
    },
    {
        'titulo': 'POR QUÊ? #2',
        'texto': 'Porque não tenho processo de prospecção\nautomatizado e trabalho manualmente',
        'y': 5,
        'cor': '#FFD700'
    },
    {
        'titulo': 'POR QUÊ? #3',
        'texto': 'Porque não há sistema integrado de\nautomação para captar e nutrir leads',
        'y': 3,
        'cor': '#98FB98'
    },
    {
        'titulo': 'POR QUÊ? #4',
        'texto': 'Porque as ferramentas manuais\nnão permitem escala e follow-up efetivo',
        'y': 1,
        'cor': '#87CEEB'
    },
    {
        'titulo': 'CAUSA RAIZ',
        'texto': 'AUSÊNCIA DE AUTOMAÇÃO INTELIGENTE\nno processo comercial de ponta a ponta',
        'y': -1,
        'cor': '#9370DB'
    }
]

# Desenhar as caixas em cascata
for i, nivel in enumerate(niveis):
    # Posição X decrescente para criar efeito cascata
    x_pos = 10 - (i * 1.5)
    y_pos = nivel['y']
    width = 8
    height = 1.3

    # Desenhar caixa
    if i == len(niveis) - 1:  # Causa raiz destacada
        box = FancyBboxPatch((x_pos, y_pos), width, height,
                            boxstyle="round,pad=0.1",
                            edgecolor='black',
                            facecolor=nivel['cor'],
                            linewidth=3,
                            alpha=0.9)
    else:
        box = FancyBboxPatch((x_pos, y_pos), width, height,
                            boxstyle="round,pad=0.05",
                            edgecolor='black',
                            facecolor=nivel['cor'],
                            linewidth=1.5,
                            alpha=0.8)

    ax.add_patch(box)

    # Adicionar título
    ax.text(x_pos + width/2, y_pos + height + 0.15,
            nivel['titulo'],
            ha='center', va='bottom',
            fontsize=10, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='black', linewidth=1))

    # Adicionar texto
    font_size = 11 if i == len(niveis) - 1 else 9.5
    font_weight = 'bold' if i == len(niveis) - 1 else 'normal'

    ax.text(x_pos + width/2, y_pos + height/2,
            nivel['texto'],
            ha='center', va='center',
            fontsize=font_size, fontweight=font_weight)

    # Adicionar seta para o próximo nível
    if i < len(niveis) - 1:
        next_nivel = niveis[i + 1]
        next_x = 10 - ((i + 1) * 1.5)

        arrow = FancyArrowPatch((x_pos + width/2, y_pos),
                               (next_x + width/2, next_nivel['y'] + height),
                               arrowstyle='->,head_width=0.6,head_length=0.8',
                               color='red',
                               linewidth=2.5,
                               alpha=0.7)
        ax.add_patch(arrow)

# Configurações do gráfico
ax.set_xlim(-1, 12)
ax.set_ylim(-2.5, 11)
ax.axis('off')
ax.set_title('DIAGRAMA DOS 5 PORQUÊS\nAnálise de Causa Raiz: Por que o negócio não está escalando?',
             fontweight='bold', fontsize=15, pad=20)

# Adicionar legenda
legend_text = """
INTERPRETAÇÃO:
A análise dos 5 Porquês revela que o problema
de escalabilidade não é superficial, mas resultado
da ausência de automação no processo comercial.

SOLUÇÃO:
Implementar sistema de IA que automatize:
• Prospecção e captação de leads
• Qualificação e nutrição automática
• Follow-up inteligente via WhatsApp
• Simulações e propostas automatizadas
• Relatórios e análises em tempo real
"""

ax.text(0.5, -2, legend_text,
        ha='left', va='top',
        fontsize=9,
        bbox=dict(boxstyle='round,pad=0.5', facecolor='lightyellow', edgecolor='black', linewidth=1))

# Adicionar nota de rodapé
fig.text(0.5, 0.02, 'Fonte: Análise de Causa Raiz aplicando metodologia dos 5 Porquês | Método: Root Cause Analysis\nObjetivo: Identificar causa fundamental da falta de escalabilidade nas vendas',
         ha='center', fontsize=8, style='italic', color='gray')

plt.tight_layout(rect=[0, 0.04, 1, 1])
plt.savefig('/home/user/Will/analise_ia_vendas/graficos/5_porques_cascata.png',
            dpi=300, bbox_inches='tight')
print("✓ Diagrama dos 5 Porquês gerado com sucesso!")
print("\nDados do Diagrama:")
print(f"Título: Análise de Causa Raiz - Por que o negócio não está escalando?")
print(f"Formato: Diagrama em Cascata Descendente")
print(f"Metodologia: 5 Porquês (Root Cause Analysis)")
print("\nNíveis de Análise:")
for i, nivel in enumerate(niveis, 1):
    print(f"\nNível {i}: {nivel['titulo']}")
    print(f"  → {nivel['texto'].replace(chr(10), ' ')}")
print("\n" + "="*70)
print("CAUSA RAIZ IDENTIFICADA:")
print("  AUSÊNCIA DE AUTOMAÇÃO INTELIGENTE no processo comercial de ponta a ponta")
print("="*70)
