from pweb_orm.query.pweb_db_query_helper import DBQueryHelper


class PWebQuery(DBQueryHelper):

    def all(self) -> "Query":
        pass

    def first(self) -> "Query":
        pass

    def first_or_404(self, description=None) -> "Query":
        pass

    def paginate(self, page=None, per_page=None, error_out=True, max_per_page=None) -> "Query":
        pass

    def count(self) -> "Query":
        pass

    def get(self, ident) -> "Query":
        pass

    def get_or_404(self, ident, description=None) -> "Query":
        pass

    def with_entities(self, *entities) -> "Query":
        pass

    def filter(self, *criterion) -> "Query":
        return self

    def filter_by(self, **kwargs) -> "Query":
        return self

    def order_by(self, *clauses) -> "Query":
        pass

    def group_by(self, *clauses) -> "Query":
        pass

    def having(self, criterion) -> "Query":
        pass

    def join(self, target, *props, **kwargs) -> "Query":
        pass

    def limit(self, limit) -> "Query":
        pass

    def offset(self, offset) -> "Query":
        pass

    def from_statement(self, statement) -> "Query":
        pass

    def one_or_none(self) -> "Query":
        pass

    def one(self) -> "Query":
        pass

    def delete(self, synchronize_session="evaluate") -> "Query":
        pass

    def update(self, values, synchronize_session="evaluate", update_args=None) -> "Query":
        pass
