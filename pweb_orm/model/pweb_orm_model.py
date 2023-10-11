from pweb_orm.common.pweb_orm_exception import PWebORMException
from pweb_orm.orm.pweb_orm import pweb_orm
from pweb_orm.query.pweb_query_suggestion import PWebQuery


class PWebORMModel(pweb_orm.Model):
    __abstract__ = True
    query: PWebQuery
    _model_list = []

    def save(self):
        self.bulk_save(self._model_list)
        self._model_list.clear()

    def delete(self):
        try:
            pweb_orm.session.delete(self)
            pweb_orm.session.commit()
        except Exception as e:
            raise PWebORMException.ins().get_exception(e)

    def add(self, model):
        self._model_list.append(model)
        return self

    def add_all(self, models: list):
        self._model_list = models
        return self

    @staticmethod
    def save_all(models: list):
        if models:
            model = models.pop(0)
            if isinstance(model, PWebORMModel):
                model.bulk_save(models)
            models.append(model)

    def bulk_save(self, models: list):
        try:
            self.before_save()
            pweb_orm.session.add(self)
            if models:
                for model in models:
                    model.before_save()
                pweb_orm.session.add_all(models)
            pweb_orm.session.commit()
            self.after_save()
            for model in models:
                model.after_save()
        except Exception as e:
            raise PWebORMException.ins().get_exception(e)

    def before_save(self):
        pass

    def after_save(self):
        pass
