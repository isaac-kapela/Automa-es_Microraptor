# 🚀 GUIA DE INSTALAÇÃO - Windows & Linux

## 📋 Requisitos do Sistema

### Comum para ambos sistemas:
- **Python 3.10+** (mínimo 3.8)
- **pip** (gerenciador de pacotes Python)
- **4 GB RAM** (recomendado)
- **100 MB** de espaço livre

---

## 🐧 LINUX (Ubuntu/Debian)

### 1️⃣ Instalar Python e pip

```bash
# Atualizar repositórios
sudo apt update

# Instalar Python 3 e pip
sudo apt install python3 python3-pip -y

# Verificar instalação
python3 --version
pip3 --version
```

### 2️⃣ Clonar/Baixar o Projeto

```bash
# Opção 1: Se tiver git
git clone <seu-repositorio>
cd "Controle de estoque"

# Opção 2: Sem git (copiar arquivos manualmente)
mkdir -p ~/projetos/"Controle de estoque"
cd ~/projetos/"Controle de estoque"
# Copie todos os arquivos .py, .md, .txt para esta pasta
```

### 3️⃣ Instalar Dependências

```bash
# Instalar todas as dependências
pip3 install --index-url https://pypi.org/simple/ openpyxl pandas matplotlib seaborn --user

# OU usando o arquivo requirements.txt
pip3 install --index-url https://pypi.org/simple/ -r requirements.txt --user
```

### 4️⃣ Executar o Sistema

```bash
# Gerar planilha inicial
python3 gerar_planilha.py

# Registrar entradas
python3 registrar_entrada.py

# Registrar saídas
python3 registrar_saida.py

# Gerar dashboard
python3 analise_dashboard.py

# Exportar para BI
python3 exportar_para_BI.py
```

### 🔧 Troubleshooting Linux

**Erro de permissão ao instalar:**
```bash
# Use --user para instalar sem sudo
pip3 install --user <pacote>
```

**Python não encontrado:**
```bash
# Criar link simbólico (se necessário)
sudo ln -s /usr/bin/python3 /usr/bin/python
```

**Erro de display ao gerar gráficos:**
```bash
# Use backend não-interativo
export MPLBACKEND=Agg
python3 analise_dashboard.py
```

---

## 🪟 WINDOWS

### 1️⃣ Instalar Python

1. **Baixar Python:**
   - Acesse: https://www.python.org/downloads/
   - Baixe Python 3.11 ou 3.10
   - Execute o instalador

2. **Durante a instalação:**
   - ✅ **MARQUE:** "Add Python to PATH"
   - ✅ **MARQUE:** "Install pip"
   - Clique em "Install Now"

3. **Verificar instalação:**
   ```cmd
   python --version
   pip --version
   ```

### 2️⃣ Baixar o Projeto

```cmd
REM Opção 1: Com git
git clone <seu-repositorio>
cd "Controle de estoque"

REM Opção 2: Manual
REM 1. Crie pasta: C:\Users\SeuUsuario\Projetos\Controle de estoque
REM 2. Copie todos os arquivos .py, .md, .txt para lá
cd C:\Users\SeuUsuario\Projetos\"Controle de estoque"
```

### 3️⃣ Instalar Dependências

Abra o **Prompt de Comando** ou **PowerShell**:

```cmd
REM Navegar até a pasta do projeto
cd "Controle de estoque"

REM Instalar dependências
pip install openpyxl pandas matplotlib seaborn

REM OU usando requirements.txt
pip install -r requirements.txt
```

### 4️⃣ Executar o Sistema

```cmd
REM Gerar planilha inicial
python gerar_planilha.py

REM Registrar entradas
python registrar_entrada.py

REM Registrar saídas
python registrar_saida.py

REM Gerar dashboard
python analise_dashboard.py

REM Exportar para BI
python exportar_para_BI.py
```

### 🔧 Troubleshooting Windows

**Python não é reconhecido:**
1. Reinstale Python marcando "Add to PATH"
2. OU adicione manualmente ao PATH:
   - Variáveis de Ambiente → PATH
   - Adicione: `C:\Users\SeuUsuario\AppData\Local\Programs\Python\Python311`

**pip não funciona:**
```cmd
python -m pip install --upgrade pip
```

**Erro de encoding:**
```cmd
REM Configure encoding UTF-8
chcp 65001
```

**Erro ao abrir planilha:**
- Feche o Excel antes de executar os scripts

---

## 📦 ARQUIVOS NECESSÁRIOS PARA TRANSFERIR

### ✅ Arquivos Obrigatórios (Python):
```
Controle de estoque/
├── utils.py                    ⭐ ESSENCIAL
├── config.py                   ⭐ ESSENCIAL
├── gerar_planilha.py           ⭐ ESSENCIAL
├── registrar_entrada.py        ⭐ ESSENCIAL
├── registrar_saida.py          ⭐ ESSENCIAL
├── analise_dashboard.py
├── exportar_para_BI.py
└── requirements.txt            ⭐ ESSENCIAL
```

