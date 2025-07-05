import flet as ft

from access import Access
from styles import MessageBox

def ModRotina(page: ft.Page):
    msg = MessageBox()
    def option_horario(e):
        op_horario.label = op.value
        page.update()

    def voltar(e):
        dialog.open = False
        page.update()
    
    def adicionarRotina(e,):
        result = Access.addRotina(dispositivo.value,insumo.value,nome_da_rotina.value,quantidade.value,op_horario.value)
        if result == True:
            dialog.open = False
            page.update()
            print("Rotina Adicionada!")
            #msg.showinfo("Status","Rotina Adicionada!")
        else:
            dialog.open = False
            page.update()
            print("Rotina não adicionada!")
            #msg.showinfo("Status","Rotina não adicionada!")

    dispositivo = ft.Dropdown(label="Dispositivo", border_radius=8, filled=True)
    insumo = ft.Dropdown(label="Insumo", border_radius=8, filled=True)
    nome_da_rotina = ft.TextField(label="Nome da Rotina", border_radius=8, filled=True)
    quantidade = ft.TextField(label="Quantidade", border_radius=8, filled=True)
    op_horario = ft.TextField(label="Horário", border_radius=8, filled=True, read_only=True)
    
    op = ft.Dropdown(on_change=option_horario,options=[ft.dropdown.Option("Horário"),ft.dropdown.Option("Intervalo")],label="Tipo de Horário",border_radius=8,filled=True)
    
    adicionar_button = ft.ElevatedButton(text="Adicionar", on_click=adicionarRotina,bgcolor=ft.colors.GREEN, color=ft.colors.WHITE,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)))
    
    voltar_button = ft.ElevatedButton(text="Voltar", on_click=voltar,bgcolor=ft.colors.RED, color=ft.colors.WHITE,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)))
    
    form = ft.Column(
        [
            ft.Text("Adicionar Nova Rotina", size=20, weight=ft.FontWeight.BOLD),
            dispositivo,insumo,nome_da_rotina,quantidade,op,op_horario,
            ft.Row([voltar_button, adicionar_button], alignment=ft.MainAxisAlignment.SPACE_EVENLY)
        ],
        spacing=15,alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )
    
    dialog = ft.AlertDialog(content=form)
    page.dialog = dialog
    dialog.open = True
    page.update()
