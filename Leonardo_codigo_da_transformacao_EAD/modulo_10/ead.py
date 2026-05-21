import requests

api_key = "SUA_CHAVE_AQUI"

cidade = input("Digite o nome da cidade: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&lang=pt_br&units=metric"

try:

    resposta = requests.get(url)

    resposta.raise_for_status()

    dados = resposta.json()

    temperatura = dados["main"]["temp"]
    sensacao = dados["main"]["feels_like"]
    clima = dados["weather"][0]["description"]
    umidade = dados["main"]["humidity"]

    print("\n===== PREVISÃO DO TEMPO =====")
    print(f"Cidade: {cidade}")
    print(f"Temperatura: {temperatura}°C")
    print(f"Sensação térmica: {sensacao}°C")
    print(f"Clima: {clima}")
    print(f"Umidade: {umidade}%")

except requests.exceptions.HTTPError:
    print("Erro HTTP! Verifique o nome da cidade ou a API.")

except requests.exceptions.ConnectionError:
    print("Erro de conexão! Verifique sua internet.")

except requests.exceptions.Timeout:
    print("A conexão demorou muito.")

except requests.exceptions.RequestException:
    print("Ocorreu um erro na requisição.")

except KeyError:
    print("Erro ao pegar informações da API.")
