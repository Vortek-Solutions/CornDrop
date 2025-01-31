import flet as ft

def TelaPerfil():
    return ft.Column([
        ft.Text("Perfil do Usuário:", size=20, weight=ft.FontWeight.BOLD),
        ft.Text("Nome: Cauane Oliveira"),
        ft.Text("Email: cauane.oliveira@example.com")
    ])
