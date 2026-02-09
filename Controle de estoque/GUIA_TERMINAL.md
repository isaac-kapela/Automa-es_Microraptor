# 📥 GUIA DE USO - REGISTRO DE ENTRADAS E SAÍDAS VIA TERMINAL

> **✨ Sistema otimizado!** Scripts 50% menores usando biblioteca compartilhada `utils.py`

## 🚀 Como Usar

### 1️⃣ Registrar Entradas

Para adicionar novas entradas de produtos no estoque:

```bash
python3 registrar_entrada.py
```

**Menu de opções:**
- **1** - Registrar nova entrada
- **2** - Listar produtos cadastrados  
- **3** - Sair

**Dados necessários para entrada:**
- 📅 **Data da entrada** (formato DD/MM/YYYY ou Enter para hoje)
- 📄 **Documento/Nota Fiscal** (ou Enter para gerar automaticamente)
- 🏷️  **Código do Produto** (ex: P001, P002, etc)
- 📦 **Quantidade** (número inteiro)
- 💰 **Valor unitário** (em R$, use ponto para decimais)

**Exemplo de uso:**
```
Escolha uma opção: 1

📅 Data da entrada (DD/MM/YYYY) [Enter = hoje]: 
   → Usando data de hoje: 08/02/2026

📄 Documento/Nota Fiscal: NF-98765

🏷️  Código do Produto: P001
   ✓ Produto encontrado: Parafuso M6

📦 Quantidade: 1000

💰 Valor unitário (R$): 0.45

CONFIRMAR DADOS:
----------------------------------------------------------------------
Data: 08/02/2026
Documento: NF-98765
Produto: P001
Quantidade: 1000
Valor Unit.: R$ 0.45
Valor Total: R$ 450.00
----------------------------------------------------------------------

✓ Confirmar registro? (s/n): s

✅ ENTRADA REGISTRADA COM SUCESSO!
```

---

### 2️⃣ Registrar Saídas

Para registrar saídas/consumo de produtos:

```bash
python3 registrar_saida.py
```

**Menu de opções:**
- **1** - Registrar nova saída
- **2** - Listar produtos com estoque atual
- **3** - Sair

**Dados necessários para saída:**
- 📅 **Data da saída** (formato DD/MM/YYYY ou Enter para hoje)
- 🏷️  **Código do Produto** (ex: P001, P002, etc)
- 📤 **Quantidade a retirar** (número inteiro)
- 📝 **Motivo** (escolha de 1 a 5 ou digite personalizado)

**Motivos pré-definidos:**
1. Uso em produção
2. Venda
3. Consumo interno
4. Perda/Avaria
5. Outro (personalizado)

**Exemplo de uso:**
```
Escolha uma opção: 1

📅 Data da saída (DD/MM/YYYY) [Enter = hoje]: 
   → Usando data de hoje: 08/02/2026

🏷️  Código do Produto: P001
   ✓ Produto encontrado: Parafuso M6
   📦 Estoque atual: 1450 unidades

📤 Quantidade a retirar: 200

📝 Motivos sugeridos:
   1 - Uso em produção
   2 - Venda
   3 - Consumo interno
   4 - Perda/Avaria
   5 - Outro

   Escolha uma opção: 1

CONFIRMAR DADOS:
----------------------------------------------------------------------
Data: 08/02/2026
Produto: P001
Quantidade: 200
Motivo: Uso em produção
----------------------------------------------------------------------

✓ Confirmar registro? (s/n): s

✅ SAÍDA REGISTRADA COM SUCESSO!
📊 Estoque anterior: 1450
📊 Estoque novo: 1250
```

---

## ⚠️ Avisos Importantes

### Estoque Negativo
Se você tentar retirar mais produtos do que há em estoque, o sistema vai avisar:
```
⚠️  ATENÇÃO: Quantidade maior que estoque atual (50)!
Deseja continuar mesmo assim? (s/n):
```

### Arquivo Aberto
Se o arquivo Excel estiver aberto, você receberá este erro:
```
❌ Erro: Arquivo 'Controle_Estoque.xlsx' está aberto!
   Feche o Excel e tente novamente.
```

