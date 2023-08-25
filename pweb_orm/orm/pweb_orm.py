from flask_sqlalchemy import SQLAlchemy
import typing as t
import sqlalchemy as sa
from flask_sqlalchemy.session import Session


class PWebORM(SQLAlchemy):

    def _make_session_factory(self, options: dict[str, t.Any]) -> sa.orm.sessionmaker[Session]:
        pass

    def init_app(self, app):
        super().init_app(app)
