import flet as ft
import requests

def login(page: ft.Page):
    global username
    page.title = "Follow Up Vendas"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = ft.Colors.WHITE

    img = ft.Image( src="https://image.winudf.com/v2/image1/Y29tLmFwcC5iYWNrdXBfc2hhcmVfaWNvbl8xNzAxMDkzNTkxXzA3NQ/icon.png?w=184&fakeurl=1", width=360, height=120)
    labelUser = ft.Text("Insira seu usuário", color="black")
    labelPassowrd = ft.Text("Insira sua senha", color="black")
    username = ft.TextField(hint_text="Insira seu usuário", color="black", autofocus=True)
    username.value = str()
    password = ft.TextField(hint_text="Insira sua senha", color="black", password=True)
    password.value = str()
    msg = ft.Text("Usuario ou senha incorretos", color="Red")
    

    

    def on_login(e):
        if(username.value == "A2091"  and  password.value == "010203"):
            home(page)
        else:
            page.add(msg)
    
    
    btn = ft.Button(text="Entrar", bgcolor="blue", color="white", width=400,height=50, on_click=on_login)

    page.add(img,labelUser,username,labelPassowrd,password,btn)


def home(page: ft.Page):
    page.controls.clear()  # Limpa a página antes de adicionar novos controles
    page.horizontal_alignment = ft.MainAxisAlignment.START
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.theme_mode = ft.ThemeMode.LIGHT
    page.appbar = ft.CupertinoAppBar(
        leading=ft.Icon(ft.Icons.SUPERVISED_USER_CIRCLE, ft.Text(username)),
        trailing = ft.ElevatedButton(
            text=".",
            icon=ft.icons.LOGOUT
        ),
      middle=ft.Text("FollowUp App Vendas"),
    )

    def get_pedidos():
        try:
            # URL da API
            api_url = f'http://127.0.0.1:5000/pedidos?vendedor={username.value}'
            
            # Fazendo a requisição GET para a API
            response = requests.get(api_url)
            
            # Verifica se a requisição foi bem-sucedida
            if response.status_code == 200:
                return response.json()  # Retorna os dados em formato JSON
            else:
                return {"error": "Erro ao obter dados da API"}
        except Exception as e:
            return {"error": str(e)}
    


    def handle_change(e: ft.ControlEvent):
        pass

    dados_info = get_pedidos()

    if "error" in dados_info:
       page.add(ft.Text(f"Erro: {dados_info['error']}"))
       return


    controls = []
    for item in dados_info:
        panel_content = f"""
        Filial: {item['ZZY_FILIAL']}
        Data Venda: {item['ZZY_FCHTVD']}
        Número: {item['ZZY_NUM']}
        Cliente: {item['ZZY_DSCCLI']}
        Data Entrada: {item['ZZY_DTENT']}
        """
        
        controls.append(
            ft.ExpansionPanel(
                ft.Text(panel_content),  # Exibe as informações do pedido no painel
                bgcolor=ft.Colors.LIGHT_GREEN if item['ZZY_FILIAL'] == "01" else ft.Colors.LIGHT_GREEN,
                expanded=False
            )
        )
    
    # Criar o painel de expansão com os controles gerados
    panel = ft.ExpansionPanelList(
        expand_icon_color=ft.Colors.AMBER,
        elevation=8,
        divider_color=ft.Colors.AMBER,
        controls=controls  # Lista de painéis gerados
    )

    # Adiciona o painel à página
    page.add(panel)

def main(page: ft.Page):
    login(page)
    
    
    

ft.app(target=main)
