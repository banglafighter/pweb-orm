from __future__ import annotations
from flask_sqlalchemy.session import Session
import typing as t
import sqlalchemy as sa
from pweb_orm.orm.pweb_saas import PWebSaaS


class PWebORMSession(Session):

    def get_bind(self, mapper: t.Any | None = None, clause: t.Any | None = None, bind: sa.engine.Engine | sa.engine.Connection | None = None, **kwargs: t.Any, ) -> sa.engine.Engine | sa.engine.Connection:
        if bind is not None:
            return bind

        engines = self._db.engines

        if mapper is not None:
            try:
                mapper = sa.inspect(mapper)
            except sa.exc.NoInspectionAvailable as e:
                if isinstance(mapper, type):
                    raise sa.orm.exc.UnmappedClassError(mapper) from e
                raise

        bind_key = PWebSaaS.get_tenant_key()
        if bind_key in engines:
            return engines[bind_key]

        return super().get_bind(mapper=mapper, clause=clause, bind=bind, kwargs=kwargs)
