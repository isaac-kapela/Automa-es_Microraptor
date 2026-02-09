# 🆕 CADASTRO AUTOMÁTICO DE PRODUTOS

## ✨ Nova Funcionalidade: Código Automático

### 📌 Como Funciona

**ANTES (método antigo):**
- ❌ Usuário digitava código manualmente (ex: P001, P002...)
- ❌ Risco de duplicação
- ❌ Precisava saber qual era o próximo código

**AGORA (automático):**
- ✅ Sistema gera código automaticamente
- ✅ Sempre incrementa o último código (P008 → P009)
- ✅ Impossível duplicar códigos
- ✅ Cadastro de produto integrado no fluxo

---

## 🎯 Como Usar

### 1️⃣ Registrar Entrada com Novo Produto

```bash
python3 registrar_entrada.py
```

**Fluxo de Trabalho:**

```
📥 REGISTRO DE ENTRADAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1 - Registrar entrada
2 - Cadastrar novo produto       ← NOVO!
3 - Listar produtos
4 - Sair

→ Escolha 1 (Registrar entrada)

→ Sistema pergunta: Selecionar ou Cadastrar?
   1 - Selecionar produto existente
   2 - Cadastrar novo produto     ← AUTOMÁTICO!
   3 - Ver lista completa

→ Se escolher "2 - Cadastrar novo produto":
   ✅ Código gerado automaticamente (P009, P010...)
   📝 Você só informa: nome, categoria, valor, etc.
```

### 2️⃣ Cadastrar Produto Diretamente

```bash
python3 registrar_entrada.py
```

**Escolha opção 2 no menu principal:**

```
📥 REGISTRO DE ENTRADAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1 - Registrar entrada
2 - Cadastrar novo produto       ← Use esta opção!
3 - Listar produtos
4 - Sair
```

**Exemplo de Cadastro:**

```
➤ python3 registrar_entrada.py
➤ Opção: 2

➕ CADASTRAR NOVO PRODUTO
══════════════════════════════════════════════════════

🏷️  Código: P009 (gerado automaticamente)    ← AUTOMÁTICO!

📦 Nome do Produto: Teclado Mecânico RGB
📂 Categoria/Tipo [Enter = Outros]: Periféricos
💰 Valor unitário (R$): 350.50
📊 Estoque mínimo: 5
🏭 Fornecedor [Enter = N/D]: TechStore

──────────────────────────────────────────────────────
Código: P009 | Nome: Teclado Mecânico RGB
Categoria: Periféricos | Valor: R$ 350.50
Estoque Mín: 5 | Fornecedor: TechStore
──────────────────────────────────────────────────────

✓ Confirmar cadastro? (s/n): s

✅ Produto P009 cadastrado com sucesso!
```

---

## 🔢 Lógica de Geração de Código

### Como o Sistema Gera Códigos:

1. **Lê todos os códigos existentes** na planilha (Base)
2. **Extrai os números** (P001 → 1, P008 → 8)
3. **Encontra o maior número**
4. **Incrementa +1** e formata como P009

### Exemplos:

```
Códigos Existentes    →    Próximo Código
─────────────────────────────────────────
P001, P002, P003      →    P004
P001, P005, P008      →    P009
P100, P101            →    P102
(vazio)               →    P001
```

### Formato do Código:

- **Prefixo:** `P` (Produto)
- **Número:** 3 dígitos com zeros à esquerda
- **Exemplos:** P001, P010, P099, P100

---

## 📝 Campos do Cadastro

| Campo | Obrigatório | Exemplo | Descrição |
|-------|-------------|---------|-----------|
| **Código** | ✅ Auto | P009 | Gerado automaticamente |
| **Nome** | ✅ Sim | Teclado RGB | Nome do produto |
| **Categoria** | ❌ Opcional | Periféricos | Tipo/categoria (padrão: "Outros") |
| **Valor** | ✅ Sim | 350.50 | Valor unitário em reais |
| **Est. Mínimo** | ✅ Sim | 5 | Estoque mínimo para alerta |
| **Fornecedor** | ❌ Opcional | TechStore | Fornecedor principal (padrão: "N/D") |

