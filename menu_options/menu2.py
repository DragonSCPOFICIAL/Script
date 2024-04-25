import json
import random
import requests

# Função para buscar os dados mais recentes dos payloads
def fetch_payload_data():
    url = "https://raw.githubusercontent.com/DragonSCPOFICIAL/Script/main/payload_config.json"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            global payload_data
            payload_data = json.loads(response.text)
            print("Payloads atualizados com sucesso.")
        else:
            print("Falha ao atualizar payloads, status code:", response.status_code)
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar JSON: {e}")
    except Exception as e:
        print(f"Erro ao buscar dados de payload: {e}")

# Função para gerar payloads com base nos dados carregados
def generate_payloads():
    fetch_payload_data()
    if not payload_data:
        print("Dados de payload não carregados. Abortando geração de payloads.")
        return

    try:
        num_payloads = int(input("Quantas payloads deseja gerar? "))
    except ValueError:
        print("Entrada inválida, por favor insira um número inteiro.")
        return

    methods = payload_data.get('methods', [])
    custom_strings = payload_data.get('custom_strings', [])
    domains = payload_data.get('domains', [])

    for i in range(1, num_payloads + 1):
        method = random.choice(methods) if methods else "GET"
        custom_string = random.choice(custom_strings) if custom_strings else "HTTP/1.1"
        domain = random.choice(domains) if domains else "example.com"
        payload = f"{method} {domain} {custom_string}"
        print(f"Payload {i}\n{payload}\n")

    input("Pressione Enter para continuar...")
    clear_screen()  # Assegure-se de definir ou importar clear_screen se necessário

