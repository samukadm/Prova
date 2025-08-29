import flet as ft

def main(page: ft.Page):
    texto=ft.Text('Olá flet!')
    page.add(texto)

    texto.size=50
    texto.weight=ft.FontWeight.W_600
    texto.italic=False
    texto.color=ft.Colors.BLUE_600

    page.add(texto)
ft.app(main)