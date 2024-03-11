from models.Reserva import Reserva
from DAL.ReservasDAL import ReservasDAL

from dataclasses import dataclass
from datetime import date

@dataclass
class ReservasBLL:
    def cadastrarReservasBLL (self, fk_nome: int, fk_titulo: int, data_reserva: date, data_prevdevol: date):
        sucesso = False
        
        try:
            if fk_nome == "":
                print("Campo: Nome, é obrigatório.")
            elif fk_titulo == "":
                print("Campo: Titulo, é obrigatório.")
            elif data_reserva is None:
                print("Campo Data da Reserva, é obrigatório.")
            elif data_prevdevol is None:
                print("Campo Data de Devolução, é obrigatório.")
            else:
                sucesso = True
                reserva = Reserva(0, fk_nome, fk_titulo, data_reserva, data_prevdevol)
                ReservasDAL().cadastrarReservasDAL(reserva)
        
        except Exception as erro:
            print(f"Erro ao cadastrar um Livro. Erro: {erro}")
        return sucesso