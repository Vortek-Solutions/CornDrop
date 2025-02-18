import flet as ft
from styles import Styles

from access import Access
from janela.add_rotina import ModRotina

def TelaRotina(page: ft.Page):
    frame_brutton = ft.Container(
        content=ft.Row(
            [
                ft.Text("Rotina",size=24,color="#000000",weight=ft.FontWeight.BOLD),
                #ft.IconButton(ft.icons.REFRESH,on_click=lambda e: print("Refresh"),icon_color="#000000",tooltip="Refresh",style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10),padding=ft.Padding(5, 2, 5, 2))),
                ft.ElevatedButton(text="Adicionar Rotina",on_click=lambda e: ModRotina(page),bgcolor=Styles.color("bg_button"),color=Styles.color("white"),style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10),padding=ft.Padding(10, 5, 10, 5))),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            spacing=10
        ),
        padding=15,border_radius=12,width=450,height=60,shadow=ft.BoxShadow(blur_radius=5, spread_radius=1, color=ft.colors.GREY_400),
    )

    rotinas_scroll = ft.Column(spacing=20)

    result = Access.listRotinas()

    for i in result:
        frame = ft.Container(
            content=ft.Row(
                [
                    ft.TextButton(text=f"Rotina {i['idRotina']}",on_click=lambda e, id=i['idRotina']: print("Botão clicado"),style=ft.ButtonStyle(color="#000000",padding=ft.Padding(10, 5, 10, 5))),
                    ft.IconButton(ft.icons.EDIT,on_click=lambda e, id=i['idRotina']: print("Botão clicado"),icon_color="#000000",tooltip="Editar"),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            padding=15,border_radius=12,bgcolor=Styles.color("bg_frame"),width=450,height=80,shadow=ft.BoxShadow(blur_radius=4, spread_radius=1, color=ft.colors.GREY_300),
        )

        rotinas_scroll.controls.append(frame)
        
    if not result:
        
        frame = ft.Container(content=ft.Row([ft.Text("Nenhuma rotina encontrada",size=16,color="#000000"),],alignment=ft.MainAxisAlignment.CENTER))
        
        rotinas_scroll.controls.append(frame)
        
            
    scroll_area = ft.Container(content=ft.ListView(controls=rotinas_scroll.controls, height=650, spacing=10))

    layout = ft.Column(controls=[frame_brutton, scroll_area], alignment=ft.MainAxisAlignment.START, spacing=20)

    return layout