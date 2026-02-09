"""
Análise de Dados e Dashboard para Controle de Estoque
Gera visualizações e relatórios para BI
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Configurar estilo dos gráficos
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

def carregar_dados(arquivo="Controle_Estoque.xlsx"):
    """Carrega os dados da planilha"""
    try:
        abas = ['Base', 'Entradas', 'Saídas', 'Estoque Atual', 'Estoque Crítico']
        return [pd.read_excel(arquivo, sheet_name=aba) for aba in abas]
    except FileNotFoundError:
        print("❌ Arquivo não encontrado! Execute: python3 gerar_planilha.py")
        return [None] * 5


def gerar_dashboard(base, entradas, saidas, estoque, critico):
    """Gera um dashboard completo com visualizações"""
    
    # Criar figura com múltiplos gráficos
    fig = plt.figure(figsize=(16, 10))
    fig.suptitle('📊 DASHBOARD - CONTROLE DE ESTOQUE', fontsize=20, fontweight='bold', y=0.98)
    
    # Configurar para não mostrar warnings de valores vazios
    import warnings
    warnings.filterwarnings('ignore')
    
    # ===== GRÁFICO 1: Estoque Atual por Produto =====
    ax1 = plt.subplot(2, 3, 1)
    
    # Merge para pegar nomes dos produtos
    estoque_nomes = pd.merge(
        estoque, 
        base[['Código', 'Nome do Produto']], 
        left_on='Produto / Material', 
        right_on='Código'
    )
    
    cores = plt.cm.viridis(range(len(estoque_nomes)))
    ax1.barh(estoque_nomes['Nome do Produto'], estoque_nomes['Saldo Atual'], color=cores)
    ax1.set_xlabel('Quantidade', fontweight='bold')
    ax1.set_title('Estoque Atual por Produto', fontweight='bold', pad=10)
    ax1.grid(axis='x', alpha=0.3)
    
    # Ajustar limites do eixo X baseado nos dados
    max_estoque = estoque_nomes['Saldo Atual'].max()
    if pd.notna(max_estoque) and max_estoque > 0:
        ax1.set_xlim(0, max_estoque * 1.15)  # 15% de margem
    else:
        ax1.set_xlim(0, 10)  # Valor padrão quando não há dados
    
    # ===== GRÁFICO 2: Valor Total em Estoque =====
    ax2 = plt.subplot(2, 3, 2)
    
    # Calcular valor total (saldo * valor unitário)
    estoque_valor = pd.merge(
        estoque_nomes,
        base[['Código', 'Valor Unitário (R$)']],
        on='Código'
    )
    estoque_valor['Valor Total'] = estoque_valor['Saldo Atual'] * estoque_valor['Valor Unitário (R$)']
    
    # Verificar se há valores para plotar
    if estoque_valor['Valor Total'].sum() > 0:
        ax2.pie(estoque_valor['Valor Total'], 
                labels=estoque_valor['Nome do Produto'], 
                autopct='%1.1f%%',
                startangle=90)
    else:
        ax2.text(0.5, 0.5, 'Sem dados\nde valor', 
                ha='center', va='center', transform=ax2.transAxes,
                fontsize=12, color='gray')
    ax2.set_title('Distribuição de Valor em Estoque (R$)', fontweight='bold', pad=10)
    
    # ===== GRÁFICO 3: Status do Estoque (Crítico/OK) =====
    ax3 = plt.subplot(2, 3, 3)
    
    # Contar quantos estão OK vs REPOR
    status_count = critico['Status (Ex.: \'Repor\' / \'OK\')'].str.contains('REPOR', na=False).value_counts()
    labels_status = ['✓ OK', '⚠️ Crítico']
    colors_status = ['#90EE90', '#FFB6C1']
    
    ok_count = status_count.get(False, 0)
    critico_count = status_count.get(True, 0)
    
    if ok_count + critico_count > 0:
        ax3.pie([ok_count, critico_count], 
                labels=labels_status,
                autopct='%1.0f%%',
                colors=colors_status,
                startangle=90,
                textprops={'fontsize': 12, 'fontweight': 'bold'})
    else:
        ax3.text(0.5, 0.5, 'Sem dados\nde status', 
                ha='center', va='center', transform=ax3.transAxes,
                fontsize=12, color='gray')
    ax3.set_title('Status de Estoque', fontweight='bold', pad=10)
    
    # ===== GRÁFICO 4: Entradas vs Saídas por Produto =====
    ax4 = plt.subplot(2, 3, 4)
    
    # Agrupar entradas e saídas por produto
    entradas_total = entradas.groupby('Produto / Material')['Quantidade'].sum()
    saidas_total = saidas.groupby('Produto / Material')['Quantidade Retirada'].sum()
    
    # Criar dataframe comparativo
    comparacao = pd.DataFrame({
        'Entradas': entradas_total,
        'Saídas': saidas_total
    }).fillna(0)
    
    x = range(len(comparacao))
    width = 0.35
    
    ax4.bar([i - width/2 for i in x], comparacao['Entradas'], width, label='Entradas', color='#4CAF50')
    ax4.bar([i + width/2 for i in x], comparacao['Saídas'], width, label='Saídas', color='#F44336')
    
    ax4.set_xlabel('Produtos', fontweight='bold')
    ax4.set_ylabel('Quantidade', fontweight='bold')
    ax4.set_title('Movimentação: Entradas vs Saídas', fontweight='bold', pad=10)
    ax4.set_xticks(x)
    ax4.set_xticklabels(comparacao.index, rotation=45, ha='right')
    ax4.legend()
    ax4.grid(axis='y', alpha=0.3)
    
    # Ajustar limites do eixo Y baseado nos dados
    max_movimentacao = max(comparacao['Entradas'].max(), comparacao['Saídas'].max())
    if pd.notna(max_movimentacao) and max_movimentacao > 0:
        ax4.set_ylim(0, max_movimentacao * 1.15)  # 15% de margem
    
    # ===== GRÁFICO 5: Produtos por Categoria =====
    ax5 = plt.subplot(2, 3, 5)
    
    categoria_count = base['Tipo de Produto'].value_counts()
    cores_cat = plt.cm.Set3(range(len(categoria_count)))
    
    ax5.bar(categoria_count.index, categoria_count.values, color=cores_cat)
    ax5.set_xlabel('Categoria', fontweight='bold')
    ax5.set_ylabel('Quantidade de Produtos', fontweight='bold')
    ax5.set_title('Produtos por Categoria', fontweight='bold', pad=10)
    ax5.tick_params(axis='x', rotation=45)
    ax5.grid(axis='y', alpha=0.3)
    
    # Ajustar limites do eixo Y baseado nos dados
    max_categoria = categoria_count.max()
    if pd.notna(max_categoria) and max_categoria > 0:
        ax5.set_ylim(0, max_categoria * 1.2)  # 20% de margem
    
    # ===== GRÁFICO 6: Top 5 Produtos Mais Movimentados =====
    ax6 = plt.subplot(2, 3, 6)
    
    # Calcular total de movimentação (entradas + saídas)
    entradas_produto = entradas.groupby('Produto / Material')['Quantidade'].sum()
    saidas_produto = saidas.groupby('Produto / Material')['Quantidade Retirada'].sum()
    
    movimentacao = pd.DataFrame({
        'Total': entradas_produto.add(saidas_produto, fill_value=0)
    }).sort_values('Total', ascending=False).head(5)
    
    cores_top = plt.cm.Oranges(range(len(movimentacao), 0, -1))
    ax6.barh(movimentacao.index, movimentacao['Total'], color=cores_top)
    ax6.set_xlabel('Quantidade Movimentada', fontweight='bold')
    ax6.set_title('Top 5 Produtos Mais Movimentados', fontweight='bold', pad=10)
    ax6.grid(axis='x', alpha=0.3)
    
    # Ajustar limites do eixo X baseado nos dados
    max_movimentacao_top = movimentacao['Total'].max()
    if pd.notna(max_movimentacao_top) and max_movimentacao_top > 0:
        ax6.set_xlim(0, max_movimentacao_top * 1.15)  # 15% de margem
    
    plt.tight_layout()
    plt.savefig('dashboard_estoque.png', dpi=300, bbox_inches='tight')
    print("\n✅ Dashboard salvo como 'dashboard_estoque.png'")
    plt.show()


def gerar_relatorio(base, entradas, saidas, estoque, critico):
    """Gera relatório textual com KPIs"""
    
    print("\n" + "="*70)
    print("📈 RELATÓRIO DE ESTOQUE - KPIs PRINCIPAIS")
    print("="*70)
    
    # Total de produtos cadastrados
    total_produtos = len(base)
    print(f"\n📦 Total de Produtos Cadastrados: {total_produtos}")
    
    # Valor total em estoque
    estoque_com_valor = pd.merge(
        estoque,
        base[['Código', 'Valor Unitário (R$)']],
        left_on='Produto / Material',
        right_on='Código'
    )
    estoque_com_valor['Valor Total'] = estoque_com_valor['Saldo Atual'] * estoque_com_valor['Valor Unitário (R$)']
    valor_total = estoque_com_valor['Valor Total'].sum()
    
    print(f"💰 Valor Total em Estoque: R$ {valor_total:,.2f}")
    
    # Produtos críticos (abaixo do mínimo)
    produtos_criticos = critico[critico['Status (Ex.: \'Repor\' / \'OK\')'].str.contains('REPOR', na=False)]
    num_criticos = len(produtos_criticos)
    
    print(f"⚠️  Produtos em Estoque Crítico: {num_criticos}")
    
    if num_criticos > 0:
        print("\n   Produtos que precisam reposição:")
        for idx, row in produtos_criticos.iterrows():
            print(f"   • {row['Nome do Produto']}: {row['Estoque Atual']:.0f} (mínimo: {row['Estoque Mínimo']:.0f})")
    
    # Total de movimentações
    total_entradas = len(entradas)
    total_saidas = len(saidas)
    
    print(f"\n📊 Movimentações:")
    print(f"   ↗️  Entradas registradas: {total_entradas}")
    print(f"   ↘️  Saídas registradas: {total_saidas}")
    
    # Produto mais movimentado
    if total_entradas > 0 or total_saidas > 0:
        entradas_por_produto = entradas.groupby('Produto / Material')['Quantidade'].sum()
        saidas_por_produto = saidas.groupby('Produto / Material')['Quantidade Retirada'].sum()
        movimentacao_total = entradas_por_produto.add(saidas_por_produto, fill_value=0)
        
        if len(movimentacao_total) > 0 and movimentacao_total.max() > 0:
            produto_top = movimentacao_total.idxmax()
            qtd_top = movimentacao_total.max()
            produto_info = base[base['Código'] == produto_top]['Nome do Produto']
            
            if len(produto_info) > 0:
                nome_top = produto_info.values[0]
                print(f"\n🏆 Produto Mais Movimentado: {nome_top} ({produto_top})")
                print(f"   Total movimentado: {qtd_top:.0f} unidades")
            else:
                print(f"\n🏆 Produto Mais Movimentado: Nenhum")
        else:
            print(f"\n🏆 Produto Mais Movimentado: Nenhum")
    else:
        print(f"\n🏆 Produto Mais Movimentado: Nenhuma movimentação registrada")
    
    # Categoria com mais produtos
    if len(base) > 0 and 'Tipo de Produto' in base.columns:
        categoria_count = base['Tipo de Produto'].value_counts()
        if len(categoria_count) > 0:
            categoria_top = categoria_count.idxmax()
            qtd_categoria = categoria_count.max()
            print(f"\n📂 Categoria com Mais Produtos: {categoria_top} ({qtd_categoria} produtos)")
        else:
            print(f"\n📂 Categoria com Mais Produtos: Nenhuma")
    
    # Fornecedor principal
    if len(base) > 0 and 'Fornecedor' in base.columns:
        fornecedor_count = base['Fornecedor'].value_counts()
        if len(fornecedor_count) > 0:
            fornecedor_top = fornecedor_count.idxmax()
            qtd_fornecedor = fornecedor_count.max()
            print(f"\n🏭 Fornecedor Principal: {fornecedor_top} ({qtd_fornecedor} produtos)")
        else:
            print(f"\n🏭 Fornecedor Principal: Nenhum")
    
    print("\n" + "="*70 + "\n")


def exportar_para_csv(base, entradas, saidas, estoque, critico):
    """Exporta dados para CSV (útil para BI externo)"""
    import os
    os.makedirs('dados_csv', exist_ok=True)
    
    dados = {'base_produtos': base, 'entradas': entradas, 'saidas': saidas, 
             'estoque_atual': estoque, 'estoque_critico': critico}
    
    for nome, df in dados.items():
        df.to_csv(f'dados_csv/{nome}.csv', index=False, encoding='utf-8-sig')
    
    print("✅ Dados exportados para 'dados_csv/'")
    print("   Pronto para Power BI, Tableau ou Looker!")


if __name__ == "__main__":
    print("\n🔄 Carregando dados da planilha...")
    
    base, entradas, saidas, estoque, critico = carregar_dados()
    
    if base is not None:
        print("✅ Dados carregados com sucesso!\n")
        
        # Gerar relatório
        gerar_relatorio(base, entradas, saidas, estoque, critico)
        
        # Gerar dashboard
        print("📊 Gerando dashboard visual...")
        gerar_dashboard(base, entradas, saidas, estoque, critico)
        
        # Exportar para CSV
        print("\n📁 Exportando dados para CSV...")
        exportar_para_csv(base, entradas, saidas, estoque, critico)
        
        print("\n✨ Análise completa!")
