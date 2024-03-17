from typing import List
from DAL.Conexao import Conexao
from models.Reserva import Reserva

class ReservasDAL:
    def cadastrarReservasDAL(self, reserva: Reserva):
        with Conexao() as conexao:
            sql = 'insert into reserva (fk_nome, fk_titulo, data_reserva, data_prevdevol) values (?,?,?,?)'
            parametros = [ reserva.fk_nome, reserva.fk_titulo, reserva.data_reserva, reserva.data_prevDevol ]
            
            conexao.execute (sql, parametros)
            
            return True
        
    def listar(self):
        with Conexao() as conexao:
            sql = 'select * from reservas'
            
            conexao.execute(sql)
            linhas = conexao.fetchall()
            
            if linhas:
                
                reservas: List[Reserva] = []
                
                for linha in linhas:
                    id, fk_nome, fk_titulo, data_reserva, data_prevdevol = linha
                    reserva = Reserva(id, fk_nome, fk_titulo, data_reserva, data_prevdevol)
                
                    reservas.append(reserva)
                
                return reservas
            
    def obter(self, codigo: int):
        with Conexao() as conexao:
            sql = 'select * from reservas where id = ?'
            parametros = [codigo]
            
            conexao.execute(sql, parametros)
            linha = conexao.fetchone()
            
            if linha:
                id, fk_nome, fk_titulo, data_reserva, data_prevdevol = linha
                reserva = Reserva(id, fk_nome, fk_titulo, data_reserva, data_prevdevol)

                return reserva
