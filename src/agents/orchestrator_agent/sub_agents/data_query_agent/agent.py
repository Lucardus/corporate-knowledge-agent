from google.adk.agents import Agent
from toolbox_core import ToolboxSyncClient

toolbox = ToolboxSyncClient("http://127.0.0.1:5000")

order_management_tools = toolbox.load_toolset("order_management_toolset")

data_query_agent = Agent(
    model='gemini-2.5-flash',
    name='data_query_agent',
    description='Consulta dados operacionais de pedidos (status, historico, listagens) via MCP Toolbox conectado ao AlloyDB.',
    instruction=(
        'Voce e o Data Query Agent do Corporate Knowledge Agent. '
        'Use as ferramentas disponiveis para consultar o status de pedidos, '
        'historico de pedidos por cliente, ou listagens por status. '
        'Nunca invente um order_id, customer_id ou status que nao veio de uma chamada de ferramenta real. '
        'Se a consulta nao retornar resultado, informe claramente que o pedido/cliente nao foi encontrado, '
        'em vez de supor um resultado. '
        'Nao exponha dados de clientes nao relacionados a pergunta feita.'
    ),
    tools=order_management_tools,
)
