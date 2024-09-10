from models.enums.sexo import Sexo
from models.enums.setor import Setor
from models.endereco import Endereco

class Funcionario:
    def __init__(self, matricula: str, nome : str,idade: int,setor : Setor, telefone: str, sexo: Sexo, endereco : Endereco ) -> None:
        self.matricula = matricula
        self.nome = nome
        self.idade = idade
        self.setor = setor
        self.telefone = telefone
        self.sexo = sexo
        self.endereco = endereco
    
    def __str__(self) -> str:
        return(
                f"\nMatricula: {self.matricula}"
                f"\nNome: {self.matricula}"
                f"\nIdade: {self.idade}"
                f"\nSetor: {self.setor.value}"
                f"\nTelefone: {self.telefone}"
                f"\nSexo: {self.sexo.value}"
                f"\nEndereco: {self.endereco}"
        )