# 📊 Sistema de Controle de Estoque

Sistema completo e otimizado para controle de estoque com:
- ✅ Geração automática de planilhas Excel
- ✅ Registro de entradas/saídas via terminal
- ✅ Dashboard de análise com gráficos
- ✅ Exportação para Power BI/Tableau
- ✅ **50% menos código** (otimizado e modular)

## �️ Arquitetura

Sistema modular com código otimizado:
- **utils.py** - Biblioteca compartilhada com funções reutilizáveis
- **Redução de 50.2%** no código dos scripts de registro
- **Funções centralizadas** para validações e operações comuns

## �🎯 Funcionalidades

### 📝 Planilha Excel Automática com 5 Abas:

1. **Base** - Cadastro de produtos
   - Código único do produto
   - Nome, descrição e tipo
   - Estoque mínimo e valor unitário
   - Fornecedor e localização

2. **Entradas** - Registro de compras/recebimentos
   - Data e documento fiscal
   - Produto e quantidade
   - Valores de compra (com cálculo automático do total)

3. **Saídas** - Registro de consumo/vendas
   - Data da movimentação
   - Produto e quantidade retirada
   - Motivo da saída

4. **Estoque Atual** - Saldo calculado automaticamente
   - Estoque inicial + entradas - saídas
   - Fórmulas automáticas com SUMIF

5. **Estoque Crítico** - Alerta de reposição
   - Compara estoque atual com estoque mínimo
   - Status automático (OK ou REPOR)

### 📈 Dashboard e Análises

- Gráficos visuais interativos
- KPIs principais do estoque
- Exportação para CSV (compatível com Power BI, Tableau, Looker)
- Relatórios automáticos

## 🚀 Como Usar

### 1. Instalar Dependências

```bash
pip3 install --index-url https://pypi.org/simple/ -r requirements.txt --user
```

Ou individualmente:
```bash
pip3 install --index-url https://pypi.org/simple/ openpyxl pandas matplotlib seaborn --user
```

### 2. Gerar a Planilha

```bash
python3 gerar_planilha.py
```

Isso criará o arquivo `Controle_Estoque.xlsx` com:
- ✅ Estrutura completa das 5 abas
- ✅ Dados de exemplo
- ✅ Fórmulas automáticas
- ✅ Formatação profissional

### 3. 🆕 Registrar Movimentações via Terminal

#### Registrar Entradas
```bash
python3 registrar_entrada.py
```

Sistema interativo para adicionar novas entradas de produtos:
- 📅 Data da entrada
- 📄 Documento/Nota Fiscal
- 🏷️  Código do produto
- 📦 Quantidade
- 💰 Valor unitário

#### Registrar Saídas
```bash
python3 registrar_saida.py
```

Sistema interativo para registrar saídas/consumo:
- 📅 Data da saída
- 🏷️  Código do produto
- 📤 Quantidade retirada
- 📝 Motivo da saída
- ⚠️ Alerta de estoque baixo

**Ver guia detalhado:** [GUIA_TERMINAL.md](GUIA_TERMINAL.md)

### 4. Gerar Dashboard e Análises

```bash
python3 analise_dashboard.py
```

Isso criará:
- 📊 `dashboard_estoque.png` - Dashboard visual com 6 gráficos
- 📁 `dados_csv/` - Pasta com CSVs para BI externo
- 📈 Relatório com KPIs no terminal

## � Arquivos do Sistema

### Scripts Principais
- **gerar_planilha.py** (289 linhas) - Cria planilha Excel inicial
- **registrar_entrada.py** (70 linhas) - Registro interativo de entradas
- **registrar_saida.py** (97 linhas) - Registro interativo de saídas
- **analise_dashboard.py** (268 linhas) - Gera dashboard e relatórios
- **exportar_para_BI.py** (332 linhas) - Exporta para ferramentas de BI

### Arquivos de Suporte
- **utils.py** (145 linhas) - 🆕 Funções compartilhadas e reutilizáveis
- **config.py** (25 linhas) - Configurações centralizadas
- **requirements.txt** - Dependências do projeto