### 📄 Arquivos de Dados (gerados):
```
├── Controle_Estoque.xlsx       (pode copiar para manter dados)
├── dashboard_estoque.png
├── modelo_estrela.sql
├── dados_csv/
└── dados_power_bi/
```

### 📚 Documentação (opcional):
```
├── INDEX.md
├── INICIO_RAPIDO.md
├── readme.md
├── GUIA_TERMINAL.md
├── OTIMIZACAO.md
└── CORRECOES_APLICADAS.md
```

---

## 🔄 MIGRAÇÃO ENTRE MÁQUINAS

### 📤 Na máquina antiga (Linux ou Windows):

```bash
# Linux
cd ~/projetos
tar -czf controle-estoque-backup.tar.gz "Controle de estoque"/

# Windows (PowerShell)
Compress-Archive -Path "Controle de estoque" -DestinationPath controle-estoque-backup.zip
```

### 📥 Na máquina nova:

#### Linux:
```bash
# Copiar arquivo e extrair
tar -xzf controle-estoque-backup.tar.gz
cd "Controle de estoque"

# Instalar dependências
pip3 install -r requirements.txt --user

# Testar
python3 gerar_planilha.py --help 2>/dev/null || python3 gerar_planilha.py
```

#### Windows:
```cmd
REM Extrair o ZIP
REM Usar Windows Explorer ou:
tar -xf controle-estoque-backup.zip

cd "Controle de estoque"

REM Instalar dependências
pip install -r requirements.txt

REM Testar
python gerar_planilha.py
```

---

## 🌐 INSTALAÇÃO EM AMBIENTE CORPORATIVO

### Com proxy:
```bash
# Linux
pip3 install --proxy http://usuario:senha@proxy:porta --user openpyxl pandas matplotlib seaborn

# Windows
pip install --proxy http://usuario:senha@proxy:porta openpyxl pandas matplotlib seaborn
```

### Em rede restrita:
```bash
# 1. Baixe os pacotes wheel em máquina com internet
pip download openpyxl pandas matplotlib seaborn -d pacotes/

# 2. Copie a pasta 'pacotes/' para máquina sem internet

# 3. Instale offline
pip install --no-index --find-links=pacotes/ openpyxl pandas matplotlib seaborn
```

---

## 📝 LISTA DE COMANDOS ESSENCIAIS

### Linux:
```bash
# Instalação completa em uma linha
sudo apt update && sudo apt install python3 python3-pip -y && pip3 install --index-url https://pypi.org/simple/ openpyxl pandas matplotlib seaborn --user

# Executar sistema
cd "Controle de estoque" && python3 gerar_planilha.py
```

### Windows:
```cmd
REM Instalação após Python instalado
pip install openpyxl pandas matplotlib seaborn && echo Instalacao concluida!

REM Executar sistema
cd "Controle de estoque" && python gerar_planilha.py
```

---

## 🔐 BACKUP DOS DADOS

### Fazer backup regular:

**Linux:**
```bash
# Backup automático com data
#!/bin/bash
DATA=$(date +%Y%m%d)
tar -czf backup-estoque-$DATA.tar.gz Controle_Estoque.xlsx dados_csv/ dados_power_bi/
```

**Windows:**
```cmd
REM Backup com data
for /f "tokens=2-4 delims=/ " %%a in ('date /t') do (set DATA=%%c%%a%%b)
tar -czf backup-estoque-%DATA%.tar.gz Controle_Estoque.xlsx dados_csv\ dados_power_bi\
```

---

## ✅ CHECKLIST PÓS-INSTALAÇÃO

### Verificar se tudo está funcionando:

```bash
# Linux
python3 --version        # Python 3.8+
pip3 --version          # pip instalado
python3 -c "import openpyxl; import pandas; import matplotlib; print('OK')"

# Windows
python --version         # Python 3.8+
pip --version           # pip instalado
python -c "import openpyxl; import pandas; import matplotlib; print('OK')"
```

Se todos retornarem "OK", está pronto para usar! ✨

---

## 📞 SUPORTE

**Problemas comuns:**
- Veja [INICIO_RAPIDO.md](INICIO_RAPIDO.md#problemas-comuns)
- Consulte [GUIA_TERMINAL.md](GUIA_TERMINAL.md#resolução-de-problemas)

**Dúvidas sobre migração:**
- Este guia cobre 99% dos casos
- Sistema funciona idêntico em ambas plataformas

---

**Sistema testado em:**
- ✅ Ubuntu 20.04, 22.04
- ✅ Debian 11, 12
- ✅ Windows 10, 11
- ✅ Python 3.8, 3.9, 3.10, 3.11

**Versão:** 2.0 | **Data:** Fevereiro 2026
