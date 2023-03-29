from br_nome_gen import pessoa_random
from cpf_generator import CPF
import unidecode, random as r


class Perfil: 
    def __init__(self, nome, nasc, cpf, email, telefone):
        self.nome = nome
        self.nasc = nasc
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
    
    # Metodo da Data de nascimento
    def monta_dt_nasc(self):
        
        self.ano = r.randint(1975, 2003)

        self.dia = r.randint(1, 29)
        if self.dia<=9:
            self.dia=(f"0{self.dia}")

        self.mes = r.randint (1, 12)
        if self.mes<=9:
            self.mes=(f"0{self.mes}")


        self.nasc = (f"{self.dia}/{self.mes}/{self.ano}") # Variavel Real
        print(self.nasc)
        return self.nasc
    
    # Metodo do Nome
    def monta_nome(self):

        self.nome = pessoa_random()
        self.nome = str(self.nome.nome)
        

        print (self.nome)
        return self.nome
    
    # Metodo de gerar CPF
    
    def monta_cpf(self):
        self.cpf = CPF.generate()
        print(f'{self.cpf[:3]}.{self.cpf[3:6]}.{self.cpf[6:9]}-{self.cpf[9:]}')
        return self.cpf

    # Metodo de gerar Email

    def monta_email(self):    
        p = pessoa_random()
        webmail = ['@gmail.com', '@hotmail.com', "@yahoo.com",  '@outlook.com']
        email= p.nome.lower()[:5] + r.choice(webmail)
        email= unidecode.unidecode(email)
        email= email.replace(' ', '' )
        print (email)
        return email

    def gerar_telefone(self):

        self.ddd = []
        self.telefone = []

        for i in range(1,3):
            self.ddd.append(r.randint(1, 9))

        for i in range(1,9):
            self.telefone.append(r.randint(1, 9))

        self.ddd.append(9)

        self.telefone = (self.ddd + self.telefone)
        
        for i in range(len(self.telefone)):
            print(f"{self.telefone[i]}", end="")

        self.telefone = str(self.telefone)
        return self.telefone
        

    # Metodo de armazenar os dados
    def exibir_informacoes(self):
        print (self.nasc, self.nome, self.cpf, self.email, self.telefone)
        Perfil.monta_nome()
        Perfil.monta_dt_nasc()
        Perfil.monta_cpf()
        Perfil.monta_email()   
        Perfil.gerar_telefone()
