from http import HTTPStatus


async def test_create_and_get_notes(client, created_note):
    response = await client.get("/notes")
    assert response.status == HTTPStatus.OK
    notes = await response.json()
    assert len(notes) == 1
    assert notes[0]["id"] == created_note["id"]
    assert notes[0]["text"] == created_note["text"]


async def test_create_and_get_note_by_id(client, created_note):
    response = await client.get(f"/notes/{created_note['id']}")
    assert response.status == HTTPStatus.OK
    note = await response.json()
    assert note["id"] == created_note["id"]
    assert note["text"] == created_note["text"]


async def test_create_note_without_text(client):
    response = await client.post("/notes", json={"text": ""})
    assert response.status == HTTPStatus.UNPROCESSABLE_CONTENT


async def test_get_wrong_note(client):
    response = await client.get("/notes/1")
    assert response.status == HTTPStatus.NOT_FOUND
    data = await response.json()
    assert data["error"] == "Заметка не найдена"


async def test_get_note_by_invalid_id(client):
    response = await client.get("/notes/invalid_id")
    assert response.status == HTTPStatus.UNPROCESSABLE_CONTENT


async def test_edit_note(client, created_note):
    response = await client.put(f"/notes/{created_note['id']}", json={"text": "Updated note text"})
    assert response.status == HTTPStatus.OK
    note = await response.json()
    assert note["id"] == created_note["id"]
    assert note["text"] == "Updated note text"


async def test_edit_note_without_text(client, created_note):
    response = await client.put(f"/notes/{created_note['id']}", json={"text": ""})
    assert response.status == HTTPStatus.UNPROCESSABLE_CONTENT


async def test_edit_wrong_note(client):
    response = await client.put("/notes/1", json={"text": "Updated note text"})
    assert response.status == HTTPStatus.NOT_FOUND
    data = await response.json()
    assert data["error"] == "Заметка не найдена"


async def test_delete_note(client, created_note):
    response = await client.delete(f"/notes/{created_note['id']}")
    assert response.status == HTTPStatus.NO_CONTENT
    response = await client.get(f"/notes/{created_note['id']}")
    assert response.status == HTTPStatus.NOT_FOUND
    data = await response.json()
    assert data["error"] == "Заметка не найдена"


async def test_delete_wrong_note(client):
    response = await client.delete("/notes/1")
    assert response.status == HTTPStatus.NOT_FOUND
    data = await response.json()
    assert data["error"] == "Заметка не найдена"
