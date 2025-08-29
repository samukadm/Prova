import flet as ft


def main(page: ft.Page):
    page.title='Minha primeira tela flet'
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER

    texto1=ft.Text('Bem vindo ao Cruzeiro Esporte Clube!')
    texto1.size=45

    page.add(texto1)
    page.add(
        ft.Text('Você está aprendendo a utilizar o flet para criar interfaces gráficas em python.', size=18, color='gray'), 
    
        ft.Text('Este é um componente de texto (ft.Text).')
    )

ft.app(main)