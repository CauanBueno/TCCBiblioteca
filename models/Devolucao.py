from dataclasses import dataclass
from datetime import date

@dataclass
class Devolucao:
    id:                  int
    fk_idreserva:        int
    data_devolucao:      date
