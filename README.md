# Test task Kultura Analitiki

**Test task Kultura Analitiki** - тестовое задание по реализации асинхронного сервера и клиента с использованием aiohttp.  
Включает генерацию OpenAPI контракта и написание тестов.

## Оглавление

- [Основные технологии](#основные-технологии)
- [Структура проекта](#структура-проекта)
- [Установка и запуск](#установка-и-запуск)
- [Документация](#документация)
- [Автор](#автор)

## Основные технологии
- Python 3.13
- aiohttp - асинхронный сервер и клиент
- aiohttp-apigami - генерация OpenAPI контракта и документации
- marshmallow - валидация и сериализация данных
- pytest + pytest-asyncio + pytest-aiohttp - тестирование асинхронного API

**Примечание:** изначально планировалось использовать [aiohttp-apispec](https://github.com/maximdanilchenko/aiohttp-apispec), но проект уже несколько лет не поддерживается, поэтому был выбран более современный форк [aiohttp-apigami](https://github.com/kulapard/aiohttp-apigami).

## Структура проекта
```
test-task-kultura-analitiki
├─ client/                  # сгенерированный клиент из OpenAPI контракта
├─ contract/                # каталог для хранения OpenAPI контракта
│  └─ openapi.yaml          # сгенерированный контракт
├─ scripts/                 # вспомогательные скрипты
│  ├─ save_contract.py      # скрипт для сохранения OpenAPI контракта
├─ server/                  # каталог для сервера
│  ├─ app/                  # серверное приложение
│  │  ├─ handlers.py        # обработчики запросов
│  │  ├─ main.py            # точка входа сервера
│  │  ├─ routes.py          # маршруты
│  │  └─ schemas.py         # схемы валидации данных
│  └─ run.py                # скрипт запуска сервера
├─ test/                    # тесты проекта
│  ├─ conftest.py           # фикстуры для тестов
│  └─ test_api.py           # тесты для API
├─ .gitignore               # файлы/папки, игнорируемые git
├─ pytest.ini               # конфигурация pytest
├─ README.md                # описание проекта, инструкции по запуску
└─ requirements.txt         # зависимости проекта

```

## Установка и запуск
### Сервер
1. Клонируйте репозиторий:
```
git clone https://github.com/aksianchuk/test-task-kultura-analitiki
cd test-task-kultura-analitiki
```
2. Создайте и активируйте виртуальное окружение:
```
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```
3. Установите зависимости:
```
pip install -r requirements.txt
```
4. Запустите сервер.
```
python -m server.run
```
Проект будет доступен по адресу:  
http://localhost:8080

### Скрипт для сохранения OpenAPI контракта
1. Запустите сервер по инструкции выше.
2. Запустите скрипт.
```
python -m scripts.save_contract
```

### Генерация клиента из OpenAPI контракта
1. Сохраните OpenAPI контракт по инструкции выше.
2. Выполните команду.
```
# NPM
openapi-generator-cli generate \
    -i contract/openapi.yaml \
    -g python \
    --library asyncio \
    --skip-validate-spec \
    -o client

# Docker
docker run --rm \
  -v ${PWD}:/local \
  openapitools/openapi-generator-cli generate \
  -i /local/contract/openapi.yaml \
  -g python \
  --library asyncio \
  --skip-validate-spec \
  -o /local/client
```

### Запуск тестов
1. Выполните команду из корня проекта.
```
pytеst
```

## Документация
Документация доступна после запуска сервера по адресу:   
http://localhost:8080/api/docs/

## Автор
https://github.com/aksianchuk (Никита Оксенчук)