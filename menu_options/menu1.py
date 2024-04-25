import requests
import random
import json
import os
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import warnings

# Ignorar avisos de certificados não verificados
warnings.simplefilter('ignore', InsecureRequestWarning)

def test_proxy(ip, port):
    proxy_url = f"http://{ip}:{port}" if port in [80, 8080] else f"https://{ip}:{port}"
    proxy_dict = {'http': proxy_url, 'https': proxy_url}
    try:
        response = requests.get('http://icanhazip.com', proxies=proxy_dict, timeout=5, verify=False)
        if response.status_code == 200:
            external_ip = response.text.strip()
            return True, external_ip
        else:
            return False, None
    except requests.exceptions.RequestException:
        return False, None

def generate_and_test_proxies():
    # Esta é uma função simplificada. Você deve implementar a lógica para gerar IPs e então testá-los.
    print("Insira um IP base para gerar proxies e testá-los:")
    base_ip = input("IP base: ")  # Simples exemplo de input
    port = 8080  # Exemplo de porta

    # Exemplo de teste de proxy com IP base e porta
    result, external_ip = test_proxy(base_ip, port)
    if result:
        print(f"Proxy {base_ip}:{port} é válido. IP Externo: {external_ip}")
    else:
        print(f"Proxy {base_ip}:{port} falhou.")

    input("Pressione Enter para continuar...")


