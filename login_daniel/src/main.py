import flet as ft

def main(page: ft.Page):
    
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    container_fundo = ft.Container(
        padding=10,
        margin=10,
        height=800,
        width=600,
        bgcolor=ft.Colors.WHITE,
        border_radius=10,
    )

    container_fundo_menor = ft.Container(
        padding=10,
        margin=10,
        height=785,
        width=585,
        bgcolor=ft.Colors.GREY_200,
        border_radius=10,
    )

    textos = [ft.Text(value="LOGIN", size=25, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER, color='black')]

    img = ft.Image(
        src=f'/img/image.png',
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN,
        border_radius=100
    )

    container_imagem = ft.Container(
        content=img,
        padding=10,
        margin=10,
        height=130,
        width=130,
        border_radius=100,
    )

    coluna_mensagem = ft.Column(
    controls=textos + [container_imagem],
    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    spacing=3,
    alignment=ft.MainAxisAlignment.START
)

    container_mensagem = ft.Container(
        content=coluna_mensagem,
        padding=10,
        margin=10,
        bgcolor=ft.Colors.GREY_200,
        height=700,
        width=385,
        border_radius=10,
        alignment=ft.alignment.center
    )

    entradas = [
    ft.TextField(
        label="Email",
        prefix_icon=ft.Icons.EMAIL,
        bgcolor=ft.Colors.GREY_300,
        border_radius=10,
        label_style=ft.TextStyle(color=ft.Colors.GREY_500),
        color=ft.Colors.GREY_800,
        prefix_style=ft.TextStyle(color=ft.Colors.GREY_800)
    ),
    ft.TextField(
        label="Senha",
        password=True,
        prefix_icon=ft.Icons.KEY,
        bgcolor=ft.Colors.GREY_300,
        border_radius=10,
        label_style=ft.TextStyle(color=ft.Colors.GREY_500),
        color=ft.Colors.GREY_800,
        prefix_style=ft.TextStyle(color=ft.Colors.GREY_800),
        can_reveal_password=True
    ),
]

    botao = ft.ElevatedButton(
    text="Fazer login",
    bgcolor=ft.Colors.BLUE_500,
    color=ft.Colors.WHITE,
    width=250,
    height=60,
    style=ft.ButtonStyle(
        shape=ft.RoundedRectangleBorder(radius=32),
        padding=20,
        text_style=ft.TextStyle(size=20, weight=ft.FontWeight.BOLD)
    )
)

    coluna_entrada = ft.Column(
        controls=entradas + [botao],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=7,
        width=800,
        alignment=ft.alignment.bottom_center
    )
    
    container_entrada = ft.Container(
        content=coluna_entrada,
        padding=10,
        margin=10,
        width=385,
        border_radius=10,
    )

    container_entrada.alignment = ft.Alignment(0, -0.5)

    page.add(
    ft.Stack([container_fundo, container_fundo_menor, container_mensagem, container_entrada], alignment=ft.alignment.center)
    )
ft.app(main)