import json
import os

# Caminho do arquivo categories.js
input_file = "categories.json"
output_dir = "categorias"

# Função para carregar o JSON do arquivo .js
def load_json_from_js(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        # Remove qualquer declaração JS, como "const categories = " ou similar
        content = content.strip()
        if content.startswith("const") or content.startswith("let") or content.startswith("var"):
            content = content.split("=", 1)[1].strip()
        # Remove ponto e vírgula no final (se houver)
        if content.endswith(";"):
            content = content[:-1]
        # Converte para JSON
        return json.loads(content)

# Carregar os dados
data = load_json_from_js(input_file)

# Cria a pasta para armazenar os arquivos
os.makedirs(output_dir, exist_ok=True)

# Processa o JSON
for key, value in data.items():
    # Nome do arquivo com base no ID
    file_name = os.path.join(output_dir, f"{key}.json")
    # Salva a categoria em um arquivo JSON
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump({key: value}, file, ensure_ascii=False, indent=4)

print(f"Arquivos salvos na pasta '{output_dir}'!")
