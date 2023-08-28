from abc import ABC, abstractmethod
from flask import g, request


class PWebSaaSTenantResolver(ABC):

    @abstractmethod
    def get_tenant_key(self) -> str:
        pass


class PWebSaaS:
    tenantResolver: PWebSaaSTenantResolver = None

    @staticmethod
    def resolve_tenant_key():
        return request.args.get("tkey")

    @staticmethod
    def init_tenant_key():
        tenant_key = None
        if PWebSaaS.tenantResolver:
            tenant_key = PWebSaaS.tenantResolver.get_tenant_key()
        else:
            tenant_key = PWebSaaS.resolve_tenant_key()

        if tenant_key:
            PWebSaaS.set_tenant_key(tenant_key)

    @staticmethod
    def set_tenant_key(key: str):
        g.pweb_saas = {"key": key}

    @staticmethod
    def get_tenant_key():
        if "pweb_saas" in g and "key" in g.pweb_saas:
            return g.pweb_saas["key"]
        return None
