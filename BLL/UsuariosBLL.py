from models.Usuario import Usuario
from DAL.UsuariosDAL import UsuariosDAL
from datetime import date


class UsuariosBLL:
    def cadastrarUsuariosBLL(self, nome: str, documento: str, data_nascimento: date, email: str, telefone: str, endereco: str):
        sucesso = False
        
        try:
            if nome == "":
                print("Campo: Nome, é obrigatório.")
            elif documento == "":
                print("Campo: Documento, é obrigatório.")
            elif data_nascimento is None:
                print("Campo: Data Nascimento, é obrigatorio.")
            elif email == "":
                print("Campo: Email, é obrigatório.")
            elif telefone == "":
                print("Campo: Telefone, é obrigatório.")
            elif endereco == "":
                print("Campo: Endereço, é obrigatório.")
            else:
                sucesso = True
                usuario = Usuario(0, nome, documento, data_nascimento, email, telefone, endereco)
                UsuariosDAL().cadastrarUsuariosDAL(usuario)
        
        except Exception as erro:
            print(f"Erro ao cadastrar um Usuario. Erro: {erro}")
        return sucesso
    
    def obter(self, codigo: int):
        try:
            return UsuariosDAL().obter(codigo)
        except Exception as erro:
            print(f"Erro ao obter um livro, Erro: {erro}")
    
    def listar(self):
        try:
            return UsuariosDAL().listar()
        except Exception as erro:
            print(f"Erro ao listar os usuários, Erro: {erro}")
    
    def alterar(self, usuario:Usuario):
    
        sucesso = False
        
        try:
            podeContinuar = False
            
            if usuario.nome == "":
                print("Nome é obrigatório!")
            elif usuario.documento == "":
                print("Documento é obrigatório!")
            elif usuario.data_nascimento == "":
                print("Data de nascimento é obrigatória!")
            elif usuario.email == "":
                print("Email é obrigatório!")
            elif usuario.telefone == "":
                print("Telefone é obrigatória!")
            elif usuario.endereco == "":
                print("Endereço é obrigatório!")
            else:
                podeContinuar = True
            
            if podeContinuar is True:
                UsuariosDAL().alterar(usuario)
                sucesso = True
                
        except Exception as erro:
            print(f"Erro ao editar o usuário. Erro: {erro}")
            
        return sucesso