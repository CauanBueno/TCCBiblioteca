from BLL.LivrosBLL import LivrosBLL
from BLL.UsuariosBLL import UsuariosBLL
from BLL.ReservasBLL import ReservasBLL
from BLL.DevolucaoBLL import DevolucaoBLL

def cadastroLivros():
    ...

def cadastroUsuarios():
    ...

def alterarLivros():
    ...

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

def cadastrarReserva():
    ...

def cadastrarDevolucao():
    ...

def relatorioLivros():
    devolucao = DevolucaoBLL().listar()
    if devolucao:
        for devolucao in devolucao:
            print(devolucao)


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
                relatorioLivros()
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

