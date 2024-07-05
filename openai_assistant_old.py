from dotenv import load_dotenv
import os
import json
import streamlit as st
from openai import OpenAI
import time
from PIL import Image
import requests

load_dotenv()

client = OpenAI()
assistant_id = "asst_h4FJ5FIIkQU92uflXQdwHdpk"
thread = client.beta.threads.create()

def convert_bools_to_strings(params):
    for key, value in params.items():
        if isinstance(value, bool):
            params[key] = str(value).lower()
    return params

def get_orders(**parameters):
    parameters = convert_bools_to_strings(parameters)
    url = "https://api.shopmonkey.io/v2/orders"
    # url = "https://a93baa29fadd5e633ce8b36ad20c843e.m.pipedream.net"
    headers = {
        "Authorization": f"Bearer {os.getenv("SHOPMONKEY_API_TOKEN")}"
    }
    response = requests.get(url, headers=headers, params=parameters)
    output = json.dumps(response.json())
    return output

function_mapping = {
    "getOrders": get_orders
}

st.title("ShopmonkeyAI - Eu vou te ajudar a consumir dados sobre ordens da Shopmonkey! ")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": """Bem-vindo! Eu sou o ShopmonkeyAI, um cérebro artificial pronto pra te ajudar a consumir dados sobre ordens da Shopmonkey.
                                     \nSou uma criação da FWK Labs. Caso queira saber mais, acesse: https://fwk.global."""}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])


if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=prompt
    )

    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant_id
    )

    while run.status != 'completed':
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
        )

        if run.status == 'requires_action':
            required_action = run.required_action

            if required_action.type == 'submit_tool_outputs':
                tool_outputs = []
                for tool_call in required_action.submit_tool_outputs.tool_calls:
                    if tool_call.type == 'function':
                        function_name = tool_call.function.name
                        arguments_json = tool_call.function.arguments

                        # Parse the JSON arguments
                        arguments = json.loads(arguments_json)

                        if function_name in function_mapping:
                            response = function_mapping[function_name](**arguments)
                            tool_outputs.append({
                                "tool_call_id": tool_call.id,
                                "output": response,
                            })
                            # submit the tool outputs to the thread and run
                            run = client.beta.threads.runs.submit_tool_outputs(
                                thread_id=thread.id,
                                run_id=run.id,
                                tool_outputs= tool_outputs
                            )

    # Retrieve messages added by the assistant
    messages = client.beta.threads.messages.list(
        thread_id=thread.id
    )

    response = messages.to_dict()

    msg = response.get('data')[0]['content'][0]['text']['value']
    msg = msg.split('【')[0]

    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)