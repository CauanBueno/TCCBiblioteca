from BLL.LivrosBLL import LivrosBLL
from BLL.UsuariosBLL import UsuariosBLL
from BLL.ReservasBLL import ReservasBLL
from BLL.DevolucaoBLL import DevolucaoBLL

#devolucao = DevolucaoBLL().listar()
#if devolucao:
#    for devolucao in devolucao:
#        print(devolucao)

usuarios = UsuariosBLL().listar()

if usuarios:
    for usuario in usuarios:
        print(usuario)