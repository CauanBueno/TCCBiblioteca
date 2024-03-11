from DAL.Conexao import Conexao
from models.Devolucao import Devolucao
from models.Reserva import Reserva

class DevolucaoDAL:
    def cadastrarDevolucoesDAL(self, devolucao: Devolucao):
        with Conexao() as conexao:
            sql = 'insert into devolucao (fk_idreserva, data_devolucao) values (?,?)'
            parametros = [devolucao.fk_idreserva, devolucao.data_devolucao]
            
            conexao.execute (sql, parametros)
            
            return True
    
    def listar (self):
        with Conexao() as conexao:
            sql = 'select fk_idreserva, data_devolucao,	data_reserva, nome, titulo from	devolucao inner join reserva on devolucao.fk_idreserva = reserva.id, usuario on reserva.fk_nome = usuario.id, livro on reserva.fk_titulo = livro.id'
            conexao.execute(sql)
            
            linhas = conexao.fetchall()
            
            if linhas:
                devolucao: list [Devolucao, Reserva] = []
                
                for linha in linhas:
                    fk_idreserva, data_devolucao, data_reserva, nome, titulo = linha
                    devolucao = Devolucao, Reserva (fk_idreserva, data_devolucao, data_reserva, nome, titulo)
                    
                return devolucao
