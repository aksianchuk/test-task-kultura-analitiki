from http import HTTPStatus

import pytest

from server.app.main import create_app


@pytest.fixture
async def client(aiohttp_client):
    app = create_app()
    return await aiohttp_client(app)


@pytest.fixture
async def created_note(client):
    response = await client.post("/notes", json={"text": "Note text"})
    assert response.status == HTTPStatus.CREATED
    data = await response.json()
    return data
