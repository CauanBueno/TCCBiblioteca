from dataclasses import dataclass

@dataclass
class Livro:
    id:             int
    titulo:         str
    subtitulo:      str
    ano:            int
    autor:          str
    editora:        str
    categoria:      str
    idioma:         str
    qtde:           int
