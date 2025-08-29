import flet as ft

def main(page: ft.Page):
    page.title='Capturando Dados'
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    def click_btn_ok(e):
        txt_saudacao.value=f'Olá, {tf_nome.value}!'
        txt_saudacao.visible=True
        page.update()

    tf_nome=ft.TextField(label='Digite seu nome: ')
    
    btn_ok=ft.ElevatedButton('OK', on_click=click_btn_ok)

    txt_saudacao=ft.Text('Olá ...!')
    txt_saudacao.visible=False

    page.add(
        tf_nome,
        btn_ok,
        txt_saudacao
    )

ft.app(main)