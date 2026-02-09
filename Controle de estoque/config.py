"""
Configurações centralizadas do sistema de controle de estoque
"""

# Configurações de arquivos
CONFIG = {
    # Arquivos principais
    'arquivo_excel': 'Controle_Estoque.xlsx',
    'arquivo_dashboard': 'dashboard_estoque.png',
    'arquivo_sql': 'modelo_estrela.sql',
    
    # Pastas
    'pasta_csv': 'dados_csv',
    'pasta_power_bi': 'dados_power_bi',
    
    # Encoding e formatação
    'encoding': 'utf-8-sig',
    'csv_separador': ';',
    'csv_decimal': ',',
    
    # Gráficos
    'dpi_dashboard': 300,
    'estilo_grafico': 'seaborn-v0_8-darkgrid',
    'paleta_cores': 'husl'
}
