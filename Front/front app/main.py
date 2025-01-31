import flet as ft
from telas.menu import criar_menu
from telas.rotina import TelaRotina
from telas.insumo import TelaInsumo
from telas.tech import TelaTech
from telas.perfil import TelaPerfil

def main(page: ft.Page):
    page.title = "CornDrop"
    page.window.max_width = 400
    page.window.max_height = 700
    page.window.width = 400
    page.window.height = 700
    page.window.resizable = False
    
    conteudo = ft.Column(expand=True)

    def navegar(nome_tela):
        conteudo.controls.clear()
        if nome_tela == "Rotina" :
            conteudo.controls.append(TelaRotina())
        elif nome_tela == "Insumo":
            conteudo.controls.append(TelaInsumo())
        elif nome_tela == "Tech":
            conteudo.controls.append(TelaTech())
        elif nome_tela == "Perfil":
            conteudo.controls.append(TelaPerfil())

        page.update()

    menu = criar_menu(navegar)

    page.add(menu,conteudo)
    navegar("Rotina")
    
    #page.window_close() #PARA FECHAR A JANELA NO COMPUTADOR
    #subprocess.run(["flet", "run", "main.py", "--android"]) #PARA RODAR O ANDROID NO FLET

ft.app(target=main)
