import flet as ft


def main(page: ft.Page):
    page.title = "Two-View Greeting App"
    page.window.width = 520
    page.window.height = 700
    page.window.min_width = 420
    page.window.min_height = 600
    page.window.minimized = False
    page.padding = 0
    page.bgcolor = "#F4F7FB"
    page.theme_mode = ft.ThemeMode.LIGHT

    name = ""
    name_field = None

    def name_changed(e):
        nonlocal name
        name = e.control.value or ""

    def home_view():
        nonlocal name_field
        name_field = ft.TextField(
            label="Your name",
            hint_text="Enter your name",
            value=name,
            prefix_icon=ft.Icons.PERSON_OUTLINE,
            border=ft.OutlineInputBorder(border_radius=12),
            autofocus=True,
            on_change=name_changed,
        )

        async def continue_click(_):
            nonlocal name
            name = (name_field.value or "").strip()
            if not name:
                page.show_dialog(
                    ft.AlertDialog(
                        modal=True,
                        title=ft.Text("Name needed"),
                        content=ft.Text("Please enter your name before continuing."),
                        actions=[
                            ft.TextButton(
                                "Got it",
                                on_click=lambda e: page.pop_dialog(),
                            )
                        ],
                    )
                )
                return

            await page.push_route("/greeting")

        return ft.View(
            route="/",
            bgcolor="#F4F7FB",
            padding=24,
            controls=[
                ft.Container(
                    expand=True,
                    alignment=ft.Alignment.CENTER,
                    content=ft.Container(
                        width=420,
                        padding=32,
                        border_radius=24,
                        bgcolor="white",
                        shadow=ft.BoxShadow(
                            blur_radius=28,
                            color="#18315318",
                            offset=ft.Offset(0, 12),
                        ),
                        content=ft.Column(
                            controls=[
                                ft.Container(
                                    width=68,
                                    height=68,
                                    border_radius=22,
                                    bgcolor="#EAF0FF",
                                    alignment=ft.Alignment.CENTER,
                                    content=ft.Icon(
                                        ft.Icons.WAVING_HAND,
                                        size=34,
                                        color="#2457D6",
                                    ),
                                ),
                                ft.Text(
                                    "A warm welcome starts here",
                                    size=14,
                                    color="#667085",
                                ),
                                ft.Text(
                                    "Say hello!",
                                    size=32,
                                    weight=ft.FontWeight.BOLD,
                                    color="#172B4D",
                                ),
                                ft.Text(
                                    "Tell us your name and we’ll make it personal.",
                                    size=15,
                                    color="#667085",
                                    text_align=ft.TextAlign.CENTER,
                                ),
                                ft.Container(height=4),
                                name_field,
                                ft.Button(
                                    content="Continue",
                                    icon=ft.Icons.ARROW_FORWARD,
                                    on_click=continue_click,
                                    style=ft.ButtonStyle(
                                        bgcolor="#2457D6",
                                        color="white",
                                        padding=ft.Padding.symmetric(
                                            horizontal=24,
                                            vertical=16,
                                        ),
                                        shape=ft.RoundedRectangleBorder(radius=12),
                                    ),
                                ),
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=16,
                            tight=True,
                        ),
                    ),
                )
            ],
        )

    def greeting_view():
        async def back_click(_):
            await page.push_route("/")

        return ft.View(
            route="/greeting",
            bgcolor="#F4F7FB",
            padding=24,
            controls=[
                ft.Container(
                    expand=True,
                    alignment=ft.Alignment.CENTER,
                    content=ft.Container(
                        width=420,
                        padding=32,
                        border_radius=24,
                        bgcolor="white",
                        shadow=ft.BoxShadow(
                            blur_radius=28,
                            color="#18315318",
                            offset=ft.Offset(0, 12),
                        ),
                        content=ft.Column(
                            controls=[
                                ft.Container(
                                    width=68,
                                    height=68,
                                    border_radius=22,
                                    bgcolor="#EAF0FF",
                                    alignment=ft.Alignment.CENTER,
                                    content=ft.Icon(
                                        ft.Icons.WAVING_HAND,
                                        size=34,
                                        color="#2457D6",
                                    ),
                                ),
                                ft.Text("It’s lovely to meet you", size=14, color="#667085"),
                                ft.Text(
                                    f"Hello, {name}!",
                                    size=32,
                                    weight=ft.FontWeight.BOLD,
                                    color="#172B4D",
                                    text_align=ft.TextAlign.CENTER,
                                ),
                                ft.Text(
                                    "We’re glad you stopped by.",
                                    size=15,
                                    color="#667085",
                                    text_align=ft.TextAlign.CENTER,
                                ),
                                ft.Container(height=4),
                                ft.Button(
                                    content="Back",
                                    icon=ft.Icons.ARROW_BACK,
                                    on_click=back_click,
                                    style=ft.ButtonStyle(
                                        bgcolor="#2457D6",
                                        color="white",
                                        padding=ft.Padding.symmetric(
                                            horizontal=24,
                                            vertical=16,
                                        ),
                                        shape=ft.RoundedRectangleBorder(radius=12),
                                    ),
                                ),
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=16,
                            tight=True,
                        ),
                    ),
                )
            ],
        )

    def route_change(_):
        page.views.clear()
        if page.route == "/greeting":
            page.views.append(greeting_view())
        else:
            page.views.append(home_view())
        page.update()

    page.on_route_change = route_change
    route_change(None)


if __name__ == "__main__":
    ft.run(main)
