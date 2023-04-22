import PySimpleGUI as sg

#Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Usuário')],
    [sg.Input(key='usuario')],
    [sg.Text('Senha')],
    [sg.Input(key='senha',password_char='*')],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Login')],
    [sg.Text('',key='mensagem')],
]

#Janela
window = sg.Window('Login',layout=layout)

#Ler os eventos
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Login':
        usuario_correto = 'admin'
        senha_correta = '1234'
        usuario = values['usuario']
        senha = values['senha']
        if usuario == usuario_correto and senha == senha_correta:
            window['mensagem'].update('Login feito com sucesso!')
        else:
            window['mensagem'].update('Usuário ou senha incorreta.')