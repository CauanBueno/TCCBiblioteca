##DALL é conexao banco user ñ tem acesso
## Classe / Componentes  
## Ou """  __BANCO = Path(__file__).parent / '..banco.sqlite3'   """"

from pathlib import Path
import sqlite3

class Conexao:
    def __init__ (self):
        self.conexao = None
        
    def __enter__ (self):
        __BANCO = 'banco.sqlite3'
        
        self.conexao = sqlite3.connect(__BANCO)
        self.cursor = self.conexao.cursor()
        
        
        return self.cursor
    
    ##No __exit__"(self, tipoExcecao, valorExcecao, traceback)" é obrigatorio!!
    def __exit__(self, tipoExcecao, valorExcecao, traceback):
        self.conexao.commit()  # Salva as alterações no Banco
        self.cursor.close()    # Fechar o cursor (Como se eu não quisesse mais mexer no arquivo)
        self.conexao.close()   # Encerra a conexao (Como se tivesse fechando o arquivo)