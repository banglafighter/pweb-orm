from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.types import TypeDecorator, JSON, Text
from sqlalchemy.dialects.postgresql import JSONB
import json


class JSONModelField:
    pass


class JSONType(TypeDecorator):
    impl = Text  # Default implementation

    def load_dialect_impl(self, dialect):
        """Chooses JSONB for PostgreSQL, JSON or Text for others."""
        if dialect.name == "postgresql":
            return dialect.type_descriptor(JSONB())
        elif dialect.name in {"mysql"}:
            return dialect.type_descriptor(Text().with_variant(LONGTEXT, "mysql"))
        else:
            return dialect.type_descriptor(Text())  # Store JSON as a string for unsupported DBs

    def process_bind_param(self, value, dialect):
        """Convert Python object to JSON string if necessary."""
        if value is None:
            return None
        if dialect.name not in {"postgresql", "mysql", "sqlite"}:
            return json.dumps(value)  # Convert to text format
        return value  # Store as JSON/JSONB directly

    def process_result_value(self, value, dialect):
        """Convert JSON string back to Python object when fetching data."""
        if value is None:
            return None
        if dialect.name not in {"postgresql", "mysql", "sqlite"}:
            return json.loads(value)  # Convert text to JSON
        return value  # Already in JSON format
