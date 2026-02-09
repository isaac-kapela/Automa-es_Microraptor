"""Sistema de Registro de Entradas - Controle de Estoque"""
from datetime import datetime
from utils import *

def registrar_entrada():
    """Registra uma nova entrada"""
    df_base = carregar_produtos()
    if df_base is None:
        return False
    
    print("\n" + "="*70)
    print("📝 REGISTRAR NOVA ENTRADA")
    print("="*70)
    
    # Coletar dados
    data = obter_data()
    doc = input("\n📄 Documento/NF [Enter = auto]: ").strip() or f"NF-{datetime.now().strftime('%Y%m%d%H%M%S')}"
    codigo = obter_produto(df_base)
    qtd = obter_numero("📦 Quantidade", minimo=0)
    valor = obter_numero("💰 Valor unitário (R$)", permitir_decimal=True, minimo=-1)
    
    # Confirmar
    print("\n" + "-"*70)
    print(f"Data: {data} | Doc: {doc} | Produto: {codigo}")
    print(f"Quantidade: {qtd} | Valor: R$ {valor:.2f} | Total: R$ {qtd*valor:.2f}")
    print("-"*70)
    
    if not confirmar("Confirmar registro"):
        print("\n❌ Cancelado!")
        return False
    
    # Salvar
    formula = f"=D{qtd+2}*E{qtd+2}"  # Aproximação da linha
    if salvar_na_planilha('Entradas', [data, doc, codigo, qtd, valor, formula]):
        print("\n✅ ENTRADA REGISTRADA!")
        print(f"💵 Valor Total: R$ {qtd*valor:.2f}\n")
        return True
    return False

def menu():
    """Menu principal"""
    while True:
        limpar_tela()
        print("="*70)
        print("📥 REGISTRO DE ENTRADAS")
        print("="*70)
        print("\n1 - Registrar entrada\n2 - Cadastrar novo produto\n3 - Listar produtos\n4 - Sair\n")
        
        op = input("Opção: ").strip()
        
        if op == '1':
            registrar_entrada()
            pausar()
        elif op == '2':
            df_base = carregar_produtos()
            if df_base is not None:
                from utils import cadastrar_novo_produto
                cadastrar_novo_produto(df_base)
            pausar()
        elif op == '3':
            listar_produtos_completo()
            pausar()
        elif op == '4':
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
