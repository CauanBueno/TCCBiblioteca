from datetime import date
from BLL.LivrosBLL import LivrosBLL
from BLL.UsuariosBLL import UsuariosBLL
from BLL.ReservasBLL import ReservasBLL
from BLL.DevolucaoBLL import DevolucaoBLL
from datetime import date

def cadastroLivros():
    
    titulo = input("qual o titulo do livro ")
    subtitulo = input("Qual o subtitulo? ")
    ano = int(input("Qual o ano? "))
    autor = input("Qual o autor? ")
    editora = input("Qual a editora? ")
    categoria = input("Qual a categoria? ")
    idioma = input("Qual o idioma? ")
    quantidade = int(input("Qual a quantidade? "))    
    
    LivrosBLL().cadastrarLivrosBLL(titulo, subtitulo, ano, autor, editora, categoria, idioma,quantidade)
    
    print ("")
    print ('Livro cadastrado com sucesso')
    print ("")
    print ("")
    print ("")
    print ("=" *50, "Reiniciando...", "=" *50)
    print ("")
    
    
    
        

def cadastroUsuarios():
    nome = input("qual o nome? ")
    documento = int(input("numero do documento? "))
    data_nascimento = input("data de nascimento? ")
    date = data_nascimento
    email = input("Qual o email? ")
    telefone = input("Qual o telefone? ")
    endereco = input("Qual o endereço? ")

    UsuariosBLL().cadastrarUsuariosBLL(nome, documento, date, email, telefone, endereco)
    
    print ("")
    print ('Usuário cadastrado com sucesso')
    print ("")
    print ("")
    print ("")
    print ("=" *50, "Reiniciando...", "=" *50)
    print ("")

def alterarLivros():
    
    livros = LivrosBLL().listar()

    if livros:
        for livro in livros:
            print(livro)
            print("")
    codigo = int(input('Qual livro deseja alterar? '))
    
    livro = LivrosBLL().obter(codigo)
    
    livro.titulo = input('Qual o titulo? ')
    livro.subtitulo = input('Qual o subtitulo? ')
    livro.ano = input('Qual o ano? ')
    livro.autor = input('Qual o autor? ')
    livro.editora = input('Qual a editora? ')
    livro.categoria = input('Qual a categoria? ')
    livro.idioma = input('Qual o idioma? ')
    livro.qtde = input('Qual a quantidade? ')
    
    LivrosBLL().alterar(livro)
    
    print ("")
    print ('Livro alterado com sucesso!')
    print ("")
    print ("")
    print ("")
    print ("=" *50, "Reiniciando...", "=" *50)
    print ("")
    
    while iniciar() == False:
        print ("")

def alterarUsuarios():
    
    
    usuarios = UsuariosBLL().listar()

    if usuarios:
        for usuario in usuarios:
            print(usuario)
            print("")
    codigo = int(input('Qual usuário deseja alterar? '))
    
    usuario = UsuariosBLL().obter(codigo)
    
    usuario.nome = input('Qual o nome? ')
    usuario.documento = input('Qual o documento? ')
    usuario.data_nascimento = input('Qual a data de nascimento? ')
    usuario.email = input('Qual o email? ')
    usuario.telefone = input('Qual o telefone? ')
    usuario.endereco = input('Qual o endereço? ')
    
    UsuariosBLL().alterar(usuario)
    print ("")
    print ('Usuário alterado com sucesso!')
    print ("")
    print ("")
    print ("")
    print ("=" *50, "Reiniciando...", "=" *50)
    print ("")
    
    while iniciar() == False:
        print ("")
    
def cadastrarReserva():
    
    
    
    livros = LivrosBLL().listar()
    usuarios = UsuariosBLL().listar()
    
    if usuarios:
        for usuario in usuarios:
            print(usuario)
            print("")
    codigo1 = int(input('Qual e o cliente? '))
    

    if livros:
        for livro in livros:
            print(livro)
            print("")
    codigo2 = int(input('Qual livro deseja reservar? '))
    
    
    

    data_reserva = input("data de reserva? ")
    data = data_reserva
    
    data_entrega = input("data de entrega?  ")
    dev = data_entrega
    
    ReservasBLL().cadastrarReservasBLL(codigo1 , codigo2, data, dev)
    
    print ("")
    print ('cadastro realizado com sucesso!')
    print ("")
    print ("")
    print ("")
    print ("=" *50, "Reiniciando...", "=" *50)
    print ("")
    


def cadastrarDevolucao():
    
    reservas = ReservasBLL().listar()
    if reservas:
        for reserva in reservas:
            print(reserva)
    
    codigo = int(input("Qual devoluçao deseja fazer?"))
    hoje = date.today()
    devolucao = (codigo, hoje)
    
    DevolucaoBLL().cadastrarDevolucaoBLL(codigo, hoje)
    
    

def relatoriotodos():
    print(" > Livros Emprestados: ")
    print("")
    reservas = ReservasBLL().listar()
    if reservas:
        for reserva in reservas:
            print(reserva)
    print("")
    print(" > Livros Devolvidos: ")
    print("")
    devolucoes = DevolucaoBLL().listar()
    if devolucoes:
        for devolucao in devolucoes:
            print(devolucao)
        
        print ("")
        print ("")
        print ("=" *50, "Reiniciando...", "=" *50)
        print ("")
    while iniciar() == False:
        print ("")


def iniciar():
    print ("=" *40)
    print ("========= Biblioteca Tavares ===========")
    print ("=" *40)
    print ("")
    print ("(1) Cadastrar novo Livro")
    print ("(2) Cadastrar novo Cliente")
    print ("(3) Alterar dados de Livros")
    print ("(4) Alterar dados do Cliente")
    print ("(5) Cadastrar uma Reserva")
    print ("(6) Cadastrar uma Devolução")
    print ("(7) Relatório de controle de Livros emprestados e com atraso")
    print ("(8) Sair")
    print ("")
    sair = False
    try:
        opcao = int(input("Selecione opção desejada (x): "))
        print("")
        
        match opcao:
            case 1:
                cadastroLivros()
            case 2:
                cadastroUsuarios()
            case 3:
                alterarLivros()
            case 4:
                alterarUsuarios()
            case 5:
                cadastrarReserva()
            case 6:
                cadastrarDevolucao()
            case 7:
                relatoriotodos()
            case 8:
                print ("Saindo...")
                print ("")
                sair = True
            case _:
                print("")
                print ("OPÇÃO INVÁLIDA!")
    except Exception as erro:
        print(f"Opção inválida! Erro: {erro}")
    return sair

while iniciar() == False:
    print ("")
    print ("")
    print ("=================== Reiniciando... ===================")

