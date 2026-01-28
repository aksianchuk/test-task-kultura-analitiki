from aiohttp import web

from .handlers import create_note, delete_note, get_note, get_notes, update_note


def setup_routes(app: web.Application) -> None:
    """Регистрирует маршруты для CRUD операций с заметками."""

    app.add_routes(
        [
            web.get("/notes", get_notes),
            web.get("/notes/{id}", get_note),
            web.post("/notes", create_note),
            web.put("/notes/{id}", update_note),
            web.delete('/notes/{id}', delete_note),
        ]
    )
