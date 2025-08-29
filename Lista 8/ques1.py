import flet as ft


def main(page: ft.Page):
    page.title='Minha primeira tela flet'
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.vertical_alignment=ft.MainAxisAlignment.CENTER

    page.add(
        ft.Column(
            controls=[
                ft.Text('Bem vindo ao Cruzeiro Esporte Clube!', size=45),
                ft.Text('Você está aprendendo a utilizar o flet para criar interfaces gráficas em python.', size=18, color='gray'), 
                ft.Text('Este é um componente de texto (ft.Text).')
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            height=300
        )
    )

ft.app(main)