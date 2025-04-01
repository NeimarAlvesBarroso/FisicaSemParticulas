import pandas as pd

# Definir o caminho do arquivo original
caminho_arquivo = r"C:\Users\PG-INFO\Mega_Resultados.xlsx"

# Ler o arquivo Excel sem cabeçalho
df = pd.read_excel(caminho_arquivo, header=None)

# Adicionar nomes adequados às colunas
df.columns = ["Concurso", "Data", "Bola1", "Bola2", "Bola3", "Bola4", "Bola5", "Bola6"]

# Converter a coluna de data para formato adequado
df["Data"] = pd.to_datetime(df["Data"], dayfirst=True).dt.strftime('%d/%m/%Y')

# Ordenar os concursos do mais antigo para o mais recente
df = df.sort_values(by="Concurso").reset_index(drop=True)

# Salvar em um novo arquivo formatado
caminho_saida = r"C:\Users\PG-INFO\Mega_Historico_Formatado.xlsx"
df.to_excel(caminho_saida, index=False)

print(f"✅ Arquivo formatado salvo em: {caminho_saida}")
