from sqlalchemy.exc import IntegrityError
from ppy_common import PPyCException


class PWebORMException:
    EXCEPTION_TYPE = "ORM Exception"

    def parse_integrity_error(self, exception: IntegrityError):
        try:
            if exception.orig and exception.orig.args and len(exception.orig.args) >= 1:
                return str(exception.orig.args[0])
        except Exception as e:
            return "Integrity Error: " + str(e)
        return str(exception.orig)

    def get_exception(self, exception: Exception):
        if isinstance(exception, IntegrityError):
            return PPyCException(self.parse_integrity_error(exception), exception_type=self.EXCEPTION_TYPE)
        return PPyCException(str(exception), exception_type=self.EXCEPTION_TYPE)

    @staticmethod
    def ins():
        return PWebORMException()
