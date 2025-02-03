import flet as ft
from styles import Syles

def criar_menu(navegar):
    frame = ft.Container(expand=True,bgcolor=Syles.color('bg_frame'),padding=ft.padding.all(10),border_radius=10,
            content=ft.Row([
                ft.ElevatedButton(text="Rotina", on_click=lambda e: navegar("Rotina"),bgcolor=Syles.color('bg_button'),color = Syles.color('white')),
                ft.ElevatedButton(text="Insumo", on_click=lambda e: navegar("Insumo"),bgcolor=Syles.color('bg_button'),color = Syles.color('white')),
                ft.ElevatedButton(text="Tech", on_click=lambda e: navegar("Tech"),bgcolor=Syles.color('bg_button'),color = Syles.color('white')),
                ], 
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN))

    layout = ft.Column(controls=[frame],alignment=ft.MainAxisAlignment.START)
    
    return layout