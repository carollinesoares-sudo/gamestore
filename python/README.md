# Sistema de Biblioteca em Python

## Descrição

Este projeto é um sistema simples de gerenciamento de livros feito em Python.
Os dados são armazenados em um arquivo JSON (`genero.json`) e organizados por gênero.

---

## Funcionalidades

* Cadastrar livros
* Listar livros por gênero
* Atualizar livros
* Remover livros
* Menu interativo no terminal

---

## Como funciona

O sistema funciona em loop:

* O usuário escolhe uma opção no menu
* Seleciona o gênero do livro
* Realiza a operação desejada
* Os dados são salvos no arquivo JSON

---

## Estrutura dos dados

Exemplo do arquivo `genero.json`:

```json
{
  "romance": [],
  "misterio": [],
  "ficcao": []
}
```

Cada livro é armazenado assim:

```json
{
  "titulo": "Nome do Livro",
  "autor": "Nome do Autor"
}
```

---

## Funções principais

* `menu()` → Exibe o menu principal
* `escolher_genero()` → Escolha do gênero
* `ler_dados()` → Lê os dados do JSON
* `salvar_dados()` → Salva no JSON
* `adicionar()` → Adiciona livro
* `listar()` → Lista livros
* `atualizar()` → Atualiza livro
* `remover()` → Remove livro
* `main()` → Controla o sistema

---

## Observações

* O arquivo `genero.json` deve existir antes da execução
* A função `atualizar()` utiliza nomes diferentes (`nome` e `telefone`), o ideal é usar `titulo` e `autor`
* Não há tratamento de erro para entradas inválidas

---

## Execução

Para rodar o programa:

```bash
python nome_do_arquivo.py
```

---

## Objetivo

Praticar:

* Python básico
* Estruturas de dados
* Manipulação de arquivos JSON