### Documentação
- **readme.md** - Documentação principal
- **GUIA_TERMINAL.md** - Guia de uso dos registros via terminal
- **OTIMIZACAO.md** - Detalhes da otimização realizada
- **CORRECOES_APLICADAS.md** - Histórico de correções

## �📋 Estrutura da Planilha

### Aba: Base (Cadastro)
| Código | Nome | Descrição | Tipo | Estoque Mín | Valor | Fornecedor | Localização |
|--------|------|-----------|------|-------------|-------|------------|-------------|
| P001   | ... | ... | ... | 100 | R$ 0,50 | ... | A1 |

### Aba: Entradas
| Data | Documento | Produto | Quantidade | Valor Unit. | Valor Total |
|------|-----------|---------|------------|-------------|-------------|
| 01/01/2026 | NF-12345 | P001 | 500 | R$ 0,48 | =D*E |

### Aba: Saídas
| Data | Produto | Qtd Retirada | Motivo |
|------|---------|--------------|--------|
| 02/01/2026 | P001 | 150 | Uso em produção |

### Aba: Estoque Atual
| Produto | Estoque Inicial | Entradas | Saídas | Saldo |
|---------|----------------|----------|--------|-------|
| P001 | 0 | =SUMIF(...) | =SUMIF(...) | =B+C-D |

### Aba: Estoque Crítico
| Nome | Estoque Atual | Estoque Mín | Status |
|------|---------------|-------------|--------|
| Produto X | 50 | 100 | ⚠️ REPOR |

## 🎨 Visualizações do Dashboard

O dashboard gera 6 gráficos:

1. **Estoque Atual por Produto** - Gráfico de barras horizontal
2. **Distribuição de Valor** - Gráfico de pizza
3. **Status do Estoque** - Pizza (OK vs Crítico)
4. **Entradas vs Saídas** - Barras comparativas
5. **Produtos por Categoria** - Barras verticais
6. **Top 5 Mais Movimentados** - Ranking

## 💡 Dicas de Uso

### Como Adicionar Novos Produtos

1. Abra `Controle_Estoque.xlsx`
2. Vá na aba **Base**
3. Adicione uma nova linha com todos os dados
4. As outras abas se atualizarão automaticamente

### Como Registrar uma Entrada

1. Aba **Entradas**
2. Adicione: Data, Nota Fiscal, Código do Produto, Quantidade, Valor
3. A coluna "Valor Total" calcula automaticamente

### Como Registrar uma Saída

1. Aba **Saídas**
2. Adicione: Data, Código do Produto, Quantidade, Motivo
3. O estoque é recalculado automaticamente

### Verificar Produtos para Repor

1. Vá na aba **Estoque Crítico**
2. Produtos com "⚠️ REPOR" estão abaixo do mínimo
3. Use esse relatório para fazer pedidos

## 🔄 Integração com BI

### Opção 1: Usar o Excel direto

Importe `Controle_Estoque.xlsx` diretamente no Power BI ou Tableau

### Opção 2: Usar os CSVs

1. Execute `python analise_dashboard.py`
2. Use os arquivos da pasta `dados_csv/`
3. Importe no Power BI, Tableau, Looker, Google Data Studio, etc.

### Opção 3: Banco de Dados

Para volumes maiores, considere migrar para:
- SQLite (simples, arquivo local)
- PostgreSQL (robusto, multi-usuário)
- MySQL (popular, bem suportado)

## 📊 KPIs Disponíveis

O relatório automático mostra:

- 📦 Total de produtos cadastrados
- 💰 Valor total em estoque (R$)
- ⚠️ Produtos em estoque crítico
- 📊 Total de movimentações (entradas/saídas)
- 🏆 Produto mais movimentado
- 📂 Categoria com mais produtos
- 🏭 Fornecedor principal

## 🎯 Melhorias Implementadas e Futuras

### ✅ Implementado (Fevereiro 2026)
- [x] **Registro via terminal** - Entradas e saídas interativas
- [x] **Validações automáticas** - Produtos, datas, quantidades
- [x] **Alerta de estoque baixo** - Avisa antes de retirar
- [x] **Código otimizado** - 50% de redução, modular
- [x] **Biblioteca compartilhada** - utils.py com funções reutilizáveis
- [x] **Exportação para BI** - Power BI, Tableau, Looker
- [x] **Dashboard visual** - 6 gráficos automáticos

