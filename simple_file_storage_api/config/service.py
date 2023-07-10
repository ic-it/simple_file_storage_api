from pydantic import BaseSettings

_SERVICE_CONFIG_PREFIX = "SFSA_"


class Service(BaseSettings):
    storage_path: str
    host: str = "0.0.0.0"
    port: int = 8000
    debug: bool = False

    class Config:
        env_prefix = _SERVICE_CONFIG_PREFIX + "APP_"
