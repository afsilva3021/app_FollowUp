# FollowUp Vendas

Aplicação desenvolvida em **Python + Flet** para gerenciamento e acompanhamento de pedidos de venda através de integração com API REST.

O sistema foi projetado para facilitar o processo de **follow up comercial**, permitindo que vendedores e equipes acompanhem pedidos, clientes e status de atendimento em uma interface moderna, leve e intuitiva.

---

## Visão Geral

O FollowUp Vendas centraliza as informações comerciais em uma única aplicação, reduzindo o tempo de consulta e melhorando a visibilidade operacional dos pedidos em andamento.

A aplicação realiza consultas em tempo real através de uma API integrada ao ERP, apresentando os dados de forma organizada e acessível para o usuário final.

---

## Funcionalidades

- Autenticação de usuário
- Consulta de pedidos por vendedor
- Integração com API REST
- Visualização detalhada de pedidos
- Interface responsiva utilizando Flet
- Atualização dinâmica das informações
- Navegação simples e objetiva

---

## Tecnologias Utilizadas

| Tecnologia | Finalidade |
|------------|-------------|
| Python 3 | Linguagem principal |
| Flet | Interface gráfica |
| Requests | Consumo de API REST |
| JSON | Manipulação de dados |

---

## Estrutura do Projeto

```bash
app_FollowUp/
│
├── src/
│   └── main.py
│
├── pyproject.toml
├── README.md
└── .gitignore
````

## Instalação

## Clone o repositório:

git clone https://github.com/afsilva3021/app_FollowUp.git

## Acesse a pasta do projeto:

cd app_FollowUp

## Instale as dependências:

pip install -r requirements.txt

ou utilizando uv:

uv sync
Execução
flet run src/main.py
Integração

A aplicação consome uma API REST responsável por fornecer os pedidos vinculados ao vendedor autenticado.

## Exemplo de requisição:

GET /pedidos?vendedor=A2091
Objetivo do Projeto

O projeto foi desenvolvido com foco em melhorar o acompanhamento comercial de pedidos, proporcionando:

maior agilidade operacional;
centralização das informações;
redução de consultas manuais no ERP;
melhor acompanhamento dos pedidos de venda;
maior produtividade para equipes comerciais.
Roadmap

## Funcionalidades previstas para futuras versões:

autenticação JWT;
integração direta com TOTVS Protheus;
dashboard gerencial;
exportação Excel/PDF;
notificações em tempo real;
aplicação Android;
indicadores comerciais;
histórico de acompanhamento.
Status do Projeto

Projeto em desenvolvimento

