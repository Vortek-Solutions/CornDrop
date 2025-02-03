import flet as ft
from styles import Syles

def TelaTech():
    
    frame_brutton = ft.Container(
            content=ft.Row([
                    ft.Text(f'Tech',size=24,color='#000000',weight=ft.FontWeight.BOLD),
                    ft.ElevatedButton(text="Add", on_click=lambda e: print('botão clicado'),bgcolor=Syles.color('bg_button'),color = Syles.color('white'))
                    ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            padding=10,border_radius=10,width=400,height=50)

    rotinas_scroll = ft.Column(spacing=30)

    for i in range(10):
        frame = ft.Container(
            content=ft.Row([ft.TextButton(text=f'Tech: {i}', on_click=lambda e: print('botão clicado'), style=ft.ButtonStyle(color='#000000')),
                    ft.IconButton(ft.icons.EDIT, on_click=lambda e: print('botão clicado'),icon_color='#000000', tooltip='Editar')],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN ),
            padding=10,border_radius=10,bgcolor=Syles.color('bg_frame'),width=400,height=100)
        
        rotinas_scroll.controls.append(frame)


    scroll_area = ft.Container(content=ft.ListView(controls=rotinas_scroll.controls,height=520,spacing=10))

    layout = ft.Column(controls=[frame_brutton,scroll_area],alignment=ft.MainAxisAlignment.START)

    return layout
