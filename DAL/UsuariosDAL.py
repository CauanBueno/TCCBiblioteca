from typing import List
from DAL.Conexao import Conexao
from models.Usuario import Usuario

class UsuariosDAL:
    def cadastrarUsuariosDAL(self, usuario: Usuario):
        with Conexao() as conexao:
            sql = 'insert into usuario (nome, documento, data_nascimento, email, telefone, endereco) values (?,?,?,?,?,?)'
            parametros = [usuario.nome, usuario.documento, usuario.data_nascimento, usuario.email, usuario.telefone, usuario.endereco]
            
            conexao.execute(sql, parametros)
            
            return True
        
    def listar(self):
        with Conexao() as conexao:
            sql = 'select * from usuarios'
            
            conexao.execute(sql)
            linhas = conexao.fetchall()
            
            if linhas:
                
                usuarios: List[Usuario] = []
                
                for linha in linhas:
                    id, nome, documento, data_nascimento, email, telefone, endereco = linha
                    usuario = Usuario(id, nome, documento, data_nascimento, email, telefone, endereco)
                
                    usuarios.append(usuario)
                
                return usuarios
        
    def alterar(self, usuario: Usuario):
        with Conexao() as conexao:
            sql = 'update usuarios set nome = ?, documento = ?, data_nascimento = ?, email = ?, telefone = ?, endereço = ? where id = ?'
            parametros = [usuario.nome, usuario.documento, usuario.data_nascimento, usuario.email, usuario.telefone, usuario.endereco, usuario.id]
            
            conexao.execute(sql, parametros)
            
            return True