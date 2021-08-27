from v2.nacos.common.lifecycle.closeable import Closeable
from v2.nacos.config.filter_impl.config_response import ConfigResponse
from v2.nacos.config.ilistener import Listener
from v2.nacos.config.impl.cache_data import CacheData


class ClientWorker(Closeable):
    NOTIFY_HEADER = "notify"

    TAG_PARAM = "tag"

    APP_NAME_PARAM = "appName"

    BETAIPS_PARAM = "betaIps"

    TYPE_PARAM = "type"

    ENCRYPTED_DATA_KEY_PARAM = "encryptedDataKey"

    DEFAULT_RESOURCE = ""

    def __init__(self):
        pass

    def add_listeners(self, data_id: str, group: str, listeners: list) -> None:
        pass

    def add_tenant_listeners(self, data_id: str, group: str, listeners: list) -> None:
        pass

    def add_tenant_listeners_with_content(self, data_id: str, group: str, content: str, listeners: list) -> None:
        pass

    def remove_listener(self, data_id: str, group: str, listener: Listener) -> None:
        pass

    def remove_tenant_listener(self, data_id: str, group: str, listener: Listener) -> None:
        pass

    def remove_cache(self, data_id: str, group: str, tenant: str) -> None:
        pass

    def remove_config(self):
        pass

    def publish_config(self, data_id: str, group:str, tenant: str, app_name: str, tag: str, beta_ips: str,
                       content: str, encrpted_data_key: str, cas_md5: str, config_type: str) -> bool:
        pass

    def add_cache_data_if_absent(self, data_id: str, group: str, tenant: str) -> CacheData:
        pass

    def get_cache(self, data_id: str, group: str) -> CacheData:
        pass

    def get_server_config(self, data: str, group: str, tenant: str, read_timeout: int, notify: bool) -> ConfigResponse:
        pass

    def is_health_server(self) -> bool:
        pass

    def get_agent_name(self) -> str:
        pass

    def shutdown(self) -> None:
        pass