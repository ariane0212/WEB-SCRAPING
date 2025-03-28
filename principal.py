import requests
import os
from zipfile import ZipFile
import time


# Função para baixar arquivos
def download_pdf(url, filename):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers, allow_redirects=True)

    if response.status_code == 200 and "application/pdf" in response.headers.get("Content-Type", ""):
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Baixado {filename} com sucesso")
    else:
        print(
            f"Falha ao baixar {filename}. Status code: {response.status_code}, Content-Type: {response.headers.get('Content-Type')}")


# URLs corrigidas
annexes = {
    "Anexo_I.pdf": "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf",
    "Anexo_II.pdf": "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf"
}

# Cria um diretório para downloads se ele não existir
if not os.path.exists("downloads"):
    os.makedirs("downloads")

# Download de cada anexo
for filename, url in annexes.items():
    filepath = os.path.join("downloads", filename)
    download_pdf(url, filepath)
    time.sleep(2)

# Cria um arquivo ZIP contendo todos os anexos baixados
zip_filename = "Anexos.zip"
with ZipFile(zip_filename, 'w') as zipf:
    for filename in annexes.keys():
        filepath = os.path.join("downloads", filename)
        if os.path.exists(filepath):
            zipf.write(filepath, filename)
            print(f"Adicionado {filename} ao {zip_filename}")

print(f"Arquivo ZIP criado com sucesso!: {zip_filename}")
