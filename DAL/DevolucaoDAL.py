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
    
    def listar(self):
        with Conexao() as conexao:
            sql = 'select * from devolucoes'
            conexao.execute(sql)
            
            linhas = conexao.fetchall()
            
            if linhas:
                devolucoes: list[Devolucao] = []
                
                for linha in linhas:
                    id, fk_idreserva, data_devolucao = linha
                    devolucao = Devolucao (id, fk_idreserva, data_devolucao)
                    
                    devolucoes.append(devolucao)
                
                return devolucoes

