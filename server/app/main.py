from aiohttp import web
from aiohttp_apigami import setup_aiohttp_apispec, validation_middleware

from .routes import setup_routes


def create_app() -> web.Application:
    """Создает и настраивает приложение."""

    app = web.Application()

    # Настраиваем маршруты
    setup_routes(app)

    # Создаем "базу данных" в памяти
    app["db"] = {}
    app["db"]["notes"] = {}
    app["db"]["notes_counter"] = 1

    # Настраиваем документацию OpenAPI
    setup_aiohttp_apispec(
        app=app,
        title="Notes",
        version="0.1",
        url="/api/docs/swagger.json",
        swagger_path="/api/docs",
        openapi_version="3.0.3"
    )

    # Добавляем middleware для валидации запросов
    app.middlewares.append(validation_middleware)

    return app