**Solução:** Feche o arquivo Excel e tente novamente.

---

## 📊 Listar Produtos

Ambos os scripts permitem ver a lista de produtos:

**No registrar_entrada.py:**
```
Escolha uma opção: 2

PRODUTOS CADASTRADOS:
Código     Nome                          Categoria       Estoque Mín. Valor (R$)
--------------------------------------------------------------------------------
P001       Parafuso M6                   Fixação         100          0.50
P002       Tinta Branca 18L              Pintura         10           85.00
P003       Lixa Grão 100                 Acabamento      50           2.30
...
```

**No registrar_saida.py (mostra estoque atual):**
```
Escolha uma opção: 2

PRODUTOS CADASTRADOS:
Código     Nome                          Estoque Atual   Estoque Mín.
--------------------------------------------------------------------------------
✓ P001     Parafuso M6                   1450            100
✓ P002     Tinta Branca 18L              45              10
⚠️ P003    Lixa Grão 100                 30              50  <- Abaixo do mínimo!
...
```

---

## 🎯 Dicas de Uso

### 1. Usar Data Automática
Pressione **Enter** quando pedir a data para usar a data de hoje automaticamente.

### 2. Documento Automático
Pressione **Enter** quando pedir o documento para gerar um número automático baseado na data/hora.

### 3. Ver Lista de Produtos
Se não souber o código, digite um código errado e o sistema perguntará se deseja ver a lista completa.

### 4. Validação em Tempo Real
O sistema valida:
- ✅ Formato de data
- ✅ Código do produto existe
- ✅ Quantidade é número positivo
- ✅ Valor é número válido
- ⚠️ Avisa se estoque ficará negativo

---

## 🔄 Fluxo Completo de Trabalho

```mermaid
1. Gerar planilha inicial
   └─> python3 gerar_planilha.py

2. Registrar entradas de produtos
   └─> python3 registrar_entrada.py

3. Registrar saídas de produtos
   └─> python3 registrar_saida.py

4. Gerar dashboard e relatórios
   └─> python3 analise_dashboard.py

5. Exportar para Power BI
   └─> python3 exportar_para_BI.py
```

---

## 📁 Estrutura de Arquivos

```
Controle de estoque/
├── Controle_Estoque.xlsx       # Planilha principal
├── gerar_planilha.py           # Criar planilha inicial
├── registrar_entrada.py        # 📥 Registrar entradas (70 linhas)
├── registrar_saida.py          # 📤 Registrar saídas (97 linhas)
├── analise_dashboard.py        # Gerar dashboard
├── exportar_para_BI.py         # Exportar para BI
├── utils.py                    # 🆕 Funções compartilhadas (145 linhas)
├── config.py                   # Configurações
└── requirements.txt            # Dependências
```

### 🆕 utils.py - Biblioteca Compartilhada
Contém funções reutilizáveis:
- Validações (data, número, produto)
- Interface (limpar tela, pausar, confirmar)
- Manipulação de dados (carregar, listar, salvar)

**Benefício:** Redução de 50% no código dos scripts de registro!

---

## 💡 Atalhos e Facilidades

### Entrada Rápida (todas as informações de uma vez)
Você pode preparar os dados antes e só digitar sequencialmente:
```
Opção: 1
Data: [Enter]
Documento: NF-12345
Produto: P001
Quantidade: 500
Valor: 0.48
Confirmar: s
```

### Cancelar a Qualquer Momento
Pressione `Ctrl+C` para sair do programa imediatamente.

---
"No module named 'utils'" | Certifique-se de estar no diretório correto |
| 
## 🆘 Resolução de Problemas

| Problema | Solução |
|----------|---------|
| "Arquivo não encontrado" | Execute `python3 gerar_planilha.py` primeiro |
| "Arquivo está aberto" | Feche o Excel/LibreOffice |
| "Produto não encontrado" | Verifique o código ou use opção 2 para listar |
| "Data inválida" | Use formato DD/MM/YYYY (ex: 08/02/2026) |
| Estoque negativo | Revise a quantidade ou confirme se deseja continuar |

---

**✨ Pronto para usar!** Comece registrando suas movimentações de estoque de forma rápida e eficiente.
