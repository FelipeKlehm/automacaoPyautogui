from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui, time
from perfil import Perfil

nomeCadastros = str(input('Nome a ser colocado nos cadastros: '))

codigoCentroCusto = str(input('Código para cadastro de Centro de Custo e Plano de conta: '))

formulaSisAvaliacao = str(input('Fórmula do sistema de Avaliação a ser ultilizada: '))

pyautogui.PAUSE = 1.0

nomeReduzido = (f'{nomeCadastros[:3]}{nomeCadastros[6:9]}')

class Perfis(Perfil):
    
    def __init__(self, nome, nasc, cpf, email, telefone):
        super().__init__(nome, nasc, cpf, email, telefone)
        self.nome = nome
        self.nasc = nasc
        self.cpf = cpf
        self.email = email
        self.telefone = telefone


class AbrirJacad:
    driver = webdriver.Firefox()
    driver.get("http://192.168.10.102")
    dowloadJacad = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div/div/div[2]/div[1]/div/div[2]/p/a").click()

    time.sleep(1)

    with pyautogui.hold('ctrlleft'):
        pyautogui.press('j')

    pyautogui.press('enter', presses=2, interval=0.5)

    time.sleep(3)
    pyautogui.press('tab', presses=2, interval=0.5)
    pyautogui.press('enter')

    driver.quit()

    usuario = 'root'
    senha = '123123'
    #Aguardar JACAD abrir
    time.sleep(10)
    pyautogui.write(usuario)    
    pyautogui.press('tab')
    pyautogui.write(senha) 
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(8)
    #clicando no Perfil

    time.sleep(3)
    pyautogui.click(x=245, y=100)

    with pyautogui.hold('ctrlleft'):
        pyautogui.press('n')

class CadastrarPerfil:
    def __init__(self) -> None:

        perfil = Perfis(nome='', nasc='', cpf='', email='', telefone='')
        nasc = perfil.monta_dt_nasc()
        nome = perfil.monta_nome()
        cpf = perfil.monta_cpf()
        email = perfil.monta_email()
        telefone = perfil.gerar_telefone()

        with pyautogui.hold('ctrlleft'):
            pyautogui.press('n')

        pyautogui.write(nome)

        #Email do perfil
        pyautogui.press('tab')
        pyautogui.write(email) 

        #Cpf do perfil
        pyautogui.press('tab', presses=2, interval=0.5)
        pyautogui.write(cpf)

        #Para o RG
        pyautogui.press('tab')
        pyautogui.write(cpf)

        #Data de Nascimento
        pyautogui.press('tab', presses=7, interval=0.5)
        pyautogui.write(nasc)

        #Sexo
        pyautogui.press('tab', presses=2, interval=0.5)
        pyautogui.press('down') 
        pyautogui.press('down')
        pyautogui.press('enter')

        #Celular
        pyautogui.press('tab', presses=16, interval=0.5)
        pyautogui.write(telefone)

        with pyautogui.hold('ctrlleft'):
            pyautogui.press('s')
            
        return None
    
for i in range(0, 5):
    time.sleep(1)
    CadastrarPerfil()

time.sleep(2)

class CursoBase:

    nomeReduzido = (f'{nomeCadastros[:3]}{nomeCadastros[6:9]}')

    #Abre a tela do Curso Base
    pyautogui.click(x=1540, y=120)
    pyautogui.click(x=88, y=37)
    pyautogui.click(x=140, y=221)

    with pyautogui.hold('ctrlleft'):
        pyautogui.press('i')

    # Escreve nomes de impressão 1,2 e 3
    for i in range(0,3):
        pyautogui.write(nomeCadastros)
        pyautogui.press('tab')

    # Escreve nome reduzido
    pyautogui.write(nomeReduzido)

    # Grau Acadêmico
    pyautogui.press('tab')
    pyautogui.press('down', presses=2, interval=0.3)
    pyautogui.press('space')

    # Grau Acadêmico a constar no Diploma
    pyautogui.click(x=624, y=715)
    pyautogui.write('Bacharel')
    pyautogui.press('tab')
    pyautogui.write('Bacharela')

    with pyautogui.hold('ctrlleft'):
        pyautogui.press('s')

    pyautogui.click(x=1459, y=142)

class CentroDeCusto:

    # Abrir tela de Centro de Custo
    pyautogui.click(x=187, y=46)
    pyautogui.moveTo(x=503, y=907)
    pyautogui.click(x=850, y=454)
    time.sleep(1.5)

    #Escreve descrição Centro de Custo
    pyautogui.click(x=750, y=429)
    pyautogui.write(nomeCadastros)

    #Escreve código
    pyautogui.press('tab')
    pyautogui.write(codigoCentroCusto)

    with pyautogui.hold('ctrlleft'):
        pyautogui.press('s')
    time.sleep(2)


