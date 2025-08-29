import flet as ft

'''def main(page: ft.Page):
    counter = ft.Text("0", size=50, data=0)

    def increment_click(e):
        counter.data += 1
        counter.value = str(counter.data)
        counter.update()

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD, on_click=increment_click
    )
    page.add(
        ft.SafeArea(
            ft.Container(
                counter,
                alignment=ft.alignment.center,
            ),
            expand=True,
        )
    )


ft.app(main)'''

#---------------------------------------------------------------------------------------------------------------------------



def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.title = "tela de login 2"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 0
    #page.window_min_width = 900 só pra eu saber que existe
    #page.window_min_height = 600 idem

    título_login = ft.Text (
        "BEM-VINDO",
        weight=ft.FontWeight.W_500,
        color=ft.Colors.WHITE,
        size=30,
        theme_style=ft.TextThemeStyle.HEADLINE_LARGE
    )

    tf_usuario = ft.TextField(
        hint_text="Digite seu usuário",
        width=500, 
        border_radius=30,
        bgcolor=ft.Colors.WHITE,
        focus_color=ft.Colors.WHITE,
        border_color=ft.Colors.WHITE,
        )
    
    tf_senha = ft.TextField(
        hint_text="Digite sua senha",
        width=500,
        border_radius=30,
        bgcolor=ft.Colors.WHITE,
        focus_color=ft.Colors.WHITE,
        border_color=ft.Colors.WHITE,
        password=True
    )

    checkbox = ft.Checkbox(
        label="lembrar-me", 
        value=False,
        active_color=ft.Colors.BLACK
        )
    
    esqueceu_senha = ft.Text(
        "esqueceu sua senha?",
        color=ft.Colors.BLACK,
    )

    textinhos = ft.Row( 
            [ checkbox,
            esqueceu_senha
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=210
    )

    botao_enviar = ft.ElevatedButton(
        "ENVIAR",
        width=500,
        bgcolor=ft.Colors.GREEN,
        color=ft.Colors.WHITE,
        )

    coluna_login = ft.Column(
        [
            título_login,
            tf_usuario,
            tf_senha,
            textinhos,
            botao_enviar
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,  
        spacing=30,  # espaço entre os itens
    )

    container_coluna_login = ft.Container(
        content = coluna_login,
        margin=150,
        padding=10
    )

    imagem_macaco = ft.Image(
        src=f"img/macaco.jpg",
        width=600,
        height=600,
        fit=ft.ImageFit.CONTAIN,
    )

    container_macaco = ft.Container(
        content=imagem_macaco,
        alignment=ft.alignment.center,
    )

    container_direita = ft.Container (
                    content=  container_coluna_login,
                    alignment=ft.alignment.center_left,
                    bgcolor=ft.Colors.BLUE,
                    width=720,
                    height=950,
                    expand=1,
                    gradient=ft.LinearGradient(
        begin=ft.alignment.top_center,
        end=ft.alignment.bottom_center,
        colors=[ft.Colors.BLUE, ft.Colors.BLUE_900],
    ),
                )

    container_esquerda =  ft.Container(
                    content=container_macaco,
                    alignment=ft.alignment.center_right,
                    bgcolor=ft.Colors.WHITE,
                    width=720,
                    height=950,
                    expand=1,
                )

    page.add(
        ft.Row( 
            [ container_direita,
            container_esquerda
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=0
        ),
    )
ft.app(main)