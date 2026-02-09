"""
Exemplo de integração com Power BI ou outros sistemas de BI
Exporta dados em formatos otimizados para análise
"""

import pandas as pd
from datetime import datetime

def preparar_dados_para_bi(arquivo="Controle_Estoque.xlsx"):
    """
    Prepara e enriquece os dados para análise em ferramentas de BI
    """
    
    # Ler dados
    base = pd.read_excel(arquivo, sheet_name='Base')
    entradas = pd.read_excel(arquivo, sheet_name='Entradas')
    saidas = pd.read_excel(arquivo, sheet_name='Saídas')
    estoque = pd.read_excel(arquivo, sheet_name='Estoque Atual')
    
    # ===== TABELA FATO: MOVIMENTAÇÕES =====
    # Combinar entradas e saídas em uma única tabela
    
    # Preparar entradas
    entradas_prep = entradas.copy()
    entradas_prep['Tipo_Movimentacao'] = 'Entrada'
    entradas_prep['Quantidade_Movimento'] = entradas_prep['Quantidade']
    entradas_prep = entradas_prep.rename(columns={
        'Produto / Material': 'Codigo_Produto',
        'Data da Entrada': 'Data_Movimentacao',
        'Documento (Nota Fiscal / Nº de Compra)': 'Documento',
        'Valor Unitário de Compra (R$)': 'Valor_Unitario'
    })
    
    # Preparar saídas
    saidas_prep = saidas.copy()
    saidas_prep['Tipo_Movimentacao'] = 'Saída'
    saidas_prep['Quantidade_Movimento'] = -saidas_prep['Quantidade Retirada']
    saidas_prep['Valor_Unitario'] = None
    saidas_prep['Documento'] = saidas_prep['Motivo da Saída']
    saidas_prep = saidas_prep.rename(columns={
        'Produto / Material': 'Codigo_Produto',
        'Data da Saída': 'Data_Movimentacao'
    })
    
    # Combinar
    colunas_comuns = ['Data_Movimentacao', 'Codigo_Produto', 'Quantidade_Movimento', 
                      'Tipo_Movimentacao', 'Documento', 'Valor_Unitario']
    
    movimentacoes = pd.concat([
        entradas_prep[colunas_comuns],
        saidas_prep[colunas_comuns]
    ], ignore_index=True)
    
    # Converter data para datetime
    movimentacoes['Data_Movimentacao'] = pd.to_datetime(movimentacoes['Data_Movimentacao'], 
                                                          format='%d/%m/%Y', errors='coerce')
    
    # Adicionar dimensões de tempo
    movimentacoes['Ano'] = movimentacoes['Data_Movimentacao'].dt.year
    movimentacoes['Mes'] = movimentacoes['Data_Movimentacao'].dt.month
    movimentacoes['Mes_Nome'] = movimentacoes['Data_Movimentacao'].dt.strftime('%B')
    movimentacoes['Dia'] = movimentacoes['Data_Movimentacao'].dt.day
    movimentacoes['Dia_Semana'] = movimentacoes['Data_Movimentacao'].dt.day_name()
    movimentacoes['Trimestre'] = movimentacoes['Data_Movimentacao'].dt.quarter
    
    # ===== TABELA DIMENSÃO: PRODUTOS =====
    dim_produtos = base.copy()
    dim_produtos = dim_produtos.rename(columns={
        'Código': 'Codigo_Produto',
        'Nome do Produto': 'Nome_Produto',
        'Descrição': 'Descricao',
        'Tipo de Produto': 'Categoria',
        'Estoque Mínimo': 'Estoque_Minimo',
        'Valor Unitário (R$)': 'Valor_Unitario',
        'Fornecedor': 'Fornecedor',
        'Localização': 'Localizacao'
    })
    
    # ===== TABELA DIMENSÃO: FORNECEDORES =====
    dim_fornecedores = base[['Fornecedor']].drop_duplicates().reset_index(drop=True)
    dim_fornecedores['ID_Fornecedor'] = dim_fornecedores.index + 1
    
    # ===== TABELA DIMENSÃO: CATEGORIAS =====
    dim_categorias = base[['Tipo de Produto']].drop_duplicates().reset_index(drop=True)
    dim_categorias = dim_categorias.rename(columns={'Tipo de Produto': 'Categoria'})
    dim_categorias['ID_Categoria'] = dim_categorias.index + 1
    
    # ===== TABELA FATO: ESTOQUE ATUAL =====
    fato_estoque = estoque.copy()
    fato_estoque = fato_estoque.rename(columns={
        'Produto / Material': 'Codigo_Produto',
        'Estoque Inicial': 'Estoque_Inicial',
        'Total de Entradas': 'Total_Entradas',
        'Total de Saídas': 'Total_Saidas',
        'Saldo Atual': 'Saldo_Atual'
    })
    
    # Adicionar data de referência
    fato_estoque['Data_Referencia'] = datetime.now().strftime('%Y-%m-%d')
    
    # Juntar com informações de produtos
    fato_estoque = fato_estoque.merge(
        dim_produtos[['Codigo_Produto', 'Nome_Produto', 'Categoria', 
                      'Valor_Unitario', 'Estoque_Minimo']],
        on='Codigo_Produto',
        how='left'
    )
    
    # Calcular métricas adicionais
    fato_estoque['Valor_Total_Estoque'] = fato_estoque['Saldo_Atual'] * fato_estoque['Valor_Unitario']
    fato_estoque['Status_Estoque'] = fato_estoque.apply(
        lambda row: 'Crítico' if row['Saldo_Atual'] < row['Estoque_Minimo'] else 'Normal',
        axis=1
    )
    fato_estoque['Deficit_Estoque'] = fato_estoque.apply(
        lambda row: max(0, row['Estoque_Minimo'] - row['Saldo_Atual']),
        axis=1
    )
    
    return {
        'fato_movimentacoes': movimentacoes,
        'fato_estoque_atual': fato_estoque,
        'dim_produtos': dim_produtos,
        'dim_fornecedores': dim_fornecedores,
        'dim_categorias': dim_categorias
    }


