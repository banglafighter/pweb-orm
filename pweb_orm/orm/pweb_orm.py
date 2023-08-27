from flask_sqlalchemy import SQLAlchemy, BaseQuery, Model
import typing as t
import sqlalchemy as sa
from flask_sqlalchemy.session import Session
from pweb_orm.common.pweb_orm_exception import PWebORMException
from pweb_orm.orm.pweb_orm_session import PWebORMSession
from pweb_orm.query.pweb_db_query_helper import DBQueryHelper


class PWebORM(SQLAlchemy):

    def __init__(self, app=None, session_options=None, metadata=None, query_class=BaseQuery, model_class=Model, engine_options=None):
        if not query_class:
            query_class = DBQueryHelper
        super().__init__(app=app, session_options=session_options, metadata=metadata, query_class=query_class, engine_options=engine_options, model_class=model_class)

    def _make_session_factory(self, options: dict[str, t.Any]) -> sa.orm.sessionmaker[Session]:
        options.setdefault("class_", PWebORMSession)
        options.setdefault("query_cls", self.Query)
        return sa.orm.sessionmaker(db=self, **options)

    def _init_db(self, bind_key):
        self.create_all(bind_key=bind_key)

    def _init_tables(self, bind_key):
        if bind_key in self.metadatas and None in self.metadatas and self.metadatas[None].tables:
            for key, table in self.metadatas[None].tables.items():
                self.metadatas[bind_key].tables._insert_item(key, table)

    def init_app(self, app):
        super().init_app(app)

    def run_sql(self, sql):
        try:
            connection = self.engine.connect()
            return connection.execute(sql)
        except Exception as e:
            raise PWebORMException.ins().get_exception(e)

    def get_tenant_list(self):
        tenants = self.engines
        tenant_list = []
        if tenants:
            for key, details in tenants.items():
                if key:
                    tenant_list.append(key)
        return tenant_list

    def register_tenant(self, app, key: str, db_url: str):
        if not key or not db_url or key in self.engines:
            return False

        echo: bool = app.config.setdefault("SQLALCHEMY_ECHO", False)

        options: dict = {"url": db_url}
        options.setdefault("echo", echo)
        options.setdefault("echo_pool", echo)

        self._make_metadata(key)
        self._apply_driver_defaults(options, app)
        engine = self._make_engine(key, options, app)
        if self._app_engines and app in self._app_engines and key not in self._app_engines[app]:
            self._app_engines[app][key] = engine
            self._init_tables(key)
            self._init_db(key)
            return True
        return False


pweb_orm = PWebORM()
