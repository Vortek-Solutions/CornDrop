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
    page.window.resizable = True

    page.bgcolor = Syles.color('white')

    conteudo = ft.Container(content=ft.Column(expand=True, alignment=ft.MainAxisAlignment.START),padding=ft.padding.all(10), width=page.window.width,  height=page.window.height)

    def navegar(nome_tela):
        conteudo.content.controls.clear()
        if nome_tela == "Rotina":
            conteudo.content.controls.append(TelaRotina(page))
        elif nome_tela == "Insumo":
            conteudo.content.controls.append(TelaInsumo(page))
        elif nome_tela == "Tech":
            conteudo.content.controls.append(TelaTech(page))

        page.update()

    menu = criar_menu(navegar)

    page.add(menu, conteudo)
    navegar("Rotina")

    def redimensionar_tela(e):
        conteudo.width = page.window.width
        conteudo.height = page.window.height
        page.update()

    page.window.on_resize = redimensionar_tela

    #page.window.close() #PARA FECHAR A JANELA NO COMPUTADOR
    #subprocess.run(["flet", "run", "main.py", "--android"]) #PARA RODAR O ANDROID NO FLET

ft.app(target=main)