### 📋 Planejado
- [ ] Interface web (Flask/Django/Streamlit)
- [ ] Controle de lotes e validade
- [ ] Múltiplos almoxarifados
- [ ] Alertas por email quando estoque crítico
- [ ] Integração com sistema de vendas
- [ ] Histórico de preços
- [ ] Previsão de demanda (ML)
- [ ] Curva ABC de produtos
- [ ] Controle de movimentação por usuário
- [ ] Código de barras / QR Code

## � Funções Utilitárias (utils.py)

Biblioteca compartilhada que elimina duplicação de código:

```python
from utils import *

# Validações
validar_data(data_str)           # Valida formato DD/MM/YYYY
obter_data(mensagem)             # Obtém data com validação automática
obter_numero(msg, decimal, min)  # Obtém número validado

# Interface
limpar_tela()                    # Limpa terminal
confirmar(mensagem)              # Confirmação s/n
pausar()                         # Aguarda Enter

# Dados
carregar_produtos()              # Carrega planilha Base
obter_produto(df_base)           # Valida e obtém código
listar_produtos_completo()       # Lista formatada
salvar_na_planilha(aba, dados)   # Salva no Excel
```

**Benefícios:**
- ✅ Código 50% menor nos scripts
- ✅ Manutenção em um único lugar
- ✅ Facilita criação de novos scripts
- ✅ Menos bugs por duplicação

## �📝 Personalização

Para adaptar à sua necessidade:

### Modificar Categorias de Produtos

Edite em `gerar_planilha.py`, na variável `produtos_exemplo`, coluna "Tipo de Produto"

### Adicionar Mais Colunas

1. Edite os `headers_*` em `gerar_planilha.py`
2. Adicione os dados em `*_exemplo`
3. Ajuste as larguras das colunas

### Mudar Cores do Dashboard

Em `analise_dashboard.py`, modifique:
```python
plt.style.use('seaborn-v0_8-darkgrid')  # Mude o estilo
sns.set_palette("husl")  # Mude a paleta de cores
```

## 🤝 Contribuindo

Sinta-se livre para melhorar este sistema:

1. Adicione novas funcionalidades
2. Melhore os gráficos
3. Crie novos relatórios
4. Otimize as fórmulas

## 📄 Licença

Livre para uso pessoal e comercial.

## 🆘 Problemas Comuns

### "ModuleNotFoundError: No module named 'openpyxl'"
```bash
pip3 install --index-url https://pypi.org/simple/ openpyxl pandas matplotlib seaborn --user
```

### "File not found: Controle_Estoque.xlsx"
Execute primeiro:
```bash
python3 gerar_planilha.py
```

### "No module named 'utils'"
Certifique-se de estar no diretório correto:
```bash
cd "Controle de estoque"
python3 registrar_entrada.py
```

### Fórmulas não calculam no Excel
- Abra o Excel
- Pressione Ctrl+Alt+F9 para recalcular

### Gráficos não aparecem
Verifique se tem matplotlib instalado:
```bash
pip install matplotlib seaborn
```

## 📊 Estatísticas do Projeto

- **Total de linhas:** 1.226 linhas de código Python
- **Redução após otimização:** 627 linhas removidas (33.8%)
- **Scripts otimizados:** registrar_entrada.py (-75.8%), registrar_saida.py (-71.3%)
- **Tempo de desenvolvimento:** Otimizado para manutenção rápida
- **Cobertura:** 5 abas Excel, 6 gráficos, 10+ KPIs

## 📚 Documentação Completa

- **[GUIA_TERMINAL.md](GUIA_TERMINAL.md)** - Como usar registro via terminal
- **[OTIMIZACAO.md](OTIMIZACAO.md)** - Detalhes técnicos da otimização
- **[CORRECOES_APLICADAS.md](CORRECOES_APLICADAS.md)** - Histórico de melhorias

---

**Desenvolvido para facilitar o controle de estoque de pequenas e médias empresas** 📦✨

**Versão:** 2.0 (Otimizado) | **Data:** Fevereiro 2026
