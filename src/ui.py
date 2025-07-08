
import flet as ft
from datetime import datetime
import asyncio
from api import get_api_data

def format_currency(value):
    return f"R$ {value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def format_number(value):
    return f"{value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def render_dashboard(page: ft.Page, title: str, endpoint: str):
    valor_text = ft.Text(f"{title}:\n--", size=22, weight="bold")
    qtde_text = ft.Text("Quantidade:\n--", size=22, weight="bold")
    last_update = ft.Text("Última atualização: --", size=12, italic=True)

    dashboard = ft.ResponsiveRow([
        ft.Container(valor_text, padding=20, bgcolor=ft.Colors.AMBER_100, col={"sm": 12, "md": 6}),
        ft.Container(qtde_text, padding=20, bgcolor=ft.Colors.CYAN_100, col={"sm": 12, "md": 6}),
    ])

    def carregar():
        data = get_api_data(endpoint)
        if "items" in data and len(data["items"]) > 0:
            item = data["items"][0]
            valor = item.get("valor_saida") or item.get("valor_total") or 0
            qtde = item.get("qtde_saida") or item.get("qtde_total") or 0
            valor_text.value = f"💰 {title}:\n{format_currency(valor)}"
            qtde_text.value = f"📦 Quantidade:\n{format_number(qtde)} m."
            last_update.value = f"Última atualização: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
        else:
            valor_text.value = "Erro ao carregar valor"
            qtde_text.value = "Erro ao carregar quantidade"
        page.update()

    async def atualizar_auto():
        while True:
            carregar()
            await asyncio.sleep(900)

    atualizar_btn = ft.ElevatedButton("Atualizar Agora", on_click=lambda e: carregar())

    page.views.clear()
    page.views.append(
        ft.View(
            route=f"/{endpoint}",
            controls=[
                menu_bar(page),
                ft.Text(f"📊 Dashboard: {title}", size=26, weight="bold"),
                atualizar_btn,
                ft.Divider(),
                dashboard,
                last_update
            ],
            scroll="adaptive"
        )
    )

    carregar()
    page.run_task(atualizar_auto)
    page.update()

def menu_bar(page: ft.Page):
    return ft.Row(
        controls=[
            ft.ElevatedButton("Faturamento", on_click=lambda _: page.go("/faturamento")),
            ft.ElevatedButton("A Receber", on_click=lambda _: page.go("/areceber")),
            ft.ElevatedButton("A Pagar", on_click=lambda _: page.go("/apagar")),
        ],
        alignment=ft.MainAxisAlignment.START,
    )

def dashboard_router(e: ft.RouteChangeEvent):
    route = e.route.strip("/")
    if route == "faturamento":
        render_dashboard(e.page, "Faturamento", "api_faturamento_mes_atual")
    elif route == "areceber":
        render_dashboard(e.page, "Contas a Receber", "api_areceber")
    elif route == "apagar":
        render_dashboard(e.page, "Contas a Pagar", "api_apagar")
    else:
        e.page.go("/faturamento")
