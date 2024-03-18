from typing import List
from DAL.Conexao import Conexao
from models.Livro import Livro

class LivrosDAL:
    def cadastrarLivrosDAL(self, livro: Livro):
        with Conexao() as conexao:
            sql = 'insert into livros (titulo, subtitulo, ano, autor, editora, categoria, idioma, qtde) values (?, ?, ?, ?, ?, ?, ?, ?)'
            parametros = [ livro.titulo, livro.subtitulo, livro.ano, livro.autor, livro.editora, livro.categoria, livro.idioma, livro.qtde ]
            
            conexao.execute(sql, parametros)
            
            return True
    
    
    def listar(self):
        with Conexao() as conexao:
            sql = 'select * from livros'
            
            conexao.execute(sql)
            linhas = conexao.fetchall()
            
            if linhas:
                
                livros: List[Livro] = []
                
                for linha in linhas:
                    id, titulo, subtitulo, ano, autor, editora, categoria, idioma, qtde = linha
                    livro = Livro(id, titulo, subtitulo, ano, autor, editora, categoria, idioma, qtde)
                
                    livros.append(livro)
                
                return livros
            
    def obter(self, codigo: int):
        with Conexao() as conexao:
            sql = 'select * from livros where id = ?'
            parametros = [codigo]
            
            conexao.execute(sql, parametros)
            linha = conexao.fetchone()
            
            if linha:
                id, titulo, subtitulo, ano, autor, editora, categoria, idioma, qtde = linha
                livro = Livro(id, titulo, subtitulo, ano, autor, editora, categoria, idioma, qtde)

                return livro
            
    def alterar(self, livro: Livro):
        with Conexao() as conexao:
            sql = 'update livros set titulo = ?, subtitulo = ?, ano = ?, autor = ?, editora = ?, categoria = ?, idioma = ?, qtde = ? where id = ?'
            parametros = [livro.titulo, livro.subtitulo, livro.ano, livro.autor, livro.editora, livro.categoria, livro.idioma, livro.qtde, livro.id]
            
            conexao.execute(sql, parametros)
            
            return True