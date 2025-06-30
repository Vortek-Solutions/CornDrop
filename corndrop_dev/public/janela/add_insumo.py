import flet as ft

def ModInsumo(page: ft.Page):

    def voltar(e):
        dialog.open = False
        page.update()
    
    insumo = ft.TextField(label="Nome do Insumo", border_radius=8, filled=True)
    data = ft.TextField(label="Data", border_radius=8, filled=True)
    preco = ft.TextField(label="Preço", border_radius=8, filled=True, read_only=True)
    quantidade = ft.TextField(label="Quantidade", border_radius=8, filled=True)
    
    adicionar_button = ft.ElevatedButton(text="Adicionar", on_click=lambda e: print("Adicionar clicked!"),bgcolor=ft.colors.GREEN, color=ft.colors.WHITE,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)))
    
    voltar_button = ft.ElevatedButton(text="Voltar", on_click=voltar,bgcolor=ft.colors.RED, color=ft.colors.WHITE,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)))
    
    form = ft.Column(
        [
            ft.Text("Adicionar Novo Insumo", size=20, weight=ft.FontWeight.BOLD),
            insumo,data,preco,quantidade,
            ft.Row([voltar_button, adicionar_button], alignment=ft.MainAxisAlignment.SPACE_EVENLY)
        ],
        spacing=15,alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )
    
    dialog = ft.AlertDialog(content=form)
    page.dialog = dialog
    dialog.open = True
    page.update()
