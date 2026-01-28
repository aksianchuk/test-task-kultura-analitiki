from http import HTTPStatus

from aiohttp import web
from aiohttp_apigami import docs
from aiohttp_apigami.decorators.request import json_schema, match_info_schema

from .schemas import ErrorMessageSchema, NoteIdSchema, NoteSchema, NoteTextSchema


@docs(
    tags=["notes"],
    summary="Получение всех заметок.",
    responses={
        HTTPStatus.OK: {"description": "Заметки получены", "schema": NoteSchema(many=True)},
        HTTPStatus.INTERNAL_SERVER_ERROR: {"description": "Ошибка сервера"},
    },
)
async def get_notes(request: web.Request) -> web.Response:
    """Получение всех заметок."""

    return web.json_response(list(request.app["db"]["notes"].values()))


@docs(
    tags=["notes"],
    summary="Получение заметки по id.",
    responses={
        HTTPStatus.OK: {"description": "Заметка получена", "schema": NoteSchema},
        HTTPStatus.NOT_FOUND: {"description": "Заметка не найдена", "schema": ErrorMessageSchema},
        HTTPStatus.UNPROCESSABLE_CONTENT: {"description": "Ошибка валидации"},
        HTTPStatus.INTERNAL_SERVER_ERROR: {"description": "Ошибка сервера"},
    },
)
@match_info_schema(NoteIdSchema)
async def get_note(request: web.Request) -> web.Response:
    """Получение заметки по id."""

    note_id = request["match_info"]["id"]
    note = request.app["db"]["notes"].get(note_id)
    if not note:
        return web.json_response({"error": "Заметка не найдена"}, status=HTTPStatus.NOT_FOUND)
    return web.json_response(note)


@docs(
    tags=["notes"],
    summary="Создание новой заметки.",
    responses={
        HTTPStatus.CREATED: {"description": "Заметка создана", "schema": NoteSchema},
        HTTPStatus.UNPROCESSABLE_CONTENT: {"description": "Ошибка валидации"},
        HTTPStatus.INTERNAL_SERVER_ERROR: {"description": "Ошибка сервера"},
    },
)
@json_schema(NoteTextSchema)
async def create_note(request: web.Request) -> web.Response:
    """Создание новой заметки."""

    new_note = request["json"]
    new_note["id"] = request.app["db"]["notes_counter"]
    request.app["db"]["notes"][new_note["id"]] = new_note
    request.app["db"]["notes_counter"] += 1
    return web.json_response(new_note, status=HTTPStatus.CREATED)


@docs(
    tags=["notes"],
    summary="Изменение заметки.",
    responses={
        HTTPStatus.OK: {"description": "Заметка изменена", "schema": NoteSchema},
        HTTPStatus.NOT_FOUND: {"description": "Заметка не найдена", "schema": ErrorMessageSchema},
        HTTPStatus.UNPROCESSABLE_CONTENT: {"description": "Ошибка валидации"},
        HTTPStatus.INTERNAL_SERVER_ERROR: {"description": "Ошибка сервера"},
    },
)
@match_info_schema(NoteIdSchema)
@json_schema(NoteTextSchema)
async def update_note(request: web.Request) -> web.Response:
    """Изменение заметки."""

    note_id = request["match_info"]["id"]
    note = request.app["db"]["notes"].get(note_id)
    if not note:
        return web.json_response({"error": "Заметка не найдена"}, status=HTTPStatus.NOT_FOUND)
    new_text = request["json"]["text"]
    request.app["db"]["notes"][note_id]["text"] = new_text
    return web.json_response(note, status=HTTPStatus.OK)


@docs(
    tags=["notes"],
    summary="Удаление заметки.",
    responses={
        HTTPStatus.NO_CONTENT: {"description": "Заметка удалена"},
        HTTPStatus.UNPROCESSABLE_CONTENT: {"description": "Ошибка валидации"},
        HTTPStatus.INTERNAL_SERVER_ERROR: {"description": "Ошибка сервера"},
    },
)
@match_info_schema(NoteIdSchema)
async def delete_note(request: web.Request) -> web.Response:
    """Удаление заметки."""

    note_id = request["match_info"]["id"]
    if note_id in request.app["db"]["notes"]:
        del request.app["db"]["notes"][note_id]
        return web.Response(status=HTTPStatus.NO_CONTENT)
    return web.json_response({"error": "Заметка не найдена"}, status=HTTPStatus.NOT_FOUND)
