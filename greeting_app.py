import flet as ft


def main(page: ft.Page):
    page.title = "Greeting App"
    page.window.width = 420
    page.window.height = 620
    page.window.min_width = 360
    page.window.min_height = 520
    page.window.minimized = False
    page.padding = 20
    page.bgcolor = "#F4F7FB"

    name_field = ft.TextField(
        label="Your name",
        hint_text="Type your name here",
        prefix_icon=ft.Icons.PERSON_OUTLINE,
        border_radius=12,
        autofocus=True,
    )
    greeting = ft.Text(
        "Your greeting will appear here",
        size=16,
        color="#667085",
        text_align=ft.TextAlign.CENTER,
    )

    def greet(_):
        name = (name_field.value or "").strip()
        greeting.value = f"Hello, {name}!" if name else "Hello! Please enter your name."
        greeting.color = "#2457D6"
        page.update()

    greet_button = ft.ElevatedButton(
        "Greet Me",
        icon=ft.Icons.WAVING_HAND,
        on_click=greet,
        style=ft.ButtonStyle(
            bgcolor="#2457D6",
            color="white",
            padding=18,
        ),
    )

    page.add(
        ft.Container(
            expand=True,
            alignment=ft.alignment.center,
            content=ft.Container(
                width=360,
                padding=30,
                border_radius=22,
                bgcolor="white",
                shadow=ft.BoxShadow(
                    spread_radius=0,
                    blur_radius=24,
                    color="#15294B18",
                    offset=ft.Offset(0, 10),
                ),
                content=ft.Column(
                    [
                        ft.Container(
                            width=64,
                            height=64,
                            border_radius=20,
                            bgcolor="#EAF0FF",
                            alignment=ft.alignment.center,
                            content=ft.Icon(ft.Icons.WAVING_HAND, size=32, color="#2457D6"),
                        ),
                        ft.Text("A little hello goes a long way", size=13, color="#667085"),
                        ft.Text("Say hello!", size=30, weight=ft.FontWeight.BOLD, color="#172B4D"),
                        ft.Text(
                            "Enter your name and we’ll make it personal.",
                            size=14,
                            color="#667085",
                            text_align=ft.TextAlign.CENTER,
                        ),
                        ft.Container(height=8),
                        name_field,
                        greet_button,
                        ft.Container(
                            padding=14,
                            border_radius=12,
                            bgcolor="#F5F8FF",
                            alignment=ft.alignment.center,
                            content=greeting,
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=14,
                    tight=True,
                ),
            ),
        )
    )


ft.app(target=main)
