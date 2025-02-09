import flet as ft

def ModRotina (page: ft.Page):
    callback = page
    page.clean()
    page.title = "Adicionar Rotina"
    
    dispositivo = ft.TextField(label="Dispositivo")
    insumo = ft.TextField(label="Insumo")
    nome_da_rotina = ft.TextField(label="Nome da Rotina")
    quantidade = ft.TextField(label="Quantidade")
    horario = ft.TextField(label="Horário")
    intervalo = ft.TextField(label="Intervalo")

    adicionar_button = ft.ElevatedButton(text="Adicionar",on_click=lambda _: print("Adicionar clicked!"),color=ft.colors.GREEN)
    voltar_button = ft.ElevatedButton(text="Voltar",on_click = lambda e: voltar())

    form = ft.Column(
        [
            voltar_button,dispositivo,
            insumo,nome_da_rotina,
            quantidade,ft.Row([horario, intervalo]),adicionar_button,
        ]
    )

    page.add(form)
    
    def voltar():
        page.clean()
        