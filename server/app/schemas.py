from marshmallow import Schema, fields, validate


class NoteSchema(Schema):
    """Схема для заметки."""

    id = fields.Integer(required=False)
    text = fields.String(required=True, validate=validate.Length(min=1, max=256))


class NoteIdSchema(Schema):
    """Схема для id заметки."""

    id = fields.Integer(required=True)


class NoteTextSchema(Schema):
    """Схема для текста заметки."""

    text = fields.String(required=True, validate=validate.Length(min=1, max=256))


class ErrorMessageSchema(Schema):
    """Схема для сообщения об ошибке."""

    message = fields.String()