def exportar_para_power_bi(dados, pasta_saida='dados_power_bi'):
    """
    Exporta dados em formato otimizado para Power BI
    """
    import os
    os.makedirs(pasta_saida, exist_ok=True)
    
    for nome, df in dados.items():
        arquivo = f"{pasta_saida}/{nome}.csv"
        df.to_csv(arquivo, index=False, encoding='utf-8-sig', sep=';', decimal=',')
        print(f"✅ {arquivo} criado")
    
    print(f"\n📊 Dados prontos para importar no Power BI!")
    print(f"   Pasta: {pasta_saida}/")


def gerar_modelo_estrela_sql(dados):
    """
    Gera scripts SQL para criar modelo estrela em banco de dados
    """
    
    sql_script = """
-- =============================================
-- MODELO ESTRELA - CONTROLE DE ESTOQUE
-- =============================================

-- TABELA DIMENSÃO: PRODUTOS
CREATE TABLE dim_produtos (
    codigo_produto VARCHAR(20) PRIMARY KEY,
    nome_produto VARCHAR(200),
    descricao TEXT,
    categoria VARCHAR(100),
    estoque_minimo DECIMAL(10,2),
    valor_unitario DECIMAL(10,2),
    fornecedor VARCHAR(200),
    localizacao VARCHAR(50)
);

-- TABELA DIMENSÃO: FORNECEDORES
CREATE TABLE dim_fornecedores (
    id_fornecedor INT PRIMARY KEY,
    nome_fornecedor VARCHAR(200)
);

-- TABELA DIMENSÃO: CATEGORIAS
CREATE TABLE dim_categorias (
    id_categoria INT PRIMARY KEY,
    nome_categoria VARCHAR(100)
);

-- TABELA DIMENSÃO: TEMPO
CREATE TABLE dim_tempo (
    data_completa DATE PRIMARY KEY,
    ano INT,
    mes INT,
    mes_nome VARCHAR(20),
    dia INT,
    dia_semana VARCHAR(20),
    trimestre INT,
    semana_ano INT
);

-- TABELA FATO: MOVIMENTAÇÕES
CREATE TABLE fato_movimentacoes (
    id_movimentacao INT PRIMARY KEY AUTO_INCREMENT,
    data_movimentacao DATE,
    codigo_produto VARCHAR(20),
    quantidade_movimento DECIMAL(10,2),
    tipo_movimentacao VARCHAR(20),
    documento VARCHAR(200),
    valor_unitario DECIMAL(10,2),
    valor_total DECIMAL(10,2),
    ano INT,
    mes INT,
    FOREIGN KEY (codigo_produto) REFERENCES dim_produtos(codigo_produto),
    FOREIGN KEY (data_movimentacao) REFERENCES dim_tempo(data_completa)
);

-- TABELA FATO: ESTOQUE ATUAL
CREATE TABLE fato_estoque_atual (
    codigo_produto VARCHAR(20) PRIMARY KEY,
    data_referencia DATE,
    estoque_inicial DECIMAL(10,2),
    total_entradas DECIMAL(10,2),
    total_saidas DECIMAL(10,2),
    saldo_atual DECIMAL(10,2),
    valor_total_estoque DECIMAL(10,2),
    status_estoque VARCHAR(20),
    deficit_estoque DECIMAL(10,2),
    FOREIGN KEY (codigo_produto) REFERENCES dim_produtos(codigo_produto)
);

-- ÍNDICES PARA PERFORMANCE
CREATE INDEX idx_mov_data ON fato_movimentacoes(data_movimentacao);
CREATE INDEX idx_mov_produto ON fato_movimentacoes(codigo_produto);
CREATE INDEX idx_mov_tipo ON fato_movimentacoes(tipo_movimentacao);
CREATE INDEX idx_estoque_status ON fato_estoque_atual(status_estoque);

-- VIEWS ÚTEIS PARA BI

-- View: Estoque com valor total
CREATE VIEW vw_estoque_valorizado AS
SELECT 
    e.codigo_produto,
    p.nome_produto,
    p.categoria,
    e.saldo_atual,
    p.valor_unitario,
    e.valor_total_estoque,
    e.status_estoque,
    p.estoque_minimo,
    e.deficit_estoque
FROM fato_estoque_atual e
JOIN dim_produtos p ON e.codigo_produto = p.codigo_produto;

-- View: Movimentações mensais
CREATE VIEW vw_movimentacoes_mensais AS
SELECT 
    m.ano,
    m.mes,
    m.tipo_movimentacao,
    p.categoria,
    COUNT(*) as num_movimentacoes,
    SUM(m.quantidade_movimento) as quantidade_total,
    SUM(m.valor_total) as valor_total
FROM fato_movimentacoes m
JOIN dim_produtos p ON m.codigo_produto = p.codigo_produto
GROUP BY m.ano, m.mes, m.tipo_movimentacao, p.categoria;

-- View: Top produtos movimentados
CREATE VIEW vw_top_produtos_movimentados AS
SELECT 
    p.codigo_produto,
    p.nome_produto,
    p.categoria,
    COUNT(*) as num_movimentacoes,
    SUM(ABS(m.quantidade_movimento)) as quantidade_total_movimentada
FROM fato_movimentacoes m
JOIN dim_produtos p ON m.codigo_produto = p.codigo_produto
GROUP BY p.codigo_produto, p.nome_produto, p.categoria
ORDER BY quantidade_total_movimentada DESC;

-- View: Produtos críticos
CREATE VIEW vw_produtos_criticos AS
SELECT 
    codigo_produto,
    nome_produto,
    categoria,
    saldo_atual,
    estoque_minimo,
    deficit_estoque,
    valor_total_estoque
FROM vw_estoque_valorizado
WHERE status_estoque = 'Crítico'
ORDER BY deficit_estoque DESC;
"""
    
    with open('modelo_estrela.sql', 'w', encoding='utf-8') as f:
        f.write(sql_script)
    
    print("\n✅ Script SQL criado: modelo_estrela.sql")
    print("   Use este script para criar o modelo em MySQL/PostgreSQL")


