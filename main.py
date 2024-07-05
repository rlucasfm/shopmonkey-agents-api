from dotenv import load_dotenv
import json
import requests
import os
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI
from llama_index.core.tools import FunctionTool, QueryEngineTool, ToolMetadata
from llama_index.core.indices.struct_store import JSONQueryEngine
from schemas import get_order_schema
from json_schema import get_order_json_schema

load_dotenv()

def convert_bools_to_strings(params):
    for key, value in params.items():
        if isinstance(value, bool):
            params[key] = str(value).lower()
    return params

# Initialize model
llm = OpenAI(model="gpt-3.5-turbo", temperature=0)

nl_query_engine = JSONQueryEngine(
    json_value=open("memory.json", "r").read(),
    json_schema=get_order_json_schema,
    llm=llm,
)

# Create tools
def get_orders(**parameters):
    parameters = convert_bools_to_strings(parameters['parameters'])
    url = "https://api.shopmonkey.io/v2/orders"
    # url = "https://a93baa29fadd5e633ce8b36ad20c843e.m.pipedream.net"
    headers = {
        "Authorization": f"Bearer {os.getenv("SHOPMONKEY_API_TOKEN")}"
    }
    response = requests.get(url, headers=headers, params=parameters)
    response_json = response.json()
    f = open("memory.json", "w")
    f.write(json.dumps(response_json))
    f.close()
    # return "ok"
    return json.dumps(response_json)

get_orders_tool = FunctionTool.from_defaults(
    fn=get_orders,
    name="Get_orders",
    description=f"this tool makes an API call to get orders from Shopmonkey and persists it on a JSON file, it follows the OpenAPI schema: {get_order_schema}",
)

json_query_tool = QueryEngineTool(
    query_engine=nl_query_engine,
    metadata=ToolMetadata(
        name="Orders_data",
        description=(
            "Provides stored info about orders, invoices and payments."
        )
    )
)

# Initialize agent
agent = ReActAgent.from_tools(
    tools=[get_orders_tool], 
    llm=llm, 
    verbose=True,
    context=f"""\
        Você é um assistente que auxilia na análise administrativa de ordens obtidas a partir Shopmonkey.
        
        Seu objetivo é entender e auxiliar gerentes a entender mais sobre as ordens, 
        invoices e pedidos pagos feitos em sua oficina através da API da Shopmonkey.

        Ao interagir com os usuários, mantenha um tom amigável e encorajador, sempre buscando facilitar a compreensão e a clareza da apresentação final. Respeite as preferências e o estilo do usuário, e esteja pronto para adaptar suas recomendações de acordo com o feedback recebido. Evite usar jargões complexos e certifique-se de que as sugestões sejam práticas e aplicáveis.

        Responda sempre com informações, formatados como tabelas se possível.
    """
)

response = agent.chat("Quais os invoices de janeiro de 2024?")