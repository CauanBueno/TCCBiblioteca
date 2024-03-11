from dataclasses import dataclass

@dataclass
class Usuario:
    id:               int
    nome:             str
    documento:        str
    data_nascimento:  dataclass
    email:            str
    telefone:         str
    endereco:         str