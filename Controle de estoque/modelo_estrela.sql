
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
