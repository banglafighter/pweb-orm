from sqlalchemy import Integer
from pweb_orm.model.pweb_orm_model import PWebORMModel
from ppy_common import PyCommon
from pweb_orm.orm.pweb_orm import pweb_orm


class PWebBaseModel(PWebORMModel):
    __abstract__ = True


class PWebRelationalModel(PWebBaseModel):
    __abstract__ = True
    id = pweb_orm.Column("id", pweb_orm.BigInteger().with_variant(Integer, "sqlite"), primary_key=True, nullable=False)
    created = pweb_orm.Column("created", pweb_orm.DateTime, default=pweb_orm.func.now(), nullable=False)
    updated = pweb_orm.Column("updated", pweb_orm.DateTime, default=pweb_orm.func.now(), onupdate=pweb_orm.func.now(), nullable=False)


class PwebModel(PWebRelationalModel):
    __abstract__ = True
    isDeleted = pweb_orm.Column("is_deleted", pweb_orm.Boolean, default=False)
    uuid = pweb_orm.Column("uuid", pweb_orm.String(50), unique=True, nullable=False, index=True)

    def before_save(self):
        if not self.uuid:
            self.uuid = PyCommon.uuid()


class PWebABCModel(object):
    __use_it__ = "only_for_structural_model"
