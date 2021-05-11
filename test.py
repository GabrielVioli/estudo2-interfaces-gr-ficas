import pygame 
import PySimpleGUI as sg
from time import sleep as sp

layout = [
    [sg.Text('Cadastro', font = ('helvetica',25), size = (30,3))],
    [sg.Text('login')],
    [sg.Input(key = 'nome')],
    [sg.Text('senha')],
    [sg.Input(key = 'senha')],
    [sg.Text(' ', size = (1,2))],
    [sg.Button('Ok')]
]

window = sg.Window('cadastro', layout, size = (400,400))

while True:
    event, values = window.read()

    login = values['nome']
    senha = values['senha']

    if event is None:
        break

    if event == 'Ok':
        break

if event == 'Ok':
    window.close()

    backcground_color = (0,50,20)
    largura = 400
    altura = 400
    screen = pygame.display.set_mode((largura, altura))
    nam = pygame.display.set_caption('jogo')
    fundo = pygame.image.load('ceu2.png')



    running = True
    while running == True:
        pygame.time.delay(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()
                    
        screen.blit(fundo,(0,0))

pygame.quit()
    