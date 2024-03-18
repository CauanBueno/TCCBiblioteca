from models.Devolucao import Devolucao
from DAL.DevolucaoDAL import DevolucaoDAL

from dataclasses import dataclass
from datetime import date

@dataclass
class DevolucaoBLL:
    def cadastrarDevolucaoBLL (self, fk_idreserva: int, data_devolucao: date):
        sucesso = False
        
        try:
            if fk_idreserva == "":
                print("Campo: ID Reserva, é obrigatório.")
            elif data_devolucao is None:
                print("Campo: Data da Devolucão, é obrigatório.")
            else:
                sucesso = True
                devolucao = Devolucao(0, fk_idreserva, data_devolucao)
                DevolucaoDAL().cadastrarDevolucoesDAL(devolucao)
        except Exception as erro:
                print(f"Erro ao cadastrar uma devolucão. Erro: {erro}")
        return sucesso
    
    def listar(self):
        try:
            return DevolucaoDAL().listar()
        except Exception as erro:
            print(f"Erro ao executar o Relatório. Erro: {erro}")