class CriarPeriodo:
    time.sleep(1)
    pyautogui.click(x=106, y=50)
    pyautogui.click(x=161, y=366)
    
    with pyautogui.hold('ctrlleft'):
        pyautogui.press('i')
    
    pyautogui.click(x=675, y=316)
    pyautogui.write(nomeCadastros)
    pyautogui.press('tab', presses=2, interval=0.5)
    pyautogui.write(nomeCadastros)
    pyautogui.press('tab', presses=3, interval=0.5)
    pyautogui.write('01012023')
    pyautogui.press('tab')
    pyautogui.write('31122023')
    pyautogui.press('tab', presses=2, interval=0.5)
    pyautogui.press('space')
    pyautogui.press('tab')
    pyautogui.write('2023')

    with pyautogui.hold('ctrlleft'):
        pyautogui.press('s')

class SubPeriodo:

    #Cadastro do 1° Semestre    
    pyautogui.click(x=709, y=278) #Clicando no menu academico
    pyautogui.click(x=547, y=420)
    
    pyautogui.press('tab', presses=2, interval=0.5)
    pyautogui.write('1° Semestre')
    pyautogui.press('tab')
    pyautogui.write('01012023')
    pyautogui.press('tab')
    pyautogui.write('01062023')
    pyautogui.press('tab')
    pyautogui.press('down', presses=2, interval=0.5)
    pyautogui.press('tab')
    pyautogui.write('105')
    pyautogui.press ('tab', presses=2, interval=0.5)

    for i in range(0, 3):
       pyautogui.press('space')
       pyautogui.press('tab')

    with pyautogui.hold('ctrlleft'):
      pyautogui.press('s')


    #Cadastro do 2° Semestre
    pyautogui.press('space')
    
    pyautogui.press('tab', presses=2, interval=0.5)
    pyautogui.write('2° Semestre')
    pyautogui.press('tab')
    pyautogui.write('02062023')
    pyautogui.press('tab')
    pyautogui.write('01122023')
    pyautogui.press('tab')
    pyautogui.press('down', presses=3, interval=0.5 )
    pyautogui.press('tab')
    pyautogui.write('105')
    pyautogui.press ('tab', presses=2, interval=0.5)

    for i in range(0, 3):
       pyautogui.press('space')
       pyautogui.press('tab')

    with pyautogui.hold('ctrlleft'):
      pyautogui.press('s')

class CriarSistemaAvaliacao:
    pyautogui.click(x=34, y=49)
    pyautogui.moveTo(x=340, y=200)
    pyautogui.click(x=635, y=711)

    with pyautogui.hold('ctrlleft'):
        pyautogui.press('i')
    
    pyautogui.write(nomeCadastros) 
    pyautogui.press('tab')
    pyautogui.write(formulaSisAvaliacao)
    pyautogui.click(x=761, y=412)
    pyautogui.write(formulaSisAvaliacao)
    
    with pyautogui.hold('ctrlleft'):
        pyautogui.press('s')
    
    pyautogui.click(x=622, y=782)
    pyautogui.press('tab')
    pyautogui.write('1')
    pyautogui.press('enter')
    pyautogui.press('tab', presses=2, interval=0.5)

    pyautogui.write('N1')
    pyautogui.press('tab')
    pyautogui.write('N1')

    pyautogui.press('tab')
    pyautogui.write('10')
    pyautogui.press('tab')

    with pyautogui.hold('ctrlleft'):
        pyautogui.press('s')
    
    pyautogui.click(x=622, y=782)
    pyautogui.press('tab')
    pyautogui.write('1')
    pyautogui.press('enter')
    pyautogui.press('tab', presses=2, interval=0.5)

    pyautogui.write('N2')
    pyautogui.press('tab')
    pyautogui.write('N2')

    pyautogui.press('tab')
    pyautogui.write('10')
    pyautogui.press('tab')

    with pyautogui.hold('ctrlleft'):
        pyautogui.press('s')

    #Adicionando o sitema de avaliação no Periodo Letivo

    pyautogui.click(x=1328, y=184)

    pyautogui.click(x=917, y=281)

    pyautogui.click(x=523, y=420)

    pyautogui.write(nomeCadastros)
    pyautogui.press('enter')
    pyautogui.press('down')
    pyautogui.press('enter')
    

class Curso:
    pyautogui.click(x=186, y=96)
    
    with pyautogui.hold('ctrlleft'):
        pyautogui.press('n')
    
    pyautogui.click(x=759, y=316)
    pyautogui.write(nomeCadastros)
    pyautogui.press('tab')
    pyautogui.write(nomeReduzido)
    pyautogui.press('tab', presses=2, interval=0.5)
    pyautogui.write(nomeCadastros)
    pyautogui.press('enter')
    pyautogui.press('tab', presses=2, interval=0.5)
    pyautogui.write(nomeCadastros)
    pyautogui.press('enter')
    pyautogui.press('tab', presses=2, interval=0.5)
    pyautogui.write('3')
    pyautogui.press('enter')
    pyautogui.press('tab', presses=8, interval=0.4)
    pyautogui.write('Presencial')
    pyautogui.press('tab', presses=3, interval=0.5)
    for i in range(0, 12):
        time.sleep(0.5)
        pyautogui.press('tab')
        pyautogui.write('100')

    pyautogui.press('tab', presses=2, interval=0.5)
    pyautogui.write('4')
    pyautogui.press('tab')
    pyautogui.write('8')
    pyautogui.press('tab', presses=3, interval=0.5)
    pyautogui.write('7')    
    pyautogui.press('tab')
    pyautogui.write('3')
    pyautogui.press('tab')
    pyautogui.write('75')
    pyautogui.press('tab', presses=2, interval=0.5)
    pyautogui.write('6')
    pyautogui.press('tab')
    pyautogui.write('6')
    with pyautogui.hold('ctrlleft'):
        pyautogui.press('s')
            

