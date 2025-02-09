import flet as ft
import subprocess
from telas.menu import criar_menu
from telas.rotina import TelaRotina
from telas.insumo import TelaInsumo
from telas.tech import TelaTech

from styles import Syles

def main(page: ft.Page):
    page.title = "CornDrop"

    page.window.width = 400
    page.window.height = 700
    page.window.resizable = False
    page.bgcolor = Syles.color('white')
    
    conteudo = ft.Column(expand=True)

    def navegar(nome_tela):
        conteudo.controls.clear()
        if nome_tela == "Rotina" :
            conteudo.controls.append(TelaRotina(page))
        elif nome_tela == "Insumo":
            conteudo.controls.append(TelaInsumo(page))
        elif nome_tela == "Tech":
            conteudo.controls.append(TelaTech())

        page.update()

    menu = criar_menu(navegar)

    page.add(menu,conteudo)
    navegar("Rotina")
    
    #page.window.close() #PARA FECHAR A JANELA NO COMPUTADOR
    #subprocess.run(["flet", "run", "main.py", "--android"]) #PARA RODAR O ANDROID NO FLET

ft.app(target=main)
