import flet as ft
from styles import Styles

def criar_menu(navegar):
    frame = ft.Container(expand=True,bgcolor=Styles.color('bg_frame'),padding=ft.padding.all(10),border_radius=10,
        content=ft.Row(
            [
                ft.ElevatedButton(text="Rotina",on_click=lambda e: navegar("Rotina"),bgcolor=Styles.color('bg_button'),color=Styles.color('white'),style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10))),
                ft.ElevatedButton(text="Insumo",on_click=lambda e: navegar("Insumo"),bgcolor=Styles.color('bg_button'),color=Styles.color('white'),style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10))),
                ft.ElevatedButton(text="Tech",on_click=lambda e: navegar("Tech"),bgcolor=Styles.color('bg_button'),color=Styles.color('white'),style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10))),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
    )

    layout = ft.Container(content=ft.Column(controls=[frame], alignment=ft.MainAxisAlignment.START),padding=ft.padding.all(10))

    return layout
