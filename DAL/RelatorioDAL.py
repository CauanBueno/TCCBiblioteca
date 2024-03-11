from DAL.Conexao import Conexao
from models.Devolucao import Devolucao
from models.Reserva import Reserva

from dataclasses import dataclass
from datetime import date

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