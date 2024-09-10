import os
from models.enums.setor import Setor
from models.enums.sexo import Sexo
from models.enums.unidadeFederativa import UnidadeFederativa 
from models.endereco import Endereco
from models.funcionario import Funcionario

os.system("cls || clear")

funcionario1 = Funcionario("7332","Caio",20,Setor.ANALISTA_DE_SISTEMA,"7344",Sexo.MASCULINO,
                           Endereco("Rua Souto Dalva","78","Fundo","40301065","Salvador",UnidadeFederativa.BAHIA))
                          
print(funcionario1)
