import json 
import os
def carregar_dados():
    #Se o arquivo não existir, retorna uma lista vazia
    if not os.path.exists("dados.json"): #Verifica se o arquivo existe
        return[]#Se o arquivo não existir, retorna uma lista vazia
    
    #abre o arquivo em modo leitura 
    with open("dados.json", "r", encoding="utf-8") as arquivo:
        #onde o r é para abrir o arquivo somente leitura READ 
        return json.load(arquivo)
    
def salvar_dados(dados):
    #Abre o arquivo em modo escrita
    with open("dados.json", "w", encoding="utf-8") as arquivo:
        #Onde w é WRITE
        #indent para deixar o json organizado
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

def criar_pessoa(nome, idade):#Recebe o nome e a idade como parâmetros
    dados = carregar_dados() #Carrega os dados existentes do arquivo JSON para a variável dados

    #Gera um ID simples
    novo_id = 1
    if dados:
        novo_id = dados[-1]["id"] + 1
    pessoa = {
        "id": novo_id,
        "nome" : nome,
        "idade": idade 
    }

    dados.append(pessoa)#Adiciona a nova pessoa à lista de dados
    salvar_dados(dados)#Salva os dados atualizados de volta no arquivo JSON

    print("Pessoa cadastrada com sucesso!")

def listar_pessoas():#Carrega os dados do arquivo JSON para a variável dados
    dados = carregar_dados()

    if not dados:#Verifica se a lista de dados está vazia
        print("Nenhum registro encontrado.")
        return
    for pessoa in dados:#Itera sobre cada pessoa na lista de dados e imprime suas informações formatadas
        print(f"ID: {pessoa['id']},| Nome: {pessoa['nome']}| Idade: {pessoa['idade']}")
def atualizar_pessoa(id, novo_nome, nova_idade):
    dados = carregar_dados()

    for pessoa in dados:
        if pessoa["id"] == id:
            pessoa["nome"] = novo_nome
            pessoa["idade"] = nova_idade
            salvar_dados(dados)
            print("Pessoa atualizada com sucesso!")
            return
    print("ID não encontrado.")
def deletar_pessoa(id):
    dados = carregar_dados()
    #Criar nova lista sem o ID informado
    dados = [pessoa for pessoa in dados if pessoa ["id"] != id]

    salvar_dados(dados)
    print("Pessoa removida (Se existia).")

while True:
    print("\n1 - Cadastrar")
    print("2 - Listar")
    print("3 - Atualizar")
    print("4 - Deletar")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome: ")
        idade = int(input("idade: "))#Converte a entrada de idade para um número inteiro
        criar_pessoa(nome, idade)

    elif opcao == "2":
        listar_pessoas()
    
    elif opcao == "3":
        id = int(input("ID: "))
        nome = input("Novo nome: ")
        idade = int(input("Nova idade: "))
        deletar_pessoa(id)

    elif opcao == "4":
        id = int(input("ID: "))
        deletar_pessoa(id)

    elif opcao == "0":
        break

    else: 
        print("Opção inválida. Tente novamente.")
        
