from DAL.Conexao import Conexao
from models.Reserva import Reserva

class ReservasDAL:
    def cadastrarReservasDAL(self, reserva: Reserva):
        with Conexao() as conexao:
            sql = 'insert into reservas (fk_nome, fk_titulo, data_reserva, data_prevdevol) values (?,?,?,?)'
            parametros = [ reserva.fk_nome, reserva.fk_titulo, reserva.data_reserva, reserva.data_prevDevol ]
            
            conexao.execute (sql, parametros)
            
            return True