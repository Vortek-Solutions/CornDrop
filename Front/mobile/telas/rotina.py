import flet as ft
from styles import Syles

def TelaRotina():

    cl = ft.Column(spacing=30,height=570,width=600,scroll=ft.ScrollMode.ALWAYS)
        
    for i in range(0,10):
        frame = ft.Container(content=ft.Text(f'Rotina {i}',size=16,color='#000000',weight=ft.FontWeight.BOLD),
                             padding=10,border_radius=10,bgcolor=Syles.color('bg_frame'),width=500,height=100)
        
        cl.controls.append(frame)
        
    return cl
