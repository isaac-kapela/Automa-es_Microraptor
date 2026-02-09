# 📚 Índice da Documentação - Sistema de Controle de Estoque

## 🚀 Para Começar

- **[INICIO_RAPIDO.md](INICIO_RAPIDO.md)** ⭐ **COMECE AQUI**
  - Instalação em 3 passos
  - Comandos principais
  - Exemplo rápido de uso
  - Solução de problemas comuns

## 📖 Documentação Principal

- **[readme.md](readme.md)** 📘 **Documentação Completa**
  - Visão geral do sistema
  - Funcionalidades detalhadas
  - Estrutura das planilhas
  - Exemplos e personalização
  - Integração com BI

## 🎯 Guias Específicos

- **[GUIA_TERMINAL.md](GUIA_TERMINAL.md)** 💻 **Registro via Terminal**
  - Como usar registrar_entrada.py
  - Como usar registrar_saida.py
  - Exemplos práticos
  - Dicas e atalhos
  - Troubleshooting

## 📊 Estrutura do Projeto

```
Controle de estoque/
│
├── 📚 DOCUMENTAÇÃO
│   ├── INDEX.md                    ← Você está aqui
│   ├── INICIO_RAPIDO.md            ← Comece por aqui!
│   ├── readme.md                   ← Documentação completa
│   ├── GUIA_TERMINAL.md            ← Uso dos registros
│
├── 🐍 CÓDIGO PYTHON
│   ├── utils.py                    ← Biblioteca compartilhada (145 linhas)
│   ├── config.py                   ← Configurações (25 linhas)
│   ├── gerar_planilha.py           ← Cria Excel (289 linhas)
│   ├── registrar_entrada.py        ← Entradas (70 linhas)
│   ├── registrar_saida.py          ← Saídas (97 linhas)
│   ├── analise_dashboard.py        ← Dashboard (268 linhas)
│   └── exportar_para_BI.py         ← Exportação BI (332 linhas)
│
├── 📦 DEPENDÊNCIAS
│   └── requirements.txt
│
└── 📊 SAÍDAS (geradas pelo sistema)
    ├── Controle_Estoque.xlsx       ← Planilha principal
    ├── dashboard_estoque.png       ← Dashboard visual
    ├── modelo_estrela.sql          ← Scripts SQL
    ├── dados_csv/                  ← CSVs para análise
    └── dados_power_bi/             ← Dados para BI
```

## 🎓 Ordem Recomendada de Leitura

### Para Usuários Finais
1. [INICIO_RAPIDO.md](INICIO_RAPIDO.md) - Começar a usar
2. [GUIA_TERMINAL.md](GUIA_TERMINAL.md) - Registrar movimentações
3. [readme.md](readme.md) - Recursos avançados

### Para Desenvolvedores
1. [readme.md](readme.md) - Visão geral
2. [OTIMIZACAO.md](OTIMIZACAO.md) - Arquitetura
3. [CORRECOES_APLICADAS.md](CORRECOES_APLICADAS.md) - Histórico
4. Código-fonte comentado

## 🔍 Busca Rápida

### Como fazer...
- **Instalar o sistema?** → [INICIO_RAPIDO.md](INICIO_RAPIDO.md#instalação-e-uso-3-passos)
- **Registrar uma entrada?** → [GUIA_TERMINAL.md](GUIA_TERMINAL.md#registrar-entradas)
- **Registrar uma saída?** → [GUIA_TERMINAL.md](GUIA_TERMINAL.md#registrar-saídas)
- **Gerar relatórios?** → [INICIO_RAPIDO.md](INICIO_RAPIDO.md#comandos-principais)
- **Exportar para BI?** → [readme.md](readme.md#integração-com-bi)
- **Personalizar categorias?** → [readme.md](readme.md#personalização)

### Problemas comuns
- **Erro de importação?** → [INICIO_RAPIDO.md](INICIO_RAPIDO.md#problemas-comuns)
- **Arquivo não encontrado?** → [GUIA_TERMINAL.md](GUIA_TERMINAL.md#resolução-de-problemas)
- **Estoque negativo?** → [GUIA_TERMINAL.md](GUIA_TERMINAL.md#avisos-importantes)

## 📈 Informações Técnicas

- **Linguagem:** Python 3.10+
- **Linhas de código:** 1.226
- **Documentação:** 1.114 linhas
- **Otimização:** 50% redução
- **Versão:** 2.0 (Otimizado)
- **Data:** Fevereiro 2026

