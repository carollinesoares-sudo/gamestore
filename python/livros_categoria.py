import json

def menu(): #há um menu para o usuário escolher a categoria do livro
    print("====== MENU ======") 
    print("1. Cadastrar Livro")
    print("2. Listar Livros")
    print("3. Atualizar Livro")
    print("4. Remover Livro")
    print("5. Sair")
    print("====================")

def escolher_genero():#há um menu para o usuário escolher o gênero do livro
    print("====== GÊNERO ======")
    print("1. Romance")
    print("2. Mistério")
    print("3. Ficção Científica")
    print("=====================")

    opcao = input("Escolha uma opção: ") #O usuário escolhe a opção do gênero do livro

    if opcao == "1":
        return "romance"
    
    elif opcao == "2":
        return "misterio"
    
    elif opcao == "3":
        return "ficcao"

    else:
        print("Opção Inválida!")

def ler_dados():
    with open("genero.json", "r", encoding="utf-8") as arquivo:
        return json.load(arquivo) #A função ler_dados() lê os dados do arquivo "genero.json" e retorna o conteúdo como um objeto Python.
    

    
def salvar_dados(dados):
    with open("genero.json", "w", encoding="utf-8") as arquivo:#A função salvar_dados(dados) salva os dados fornecidos no arquivo "genero.json". O arquivo é aberto no modo de escrita ("w") 
        json.dump(dados, arquivo, indent=2, ensure_ascii=False)#A função json.dump() é usada para escrever os dados no arquivo JSON. O parâmetro indent=2 é usado para formatar o JSON com uma indentação de 2 espaços, tornando-o mais legível.



def adicionar():#A função adicionar() é responsável por adicionar um novo livro à categoria escolhida pelo usuário. Ela solicita ao usuário que escolha um gênero, insira o título e o autor do livro, e então salva essas informações no arquivo JSON correspondente ao gênero escolhido.
    genero = escolher_genero()
    if not genero:
        return
    
    titulo = input("Título: ")
    autor = input("Autor: ")

    dados = ler_dados()
    dados[genero].append({ #Adiciona um novo livro à lista do gênero escolhido, onde o título e o autor são armazenados como um dicionário.
        "titulo": titulo,
        "autor": autor
    })

    salvar_dados(dados)
    print("Livro Adicionado na Biblioteca!")



def listar(): #A função listar() é responsável por listar os livros de uma categoria escolhida pelo usuário. 
    genero = escolher_genero()
    if not genero:
        return
    
    dados = ler_dados()
    print(f"Lista de {genero.upper()}:")
    
    for codigo, livro in enumerate(dados[genero], start=1): #A função enumerate() é usada para iterar sobre a lista de livros do gênero escolhido, fornecendo um índice (index) e o livro correspondente (livro) em cada iteração. O parâmetro start=1 é usado para iniciar a contagem dos índices a partir de 1, em vez de 0.
        print(f"{codigo}. {livro['titulo']} - {livro['autor']}")




def atualizar():#
    genero = escolher_genero()

    if not genero:
        return
    
    dados = ler_dados()

    codigo = int(input("Indice do contato: ")) -1

    if 0 <= codigo < len(dados[genero]):
        nome = input("Novo Titulo: ")
        telefone = input("Novo Autor: ")

        dados[genero][codigo] = {
            "nome": nome,
            "telefone": telefone
        }
        salvar_dados(dados)#A função salvar_dados(dados) é chamada para salvar as alterações feitas no arquivo JSON, garantindo que as informações atualizadas sejam persistidas.
        print("Contato Atualizado!")

    else: 
        print("Índice Invcálido...")

def remover():
    genero = escolher_genero()
    if not genero:
        return
    
    dados = ler_dados()

    codigo = int(input("Código do Livro: ")) -1

    if 0 <= codigo < len(dados[genero]):
        dados[genero].pop(codigo)

        salvar_dados(dados)
        print("Livro Removido")
        
    else:
        print("Código Inválifo...")

def main():
    while True:#O loop while True: é usado para criar um loop infinito que mantém o programa em execução até que o usuário escolha a opção de sair (opção 5). Dentro do loop, o menu é exibido e o programa aguarda a entrada do usuário para escolher uma opção. Dependendo da opção escolhida, a função correspondente (adicionar, listar, atualizar ou remover) é chamada para realizar a ação desejada. Se o usuário escolher a opção de sair, o loop é interrompido e o programa é encerrado.
        menu()
        opcao = input("Escolha: ")
        if opcao == "1":
            adicionar()

        elif opcao == "2":
            listar()

        elif  opcao == "3":
            atualizar()

        elif opcao == "4":
            remover()

        elif opcao == "5":
            print("Saindo...")
            break
        else: 
            print("Opção Inválido!")

# Executa o programa
main()