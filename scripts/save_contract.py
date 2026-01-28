import os

import requests
import yaml

# Веб-адрес контракта
CONTRACT_URL = "http://localhost:8080/api/docs/swagger.json"

# Папка для контракта
CONTRACT_PATH = "contract/"

# Файл контракта
CONTRACT_FILE_PATH = CONTRACT_PATH + "openapi.yaml"

try:
    response = requests.get(CONTRACT_URL)
    response.raise_for_status()

    data = response.json()

    os.makedirs(CONTRACT_PATH, exist_ok=True)
    with open(CONTRACT_FILE_PATH, "x", encoding="utf-8") as file:
        yaml.dump(data, file, sort_keys=False, allow_unicode=True)
    print(f"Контракт сохранен в '{CONTRACT_FILE_PATH}'")

except FileExistsError:
    print(f"Файл '{CONTRACT_FILE_PATH}' уже существует!")
except requests.exceptions.RequestException as error:
    print(f"Ошибка при загрузке контракта: {error}")
except Exception as error:
    print(f"Произошла непредвиденная ошибка: {error}")
