import flet as ft
from ui import dashboard_router

def main(page: ft.Page):
    page.title = "Dashboard Financeiro"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    page.on_route_change = dashboard_router
    page.go("/faturamento")

ft.app(target=main, view=ft.WEB_BROWSER)