if __name__ == "__main__":
    print("\n🔄 Preparando dados para BI...")
    
    dados = preparar_dados_para_bi()
    
    print("\n📊 Estrutura de dados preparada:")
    for nome, df in dados.items():
        print(f"   • {nome}: {len(df)} registros, {len(df.columns)} colunas")
    
    # Exportar para Power BI
    print("\n📁 Exportando para Power BI...")
    exportar_para_power_bi(dados)
    
    # Gerar modelo SQL
    print("\n💾 Gerando modelo SQL...")
    gerar_modelo_estrela_sql(dados)
    
    print("\n" + "="*70)
    print("✨ PRONTO PARA USAR NO SEU BI!")
    print("="*70)
    print("\n📌 Próximos passos:")
    print("\n   POWER BI:")
    print("   1. Abra o Power BI Desktop")
    print("   2. Obter Dados → Texto/CSV")
    print("   3. Selecione os arquivos da pasta 'dados_power_bi/'")
    print("   4. Crie relacionamentos entre as tabelas")
    print("   5. Monte seus dashboards!")
    
    print("\n   TABLEAU:")
    print("   1. Abra o Tableau")
    print("   2. Conectar → Arquivo de texto")
    print("   3. Importe os CSVs da pasta 'dados_power_bi/'")
    print("   4. Crie seus gráficos")
    
    print("\n   BANCO DE DADOS (MySQL/PostgreSQL):")
    print("   1. Execute o script 'modelo_estrela.sql'")
    print("   2. Importe os CSVs usando ferramentas do banco")
    print("   3. Conecte seu BI direto no banco")
    
    print("\n" + "="*70 + "\n")
