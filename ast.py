from enum import Enum
from enum import unique


@unique
class AstNodeTypes(Enum):
    OBJECT = "object",
    VALUE = "value",
    DOCUMENT = "document",
    KEY = "key",
    PAIR = "pair",
    STRING = "string",
    NUMBER = "number",
    COMMENT = "comment",
    BOOLEAN = "boolean",
    ARRAY = "array"


class JsonNode(object):
    def __init__(self, _type):
        self._type = _type

    def accept(self, visitor):
        # 采用visitor模式
        visitor.visitNode(self)


class JsonDocument(JsonNode):
    def __init__(self, _type):
        super(JsonNode).__init__(_type)
        self.children = None

    def accept(self, visitor):
        visitor.visitDocument(self)


class JsonObject(JsonNode):
    def __init__(self, _type):
        super(JsonNode).__init__(_type)
        self.children = []

    def accept(self, visitor):
        visitor.visitObject(self)


class JsonPair(JsonNode):
    def __init__(self, key, value):
        super(JsonNode).__init__()
        self.key = key
        self.value = value

    def accept(self, visitor):
        visitor.visitPair(self)


class JsonKey(JsonNode):
    def __init__(self, value):
        super(JsonNode).__init__()
        self.value = value

    def accept(self, visitor):
        visitor.visitKey(self)


class JsonValue(JsonNode):
    def __init__(self):
        super(JsonNode).__init__()
        self.children = []

    def accept(self, visitor):
        visitor.visitValue(self)


class JsonString(JsonNode):
    def __init__(self, value):
        super(JsonNode).__init__()
        self.value = value

    def accept(self, visitor):
        visitor.visitString(self)


class JsonNumber(JsonNode):
    def __init__(self, value):
        super(JsonNode).__init__()
        self.value = value

    def accept(self, visitor):
        visitor.visitNumber(self)


class JsonBoolean(JsonNode):
    def __init__(self, value):
        super(JsonNode).__init__()
        self.value = value

    def accept(self, visitor):
        visitor.visitBoolean(self)


class JsonComment(JsonNode):
    def __init__(self, value):
        super(JsonNode).__init__()
        self.value = value

    def accept(self, visitor):
        visitor.visitComment(self)
