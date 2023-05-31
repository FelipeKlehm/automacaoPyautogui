from selenium import webdriver
from selenium.webdriver.common.by import By
from perfil import Perfil

class Perfis(Perfil):
    
    def __init__(self, nome, nasc, cpf, email, telefone):
        super().__init__(nome, nasc, cpf, email, telefone)
        self.nome = nome
        self.nasc = nasc
        self.cpf = cpf
        self.email = email
        self.telefone = telefone

class CadastrarPerfil:
    def  perfil0() -> None:

        perfi0 = Perfis(nome='', nasc='', cpf='', email='', telefone='')
        nasc0 = perfi0.monta_dt_nasc()
        nome0 = perfi0.monta_nome()
        cpf0 = perfi0.monta_cpf()
        email0 = perfi0.monta_email()

        print(perfi0)

        return nome0

        
    def perfil1(perfi1) -> None:

        perfi1 = Perfis(nome='', nasc='', cpf='', email='', telefone='')
        nasc1= perfi1.monta_dt_nasc()
        nome1 = perfi1.monta_nome()
        cpf1 = perfi1.monta_cpf()
        email1 = perfi1.monta_email()
        telefone1 = perfi1.gerar_telefone()

perfil0 = CadastrarPerfil.perfil0()

print(perfil0)