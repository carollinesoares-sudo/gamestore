Sistema de Gerenciamento de Livros (CLI)

Este projeto é um sistema simples em Python para gerenciamento de livros via terminal (linha de comando). Ele permite cadastrar, listar, atualizar e remover livros organizados por gênero.

Funcionalidades
Cadastrar livros por gênero
Listar livros cadastrados
Atualizar informações de um livro
Remover livros
Armazenamento em arquivo JSON
Gêneros disponíveis
Romance
Mistério
Ficção Científica
Tecnologias utilizadas
Python 3
Biblioteca padrão json
Estrutura do projeto
projeto/
 ├── main.py
 ├── genero.json
 └── README.md
Formato do arquivo JSON

O arquivo genero.json deve conter uma estrutura como esta:

{
  "romance": [],
  "misterio": [],
  "ficcao": []
}
Como executar
Certifique-se de ter o Python instalado
Crie o arquivo genero.json com o conteúdo acima
Execute o programa:
python main.py
Menu do sistema
====== MENU ======
1. Cadastrar Livro
2. Listar Livros
3. Atualizar Livro
4. Remover Livro
5. Sair
====================
Observações importantes
O índice dos livros começa em 1, mas internamente o Python usa 0
O programa depende do arquivo genero.json existir
Entradas inválidas podem gerar erros (por exemplo, letras em vez de números)
Possíveis melhorias
Validação de entrada do usuário
Tratamento de erros (try/except)
Interface gráfica
Busca de livros por nome
Mais gêneros
Uso de banco de dados (como SQLite)
Autor

Projeto desenvolvido para prática de estruturas de dados, manipulação de arquivos JSON e programação em Python.