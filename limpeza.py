import os
import schedule
import time
from datetime import datetime

# Diretório alvo
DIRECTORY = r"C:\Users\SANTIAGO\Pictures\PRINT"

def delete_files():
    try:
        if not os.path.exists(DIRECTORY):
            print(f"Diretório {DIRECTORY} não encontrado.")
            return
        
        for filename in os.listdir(DIRECTORY):
            file_path = os.path.join(DIRECTORY, filename)
            if os.path.isfile(file_path):
                try:
                    os.remove(file_path)
                    print(f"Arquivo {filename} excluído com sucesso.")
                except Exception as e:
                     print(f"Erro ao excluir {filename}: {e}")
        
        print(f"[{datetime.now()}] Todos os arquivos foram excluídos do diretório {DIRECTORY}")
    
    except Exception as e:
        print(f"Erro ao processar o diretório: {e}")

# Configura a automação para rodar todos os dias às 18:00
schedule.every().day.at("18:00").do(delete_files)

if __name__ == "__main__":
    print(f"Iniciando automação para excluir arquivos em {DIRECTORY}")
    delete_files()  # Executa a função imediatamente ao iniciar o script
    
    while True:
        schedule.run_pending()
        time.sleep(60)