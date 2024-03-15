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
            sql = 'select * from devolucoes'
            conexao.execute(sql)
            
            linhas = conexao.fetchall()
            
            if linhas:
                devolucao: list [Devolucao] = []
                
                for linha in linhas:
                    fk_idreserva, data_devolucao = linha
                    devolucao = Devolucao (fk_idreserva, data_devolucao)
                    
                return devolucao


class RelatorioDAL:
    def listarRelarorioDAL(self, fk_nome: Reserva, fk_titulo: Reserva, data_reserva: Reserva, data_prevdevol: Reserva, data_devolucao: Devolucao):
        with Conexao() as conexao:
            sql = "select nome 'Nome Cliente:', titulo 'Titulo Livro:', data_reserva 'Data da reserva:', data_prevdevol 'Data prevista de devolução:', data_devolucao 'Data real devolução:' from reservas left join devolucoes on devolucoes.fk_idreservas = reservas.id, usuarios on reservas.fk_nome = usuarios.id, livros on reservas.fk_titulo = livros.id"
            parametros = [fk_nome, fk_titulo, data_reserva, data_prevdevol, data_devolucao]
            conexao.execute(sql, parametros)
            linhas = conexao.fetchmany()
            
            if linhas:
                relatorios: list [Reserva, Devolucao] = []
                
                for linha in linhas:
                    fk_nome, fk_titulo, data_reserva, data_prevdevol, data_devolucao = linha
                    relatorio = Reserva (fk_nome, fk_titulo, data_reserva, data_prevdevol), Devolucao (data_devolucao)
                    
                    relatorios.append(relatorio)
                
                return relatorios
