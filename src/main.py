import flet as ft
from ui import router
import structlog

def configure_logging():
    structlog.configure(
        processors=[
            structlog.stdlib.add_log_level,
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.JSONRenderer()
        ],
        logger_factory=structlog.stdlib.LoggerFactory(),
    )

def main(page: ft.Page):
    configure_logging()
    page.title = "Dashboard Financeiro"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    
    def on_route_change(route):
        page.views.clear()
        router(page, route.route)
        page.update()
    
    page.on_route_change = on_route_change
    page.go("/faturamento")

# Versão simplificada sem async_io
ft.app(target=main, view=ft.AppView.WEB_BROWSER)