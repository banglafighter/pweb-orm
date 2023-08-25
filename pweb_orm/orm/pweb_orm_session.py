from __future__ import annotations
from flask_sqlalchemy.session import Session
import typing as t
import sqlalchemy as sa


class PWebORMSession(Session):

    def get_bind(self, mapper: t.Any | None = None, clause: t.Any | None = None, bind: sa.engine.Engine | sa.engine.Connection | None = None, **kwargs: t.Any, ) -> sa.engine.Engine | sa.engine.Connection:
        return super().get_bind(mapper=mapper, clause=clause, bind=bind, kwargs=kwargs)
