import flet as ft

def ModInsumo(page: ft.Page):
    
    callback = page
    page.clean()
    page.title = "Adicionar Insumo"
    
    nome_insumo = ft.TextField(label="Nome")
    data = ft.TextField(label="Data")
    preco = ft.TextField(label="Preço")
    quantidade = ft.TextField(label="Quantidade")

    adicionar_button = ft.ElevatedButton(text="Adicionar",on_click=lambda _: print("Adicionar clicked!"),color=ft.colors.GREEN)
    voltar_button = ft.ElevatedButton(text="Voltar",on_click = lambda e: voltar())

    form = ft.Column(
        [
            voltar_button,nome_insumo,
            ft.Row([data, preco]),quantidade, adicionar_button
        ]
    )

    page.add(form)
    
    def voltar():
        page.clean()