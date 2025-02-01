import flet as ft

from styles import Syles

def criar_menu(navegar):
    return ft.AppBar(toolbar_height=60,bgcolor=Syles.color('bg_frame'),
        actions=[
            ft.Container(expand=True,padding=ft.padding.all(10),
                content=ft.Row(
                    controls=[
                        ft.ElevatedButton(text="Rotina", on_click=lambda e: navegar("Rotina"),bgcolor=Syles.color('bg_button'),color = Syles.color('white')),
                        ft.ElevatedButton(text="Insumo", on_click=lambda e: navegar("Insumo"),bgcolor=Syles.color('bg_button'),color = Syles.color('white')),
                        ft.ElevatedButton(text="Tech", on_click=lambda e: navegar("Tech"),bgcolor=Syles.color('bg_button'),color = Syles.color('white')),
                        ft.ElevatedButton(text="Perfil", on_click=lambda e: navegar("Perfil"),bgcolor=Syles.color('bg_button'),color = Syles.color('white')),
                    ],
                ),
            ),
        ],
    )
