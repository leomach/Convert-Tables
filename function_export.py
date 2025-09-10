import os
import pandas as pd  # type: ignore

def clear() -> None:
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def structured_constant_export(path: str, header_lines: int = 0, columns: list = None) -> None:
    """
    Utiliza dados de uma tabela para pegar duas colunas específicas e exportá-las para um arquivo Python com
    uma contante estruturada da seguinte forma: (coluna1: int, coluna2: str).

    Parameters:
    - path (str): The file path where is the CSV.
    - header_lines (int): Number of header lines to include in the CSV file.
    - columns (list): List of two columns to export.

    Returns:
    - None
    """
    print("")
    print("Exportando constante estruturada...")
    path_export = "./export/constants/structured_constants.py"

    if columns is None or len(columns) != 2:
        raise ValueError("Forneça exatamente duas colunas para exportar.")
    
    # Se for um arquivo .xls ou .xlsx, leia com pd.read_excel
    if path.endswith('.xls') or path.endswith('.xlsx'):
        df = pd.read_excel(path, header=header_lines)
    else:
        df = pd.read_csv(path, header=header_lines)
        
    # Verifica cabeçalhos
    print(f"Cabeçalhos disponíveis: {list(df.columns)}")
    print("")

    if not all(col in df.columns for col in columns):
        raise ValueError("Uma ou ambas as colunas não estão no quadro de dados.")

    # Select the specified columns
    structured_constant = df[columns]

    # Transforma as colunas em uma tupla de tuplas
    structured_constant_list = tuple(structured_constant.itertuples(index=False, name=None))
    
    # Exporta para um arquivo Python
    with open(path_export, 'w', encoding='utf-8') as file:
        file.write(f"STRUCTURED_CONSTANT = {structured_constant_list}\n")
        file.write("")
    
    print(f"Constante estruturada exportada para {path_export} com sucesso. 🚀")
    print("")
    print("")

response = ""
while response != "0":
    
    print("Programa para transformar dados de uma tabela")
    print("--------------------------------------------")
    print("Instruções:")
    print("1. Coloque o arquivo da planilha na pasta 'import'")
    print("2. O arquivo pode ser .csv, .xls ou .xlsx")
    print("3. O arquivo exportado estará na pasta 'export'")
    print("--------------------------------------------")
    print("")
    print("1. Exportar constante estruturada - TUPLA DE TUPLAS")
    print("0. Sair")
    response = input("Escolha uma opção: ")
    
    if response == "1":
        clear()
        path = "./import"
        file_name = input("Digite o nome do arquivo de planilha (com extensão): ")
        full_path = f"{path}/{file_name}"
        
        # Verifica se o arquivo existe
        if not os.path.isfile(full_path):
            print("Arquivo não encontrado. Verifique o nome e a extensão.")
            continue
        
        try:
            header_lines = int(input("Número da linha de cabeçalho (padrão 0): ") or "0")
        except ValueError:
            print("Entrada inválida. Usando linha 0 de cabeçalho. Cancelar? (s/n): ")
            if input().strip().lower() == "s":
                continue
            header_lines = 0
        
        columns_input = input("Digite os nomes das duas colunas separadas por vírgula (ex: id,name): ")
        columns = [col.strip() for col in columns_input.split(",")]
        if len(columns) != 2:
            print("Você deve fornecer exatamente duas colunas. Tente novamente.")
            continue
        
        try:
            structured_constant_export(full_path, header_lines, columns)
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
    elif response == "0":
        print("Saindo do programa.")
    else:
        print("Opção inválida. Tente novamente.")
        
