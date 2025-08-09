Limpeza de Pastas
Este repositório contém um script Python (limpeza.py) que automatiza a exclusão de arquivos em um diretório específico, configurado para rodar diariamente às 18:00. O script é útil para manter pastas limpas, como diretórios de capturas de tela ou arquivos temporários.
Funcionalidade

Objetivo: Exclui todos os arquivos no diretório especificado.
Diretório Alvo: Configurado por padrão para C:\Users\SANTIAGO\Pictures\PRINT (pode ser alterado via variável de ambiente TARGET_DIR).
Agendamento: Executa automaticamente às 18:00 todos os dias usando o módulo schedule.
Logs: Exibe mensagens no console indicando sucesso ou erros durante a exclusão.

Requisitos

Python 3.x
Bibliotecas Python:
schedule
os
datetime
time



Instale as dependências com:
pip install schedule

Como Usar

Clone o Repositório:
git clone https://github.com/santiago0070/limpeza-pastas.git
cd limpeza-pastas


Configurar o Diretório (opcional):

Por padrão, o script exclui arquivos em C:\Users\SANTIAGO\Pictures\PRINT.
Para usar outro diretório, defina a variável de ambiente TARGET_DIR:export TARGET_DIR="caminho/do/seu/diretório"

No Windows, use:set TARGET_DIR=caminho\do\seu\diretório




Executar o Script:

Rode o script diretamente:python limpeza.py


O script excluirá os arquivos imediatamente e continuará rodando para executar a limpeza diária às 18:00.


Parar o Script:

Pressione Ctrl+C para interromper a execução.



Estrutura do Projeto
limpeza-pastas/
│
├── limpeza.py      # Script principal para limpeza de arquivos
├── README.md       # Este arquivo
└── .gitignore      # Ignora arquivos temporários e caches

Notas

Atenção: O script exclui todos os arquivos no diretório especificado sem confirmação. Use com cuidado.
Personalização: Modifique a variável DIRECTORY no script ou use TARGET_DIR para alterar o diretório alvo.
Logs: Erros ou sucessos são registrados no console com timestamps.

Contribuições
Sinta-se à vontade para abrir issues ou pull requests com melhorias, como suporte a múltiplos diretórios ou exclusão seletiva de arquivos.