class DisciplinaCurso:
    pyautogui.click(x=415, y=831)
    pyautogui.write('1 Periodo')
    pyautogui.press('enter')
    pyautogui.press('down')
    pyautogui.press('enter')

    pyautogui.click(x=415, y=831)
    pyautogui.write('2 Periodo')
    pyautogui.press('enter')
    pyautogui.press('down')
    pyautogui.press('enter')

    pyautogui.click(x=415, y=831)
    pyautogui.write('3 Periodo')
    pyautogui.press('enter')
    pyautogui.press('down')
    pyautogui.press('enter')
    
    pyautogui.click(x=473, y=654)
    pyautogui.click(x=672, y=827)
    pyautogui.press('tab', presses=4, interval=0.5)
    pyautogui.write('Disciplina Normal 1')
    pyautogui.press('tab', presses=3, interval=0.5)
    pyautogui.write('Disc.Norm 1')
    pyautogui.press('tab', presses=9, interval=0.5)
      
    for i in range(0, 11):
        time.sleep(0.5)
        pyautogui.press('tab')
        pyautogui.write('100')

    with pyautogui.hold('ctrlleft'):
        pyautogui.press('s')

    pyautogui.click(x=473, y=654)
    pyautogui.click(x=672, y=827)
    pyautogui.press('tab', presses=4, interval=0.5)
    pyautogui.write('Disciplina Normal 2')
    pyautogui.press('tab', presses=3, interval=0.5)
    pyautogui.write('Disc.Norm 2')
    pyautogui.press('tab', presses=9, interval=0.5)
      
    for i in range(0, 11):
        time.sleep(0.5)
        pyautogui.press('tab')
        pyautogui.write('100')

    with pyautogui.hold('ctrlleft'):
        pyautogui.press('s')

    
    pyautogui.click(x=473, y=654)
    pyautogui.click(x=672, y=827)
    pyautogui.press('tab', presses=4, interval=0.5)
    pyautogui.write('Disciplina Opt. 1')
    pyautogui.press('tab', presses=3, interval=0.5)
    pyautogui.write('Disciplina.Opt 1')
    pyautogui.press('tab', presses=9, interval=0.5)
 


    for i in range(0, 11):
        time.sleep(0.5)
        pyautogui.press('tab')
        pyautogui.write('100')
        
    pyautogui.press('tab', presses=2, interval=0.5)
    pyautogui.press('space')
    pyautogui.press('down')
    pyautogui.press('enter')
    
    with pyautogui.hold('ctrlleft'):
        pyautogui.press('s')

    pyautogui.click(x=473, y=654)
    pyautogui.click(x=672, y=827)
    pyautogui.press('tab', presses=4, interval=0.5)
    pyautogui.write('Disciplina Opt.2')
    pyautogui.press('tab', presses=3, interval=0.5)
    pyautogui.write('Disciplina.Opt.2')
    pyautogui.press('tab', presses=9, interval=0.5)

    for i in range(0, 11):
        time.sleep(0.5)
        pyautogui.press('tab')
        pyautogui.write('100')
        
    pyautogui.press('tab', presses=2, interval=0.5)
    pyautogui.press('space')
    pyautogui.press('down')
    pyautogui.press('enter')
    
    with pyautogui.hold('ctrlleft'):
        pyautogui.press('s')
    
    pyautogui.click(x=934, y=703)

    with pyautogui.hold('shift'):
        pyautogui.click(x=934, y=703)
    
    with pyautogui.hold('shift'):
        pyautogui.click(x=952, y=724)
    
    pyautogui.click(x=900, y=836)

    pyautogui.click(x=892, y=751)

    
    pyautogui.write('Optativas')
    pyautogui.press('tab')
    pyautogui.press('down', presses=2, interval=1)
    pyautogui.press('enter')
    pyautogui.press('tab')
    pyautogui.write('200')
    pyautogui.press('tab')   
    pyautogui.press('space')
    pyautogui.click(x=821, y=407)
    pyautogui.press('enter')



class Turma:
    pyautogui.alert('aaaa')
    pyautogui.click(x=135, y=93)

    with pyautogui.hold('ctrlleft'):
        pyautogui.press('n')
    
    pyautogui.click(x=837, y=280)
    pyautogui.write(nomeCadastros)
    pyautogui.press('tab')
    pyautogui.write(nomeReduzido)
    pyautogui.press('tab', presses=2, interval=0.5)
    pyautogui.write(nomeCadastros)
    pyautogui.press('tab')
    pyautogui.write(nomeReduzido)

    