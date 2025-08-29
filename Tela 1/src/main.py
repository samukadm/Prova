import flet as ft

def main(page: ft.Page):
    # Configuração da página
    page.title = "Login"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 0
    
    # Container com imagem de fundo
    background_container = ft.Container(
        content=ft.Image(
            src="https://logodownload.org/wp-content/uploads/2023/10/sc-corinthians-logo-1.png",
            width=page.width,
            height=page.height,
            fit=ft.ImageFit.COVER,
            opacity=0.7
        ),
        width=page.width,
        height=page.height,
        alignment=ft.alignment.center
    )
    
    # Card de login
    login_card = ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    value="Login",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLACK
                ),
                ft.Container(height=20),
                ft.TextField(
                    label="E-mail",
                    width=300,
                    border_color=ft.Colors.BLUE_700,
                    text_size=14,
                    bgcolor=ft.Colors.with_opacity(0.9, ft.Colors.WHITE)
                ),
                ft.Container(height=10),
                ft.TextField(
                    label="Senha",
                    width=300,
                    password=True,
                    can_reveal_password=True,
                    border_color=ft.Colors.BLUE_700,
                    text_size=14,
                    bgcolor=ft.Colors.with_opacity(0.9, ft.Colors.WHITE)
                ),
                ft.Container(height=20),
                ft.ElevatedButton(
                    text="Fazer Login",
                    width=300,
                    height=45,
                    style=ft.ButtonStyle(
                        bgcolor=ft.Colors.BLUE_700,
                        color=ft.Colors.WHITE
                    )
                ),
                ft.Container(height=15),
                ft.ElevatedButton(
                    content=ft.Row([
                        ft.Image(
                            src="https://cdn-icons-png.flaticon.com/512/2991/2991148.png", 
                            width=24, 
                            height=24
                        ),
                        ft.Text("Logar com o Google", color=ft.Colors.BLACK87)
                    ], alignment=ft.MainAxisAlignment.CENTER),
                    width=300,
                    height=45,
                    style=ft.ButtonStyle(
                        bgcolor=ft.Colors.WHITE,
                        side=ft.BorderSide(1, ft.Colors.GREY_400)
                    )
                ),
                ft.Container(height=10),
                ft.ElevatedButton(
                    content=ft.Row([
                        ft.Image(
                            src="https://cdn-icons-png.flaticon.com/512/0/747.png", 
                            width=24, 
                            height=24
                        ),
                        ft.Text("Logar com a Apple", color=ft.Colors.BLACK87)
                    ], alignment=ft.MainAxisAlignment.CENTER),
                    width=300,
                    height=45,
                    style=ft.ButtonStyle(
                        bgcolor=ft.Colors.WHITE,
                        side=ft.BorderSide(1, ft.Colors.GREY_400)
                    )
                ),
                ft.Container(height=20),
                ft.Text(
                    value="Crie sua conta com e-mail aqui",
                    size=12,
                    color=ft.Colors.BLUE_700
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        width=400,
        padding=30,
        border_radius=10,
        bgcolor=ft.Colors.with_opacity(0.8, ft.Colors.WHITE),
        shadow=ft.BoxShadow(blur_radius=10, color=ft.Colors.BLACK12)
    )
    
    # Layout principal com Stack
    page.add(
        ft.Stack(
            [
                background_container,
                ft.Row(
                    [login_card],
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER
                )
            ],
            width=page.width,
            height=page.height
        )
    )

ft.app(target=main)