from tkinter import messagebox
import flet as ft
import asyncio

class Styles:
    
    def color(color):
        
        colors = {
            'white':'#FFFFFF',
            'bg_button':"#007728",
            'bg_frame':"#D9D9D9",
            'hover' : "#5d732f",  # Cor ao passar o mouse - Verde Claro
        }
        
        return colors.get(color)
    
    def font_style():
        fontStyle = ("Lucida Grande",16)
        return fontStyle
    
    def centralizar_janela(root, largura, altura):
        
        tela_largura = root.winfo_screenwidth()
        tela_altura = root.winfo_screenheight()

        x = (tela_largura // 2) - (largura // 2)
        y = (tela_altura // 2) - (altura // 2)

        root.geometry(f"{largura}x{altura}+{x}+{y}")
    
class MessageBox:
    Style = Styles()
    def showinfo(self, title, message):
        return messagebox.showinfo(title, message)

    def showwarning(self, title, message):
        return messagebox.showwarning(title, message)

    def showerror(self, title, message):
        return messagebox.showerror(title, message)

    def askquestion(self, title, message):
        return messagebox.askquestion(title, message)

    def askretrycancel(self, title, message):
        return messagebox.askretrycancel(title, message)
    
    def showinfo_autoclose(page: ft.Page, message, timeout=2000):
        form = ft.Column([ft.Text(message, size=20, weight=ft.FontWeight.BOLD)], spacing=15, width=400, height=100)
        
        dialog = ft.AlertDialog(content=form)
        page.dialog = dialog
        dialog.open = True
        