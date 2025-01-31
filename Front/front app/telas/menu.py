import flet as ft

def criar_menu(navegar):
    return ft.AppBar(
        actions=[
            ft.Row(
                controls=[
                    ft.ElevatedButton(text="Rotina", on_click=lambda e: navegar("Rotina")),
                    ft.ElevatedButton(text="Insumo", on_click=lambda e: navegar("Insumo")),
                    ft.ElevatedButton(text="Tech", on_click=lambda e: navegar("Tech")),
                    ft.ElevatedButton(text="Perfil", on_click=lambda e: navegar("Perfil")),
                ],
                alignment=ft.MainAxisAlignment.CENTER
                
            )
        ]
    )
