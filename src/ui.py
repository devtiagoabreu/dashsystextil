import flet as ft
from datetime import datetime
from api import get_api_data, APIError
import structlog

logger = structlog.get_logger(__name__)

def format_currency(value: float) -> str:
    try:
        return f"R$ {value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    except (ValueError, TypeError):
        return "R$ --"

def format_number(value: float) -> str:
    try:
        return f"{value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    except (ValueError, TypeError):
        return "--"

class Dashboard:
    def __init__(self, page: ft.Page, title: str, endpoint: str):
        self.page = page
        self.title = title
        self.endpoint = endpoint
        self.error_display = ft.Text(color=ft.Colors.RED, visible=False)
        self.valor_text = ft.Text(size=22, weight=ft.FontWeight.BOLD)
        self.qtde_text = ft.Text(size=22, weight=ft.FontWeight.BOLD)
        self.last_update = ft.Text("Última atualização: --", size=12, italic=True)
        self.setup_view()

    def setup_view(self):
        dashboard = ft.Row(
            controls=[
                ft.Container(
                    content=ft.Column([self.valor_text], alignment=ft.MainAxisAlignment.CENTER),
                    padding=20, bgcolor=ft.Colors.AMBER_100, expand=True
                ),
                ft.Container(
                    content=ft.Column([self.qtde_text], alignment=ft.MainAxisAlignment.CENTER),
                    padding=20, bgcolor=ft.Colors.CYAN_100, expand=True
                ),
            ]
        )

        self.page.views.append(
            ft.View(
                route=f"/{self.endpoint}",
                controls=[
                    ft.Row([
                        ft.ElevatedButton("Faturamento", on_click=lambda e: self.page.go("/faturamento")),
                        ft.ElevatedButton("A Receber", on_click=lambda e: self.page.go("/areceber")),
                        ft.ElevatedButton("A Pagar", on_click=lambda e: self.page.go("/apagar")),
                    ]),
                    ft.Text(f"📊 Dashboard: {self.title}", size=26, weight=ft.FontWeight.BOLD),
                    self.error_display,
                    ft.Divider(),
                    dashboard,
                    self.last_update,
                    ft.ElevatedButton(
                        "Atualizar Agora",
                        on_click=lambda e: self.load_data()
                    )
                ]
            )
        )
        self.load_data()

    def load_data(self):
        try:
            data = get_api_data(self.endpoint)
            if not data or "items" not in data or len(data["items"]) == 0:
                raise APIError("Dados não encontrados", 404)

            item = data["items"][0]
            valor = item.get("valor_saida") or item.get("valor_total") or 0
            qtde = item.get("qtde_saida") or item.get("qtde_total") or 0

            self.valor_text.value = f"💰 {self.title}:\n{format_currency(valor)}"
            self.qtde_text.value = f"📦 Quantidade:\n{format_number(qtde)} m."
            self.error_display.visible = False
        except APIError as e:
            self.valor_text.value = f"💰 {self.title}:\n--"
            self.qtde_text.value = "📦 Quantidade:\n-- m."
            self.error_display.value = f"Erro: {e.message}"
            self.error_display.visible = True
        except Exception as e:
            logger.error("Erro inesperado", error=str(e))
            self.error_display.value = "Erro interno"
            self.error_display.visible = True

        self.last_update.value = f"Última atualização: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
        self.page.update()

def router(page: ft.Page, route: str):
    routes = {
        "faturamento": ("Faturamento", "api_faturamento_mes_atual"),
        "areceber": ("Contas a Receber", "api_areceber"),
        "apagar": ("Contas a Pagar", "api_apagar")
    }
    
    route = route.strip("/") or "faturamento"
    title, endpoint = routes.get(route, routes["faturamento"])
    
    Dashboard(page, title, endpoint)