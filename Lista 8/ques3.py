import flet as ft

def main(page: ft.Page):
    page.title='Calculadora'
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.padding=50

    def menos(e):
        n=int(txt_contador.value)
        n-=1
        txt_contador.value=str(n)
        page.update()
    def mais(e):
        n=int(txt_contador.value)
        n+=1
        txt_contador.value=str(n)
        page.update()
    def zerar(e):
        n=int(txt_contador.value)
        n=0
        txt_contador.value=str(n)
        page.update()

    txt_contador=ft.Text('0', size=50, weight=ft.FontWeight.BOLD)

    btn_menos=ft.ElevatedButton('-', on_click=menos)
    btn_mais=ft.ElevatedButton('+', on_click=mais)
    btn_zerar= ft.ElevatedButton('Zerar', on_click=zerar)
    page.add(
        txt_contador,
        ft.Row(
            controls=[
                btn_menos,
                btn_mais
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY
        ),
        btn_zerar
    )

ft.app(main)