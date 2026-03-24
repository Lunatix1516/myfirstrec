import flet as ft

counter = 0 

def main(page: ft.Page):

    def count_click(e):
        global counter
        counter += 1
        counter_text.value = f"Clicks: {counter}"

        if counter == 5:
            achievement_text.value = "Achievement reached: 5 clicks"
        elif counter == 10:
            achievement_text.value = "Achievement reached: 10 clicks"
        elif counter == 15:
            achievement_text.value = "Achievement reached: 15 clicks"
        elif counter == 20:
            achievement_text.value = "Achievement reached: 20 clicks"

        page.update()

    def reset_click(e):
        global counter
        counter = 0
        counter_text.value = "Clicks: 0"
        achievement_text.value = ""
        page.update()

    page.theme_mode = "LIGHT"

    click_button = ft.Button(content="Click here", on_click=count_click)
    reset_button = ft.Button(content="Reset", on_click=reset_click)

    counter_text = ft.Text(value="Clicks: 0")
    achievement_text = ft.Text(value="")

    page.add(click_button, reset_button, counter_text, achievement_text)

ft.app(target=main)
