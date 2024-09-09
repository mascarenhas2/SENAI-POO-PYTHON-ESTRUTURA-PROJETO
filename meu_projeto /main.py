import os


from models.pessoa import Pessoa
from models.enums.sexo import Sexo
from models.endereco import Endereco

os.system("cls || clear")

pessoa1 = Pessoa("Caio",22,Sexo.MASCULINO,
                 Endereco("Rua Souto Dalva", 78))

print(pessoa1)