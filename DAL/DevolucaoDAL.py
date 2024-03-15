from DAL.Conexao import Conexao
from models.Devolucao import Devolucao
from models.Reserva import Reserva

class DevolucaoDAL:
    def cadastrarDevolucoesDAL(self, devolucao: Devolucao):
        with Conexao() as conexao:
            sql = 'insert into devolucoes (fk_idreserva, data_devolucao) values (?,?)'
            parametros = [devolucao.fk_idreserva, devolucao.data_devolucao]
            
            conexao.execute (sql, parametros)
            
            return True
    
    def listar (self):
        with Conexao() as conexao:
            sql = 'select fk_idreserva, data_devolucao,	data_reserva, nome, titulo from	devolucoes inner join reservas on devolucoes.fk_idreserva = reservas.id, usuarios on reservas.fk_nome = usuarios.id, livros on reservas.fk_titulo = livros.id'
            conexao.execute(sql)
            
            linhas = conexao.fetchall()
            
            if linhas:
                devolucao: list [Devolucao, Reserva] = []
                
                for linha in linhas:
                    fk_idreserva, data_devolucao, data_reserva, nome, titulo = linha
                    devolucao = Devolucao, Reserva (fk_idreserva, data_devolucao, data_reserva, nome, titulo)
                    
                return devolucao


class Relatorio:
    def listar (self):
        with Conexao() as conexao:
            sql = 'select fk_idreserva, data_devolucao, data_reserva, nome, titulo from devolucao'
            conexao.execute(sql)
            linhas = conexao.fetchall()
            
            if linhas:
                relatorio: list [Relatorio] = []
                
                for linha in linhas:
                    id, fk_idreserva, data_devolucao, data_reserva, nome, titulo = linha
                    relatorio = Devolucao (id, fk_idreserva, data_devolucao, data_reserva, nome, titulo)
                    
                return relatorio
