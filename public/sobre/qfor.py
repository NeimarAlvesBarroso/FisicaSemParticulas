import pandas as pd

# 📂 Caminho do arquivo formatado
arquivo_formatado = r"C:\Users\PG-INFO\Quina_Historico.xlsx"

# 🔍 Carregar a planilha garantindo que não há cabeçalhos indesejados
df = pd.read_excel(arquivo_formatado)

# 🔄 Verificar se a primeira linha contém strings ao invés de números
if not df.iloc[0, 2:].apply(lambda x: str(x).isdigit()).all():
    df = df.iloc[1:]  # Remover a primeira linha se ela contiver texto

# 🛠️ Converter todas as colunas numéricas corretamente
df.iloc[:, 2:] = df.iloc[:, 2:].apply(pd.to_numeric, errors='coerce')

# 📅 Certificar-se de que a coluna "Data" está formatada corretamente
df["Data"] = pd.to_datetime(df["Data"], errors='coerce')

# 🔄 Remover quaisquer linhas com valores ausentes
df.dropna(inplace=True)

# 📝 Salvar a planilha corrigida
df.to_excel(arquivo_formatado, index=False)

print(f"✅ Planilha corrigida e pronta para o modelo!")
