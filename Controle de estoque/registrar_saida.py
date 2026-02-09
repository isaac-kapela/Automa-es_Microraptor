"""Sistema de Registro de Saídas - Controle de Estoque"""
from utils import *
import pandas as pd

def obter_estoque(codigo):
    """Obtém estoque atual do produto"""
    try:
        df = pd.read_excel(CONFIG['arquivo_excel'], sheet_name='Estoque Atual')
        prod = df[df['Produto / Material'] == codigo]
        return prod['Saldo Atual'].values[0] if not prod.empty else 0
    except:
        return None

def registrar_saida():
    """Registra uma nova saída"""
    df_base = carregar_produtos()
    if df_base is None:
        return False
    
    print("\n" + "="*70)
    print("📝 REGISTRAR NOVA SAÍDA")
    print("="*70)
    
    # Coletar dados
    data = obter_data()
    codigo = obter_produto(df_base)
    
    estoque = obter_estoque(codigo)
    if estoque is not None and estoque > 0:
        print(f"   📦 Estoque atual: {estoque:.0f} unidades")
    
    qtd = obter_numero("📤 Quantidade a retirar", minimo=0)
    
    # Verificar estoque
    if estoque is not None and qtd > estoque:
        print(f"\n⚠️  ATENÇÃO: Quantidade > estoque ({estoque:.0f})!")
        if not confirmar("Continuar mesmo assim"):
            print("\n❌ Cancelado!")
            return False
    
    # Motivo
    print("\n📝 Motivos: 1-Produção 2-Venda 3-Consumo 4-Perda 5-Outro")
    motivos = {'1': 'Uso em produção', '2': 'Venda', '3': 'Consumo interno', '4': 'Perda/Avaria'}
    motivo_op = input("   Escolha ou digite: ").strip()
    motivo = motivos.get(motivo_op, motivo_op if motivo_op != '5' else input("   Digite: ").strip())
    
    # Confirmar
    print("\n" + "-"*70)
    print(f"Data: {data} | Produto: {codigo} | Quantidade: {qtd}")
    print(f"Motivo: {motivo}")
    if estoque is not None:
        print(f"Estoque: {estoque:.0f} → {estoque-qtd:.0f}")
    print("-"*70)
    
    if not confirmar("Confirmar registro"):
        print("\n❌ Cancelado!")
        return False
    
    # Salvar
    if salvar_na_planilha('Saídas', [data, codigo, qtd, motivo]):
        print("\n✅ SAÍDA REGISTRADA!")
        if estoque is not None:
            print(f"📊 Novo estoque: {estoque-qtd:.0f}\n")
        return True
    return False

def menu():
    """Menu principal"""
    while True:
        limpar_tela()
        print("="*70)
        print("📤 REGISTRO DE SAÍDAS")
        print("="*70)
        print("\n1 - Registrar saída\n2 - Listar produtos (com estoque)\n3 - Sair\n")
        
        op = input("Opção: ").strip()
        
        if op == '1':
            registrar_saida()
            pausar()
        elif op == '2':
            listar_produtos_completo(com_estoque=True)
            pausar()
        elif op == '3':
            print("\n👋 Até logo!\n")
            break
        else:
            print("\n❌ Opção inválida!")
            pausar()

if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print("\n\n⚠️  Cancelado.\n")
    except Exception as e:
        print(f"\n❌ Erro: {e}\n")
