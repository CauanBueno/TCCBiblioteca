from dataclasses import dataclass
from datetime import date

@dataclass
class Reserva:
    id:                 int
    fk_nome:            int
    fk_titulo:          int
    data_reserva:        date
    data_prevdevol:      date