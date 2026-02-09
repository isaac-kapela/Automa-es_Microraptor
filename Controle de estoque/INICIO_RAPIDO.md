# 📦 Controle de Estoque - Início Rápido

Sistema otimizado de controle de estoque com interface terminal e exportação para BI.

## ⚡ Instalação e Uso (3 passos)

### 1️⃣ Instalar
```bash
pip3 install --index-url https://pypi.org/simple/ openpyxl pandas matplotlib seaborn --user
```

### 2️⃣ Criar Planilha
```bash
python3 gerar_planilha.py
```

### 3️⃣ Usar o Sistema
```bash
python3 registrar_entrada.py    # Adicionar entradas
python3 registrar_saida.py       # Registrar saídas
python3 analise_dashboard.py     # Gerar relatórios
```

## 📋 Comandos Principais

| Comando | Função |
|---------|--------|
| `python3 gerar_planilha.py` | Cria planilha Excel com 5 abas |
| `python3 registrar_entrada.py` | Sistema interativo de entradas |
| `python3 registrar_saida.py` | Sistema interativo de saídas |
| `python3 analise_dashboard.py` | Gera dashboard PNG + CSVs |
| `python3 exportar_para_BI.py` | Exporta para Power BI/Tableau |

## 📊 O Que o Sistema Faz

- ✅ Cria planilha Excel com fórmulas automáticas
- ✅ Registra entradas e saídas via terminal (validação automática)
- ✅ Calcula estoque atual automaticamente
- ✅ Alerta quando estoque está baixo
- ✅ Gera dashboard com 6 gráficos
- ✅ Exporta para Power BI, Tableau, Looker
- ✅ KPIs e relatórios completos

## 🎯 Arquivos Gerados

```
Controle_Estoque.xlsx        # Planilha principal
dashboard_estoque.png        # Dashboard visual
dados_csv/                   # CSVs para análise
dados_power_bi/              # Dados para BI
modelo_estrela.sql           # Scripts SQL
```

## 📚 Documentação Completa

- **[readme.md](readme.md)** - Documentação detalhada
- **[GUIA_TERMINAL.md](GUIA_TERMINAL.md)** - Guia de uso terminal
- **[OTIMIZACAO.md](OTIMIZACAO.md)** - Detalhes técnicos

## 💡 Exemplo de Uso

```bash
# 1. Criar planilha inicial
python3 gerar_planilha.py

# 2. Adicionar entrada de 1000 parafusos
python3 registrar_entrada.py
# Escolher opção 1, preencher dados

# 3. Registrar saída de 200 parafusos
python3 registrar_saida.py
# Escolher opção 1, preencher dados

# 4. Gerar relatório visual
python3 analise_dashboard.py
```

## 🏗️ Arquitetura (Otimizada)

- **utils.py** (145 linhas) - Biblioteca compartilhada
- **registrar_entrada.py** (70 linhas) - 75% menor após otimização
- **registrar_saida.py** (97 linhas) - 71% menor após otimização
- **Redução total:** 50% menos código, mais eficiente

## ❓ Problemas Comuns

**"ModuleNotFoundError"**
```bash
pip3 install --index-url https://pypi.org/simple/ -r requirements.txt --user
```

**"Arquivo não encontrado"**
```bash
python3 gerar_planilha.py  # Execute primeiro
```

**"Arquivo está aberto"**
- Feche o Excel antes de registrar movimentações

## 📈 Estatísticas

- 📦 1.226 linhas de código Python
- 🎯 50% de redução após otimização
- 📊 5 abas Excel + 6 gráficos
- ⚡ Validação automática de dados
- 🔧 Modular e fácil de manter

---

**Versão 2.0 (Otimizado)** | Fev 2026 | Pronto para produção ✨
