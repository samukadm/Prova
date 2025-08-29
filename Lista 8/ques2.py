import flet as ft

def main(page: ft.Page):
    page.title='Capturando Dados'
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.padding=50
    def click_btn_ok(e):
        txt_saudacao.value=f'Olá, {tf_nome.value}!'
        txt_saudacao.visible=True
        page.update()
        tf_nome.focus()

    tf_nome=ft.TextField(label='Digite seu nome: ', on_submit=click_btn_ok)
    
    btn_ok=ft.ElevatedButton('MOSTRAR', on_click=click_btn_ok)

    txt_saudacao=ft.Text('Olá ...!')
    txt_saudacao.visible=False

    page.add(
        tf_nome,
        btn_ok,
        txt_saudacao
    )
    tf_nome.focus()

ft.app(main)