---

## 🔄 Integração com Fluxo de Entrada

### Cenário: Recebeu produto novo que não está cadastrado

**Fluxo Otimizado:**

```bash
python3 registrar_entrada.py
```

1. **Escolha:** 1 - Registrar entrada
2. **Quando solicitar produto:** 2 - Cadastrar novo produto
3. **Sistema gera código:** P009
4. **Preencha dados** do produto
5. **Confirme cadastro**
6. **Continue o registro** da entrada normalmente

✅ **Produto cadastrado E entrada registrada em um único fluxo!**

---

## 🛡️ Vantagens

### ✅ Segurança
- Impossível duplicar códigos
- Sempre sequencial e organizado
- Sem erros de digitação

### ✅ Produtividade
- Não precisa verificar qual é o próximo código
- Cadastro integrado ao fluxo de entrada
- Menos etapas, mais rapidez

### ✅ Organização
- Códigos sempre em sequência
- Fácil rastrear ordem de cadastro
- Padrão consistente (P001, P002...)

---

## 🔧 Arquivos Modificados

Esta funcionalidade modificou:

1. **[utils.py](utils.py)**
   - ✨ `gerar_proximo_codigo()` - Gera código automático
   - ✨ `cadastrar_novo_produto()` - Cadastra com código auto
   - 🔄 `obter_produto()` - Agora oferece opção de cadastro

2. **[registrar_entrada.py](registrar_entrada.py)**
   - 🔄 Menu atualizado com opção de cadastro direto

---

## 💡 Dicas de Uso

### ✅ FAÇA:
- Use "2 - Cadastrar novo produto" ao receber item novo
- Deixe o sistema gerar o código automaticamente
- Preencha todos os campos com atenção

### ❌ NÃO FAÇA:
- Não edite códigos manualmente na planilha Excel
- Não pule números na sequência
- Não use códigos duplicados

---

## 🐛 Resolução de Problemas

### Problema: Código gerado está errado

**Solução:**
- Verifique se há códigos fora do padrão na planilha
- Sistema busca o maior número e incrementa
- Códigos devem seguir formato: P + 3 dígitos

### Problema: Erro ao cadastrar

**Causa:** Planilha Excel está aberta
**Solução:** Feche `Controle_Estoque.xlsx` e tente novamente

### Problema: Produto não aparece após cadastro

**Solução:** 
- Sistema recarrega automaticamente
- Se não aparecer, escolha "3 - Listar produtos" para verificar

---

## 📊 Exemplo Completo

### Cadastro + Entrada em Sequência:

```bash
# 1. Iniciar sistema
python3 registrar_entrada.py

# 2. Menu principal
Opção: 1  # Registrar entrada

# 3. Selecionar produto
Opção: 2  # Cadastrar novo

# 4. Sistema gera: P009
Nome: Mouse Gamer 16000 DPI
Categoria: Periféricos
Valor: 189.90
Est. Mínimo: 10
Fornecedor: GamerStore

# 5. Confirmar: s

# 6. Continuar com a entrada
Data: 08/02/2026
Documento: NF-123456
Produto: P009 (já selecionado!)
Quantidade: 20
Valor: 189.90

# 7. Produto cadastrado + Entrada registrada! ✅
```

---

## 🎓 Resumo

| Item | Status |
|------|--------|
| Código Manual | ❌ Desativado |
| Código Automático | ✅ Ativo |
| Cadastro Integrado | ✅ Disponível |
| Formato | P + 3 dígitos |
| Duplicação | ❌ Impossível |

**Versão:** 2.1  
**Data:** 08/02/2026  
**Funcionalidade:** Código Automático Ativo ✨
