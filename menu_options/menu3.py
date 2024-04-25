import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import warnings
import os
import sys

# Ignorar avisos de certificados não verificados
warnings.simplefilter('ignore', InsecureRequestWarning)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

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

def test_individual_proxy():
    input_proxies = input("Insira os IPs dos proxies separados por '#': ")
    proxies = input_proxies.split('#')
    ports = [80, 8080, 443]
    proxy_results = {}

    print("Testando proxies, por favor aguarde...")
    for ip in proxies:
        successful_ports = []
        for port in ports:
            result, external_ip = test_proxy(ip, port)
            if result:
                if port not in successful_ports:
                    successful_ports.append(port)
        if successful_ports:
            proxy_results[ip] = {'external_ip': external_ip, 'ports': sorted(successful_ports)}

    if proxy_results:
        print("\nProxies que funcionaram:")
        for ip, details in proxy_results.items():
            print(f"{ip}\nIP Externo: {details['external_ip']}\nPortas que pegaram: {', '.join(map(str, details['ports']))}")
    else:
        print("\nNenhum proxy funcionou. Tente outros IPs.")

    input("Pressione Enter para continuar...")
    clear_screen()

