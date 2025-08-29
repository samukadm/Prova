import flet as ft

def main(page: ft.Page):
    page.title = "ToDo App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.ADAPTIVE
    page.padding = 20
    
    # Variáveis de estado
    tasks = []
    current_filter = "all"
    
    # Elementos da UI
    new_task = ft.TextField(
        hint_text="What needs to be done?",
        expand=True
    )
    
    tasks_view = ft.Column()
    
    # Botões de filtro
    all_button = ft.ElevatedButton("all")
    active_button = ft.ElevatedButton("active")
    completed_button = ft.ElevatedButton("completed")
    
    # Atualizar visualização das tarefas
    def update_tasks_view():
        tasks_view.controls.clear()
        
        for task in tasks:
            task_checkbox, task_delete_btn, task_completed = task
            
            if current_filter == "all":
                tasks_view.controls.append(
                    ft.Row(
                        controls=[
                            task_checkbox,
                            task_delete_btn
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    )
                )
            elif current_filter == "active" and not task_completed:
                tasks_view.controls.append(
                    ft.Row(
                        controls=[
                            task_checkbox,
                            task_delete_btn
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    )
                )
            elif current_filter == "completed" and task_completed:
                tasks_view.controls.append(
                    ft.Row(
                        controls=[
                            task_checkbox,
                            task_delete_btn
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    )
                )
        
        # Atualizar estilo dos botões de filtro
        all_button.style = ft.ButtonStyle(
            bgcolor=ft.Colors.BLUE_700 if current_filter == "all" else None,
            color=ft.Colors.WHITE if current_filter == "all" else None
        )
        active_button.style = ft.ButtonStyle(
            bgcolor=ft.Colors.BLUE_700 if current_filter == "active" else None,
            color=ft.Colors.WHITE if current_filter == "active" else None
        )
        completed_button.style = ft.ButtonStyle(
            bgcolor=ft.Colors.BLUE_700 if current_filter == "completed" else None,
            color=ft.Colors.WHITE if current_filter == "completed" else None
        )
        
        page.update()
    
    # Adicionar nova tarefa
    def add_task(e):
        if new_task.value:
            task_completed = False
            task_checkbox = ft.Checkbox(
                label=new_task.value,
                value=False,
                on_change=lambda e, task=task_completed: toggle_task(e, task)
            )
            
            task_delete_btn = ft.IconButton(
                icon=ft.Icons.DELETE_OUTLINE,
                on_click=lambda e, task=task_checkbox: delete_task(e, task)
            )
            
            tasks.append([task_checkbox, task_delete_btn, task_completed])
            new_task.value = ""
            update_tasks_view()
    
    # Alternar status da tarefa
    def toggle_task(e, task_completed_ref):
        # Encontrar a tarefa na lista e atualizar seu status
        for task in tasks:
            task_checkbox, task_delete_btn, task_completed = task
            if task_checkbox == e.control:
                task[2] = e.ontrol.value  # Atualizar o status completado
                break
        update_tasks_view()
    
    # Deletar tarefa
    def delete_task(e, task_to_delete):
        for i, task in enumerate(tasks):
            task_checkbox, task_delete_btn, task_completed = task
            if task_checkbox == task_to_delete:
                tasks.pop(i)
                break
        update_tasks_view()
    
    # Mudar filtro
    def change_filter(e, filter_type):
        nonlocal current_filter
        current_filter = filter_type
        update_tasks_view()
    
    # Limpar tarefas completadas
    def clear_completed(e):
        nonlocal tasks
        tasks = [task for task in tasks if not task[2]]  # Manter apenas tarefas não completadas
        update_tasks_view()
    
    # Configurar handlers dos botões
    all_button.on_click = lambda e: change_filter(e, "all")
    active_button.on_click = lambda e: change_filter(e, "active")
    completed_button.on_click = lambda e: change_filter(e, "completed")
    
    # Adicionar tarefas iniciais
    initial_tasks = [
        "Create Flet app",
        "Final touches", 
        "Deploy app"
    ]
    
    for task_name in initial_tasks:
        task_completed = False
        task_checkbox = ft.Checkbox(
            label=task_name,
            value=False,
            on_change=lambda e, task=task_completed: toggle_task(e, task)
        )
        
        task_delete_btn = ft.IconButton(
            icon=ft.Icons.DELETE_OUTLINE,
            on_click=lambda e, task=task_checkbox: delete_task(e, task)
        )
        
        tasks.append([task_checkbox, task_delete_btn, task_completed])
    
    # Layout principal
    page.add(
        ft.Column(
            width=600,
            controls=[
                ft.Row(
                    [ft.Text(value="Todos", style=ft.TextThemeStyle.HEADLINE_MEDIUM)],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    controls=[
                        new_task,
                        ft.FloatingActionButton(
                            icon=ft.Icons.ADD,
                            on_click=add_task
                        )
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                ft.Divider(),
                ft.Row(
                    controls=[all_button, active_button, completed_button],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=10
                ),
                ft.Divider(),
                tasks_view,
                ft.Row(
                    controls=[
                        ft.ElevatedButton(
                            "Clear completed",
                            on_click=clear_completed
                        )
                    ],
                    alignment=ft.MainAxisAlignment.END
                )
            ]
        )
    )
    
    # Atualizar visualização inicial
    update_tasks_view()

ft.app(target=main)