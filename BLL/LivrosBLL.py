# instanciando a classe para virar objeto

from models.Livro import Livro
from DAL.LivrosDAL import LivrosDAL

class LivrosBLL:
    def cadastrarLivrosBLL(self, titulo: str, subtitulo: str, ano: int, autor: str, editora:str, categoria: str, idioma: str, qtde: int):
        sucesso = False
        
        try:        
            if titulo == "":
                print("Campo: Titulo, é obrigatório.")
            elif subtitulo == "":
                print("Campo: Subtitulo, é obrigatório.")
            elif ano is None:
                print("Campo: Ano, é obrigatório.")
            elif autor == "":
                print("Campo: Autor, é obrigatório.")
            elif editora == "":
                print("Campo: Editora, é obrigatório.")
            elif categoria == "":
                print("Campo: Categoria, é obrigatório.")
            elif idioma == "":
                print("Campo: Idioma, é obrigatório.")
            elif qtde is None:
                print("Campo: Quantidade, é obrigatório.")
            else:
                sucesso = True
                livro = Livro(0, titulo, subtitulo, ano, autor, editora, categoria, idioma, qtde)
                LivrosDAL().cadastrarLivrosDAL(livro)
        
        except Exception as erro:
            print(f"Erro ao cadastrar um Livro. Erro: {erro}")
        return sucesso
    
    def listar(self):
        try:
            return LivrosDAL().listar()
        except Exception as erro:
            print(f"Erro ao listar os livros, Erro: {erro}")
            
    def obter(self, codigo: int):
        try:
            return LivrosDAL().obter(codigo)
        except Exception as erro:
            print(f"Erro ao obter um livro, Erro: {erro}")
            
    def alterar(self, livro:Livro):
        sucesso = False
        
        try:
            podeContinuar = False
                    
            if livro.titulo == "":
                print("Campo: Titulo, é obrigatório.")
            elif livro.subtitulo == "":
                print("Campo: Subtitulo, é obrigatório.")
            elif livro.ano is None:
                print("Campo: Ano, é obrigatório.")
            elif livro.autor == "":
                print("Campo: Autor, é obrigatório.")
            elif livro.editora == "":
                print("Campo: Editora, é obrigatório.")
            elif livro.categoria == "":
                print("Campo: Categoria, é obrigatório.")
            elif livro.idioma == "":
                print("Campo: Idioma, é obrigatório.")
            elif livro.qtde is None:
                print("Campo: Quantidade, é obrigatório.")
            else:
                
                podeContinuar = True
                
            if podeContinuar is True:
                LivrosDAL().alterar(livro)
                sucesso = True
                
        
        except Exception as erro:
            print(f"Erro ao cadastrar um Livro. Erro: {erro}")
        return sucesso