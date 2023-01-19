from pydantic import BaseSettings


class Settings(BaseSettings):
    redis_host: str
    redis_port: int
    redis_db_number: int
    redis_password: str
    redis_queue_name: str
    

    class Config:
        env_file = ".env"


configs = Settings()